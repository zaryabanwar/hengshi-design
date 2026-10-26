"""Synthetic in-memory archive boundary tests; no trial artifacts or installs."""
import hashlib
import io
import stat
import struct
import tarfile
import unittest
from unittest.mock import patch
import zipfile

from archive_admission import AdmissionError, Limits, inspect_archive


def zip_bytes(entries):
    out = io.BytesIO()
    with zipfile.ZipFile(out, "w", compression=zipfile.ZIP_STORED) as archive:
        for name, data in entries:
            archive.writestr(name, data)
    return out.getvalue()


def tar_bytes(entries):
    out = io.BytesIO()
    with tarfile.open(fileobj=out, mode="w", format=tarfile.PAX_FORMAT) as archive:
        for name, data, kind in entries:
            info = tarfile.TarInfo(name)
            info.type = kind
            info.size = len(data) if kind == tarfile.REGTYPE else 0
            if kind in (tarfile.LNKTYPE, tarfile.SYMTYPE):
                info.linkname = "../outside"
            archive.addfile(info, io.BytesIO(data) if info.size else None)
    return out.getvalue()


class ArchiveAdmissionTests(unittest.TestCase):
    def inspect(self, raw, kind="zip", **kwargs):
        return inspect_archive(io.BytesIO(raw), kind=kind,
                               expected_size=kwargs.pop("expected_size", len(raw)),
                               expected_digest=kwargs.pop("expected_digest", hashlib.sha256(raw).hexdigest()),
                               **kwargs)

    def test_valid_zip_reports_payload_identity_and_no_extraction(self):
        raw = zip_bytes([("tools/", b""), ("tools/alpha.txt", b"abc"),
                         ("tools/beta.txt", b"defg")])
        with patch.object(zipfile.ZipFile, "extract", side_effect=AssertionError("extract called")), \
                patch.object(zipfile.ZipFile, "extractall", side_effect=AssertionError("extractall called")):
            report = self.inspect(raw)
        self.assertEqual(report.archive_bytes, len(raw))
        self.assertEqual(report.expanded_bytes, 7)
        self.assertEqual([(m.path, m.kind, m.expanded_bytes) for m in report.members],
                         [("tools", "directory", 0), ("tools/alpha.txt", "file", 3),
                          ("tools/beta.txt", "file", 4)])
        self.assertEqual(report.members[1].sha256, hashlib.sha256(b"abc").hexdigest())
        self.assertIsNone(report.members[0].sha256)

    def test_valid_tar_uses_regular_files_and_directories_only(self):
        raw = tar_bytes([("pkg", b"", tarfile.DIRTYPE),
                         ("pkg/setup.py", b"test", tarfile.REGTYPE)])
        with patch.object(tarfile.TarFile, "extract", side_effect=AssertionError("extract called")), \
                patch.object(tarfile.TarFile, "extractall", side_effect=AssertionError("extractall called")):
            report = self.inspect(raw, "tar")
        self.assertEqual(report.expanded_bytes, 4)
        self.assertEqual(report.members[1].sha256, hashlib.sha256(b"test").hexdigest())

    def test_trusted_size_and_digest_are_checked_before_parser_admission(self):
        raw = zip_bytes([("a", b"x")])
        with patch.object(zipfile, "ZipFile", side_effect=AssertionError("parser reached")):
            for values, code in (({"expected_digest": "0" * 64}, "archive_digest"),
                                 ({"expected_size": len(raw) - 1}, "archive_size"),
                                 ({"expected_size": len(raw) + 1}, "archive_size")):
                with self.subTest(values=values), self.assertRaisesRegex(AdmissionError, "^" + code + "$"):
                    self.inspect(raw, **values)

    def test_windows_paths_are_rejected_without_normalizing_them_into_safe_names(self):
        invalid = ("../outside", "/outside", "C:/outside", "C:relative", "//host/share",
                   "a\\b", "a/./b", "a//b", "NUL.txt", "LPT1", "a:b", "a.", "a ",
                   "a/../b", "a\nb", "a/", "e\u0301.txt")
        for name in invalid:
            for kind in ("zip", "tar"):
                with self.subTest(name=name, kind=kind):
                    raw = (zip_bytes([(name, b"x")]) if kind == "zip" else
                           tar_bytes([(name, b"x", tarfile.REGTYPE)]))
                    with self.assertRaises(AdmissionError):
                        self.inspect(raw, kind)

    def test_duplicate_case_and_parent_file_aliases_are_denied_in_both_orders(self):
        cases = (("a", "A"), ("a", "a/b"), ("a/b", "a"),
                 ("Tools/a", "tools/b"), ("a", "a"))
        for names in cases:
            for kind in ("zip", "tar"):
                with self.subTest(names=names, kind=kind):
                    if kind == "zip":
                        with self.assertWarns(UserWarning) if names == ("a", "a") else self.subTest():
                            raw = zip_bytes([(n, b"x") for n in names])
                    else:
                        raw = tar_bytes([(n, b"x", tarfile.REGTYPE) for n in names])
                    with self.assertRaisesRegex(AdmissionError, "^path_collision$"):
                        self.inspect(raw, kind)

    def test_zip_links_reparse_and_file_type_mismatch_are_denied(self):
        for name, attrs in (("a", (stat.S_IFLNK | 0o777) << 16),
                            ("a", 0x400), ("a", stat.S_IFDIR << 16),
                            ("a/", stat.S_IFREG << 16)):
            info = zipfile.ZipInfo(name)
            info.create_system = 3
            info.external_attr = attrs
            raw = zip_bytes([(info, b"")])
            with self.subTest(name=name, attrs=attrs), self.assertRaisesRegex(AdmissionError, "^member_type$"):
                self.inspect(raw)

    def test_zip_encryption_and_unsupported_compression_are_not_silently_accepted(self):
        original = zip_bytes([("a", b"x")])
        for flag in (1, 64):
            raw = bytearray(original)
            central = raw.index(b"PK\x01\x02")
            struct.pack_into("<H", raw, 6, flag)
            struct.pack_into("<H", raw, central + 8, flag)
            with self.subTest(flag=flag), self.assertRaisesRegex(AdmissionError, "^encrypted_member$"):
                self.inspect(bytes(raw))
        raw = bytearray(original)
        central = raw.index(b"PK\x01\x02")
        struct.pack_into("<H", raw, 8, 99)
        struct.pack_into("<H", raw, central + 10, 99)
        with self.assertRaisesRegex(AdmissionError, "^compression_profile$"):
            self.inspect(bytes(raw))

    def test_tar_hardlinks_symlinks_devices_and_fifo_are_denied(self):
        for kind in (tarfile.LNKTYPE, tarfile.SYMTYPE, tarfile.CHRTYPE,
                     tarfile.BLKTYPE, tarfile.FIFOTYPE):
            with self.subTest(kind=kind), self.assertRaisesRegex(AdmissionError, "^member_type$"):
                self.inspect(tar_bytes([("a", b"", kind)]), "tar")

    def test_declared_expansion_and_metadata_limits_refuse_before_payload_read(self):
        raw = zip_bytes([("longname.txt", b"1234"), ("other.txt", b"x")])
        for limits, code in ((Limits(archive_bytes=len(raw) - 1), "invalid_identity"),
                             (Limits(expanded_bytes=3), "expanded_limit"),
                             (Limits(members=1), "member_limit"),
                             (Limits(path_bytes=3), "path_limit"),
                             (Limits(path_metadata_bytes=15), "path_limit")):
            with self.subTest(code=code), self.assertRaisesRegex(AdmissionError, "^" + code + "$"):
                self.inspect(raw, limits=limits)
        self.assertEqual(self.inspect(zip_bytes([("a", b"1234")]),
                                      limits=Limits(expanded_bytes=4)).expanded_bytes, 4)

    def test_payload_crc_and_truncated_header_errors_do_not_return_partial_reports(self):
        raw = zip_bytes([("a", b"PAYLOAD")]).replace(b"PAYLOAD", b"PBYLOAD")
        with self.assertRaisesRegex(AdmissionError, "^archive_parse$"):
            self.inspect(raw)
        for kind, raw in (("zip", b"PKbad"), ("tar", b"bad")):
            with self.subTest(kind=kind), self.assertRaisesRegex(AdmissionError, "^archive_parse$"):
                self.inspect(raw, kind)

    def test_zip_original_name_cannot_be_hidden_by_null_byte_sanitization(self):
        raw = zip_bytes([("evilXfile", b"x")]).replace(b"evilXfile", b"evil\x00file")
        with self.assertRaisesRegex(AdmissionError, "^sanitized_path$"):
            self.inspect(raw)

    def test_deadline_empty_archive_and_directory_payload_are_denied(self):
        raw = zip_bytes([("a", b"x")])
        ticks = iter((0, 180))
        with self.assertRaisesRegex(AdmissionError, "^deadline$"):
            self.inspect(raw, clock=lambda: next(ticks))
        for kind, empty in (("zip", zip_bytes([])), ("tar", tar_bytes([]))):
            with self.subTest(kind=kind), self.assertRaisesRegex(AdmissionError, "^empty_archive$"):
                self.inspect(empty, kind)
        with self.assertRaisesRegex(AdmissionError, "^invalid_size$"):
            self.inspect(zip_bytes([("a/", b"payload")]))

    def test_sha512_profile_and_invalid_trusted_parameters(self):
        raw = zip_bytes([("a", b"x")])
        report = self.inspect(raw, digest_algorithm="sha512", expected_digest=hashlib.sha512(raw).hexdigest())
        self.assertEqual(report.digest, hashlib.sha512(raw).hexdigest())
        for kwargs in ({"kind": "rar"}, {"digest_algorithm": "md5"},
                       {"expected_digest": "A" * 64}, {"expected_size": True},
                       {"limits": Limits(members=0)}, {"limits": Limits(seconds=181)}):
            with self.subTest(kwargs=kwargs), self.assertRaises(AdmissionError):
                if "kind" in kwargs:
                    self.inspect(raw, **kwargs)
                else:
                    self.inspect(raw, **kwargs)


if __name__ == "__main__":
    unittest.main()

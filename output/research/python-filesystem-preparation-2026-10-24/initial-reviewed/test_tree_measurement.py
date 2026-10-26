"""Windows helper boundary tests; small fixtures are retained, never cleaned up.

Uses the existing host interpreter, not the proposed Python trial runtime.
Actual files exercise counts/limits/identities/hard links. OS fault/race/reparse
samples are injected at lstat/scandir/disk_usage seams, not OS sandbox proofs.
"""
from dataclasses import replace
from pathlib import Path
from types import SimpleNamespace
import os
import tempfile
import unittest
from unittest.mock import patch

from tree_measurement import Limits, MeasurementError, measure_tree


class TreeMeasurementTests(unittest.TestCase):
    def setUp(self):
        fixture_parent = Path(__file__).parent / "fixtures"
        fixture_parent.mkdir(exist_ok=True)
        self.root = Path(tempfile.mkdtemp(prefix="case-", dir=fixture_parent)).absolute()
        item = os.lstat(self.root)
        self.identity = item.st_dev, item.st_ino

    def run_measure(self, **kwargs):
        return measure_tree(str(self.root), expected_identity=self.identity, **kwargs)

    def reject(self, code, **kwargs):
        with self.assertRaisesRegex(MeasurementError, "^" + code + "$"):
            self.run_measure(**kwargs)

    def test_exact_default_stream_lengths_and_directory_count(self):
        (self.root / "one.txt").write_bytes(b"abc")
        (self.root / "nested").mkdir()
        (self.root / "nested" / "two.bin").write_bytes(b"12345")
        (self.root / "empty").mkdir()
        result = self.run_measure(limits=Limits(entries=5, logical_bytes=8))
        self.assertEqual((result.files, result.directories, result.logical_bytes), (2, 3, 8))
        self.assertEqual(result.root_identity, self.identity)
        self.assertGreaterEqual(result.free_bytes, 0)

    def test_missing_root_does_not_become_empty_success(self):
        with self.assertRaisesRegex(MeasurementError, "^filesystem_read$"):
            measure_tree(str(self.root / "missing"), expected_identity=self.identity)

    def test_relative_or_drive_root_is_rejected(self):
        for value in ("relative", "C:\\", str(self.root) + "\\..", "\\\\server\\share"):
            with self.subTest(value=value), self.assertRaisesRegex(MeasurementError, "^invalid_root$"):
                measure_tree(value, expected_identity=self.identity)

    def test_wrong_previously_recorded_root_identity_is_rejected(self):
        with self.assertRaisesRegex(MeasurementError, "^root_changed$"):
            measure_tree(str(self.root), expected_identity=(self.identity[0], self.identity[1] + 1))

    def test_file_root_is_rejected(self):
        target = self.root / "file"
        target.write_bytes(b"a")
        with self.assertRaisesRegex(MeasurementError, "^not_directory$"):
            measure_tree(str(target), expected_identity=self.identity)

    def test_real_hard_link_is_rejected_not_double_counted(self):
        source = self.root / "original"
        source.write_bytes(b"retained")
        os.link(source, self.root / "alias")
        self.reject("hard_link")

    def test_entry_depth_and_logical_limits(self):
        (self.root / "nested").mkdir()
        (self.root / "nested" / "payload").write_bytes(b"123")
        self.reject("entry_limit", limits=Limits(entries=2))
        self.reject("depth_limit", limits=Limits(depth=1))
        self.reject("logical_limit", limits=Limits(logical_bytes=2))

    def test_invalid_limits_reject_before_reading_filesystem(self):
        for values in ({"entries": True}, {"depth": 0}, {"seconds": float("nan")},
                       {"seconds": 181}, {"logical_bytes": -1}):
            with self.subTest(values=values), patch("tree_measurement.os.lstat") as read:
                self.reject("invalid_limits", limits=replace(Limits(), **values))
                read.assert_not_called()

    def test_reparse_attribute_on_root_or_ancestor_is_rejected(self):
        real = os.lstat
        for affected in (str(self.root), str(self.root.parent)):
            def read(path):
                item = real(path)
                if str(path) == affected:
                    return SimpleNamespace(st_file_attributes=item.st_file_attributes | 0x400)
                return item
            with self.subTest(affected=affected), patch("tree_measurement.os.lstat", side_effect=read):
                self.reject("unsafe_entry")

    def test_volume_change_is_rejected(self):
        target = self.root / "payload"
        target.write_bytes(b"a")
        real = os.lstat
        def read(path):
            item = real(path)
            if str(path) == str(target):
                return SimpleNamespace(st_mode=item.st_mode, st_file_attributes=item.st_file_attributes,
                                       st_ino=item.st_ino, st_dev=item.st_dev + 1,
                                       st_nlink=item.st_nlink, st_size=item.st_size)
            return item
        with patch("tree_measurement.os.lstat", side_effect=read):
            self.reject("different_volume")

    def test_read_errors_are_terminal_and_redacted(self):
        with patch("tree_measurement.os.scandir", side_effect=PermissionError("private path")):
            self.reject("filesystem_read")
        with patch("tree_measurement.shutil.disk_usage", side_effect=OSError("private path")):
            self.reject("filesystem_read")

    def test_detected_file_change_invalidates_entire_measurement(self):
        target = self.root / "payload"
        target.write_bytes(b"a")
        real = os.lstat
        calls = 0
        def read(path):
            nonlocal calls
            if str(path) == str(target):
                calls += 1
                if calls == 2:
                    target.write_bytes(b"changed")
            return real(path)
        with patch("tree_measurement.os.lstat", side_effect=read):
            self.reject("tree_changed")

    def test_cooperative_deadline_stops_before_scan(self):
        ticks = iter((0.0, 180.0))
        with patch("tree_measurement.os.scandir") as scan:
            self.reject("deadline", clock=lambda: next(ticks))
            scan.assert_not_called()


if __name__ == "__main__":
    unittest.main(verbosity=2)

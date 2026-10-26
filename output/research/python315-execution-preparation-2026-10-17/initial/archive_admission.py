"""Read-only research archive inspector; not an extractor or trial execution gate.

Only synthetic fixtures have qualified this candidate. No downloads, writes,
imports from inspected packages or execution of archive contents occur here.
The parent controller still needs reviewed ownership, disk reservation, process
deadlines and artifact/graph admission. A cooperative clock is not a hard CPU or
memory quota: stdlib archive metadata parsing can allocate before member checks.
"""
from __future__ import annotations

from dataclasses import dataclass
import hashlib
import hmac
import ntpath
import re
import stat
import tarfile
import time
import unicodedata
from typing import BinaryIO, Literal
import zipfile
import zlib


class AdmissionError(ValueError):
    """Fixed category; no member content or untrusted filename in diagnostics."""


@dataclass(frozen=True)
class Limits:
    archive_bytes: int = 64 * 1024 * 1024
    expanded_bytes: int = 128 * 1024 * 1024
    members: int = 10000
    path_bytes: int = 512
    path_metadata_bytes: int = 2 * 1024 * 1024
    seconds: float = 180

    def validate(self):
        for value in (self.archive_bytes, self.expanded_bytes, self.members,
                      self.path_bytes, self.path_metadata_bytes):
            if type(value) is not int or value < 1:
                raise AdmissionError("invalid_limits")
        if (type(self.seconds) not in (int, float) or
                not 0 < self.seconds <= 180):
            raise AdmissionError("invalid_limits")


@dataclass(frozen=True)
class Member:
    path: str
    kind: Literal["file", "directory"]
    expanded_bytes: int
    sha256: str | None


@dataclass(frozen=True)
class Report:
    archive_bytes: int
    expanded_bytes: int
    digest_algorithm: str
    digest: str
    members: tuple[Member, ...]


class _Inventory:
    def __init__(self, limits: Limits, deadline: float, clock):
        self.limits = limits
        self.deadline = deadline
        self.clock = clock
        self.paths: dict[str, bool] = {}
        self.spellings: dict[str, str] = {}
        self.parents: set[str] = set()
        self.metadata_bytes = 0
        self.expanded = 0
        self.members: list[Member] = []

    def tick(self):
        if self.clock() >= self.deadline:
            raise AdmissionError("deadline")

    def admit(self, name: str, directory: bool, size: int):
        self.tick()
        if len(self.members) >= self.limits.members:
            raise AdmissionError("member_limit")
        if (not name or "\\" in name or name.startswith("/") or
                name != unicodedata.normalize("NFC", name)):
            raise AdmissionError("unsafe_path")
        try:
            encoded_size = len(name.encode("utf-8", errors="strict"))
        except UnicodeError:
            raise AdmissionError("unsafe_path") from None
        self.metadata_bytes += encoded_size
        if (encoded_size > self.limits.path_bytes or
                self.metadata_bytes > self.limits.path_metadata_bytes):
            raise AdmissionError("path_limit")
        path = name[:-1] if directory and name.endswith("/") else name
        parts = path.split("/")
        if any(part in ("", ".", "..") or ntpath.isreserved(part) for part in parts):
            raise AdmissionError("unsafe_path")
        if type(size) is not int or size < 0 or (directory and size != 0):
            raise AdmissionError("invalid_size")
        if self.expanded + size > self.limits.expanded_bytes:
            raise AdmissionError("expanded_limit")
        folded = path.casefold()
        if folded in self.paths or (not directory and folded in self.parents):
            raise AdmissionError("path_collision")
        for count in range(1, len(parts) + 1):
            spelling = "/".join(parts[:count])
            key = spelling.casefold()
            if key in self.spellings and self.spellings[key] != spelling:
                raise AdmissionError("path_collision")
            self.spellings[key] = spelling
            if count < len(parts):
                if key in self.paths and not self.paths[key]:
                    raise AdmissionError("path_collision")
                self.parents.add(key)
        self.paths[folded] = directory
        self.expanded += size
        return path

    def payload(self, stream: BinaryIO, size: int):
        digest = hashlib.sha256()
        count = 0
        while True:
            self.tick()
            chunk = stream.read(min(256 * 1024, size - count + 1))
            if not chunk:
                break
            count += len(chunk)
            if count > size:
                raise AdmissionError("payload_size")
            digest.update(chunk)
        if count != size:
            raise AdmissionError("payload_size")
        return digest.hexdigest()


def _zip(stream: BinaryIO, inventory: _Inventory):
    with zipfile.ZipFile(stream, "r") as archive:
        # ZipFile parses its central directory first. Parent process/resource
        # control remains necessary; this count is not a pre-allocation guard.
        if len(archive.infolist()) > inventory.limits.members:
            raise AdmissionError("member_limit")
        for info in archive.infolist():
            if info.orig_filename != info.filename:
                raise AdmissionError("sanitized_path")
            if info.flag_bits & (1 | 64):
                raise AdmissionError("encrypted_member")
            if info.compress_type not in (zipfile.ZIP_STORED, zipfile.ZIP_DEFLATED):
                raise AdmissionError("compression_profile")
            mode = stat.S_IFMT(info.external_attr >> 16)
            directory = info.is_dir()
            if (mode not in (0, stat.S_IFREG, stat.S_IFDIR) or
                    (mode == stat.S_IFDIR and not directory) or
                    (mode == stat.S_IFREG and directory) or
                    (info.external_attr & 0x400) or
                    (info.external_attr & 0x10 and not directory)):
                raise AdmissionError("member_type")
            path = inventory.admit(info.orig_filename, directory, info.file_size)
            # Reading to EOF exercises stdlib local-name/overlap/CRC checks,
            # including empty directory members. No extract/extractall call.
            with archive.open(info, "r") as member:
                digest = inventory.payload(member, info.file_size)
            inventory.members.append(Member(path, "directory" if directory else "file",
                                             info.file_size, None if directory else digest))


def _tar(stream: BinaryIO, inventory: _Inventory):
    # stream=True avoids retaining TarInfo entries. Tarfile may still parse
    # extension headers before yielding; no hard parser memory bound is claimed.
    with tarfile.open(fileobj=stream, mode="r:*", stream=True) as archive:
        for info in archive:
            if (not (info.isdir() or info.isreg()) or info.issparse() or
                    info.linkname):
                raise AdmissionError("member_type")
            path = inventory.admit(info.name, info.isdir(), info.size)
            if info.isdir():
                digest = None
            else:
                member = archive.extractfile(info)
                if member is None:
                    raise AdmissionError("missing_payload")
                with member:
                    digest = inventory.payload(member, info.size)
            inventory.members.append(Member(path, "directory" if info.isdir() else "file",
                                             info.size, digest))


def inspect_archive(stream: BinaryIO, *, kind: Literal["zip", "tar"],
                    expected_size: int, expected_digest: str,
                    digest_algorithm: Literal["sha256", "sha512"] = "sha256",
                    limits: Limits = Limits(), clock=time.monotonic) -> Report:
    """Inspect seekable already-owned bytes; return only after complete success.

    Expected identity/limits must come from a separately reviewed trusted plan,
    never from an archive member. This report grants no extraction/execution.
    """
    limits.validate()
    if (kind not in ("zip", "tar") or digest_algorithm not in ("sha256", "sha512") or
            type(expected_size) is not int or not 0 < expected_size <= limits.archive_bytes):
        raise AdmissionError("invalid_identity")
    length = 64 if digest_algorithm == "sha256" else 128
    if (not isinstance(expected_digest, str) or
            re.fullmatch("[0-9a-f]{" + str(length) + "}", expected_digest) is None):
        raise AdmissionError("invalid_identity")
    inventory = _Inventory(limits, clock() + limits.seconds, clock)
    try:
        stream.seek(0)
        digest = hashlib.new(digest_algorithm)
        count = 0
        while True:
            inventory.tick()
            chunk = stream.read(min(256 * 1024, expected_size - count + 1))
            if not chunk:
                break
            count += len(chunk)
            if count > expected_size:
                raise AdmissionError("archive_size")
            digest.update(chunk)
        if count != expected_size:
            raise AdmissionError("archive_size")
        if not hmac.compare_digest(digest.hexdigest(), expected_digest):
            raise AdmissionError("archive_digest")
        stream.seek(0)
        (_zip if kind == "zip" else _tar)(stream, inventory)
        inventory.tick()
        if not inventory.members:
            raise AdmissionError("empty_archive")
        return Report(count, inventory.expanded, digest_algorithm, digest.hexdigest(),
                      tuple(inventory.members))
    except AdmissionError:
        raise
    except (OSError, ValueError, EOFError, RuntimeError, NotImplementedError,
            zipfile.BadZipFile, tarfile.TarError, zlib.error):
        raise AdmissionError("archive_parse") from None

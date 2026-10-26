"""Read-only Windows default-stream measurement for isolated research preparation.

This is a cooperative snapshot, NOT ownership authentication, a reservation,
content-integrity proof or a race-resistant filesystem sandbox. Path-based
lstat/scandir cannot fence concurrent ancestor replacement. A future execution
controller must establish exclusive private-tree ownership/handle protections,
account for alternate streams, and supply the separately recorded root identity.
No extraction, file opening for payload reads, writes, cleanup or trial starts.
"""
from dataclasses import dataclass
import math
import ntpath
import os
import re
import shutil
import stat
import time
import unicodedata


class MeasurementError(ValueError):
    """Fixed error category, without supplied paths or OS exception details."""


@dataclass(frozen=True)
class Limits:
    entries: int = 10000
    depth: int = 64
    logical_bytes: int = 512 * 1024 * 1024
    seconds: float = 180

    def validate(self):
        if (type(self.entries) is not int or not 1 <= self.entries <= 10000 or
                type(self.depth) is not int or not 1 <= self.depth <= 64 or
                type(self.logical_bytes) is not int or
                not 0 <= self.logical_bytes <= 512 * 1024 * 1024 or
                type(self.seconds) not in (int, float) or
                not math.isfinite(self.seconds) or not 0 < self.seconds <= 180):
            raise MeasurementError("invalid_limits")


@dataclass(frozen=True)
class Measurement:
    root_identity: tuple[int, int]
    files: int
    directories: int
    logical_bytes: int
    free_bytes: int


def _root(value):
    if os.name != "nt":
        raise MeasurementError("unsupported_platform")
    # Finite lexical bounds precede normalization/splitting/ancestor storage.
    if (type(value) is not str or not 4 <= len(value) <= 1024 or
            re.match(r"^[A-Za-z]:\\", value) is None or
            "/" in value or value != unicodedata.normalize("NFC", value)):
        raise MeasurementError("invalid_root")
    parts = value[3:].split("\\")
    if (len(parts) > 64 or ntpath.normpath(value) != value or
            any(p in ("", ".", "..") or ntpath.isreserved(p) for p in parts)):
        raise MeasurementError("invalid_root")
    return value


def _observed(path):
    # Do not use DirEntry.stat: Windows DirEntry identity fields can be zero
    # and its cached information cannot revalidate a prior measurement.
    item = os.lstat(path)
    if (item.st_file_attributes & stat.FILE_ATTRIBUTE_REPARSE_POINT or
            not (stat.S_ISDIR(item.st_mode) or stat.S_ISREG(item.st_mode))):
        raise MeasurementError("unsafe_entry")
    if (item.st_ino <= 0 or item.st_dev < 0 or item.st_nlink < 1 or
            item.st_size < 0):
        raise MeasurementError("unknown_identity")
    if stat.S_ISREG(item.st_mode) and item.st_nlink != 1:
        raise MeasurementError("hard_link")
    return item


def _identity(item):
    return item.st_dev, item.st_ino


def _fingerprint(item):
    return (_identity(item), item.st_mode, item.st_nlink, item.st_size,
            item.st_mtime_ns, item.st_file_attributes)


def measure_tree(root: str, *, expected_identity: tuple[int, int],
                 limits: Limits = Limits(), clock=time.monotonic) -> Measurement:
    """Measure a quiescent private tree; reject known unsafe/incomplete snapshots.

    expected_identity is the controller's previously established (st_dev,st_ino),
    not a value to infer from a marker file or accept from untrusted input.
    The result covers ordinary default-stream lengths and sampled free bytes,
    not allocated blocks/ADS/ACL authority. It is unusable as a write permit.
    Blocking OS calls can exceed the cooperative clock; no hard deadline claim.
    """
    limits.validate()
    root = _root(root)
    if (type(expected_identity) is not tuple or len(expected_identity) != 2 or
            any(type(n) is not int for n in expected_identity) or
            expected_identity[0] < 0 or expected_identity[1] <= 0):
        raise MeasurementError("invalid_identity")
    deadline = clock() + limits.seconds

    def tick():
        if clock() >= deadline:
            raise MeasurementError("deadline")

    try:
        # Inspect every existing ancestor without resolving away a junction.
        chain = [root]
        while ntpath.dirname(chain[-1]) != chain[-1]:
            tick()
            chain.append(ntpath.dirname(chain[-1]))
        ancestors = []
        for path in reversed(chain):
            tick()
            info = _observed(path)
            if not stat.S_ISDIR(info.st_mode):
                raise MeasurementError("not_directory")
            ancestors.append((path, _identity(info)))
        if ancestors[-1][1] != expected_identity:
            raise MeasurementError("root_changed")
        device = expected_identity[0]
        pending = [(root, 0)]
        observations = []
        identities = set()
        files = directories = total = discovered = 0
        while pending:
            tick()
            path, depth = pending.pop()
            info = _observed(path)
            identity = _identity(info)
            if info.st_dev != device:
                raise MeasurementError("different_volume")
            if identity in identities:
                raise MeasurementError("identity_alias")
            identities.add(identity)
            observations.append((path, _fingerprint(info)))
            if stat.S_ISREG(info.st_mode):
                files += 1
                total += info.st_size
                if total > limits.logical_bytes:
                    raise MeasurementError("logical_limit")
                continue
            directories += 1
            with os.scandir(path) as entries:
                for entry in entries:
                    tick()
                    discovered += 1
                    if discovered + 1 > limits.entries:
                        raise MeasurementError("entry_limit")
                    if depth + 1 > limits.depth:
                        raise MeasurementError("depth_limit")
                    if (entry.name in ("", ".", "..") or
                            ntpath.isreserved(entry.name) or
                            "\\" in entry.name or "/" in entry.name or
                            entry.name != unicodedata.normalize("NFC", entry.name)):
                        raise MeasurementError("unsafe_name")
                    pending.append((ntpath.join(path, entry.name), depth + 1))
        # Sample free space only after complete enumeration. No payload reads.
        tick()
        free = shutil.disk_usage(root).free
        if type(free) is not int or free < 0:
            raise MeasurementError("invalid_free_bytes")
        for path, before in observations:
            tick()
            if _fingerprint(_observed(path)) != before:
                raise MeasurementError("tree_changed")
        for path, identity in ancestors:
            tick()
            info = _observed(path)
            if not stat.S_ISDIR(info.st_mode) or _identity(info) != identity:
                raise MeasurementError("ancestor_changed")
        return Measurement(expected_identity, files, directories, total, free)
    except MeasurementError:
        raise
    except (OSError, ValueError, UnicodeError):
        raise MeasurementError("filesystem_read") from None

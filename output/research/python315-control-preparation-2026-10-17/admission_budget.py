"""Pure admission arithmetic for the reviewed research envelope, not a quota.

The caller supplies fresh owned-tree logical bytes and same-volume free bytes.
This module neither measures those values nor authenticates their provenance,
reserves disk blocks, serializes competing writers, writes files or starts work.
All trial commands and ownership/process controls still require separate review.
"""
from dataclasses import dataclass


MIB = 1024 * 1024
RETAINED_LIMIT = 512 * MIB
FREE_FLOOR = 1024 * MIB
STEP_OVERHEAD = 64 * MIB


class BudgetError(ValueError):
    """Fixed rejection category; no machine or untrusted path in diagnostics."""


def _count(value):
    if type(value) is not int or value < 0:
        raise BudgetError("invalid_count")
    return value


@dataclass(frozen=True)
class PlannedWrite:
    bytes_per_copy: int
    copies: int = 1


@dataclass(frozen=True)
class Reservation:
    pending_bytes: int
    projected_retained_bytes: int
    required_free_bytes: int


def admit_initial(*, free_bytes: int) -> None:
    """Require the whole reviewed allowance plus the floor before acquisition."""
    if _count(free_bytes) < RETAINED_LIMIT + FREE_FLOOR:
        raise BudgetError("free_floor")


def check_measured(*, retained_bytes: int, free_bytes: int) -> None:
    """Post-stage measured stop; equality is allowed, over-budget is not."""
    if _count(retained_bytes) > RETAINED_LIMIT:
        raise BudgetError("retained_limit")
    if _count(free_bytes) < FREE_FLOOR:
        raise BudgetError("free_floor")


def reserve_step(*, retained_bytes: int, free_bytes: int,
                 writes: tuple[PlannedWrite, ...]) -> Reservation:
    """Conservatively admit declared future writes plus 64MiB overhead.

    Already-retained bytes are counted once. The plan's two pending expanded
    copies must be supplied as copies=2, alongside any not-yet-retained archive,
    output, environment and log bytes. Omitting a write invalidates admission.
    This is a calculation from a snapshot, not a physical or concurrent quota.
    """
    check_measured(retained_bytes=retained_bytes, free_bytes=free_bytes)
    if type(writes) is not tuple:
        raise BudgetError("invalid_writes")
    pending = STEP_OVERHEAD
    for write in writes:
        if type(write) is not PlannedWrite:
            raise BudgetError("invalid_writes")
        if type(write.copies) is not int or write.copies < 1:
            raise BudgetError("invalid_count")
        pending += _count(write.bytes_per_copy) * write.copies
    projected = retained_bytes + pending
    required_free = FREE_FLOOR + pending
    if projected > RETAINED_LIMIT:
        raise BudgetError("retained_limit")
    if free_bytes < required_free:
        raise BudgetError("free_floor")
    return Reservation(pending, projected, required_free)

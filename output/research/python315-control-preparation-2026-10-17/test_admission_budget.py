"""Boundary arithmetic only; no disk allocation, downloads, trial or subprocess."""
import unittest

from admission_budget import (BudgetError, PlannedWrite, admit_initial,
                              check_measured, reserve_step)


class AdmissionBudgetTests(unittest.TestCase):
    def test_initial_requires_full_allowance_and_floor(self):
        admit_initial(free_bytes=1610612736)
        with self.assertRaisesRegex(BudgetError, "^free_floor$"):
            admit_initial(free_bytes=1610612735)

    def test_two_pending_expanded_copies_and_download_are_reserved(self):
        # 128MiB retained; 16MiB download + 2*100MiB expansion +64MiB
        # overhead = 280MiB pending, 408MiB projected, 1304MiB free needed.
        result = reserve_step(retained_bytes=134217728, free_bytes=1367343104,
                              writes=(PlannedWrite(16777216), PlannedWrite(104857600, 2)))
        self.assertEqual(result.pending_bytes, 293601280)
        self.assertEqual(result.projected_retained_bytes, 427819008)
        self.assertEqual(result.required_free_bytes, 1367343104)

    def test_one_byte_less_free_cannot_spend_the_floor(self):
        with self.assertRaisesRegex(BudgetError, "^free_floor$"):
            reserve_step(retained_bytes=134217728, free_bytes=1367343103,
                         writes=(PlannedWrite(16777216), PlannedWrite(104857600, 2)))

    def test_retained_cap_is_separate_from_free_capacity(self):
        with self.assertRaisesRegex(BudgetError, "^retained_limit$"):
            reserve_step(retained_bytes=268435456, free_bytes=2147483648,
                         writes=(PlannedWrite(104857600, 2),))

    def test_exact_retained_boundary_and_overhead_only_step(self):
        result = reserve_step(retained_bytes=469762048, free_bytes=1140850688, writes=())
        self.assertEqual(result.projected_retained_bytes, 536870912)
        self.assertEqual(result.pending_bytes, 67108864)
        with self.assertRaisesRegex(BudgetError, "^retained_limit$"):
            reserve_step(retained_bytes=469762049, free_bytes=2147483648, writes=())

    def test_post_stage_checks_do_not_reuse_a_prior_admission(self):
        check_measured(retained_bytes=536870912, free_bytes=1073741824)
        for retained, free, error in ((536870913, 2147483648, "retained_limit"),
                                      (1, 1073741823, "free_floor")):
            with self.subTest(error=error), self.assertRaisesRegex(BudgetError, "^" + error + "$"):
                check_measured(retained_bytes=retained, free_bytes=free)

    def test_invalid_or_negative_counts_cannot_reduce_reservations(self):
        for bad in (True, -1, 1.5, "1", None):
            with self.subTest(value=bad), self.assertRaisesRegex(BudgetError, "^invalid_count$"):
                admit_initial(free_bytes=bad)
        for writes in ([PlannedWrite(1)], (1,), (PlannedWrite(-1),),
                       (PlannedWrite(1, 0),), (PlannedWrite(1, True),)):
            with self.subTest(writes=writes), self.assertRaises(BudgetError):
                reserve_step(retained_bytes=0, free_bytes=2147483648, writes=writes)


if __name__ == "__main__":
    unittest.main()

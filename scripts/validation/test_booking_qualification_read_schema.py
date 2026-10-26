"""Qualification-read representation boundary only; no GET/PATCH/runtime proof."""
import copy
import json
from pathlib import Path
import unittest

from jsonschema import Draft202012Validator
from referencing import Resource

from scripts.validation import test_booking_qualification_schema as qualification_fixture
from scripts.validation import test_process_value_schema as common_fixture

CONTRACTS = Path(__file__).resolve().parents[2] / "docs/phase-1-architecture/contracts"
LINEAGE = "919108f7-52d1-4320-9bac-f847db4148a8"


class QualificationReadShapeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        fixture = common_fixture.ProcessValueShapeTests
        fixture.setUpClass()
        registry = fixture.registry
        for name in ("booking-creation-request.schema.json", "chat-creation-request.schema.json",
                     "booking-qualification.schema.json", "booking-qualification-read.schema.json"):
            path = CONTRACTS / name
            schema = json.loads(path.read_text(encoding="utf-8"))
            Draft202012Validator.check_schema(schema)
            registry = registry.with_resource(path.as_uri(), Resource.from_contents(schema))
        uri = (CONTRACTS / "booking-qualification-read.schema.json").as_uri()
        cls.response = Draft202012Validator(
            {"$ref": uri + "#/$defs/response"}, registry=registry, format_checker=fixture.checker)
        cls.root = Draft202012Validator(
            {"$ref": uri}, registry=registry, format_checker=fixture.checker)

    def snapshot(self):
        submission = qualification_fixture.BookingQualificationShapeTests().submission()
        consent = submission["consent"]
        return {
            "kind": "qualification_review", "lineage_id": LINEAGE, "revision": 7,
            "qualification": submission["qualification"],
            "purpose_reference": {
                "purpose_key": consent["purpose_key"],
                "notice_reference": consent["notice_reference"],
            },
        }

    def test_complete_snapshot_and_three_fixed_errors(self):
        self.assertTrue(self.response.is_valid(self.snapshot()))
        for code, recovery in (
                ("INVALID_REQUEST", "correct_request"), ("ACCESS_UNAVAILABLE", "contact"),
                ("SERVICE_UNAVAILABLE", "refresh_review")):
            value = {"state": "unavailable", "code": code, "recovery": recovery}
            with self.subTest(code=code):
                self.assertTrue(self.response.is_valid(value))
                self.assertFalse(self.response.is_valid(dict(value, recovery="retry_forever")))
                self.assertFalse(self.response.is_valid(dict(value, reason="expired-proof")))
                self.assertFalse(self.response.is_valid(dict(value, lineage_id=LINEAGE)))

    def test_snapshot_is_whole_and_closed_at_each_private_boundary(self):
        snapshot = self.snapshot()
        for field in ("kind", "lineage_id", "revision", "qualification", "purpose_reference"):
            changed = copy.deepcopy(snapshot)
            del changed[field]
            with self.subTest(missing=field):
                self.assertFalse(self.response.is_valid(changed))
        for field in ("email", "organization", "role", "desired_outcome", "wing_key", "timing"):
            changed = self.snapshot()
            del changed["qualification"][field]
            with self.subTest(qualification_missing=field):
                self.assertFalse(self.response.is_valid(changed))
        for target, field in (("qualification", "budget"), ("qualification", "owner_id"),
                              ("purpose_reference", "decision"), ("purpose_reference", "recorded_at")):
            changed = self.snapshot()
            changed[target][field] = "untrusted"
            self.assertFalse(self.response.is_valid(changed), (target, field))

    def test_read_does_not_deliver_client_base_grants_or_operation_details(self):
        for field in ("state", "edit_base_revision", "latest_observed_revision", "can_edit",
                      "operation_id", "expected_revision", "consent", "verified", "challenge",
                      "proof", "csrf_token", "expires_at", "provider", "staff_id"):
            changed = self.snapshot()
            changed[field] = "untrusted"
            with self.subTest(field=field):
                self.assertFalse(self.response.is_valid(changed))

    def test_read_is_not_mutation_receipt_request_or_minimal_status(self):
        submission = qualification_fixture.BookingQualificationShapeTests().submission()
        values = (submission,
                  {"kind": "reconcile_qualification", "operation_id": submission["operation_id"]},
                  {"state": "applied", "operation_id": submission["operation_id"], "applied_revision": 8},
                  {"state": "pending", "operation_id": submission["operation_id"]},
                  {"lineage_id": LINEAGE, "lineage": {"revision": 7, "state": "VERIFIED"},
                   "booking": {"current_occurrence": None}})
        for value in values:
            with self.subTest(value=value):
                self.assertFalse(self.response.is_valid(value))
        for value in (self.snapshot(), {}, None, "", b""):
            self.assertFalse(self.root.is_valid(value))
        for value in ({}, None, "", []):
            self.assertFalse(self.response.is_valid(value))

    def test_shared_uuid_revision_and_reference_shapes_are_enforced(self):
        for revision in (0, True, "7", 9007199254740992):
            changed = self.snapshot()
            changed["revision"] = revision
            self.assertFalse(self.response.is_valid(changed), revision)
        for revision in (1, 9007199254740991):
            changed = self.snapshot()
            changed["revision"] = revision
            self.assertTrue(self.response.is_valid(changed))
        for lineage in (LINEAGE.upper(), LINEAGE + "\n", None):
            changed = self.snapshot()
            changed["lineage_id"] = lineage
            self.assertFalse(self.response.is_valid(changed), lineage)
        for field in ("purpose_key", "notice_reference"):
            changed = self.snapshot()
            del changed["purpose_reference"][field]
            self.assertFalse(self.response.is_valid(changed), field)
        for field in ("notice_id", "notice_revision", "notice_sha256"):
            changed = self.snapshot()
            del changed["purpose_reference"]["notice_reference"][field]
            self.assertFalse(self.response.is_valid(changed), field)
        changed = self.snapshot()
        changed["purpose_reference"]["notice_reference"]["notice_sha256"] = "A" * 64
        self.assertFalse(self.response.is_valid(changed))

    def test_existing_qualification_bounds_are_reused_without_extra_fields(self):
        for field, maximum in (("email", 320), ("organization", 200), ("role", 200),
                               ("desired_outcome", 2000)):
            changed = self.snapshot()
            changed["qualification"][field] = "x" * maximum
            self.assertTrue(self.response.is_valid(changed), field)
            changed["qualification"][field] += "x"
            self.assertFalse(self.response.is_valid(changed), field)
        changed = self.snapshot()
        changed["qualification"]["timing"]["description"] = "x" * 500
        self.assertTrue(self.response.is_valid(changed))
        changed["qualification"]["timing"]["description"] += "x"
        self.assertFalse(self.response.is_valid(changed))
        changed = self.snapshot()
        changed["qualification"]["wing_key"] = "ROUTE-WING-OTHER"
        self.assertFalse(self.response.is_valid(changed))

    def test_notice_and_purpose_are_references_not_new_decisions_or_history(self):
        for extra in ("decision", "history", "basis", "recorded_at", "grant_id"):
            changed = self.snapshot()
            changed["purpose_reference"][extra] = "private"
            self.assertFalse(self.response.is_valid(changed), extra)
        changed = self.snapshot()
        changed["purpose_reference"]["notice_reference"]["text"] = "private"
        self.assertFalse(self.response.is_valid(changed))
        changed = self.snapshot()
        changed["purpose_reference"]["purpose_key"] = ""
        self.assertFalse(self.response.is_valid(changed))

    def test_shape_does_not_prove_admission_purpose_currentness_or_rebase(self):
        changed = self.snapshot()
        changed["qualification"]["email"] = "not-an-email"
        changed["purpose_reference"]["purpose_key"] = "syntactically_valid_unapproved_purpose"
        self.assertTrue(self.response.is_valid(changed))
        # No validator assertion can establish a current revision or UI edit-base relation.
        changed["revision"] = 1
        self.assertTrue(self.response.is_valid(changed))


if __name__ == "__main__":
    unittest.main()

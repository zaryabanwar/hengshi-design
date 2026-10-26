"""Operator-read representation boundaries only; no staff query/cursor security proof."""
import base64
import copy
import json
from pathlib import Path
import unittest

from jsonschema import Draft202012Validator, FormatChecker
from referencing import Resource

from scripts.validation import test_process_value_schema as common_fixture


CONTRACTS = Path(__file__).resolve().parents[2] / "docs/phase-1-architecture/contracts"
ID = "10286f82-cad4-4b14-a76a-e60d6c09ca09"
WHEN = "2041-02-03T04:05:06.125Z"
# Public synthetic envelope: base64url('f') and 32 zero bytes. Never issued/signed.
TOKEN = "q1.Zg." + "A" * 43


class OperatorReadShapeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        fixture = common_fixture.ProcessValueShapeTests
        fixture.setUpClass()
        registry = fixture.registry
        for name in ("booking-status-response.schema.json", "operator-read.schema.json"):
            path = CONTRACTS / name
            schema = json.loads(path.read_text(encoding="utf-8"))
            Draft202012Validator.check_schema(schema)
            registry = registry.with_resource(path.as_uri(), Resource.from_contents(schema))
        cls.registry = registry
        cls.checker = FormatChecker(formats=["uuid", "date-time"])
        if (cls.checker.conforms("not-a-uuid", "uuid") or
                cls.checker.conforms("2041-02-31T04:05:06.125Z", "date-time")):
            raise RuntimeError("Required UUID/calendar assertion unavailable")
        cls.uri = (CONTRACTS / "operator-read.schema.json").as_uri()

    def validator(self, name=None):
        uri = self.uri if name is None else self.uri + "#/$defs/" + name
        return Draft202012Validator({"$ref": uri}, registry=self.registry,
                                    format_checker=self.checker)

    def item(self, family):
        common = {"revision": 7, "recorded_at": WHEN}
        if family == "handoff":
            return dict(common, handoff_id=ID, wing_key=None)
        if family == "alert":
            return dict(common, intent_id=ID, origin="booking", issue_class="ACTION_REQUIRED")
        return dict(common, exception_id=ID, lineage_id=ID, issue_class="MISMATCH")

    def page(self, family="handoff", count=1, limit=25, more=False):
        kinds = {"handoff": "handoff_queue", "alert": "alert_exceptions",
                 "booking_exception": "booking_exceptions"}
        return {"kind": kinds[family],
                "items": [self.item(family) for _ in range(count)],
                "page": {"limit": limit, "has_more": more,
                         "next_cursor": TOKEN if more else None, "consistency": "live"}}

    def payload(self):
        return {"protocol": 1, "filter": None, "limit": 25,
                "ceiling": {"recorded_at": WHEN, "item_id": ID},
                "after": {"recorded_at": WHEN, "item_id": ID},
                "issued_at": WHEN, "expires_at": "2041-02-03T04:15:06.125Z"}

    def test_each_response_accepts_only_its_own_minimal_page_and_fixed_errors(self):
        for family in ("handoff", "alert", "booking_exception"):
            validator = self.validator(family + "_response")
            self.assertTrue(validator.is_valid(self.page(family)))
            self.assertTrue(validator.is_valid(self.page(family, count=0)))
            for other in ("handoff", "alert", "booking_exception"):
                if other != family:
                    self.assertFalse(validator.is_valid(self.page(other)))
            for code, recovery in (("invalid_request", "correct_request"),
                                   ("request_denied", "check_access"),
                                   ("page_changed", "restart_view"),
                                   ("request_limited", "wait"),
                                   ("service_unavailable", "refresh_view"),
                                   ("internal_error", "refresh_view")):
                value = {"code": code, "recovery": recovery}
                self.assertTrue(validator.is_valid(value))
                self.assertFalse(validator.is_valid(dict(value, reason="expired-source")))
                self.assertFalse(validator.is_valid(dict(value, recovery="auto_retry")))
            self.assertFalse(validator.is_valid({"code": "not_found", "recovery": "contact"}))

    def test_page_cardinality_and_next_cursor_follow_limit_and_lookahead_shape(self):
        validator = self.validator("handoff_response")
        for limit in range(1, 26):
            with self.subTest(limit=limit):
                self.assertTrue(validator.is_valid(self.page(count=limit, limit=limit, more=True)))
                self.assertFalse(validator.is_valid(self.page(count=limit - 1, limit=limit, more=True)))
                self.assertFalse(validator.is_valid(self.page(count=limit + 1, limit=limit)))
                # A full final page is legitimate; schema cannot prove actual lookahead.
                self.assertTrue(validator.is_valid(self.page(count=limit, limit=limit)))
        for more, token in ((True, None), (False, TOKEN)):
            value = self.page(count=1, limit=1, more=more)
            value["page"]["next_cursor"] = token
            self.assertFalse(validator.is_valid(value))
        for limit in (0, 26, -1, 1.5, True, "25", None):
            value = self.page()
            value["page"]["limit"] = limit
            self.assertFalse(validator.is_valid(value))
        value = self.page()
        value["page"]["consistency"] = "snapshot"
        self.assertFalse(validator.is_valid(value))

    def test_required_fields_and_closed_private_projection_at_every_level(self):
        for family in ("handoff", "alert", "booking_exception"):
            validator = self.validator(family + "_response")
            value = self.page(family)
            for path in ((), ("page",), ("items", 0)):
                target = value
                for key in path:
                    target = target[key]
                for key in tuple(target):
                    changed = copy.deepcopy(value)
                    branch = changed
                    for part in path:
                        branch = branch[part]
                    del branch[key]
                    self.assertFalse(validator.is_valid(changed), (family, path, key))
                for key in ("email", "name", "qualification", "transcript", "provider",
                            "staff_id", "total", "denied_count", "role", "can_accept",
                            "reason", "csrf_token", "proof", "meeting_url", "operation_id"):
                    changed = copy.deepcopy(value)
                    branch = changed
                    for part in path:
                        branch = branch[part]
                    branch[key] = "forbidden"
                    self.assertFalse(validator.is_valid(changed), (family, path, key))

    def test_reused_id_revision_and_calendar_boundaries(self):
        validator = self.validator("handoff_response")
        for field, invalid in (("handoff_id", ID.upper()), ("handoff_id", ID + "\n"),
                               ("revision", 0), ("revision", True),
                               ("revision", 9007199254740992),
                               ("recorded_at", "2041-02-31T04:05:06.125Z"),
                               ("recorded_at", "2041-02-03T04:05:06Z"),
                               ("recorded_at", "2041-02-03T04:05:06.125+00:00"),
                               ("recorded_at", WHEN + "\n")):
            value = self.page()
            value["items"][0][field] = invalid
            self.assertFalse(validator.is_valid(value), (field, invalid))

    def test_classification_and_wing_domains_do_not_invent_workflow_states(self):
        for wing in (None, "ROUTE-WING-STRATEGY", "ROUTE-WING-DIGITAL", "ROUTE-WING-AI-DATA",
                     "ROUTE-WING-IMMERSIVE", "ROUTE-WING-CLOUD-TRUST"):
            value = self.page()
            value["items"][0]["wing_key"] = wing
            self.assertTrue(self.validator("handoff_response").is_valid(value))
        for family, values in (("alert", ("OUTCOME_UNKNOWN", "ACTION_REQUIRED")),
                               ("booking_exception", ("DUPLICATE", "MISSING", "MISMATCH",
                                                      "ALERT", "NO_SLOTS", "OUTCOME_UNKNOWN"))):
            for issue in values:
                value = self.page(family)
                value["items"][0]["issue_class"] = issue
                self.assertTrue(self.validator(family + "_response").is_valid(value))
            for issue in ("CONFIRMED_QUALIFIED", "resolved", "failed", "", None):
                value = self.page(family)
                value["items"][0]["issue_class"] = issue
                self.assertFalse(self.validator(family + "_response").is_valid(value))

    def test_query_directions_are_closed_and_cursor_cannot_override_first_page(self):
        for family, field, allowed, other in (
                ("handoff", "wing_key", "ROUTE-WING-DIGITAL", "origin"),
                ("alert", "origin", "booking", "issue_class"),
                ("booking_exception", "issue_class", "MISMATCH", "wing_key")):
            validator = self.validator(family + "_query")
            for value in ({}, {"limit": "1"}, {"limit": "25", field: allowed},
                          {field: allowed}, {"cursor": TOKEN}):
                self.assertTrue(validator.is_valid(value))
            for value in ({"cursor": TOKEN, "limit": "1"}, {"cursor": TOKEN, field: allowed},
                          {other: allowed}, {field: None}, {field: ""},
                          {"sort": "recorded_at"}, {"offset": "25"},
                          {"limit": 25}, {"limit": ["1", "25"]}):
                self.assertFalse(validator.is_valid(value))
            for limit in ("0", "26", "01", "+1", "1.0", "1e0", " 1", "1\n", "١"):
                self.assertFalse(validator.is_valid({"limit": limit}), limit)

    def test_cursor_lexical_profile_rejects_padding_alphabet_and_pad_bit_aliases(self):
        validator = self.validator("cursor")
        # RFC4648 known encodings; payload here intentionally need not be JSON.
        for encoded in ("Zg", "Zm8", "Zm9v", "Zm9vYg", "Zm9vYmE", "Zm9vYmFy"):
            self.assertTrue(validator.is_valid("q1." + encoded + "." + "A" * 43))
        for payload in ("", "Z", "Zh", "Zm9", "Zg==", "Zg=", "Z+", "Z/", "Zg\n"):
            self.assertFalse(validator.is_valid("q1." + payload + "." + "A" * 43), payload)
        for token in (TOKEN + "\n", " " + TOKEN, TOKEN + "=", TOKEN.replace("q1", "q2"),
                      TOKEN + ".extra", "q1.Zg." + "A" * 42,
                      "q1.Zg." + "A" * 42 + "B"):
            self.assertFalse(validator.is_valid(token), token)
        encode = lambda data: base64.urlsafe_b64encode(data).decode("ascii").rstrip("=")
        self.assertTrue(validator.is_valid("q1." + encode(b"x" * 512) + "." + "A" * 43))
        self.assertFalse(validator.is_valid("q1." + encode(b"x" * 513) + "." + "A" * 43))

    def test_route_payloads_are_closed_without_principal_or_provider_fields(self):
        for family, allowed, other in (("handoff", "ROUTE-WING-DIGITAL", "booking"),
                                      ("alert", "booking", "MISMATCH"),
                                      ("booking_exception", "MISMATCH", "ROUTE-WING-DIGITAL")):
            validator = self.validator(family + "_cursor_payload")
            self.assertTrue(validator.is_valid(self.payload()))
            value = self.payload()
            value["filter"] = allowed
            self.assertTrue(validator.is_valid(value))
            value["filter"] = other
            self.assertFalse(validator.is_valid(value))
            for field in self.payload():
                changed = self.payload()
                del changed[field]
                self.assertFalse(validator.is_valid(changed), field)
            for field in ("session_id", "principal_id", "route", "grant", "role", "email",
                          "purpose", "staff_id", "secret", "provider", "retention_expires_at"):
                changed = self.payload()
                changed[field] = "forbidden"
                self.assertFalse(validator.is_valid(changed), field)
            changed = self.payload()
            changed["after"]["revision"] = 7
            self.assertFalse(validator.is_valid(changed))

    def test_shape_explicitly_does_not_validate_mac_current_truth_or_time_order(self):
        self.assertTrue(self.validator("cursor").is_valid(TOKEN))  # Not signed or JSON.
        changed = self.payload()
        changed["expires_at"] = "2040-01-01T00:00:00.000Z"
        self.assertTrue(self.validator("handoff_cursor_payload").is_valid(changed))
        # Schema cannot prove source uniqueness, key order, real lookahead or eligibility.
        self.assertTrue(self.validator("handoff_response").is_valid(self.page(count=2)))
        value = self.page()
        value["page"]["limit"] = json.loads("25.0")
        self.assertTrue(self.validator("handoff_response").is_valid(value))
        for value in (self.page(), self.payload(), {"cursor": TOKEN}, None, {}, TOKEN):
            self.assertFalse(self.validator().is_valid(value))


if __name__ == "__main__":
    unittest.main()

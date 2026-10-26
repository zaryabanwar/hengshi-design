"""Directional session representations only; no actual JWT/session/HTTP security proof."""
import copy
import json
from pathlib import Path
import unittest

from jsonschema import Draft202012Validator, FormatChecker
from referencing import Resource

from scripts.validation import test_process_value_schema as common_fixture


CONTRACTS = Path(__file__).resolve().parents[2] / "docs/phase-1-architecture/contracts"
ID = "10286f82-cad4-4b14-a76a-e60d6c09ca09"
CSRF = "A" * 43  # Public synthetic zero bytes, not an issued or random secret.


class StaffSessionControlShapeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        fixture = common_fixture.ProcessValueShapeTests
        fixture.setUpClass()
        registry = fixture.registry
        for name in ("booking-creation-response.schema.json", "staff-session-control.schema.json"):
            path = CONTRACTS / name
            schema = json.loads(path.read_text(encoding="utf-8"))
            Draft202012Validator.check_schema(schema)
            registry = registry.with_resource(path.as_uri(), Resource.from_contents(schema))
        cls.registry = registry
        cls.checker = FormatChecker(formats=["uuid"])
        if cls.checker.conforms("not-a-uuid", "uuid"):
            raise RuntimeError("UUID assertion unavailable")
        cls.uri = (CONTRACTS / "staff-session-control.schema.json").as_uri()

    def validator(self, name=None):
        uri = self.uri if name is None else self.uri + "#/$defs/" + name
        return Draft202012Validator({"$ref": uri}, registry=self.registry,
                                    format_checker=self.checker)

    def status(self):
        return {"kind": "staff_session", "context_id": ID, "authority_revision": 3,
                "state": "current", "server_time_ms": 2000000000123,
                "idle_deadline_ms": 2000001800123, "absolute_deadline_ms": 2000028800123,
                "renewal_due_ms": 2000000900123, "token_expires_ms": 2000028800000}

    def csrf(self):
        return {"kind": "staff_csrf", "context_id": ID, "csrf_generation": 1,
                "csrf_token": CSRF}

    def claims(self):
        return {"iss": "hengshi-design-staff-v1", "aud": "hengshi-design-staff-api-v1",
                "sub": ID, "sid": "5f081ee2-4254-4aa9-8df3-08bad3d67964",
                "jti": "17bf4105-a310-4d64-8ea5-a2e4b8368ce9",
                "iat": 2000000000, "nbf": 2000000000, "exp": 2000028800}

    def test_directional_success_and_bodyless_success_separation(self):
        self.assertTrue(self.validator("status_response").is_valid(self.status()))
        self.assertTrue(self.validator("csrf_response").is_valid(self.csrf()))
        self.assertFalse(self.validator("status_response").is_valid(self.csrf()))
        self.assertFalse(self.validator("csrf_response").is_valid(self.status()))
        for name in ("renewal_request", "logout_request"):
            self.assertTrue(self.validator(name).is_valid({}))
            for value in (None, [], "", {"session_id": ID}, self.status(), self.csrf()):
                self.assertFalse(self.validator(name).is_valid(value))
        for name in ("renewal_error", "logout_error"):
            for value in ({}, None, self.status(), self.csrf(), self.claims()):
                self.assertFalse(self.validator(name).is_valid(value))
        for value in ({}, self.status(), self.csrf(), self.claims()):
            self.assertFalse(self.validator().is_valid(value))

    def test_required_closed_own_session_projections(self):
        for name, original in (("status", self.status()), ("csrf", self.csrf()),
                               ("private_claims", self.claims())):
            for field in original:
                value = dict(original)
                del value[field]
                self.assertFalse(self.validator(name).is_valid(value), (name, field))
            for field in ("name", "email", "roles", "grants", "jwt", "session_token",
                          "staff_count", "reason", "tenant", "oid", "purpose", "provider"):
                self.assertFalse(self.validator(name).is_valid(dict(original, **{field: "extra"})))
        for field in ("csrf_token", "csrf_generation"):
            self.assertFalse(self.validator("status").is_valid(dict(self.status(), **{field: CSRF})))

    def test_identifier_revision_and_state_domains(self):
        for name, field, original in (("status", "authority_revision", self.status()),
                                      ("csrf", "csrf_generation", self.csrf())):
            for bad in (ID.upper(), ID + "\n", "not-a-uuid", None, 1):
                self.assertFalse(self.validator(name).is_valid(dict(original, context_id=bad)))
            for good in (1, 9007199254740991):
                self.assertTrue(self.validator(name).is_valid(dict(original, **{field: good})))
            for bad in (0, -1, 9007199254740992, True, "1", 1.5):
                self.assertFalse(self.validator(name).is_valid(dict(original, **{field: bad})))
        self.assertTrue(self.validator("status").is_valid(dict(self.status(), state="renewal_required")))
        for bad in ("signed_out", "expired", "prior", "active", "CURRENT", None):
            self.assertFalse(self.validator("status").is_valid(dict(self.status(), state=bad)))

    def test_millisecond_and_numericdate_bounds_are_independent_shapes(self):
        for name, maximum in (("unix_milliseconds", 253402300799999),
                               ("numeric_date", 253402300799)):
            for good in (0, maximum):
                self.assertTrue(self.validator(name).is_valid(good))
            for bad in (-1, maximum + 1, True, None, "1", 1.25):
                self.assertFalse(self.validator(name).is_valid(bad))

    def test_csrf_canonical_text_has_no_jwt_or_padding_alias(self):
        for final in "AEIMQUYcgkosw048":
            self.assertTrue(self.validator("csrf").is_valid(dict(self.csrf(), csrf_token="A" * 42 + final)))
        for bad in ("A" * 42, "A" * 44, CSRF + "=", CSRF + "\n", " " + CSRF,
                    "A" * 42 + "B", "+" + "A" * 42, "a.b.c", None):
            self.assertFalse(self.validator("csrf").is_valid(dict(self.csrf(), csrf_token=bad)))

    def test_fixed_errors_and_route_exclusions(self):
        read_pairs = (("invalid_request", "correct_request"), ("request_denied", "check_access"),
                      ("request_limited", "wait"), ("service_unavailable", "check_session"),
                      ("internal_error", "check_session"))
        post_pairs = (("request_too_large", "correct_request"),
                      ("unsupported_media_type", "correct_request"))
        for name in ("status_response", "csrf_response", "renewal_error", "logout_error"):
            for code, recovery in read_pairs:
                value = {"code": code, "recovery": recovery}
                self.assertTrue(self.validator(name).is_valid(value))
                self.assertFalse(self.validator(name).is_valid(dict(value, recovery="auto_retry")))
                self.assertFalse(self.validator(name).is_valid(dict(value, reason="session_absent")))
            for code, recovery in post_pairs:
                self.assertEqual(self.validator(name).is_valid({"code": code, "recovery": recovery}),
                                 name in ("renewal_error", "logout_error"))
            changed = {"code": "session_changed", "recovery": "check_session"}
            self.assertEqual(self.validator(name).is_valid(changed), name == "renewal_error")

    def test_minimal_claims_profile_is_private_and_closed(self):
        validator = self.validator("private_claims")
        self.assertTrue(validator.is_valid(self.claims()))
        for field, bad in (("iss", "HENGSHI-DESIGN-STAFF-v1"), ("aud", ["hengshi-design-staff-api-v1"]),
                           ("aud", "*"), ("sub", ID.upper()), ("sid", ID + "\n"), ("jti", "token"),
                           ("iat", True), ("nbf", "2000000000"), ("exp", 253402300800)):
            self.assertFalse(validator.is_valid(dict(self.claims(), **{field: bad})))
        for name in ("status_response", "csrf_response", "renewal_request", "logout_request"):
            self.assertFalse(self.validator(name).is_valid(self.claims()))

    def test_shape_explicitly_does_not_prove_time_or_crypto_semantics(self):
        # Parsed integral floats can pass JSON Schema: raw numeric spelling is a separate gate.
        self.assertTrue(self.validator("numeric_date").is_valid(json.loads("1.0")))
        invalid_authority = dict(self.claims(), nbf=5, exp=0)
        self.assertTrue(self.validator("private_claims").is_valid(invalid_authority))
        wrong_clock = copy.deepcopy(self.status())
        wrong_clock["idle_deadline_ms"] = 0
        self.assertTrue(self.validator("status").is_valid(wrong_clock))
        # These accepted shapes are not valid issued credentials, eligible states or crypto proof.


if __name__ == "__main__":
    unittest.main()

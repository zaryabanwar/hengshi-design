"""IF-STAFF-09 proposed wire shapes only; no HTTP/auth/transaction proof."""
from copy import deepcopy
import json
from pathlib import Path
import random
import unittest

from jsonschema import Draft202012Validator
from referencing import Registry, Resource

ROOT = Path(__file__).resolve().parents[2]
SCHEMA = ROOT / "docs/phase-1-architecture/contracts/availability-write.schema.json"
READ_SCHEMA = SCHEMA.with_name("availability-read.schema.json")
OPERATION = "92e50e5ed07a4e3f8181ff975e889be2"
SETTING = "a" * 32  # synthetic syntax; no entropy or issued-identity claim


def command():
    return {"operation_id": OPERATION, "expected": {"state": "none"},
            "declaration": {"state": "on"}}


def current_binding(revision="1"):
    return {"state": "current", "setting_id": SETTING, "revision": revision}


def response(result):
    return {"department_id": "ROUTE-WING-STRATEGY", "operation_id": OPERATION,
            "result": result}


class AvailabilityWriteShapeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        resources = []
        write_id = None
        for path in (SCHEMA, READ_SCHEMA):
            schema = json.loads(path.read_text(encoding="utf-8"))
            Draft202012Validator.check_schema(schema)
            resource = Resource.from_contents(schema)
            resources.extend(((path.as_uri(), resource), (schema["$id"], resource)))
            if path == SCHEMA:
                write_id = schema["$id"]
        registry = Registry().with_resources(resources)
        cls.command_validator = Draft202012Validator({"$ref": write_id}, registry=registry)
        cls.response_validator = Draft202012Validator(
            {"$ref": write_id + "#/$defs/response"}, registry=registry)
        cls.revision_validator = Draft202012Validator(
            {"$ref": write_id + "#/$defs/revision"}, registry=registry)
        cls.file_command_validator = Draft202012Validator(
            {"$ref": SCHEMA.as_uri()}, registry=registry)
        cls.file_response_validator = Draft202012Validator(
            {"$ref": SCHEMA.as_uri() + "#/$defs/response"}, registry=registry)

    def assert_shape(self, validator, record, valid):
        self.assertEqual(validator.is_valid(record), valid, repr(record))

    def test_command_is_directional_and_closes_client_authority_fields(self):
        records = [command()]
        records.append(dict(command(), declaration={"state": "off"}))
        records.append(dict(command(), expected=current_binding()))
        for record in records:
            self.assert_shape(self.command_validator, record, True)
            self.assert_shape(self.file_command_validator, record, True)
            self.assert_shape(self.response_validator, record, False)
            for path in ((), ("expected",), ("declaration",)):
                changed = deepcopy(record)
                target = changed
                for key in path:
                    target = target[key]
                target["staff_id"] = "synthetic-forbidden-input"
                self.assert_shape(self.command_validator, changed, False)
        for field in ("operation_id", "expected", "declaration"):
            missing = command()
            del missing[field]
            self.assert_shape(self.command_validator, missing, False)
        for expected in ({"state": "expired"}, {}, None,
                         {"state": "none", "revision": "1"},
                         {"state": "current", "revision": "1"}):
            self.assert_shape(self.command_validator, dict(command(), expected=expected), False)
        for declaration in ({"state": "toggle"}, {"state": "on", "expires_at": "2041-02"},
                            {}, None, True):
            self.assert_shape(self.command_validator, dict(command(), declaration=declaration), False)
        for identity in (OPERATION.upper(), OPERATION + "\n", "a" * 31,
                         "a" * 33, "g" * 32, "\uff41" * 32, None, 1):
            self.assert_shape(self.command_validator, dict(command(), operation_id=identity), False)

    def test_revision_bound_uses_independent_integer_oracle(self):
        # The oracle is arithmetic, not a copy of the schema's lexical alternatives.
        ceiling = 2 ** 64 - 1
        values = {0, 1, 2 ** 53 - 1, 2 ** 53, 2 ** 53 + 1,
                  ceiling - 1, ceiling, ceiling + 1, 10 ** 20}
        for exponent in range(21):
            values.update((10 ** exponent - 1, 10 ** exponent, 10 ** exponent + 1))
        # Exercise every twenty-digit decimal threshold and its adjacent values.
        for digits in range(1, 21):
            step = 10 ** (20 - digits)
            threshold = (ceiling // step) * step
            values.update((threshold - 1, threshold, threshold + 1))
        rng = random.Random(9009)
        values.update(rng.randrange(10 ** 19, 10 ** 20) for _ in range(200))
        for value in sorted(values):
            self.assert_shape(self.revision_validator, str(value), 1 <= value <= ceiling)
        for value in (1, True, None, "", "00", "01", "-1", "+1", "1.0", "1e0",
                      " 1", "1 ", "1\n", "\u0661", "\uff11"):
            self.assert_shape(self.revision_validator, value, False)

    def test_outcome_binding_and_private_projection(self):
        results = [
            {"state": "declared", "binding": current_binding()},
            {"state": "withdrawn", "binding": current_binding()},
            {"state": "withdrawn", "binding": {"state": "none"}},
            {"state": "pending", "recovery": "reconcile_same_operation"},
        ]
        for result in results:
            record = response(result)
            self.assert_shape(self.response_validator, record, True)
            self.assert_shape(self.file_response_validator, record, True)
            self.assert_shape(self.command_validator, record, False)
            paths = [(), ("result",)]
            if "binding" in result:
                paths.append(("result", "binding"))
            for path in paths:
                changed = deepcopy(record)
                target = changed
                for key in path:
                    target = target[key]
                target["expires_at"] = "2041-02-03T04:05:06Z"
                self.assert_shape(self.response_validator, changed, False)
        for result in ({"state": "declared", "binding": {"state": "none"}},
                       {"state": "pending", "binding": current_binding()},
                       {"state": "pending", "recovery": "retry_new_operation"},
                       {"state": "available"}, {"state": "withdrawn"}):
            self.assert_shape(self.response_validator, response(result), False)
        for key in ("ROUTE-WING-DIGITAL", "ROUTE-WING-AI-DATA", "ROUTE-WING-IMMERSIVE",
                    "ROUTE-WING-CLOUD-TRUST"):
            self.assert_shape(self.response_validator, dict(response(results[0]), department_id=key), True)
        self.assert_shape(self.response_validator,
                          dict(response(results[0]), department_id="synthetic-private-department"), False)

    def test_error_recovery_correlations_and_binding_disclosure(self):
        # Expected alternatives are read from the reviewed HTTP proposal, not the schema.
        pairs = (
            ("invalid_request", "correct_request"), ("authentication_required", "authenticate"),
            ("request_denied", "stop"), ("scope_unavailable", "stop"),
            ("operation_conflict", "stop"), ("request_too_large", "correct_request"),
            ("unsupported_media", "correct_request"), ("request_limited", "wait_same_operation"),
            ("outcome_unresolved", "reconcile_same_operation"),
            ("service_unavailable", "wait_same_operation"),
            ("internal_error", "reconcile_same_operation"),
        )
        for code, recovery in pairs:
            error = {"code": code, "recovery": recovery}
            self.assert_shape(self.response_validator, {"error": error}, True)
            for changed in (dict(error, current=current_binding()), dict(error, diagnostic="private"),
                            {"code": code}, dict(error, recovery="invented-recovery")):
                self.assert_shape(self.response_validator, {"error": changed}, False)
        for binding in ({"state": "none"}, current_binding()):
            stale = {"code": "stale_binding", "recovery": "review_current_binding", "current": binding}
            self.assert_shape(self.response_validator, {"error": stale}, True)
            del stale["current"]
            self.assert_shape(self.response_validator, {"error": stale}, False)
        self.assert_shape(self.response_validator, {"error": {"code": "unknown", "recovery": "stop"}}, False)
        mixed = response({"state": "withdrawn", "binding": {"state": "none"}})
        mixed["error"] = {"code": "request_denied", "recovery": "stop"}
        self.assert_shape(self.response_validator, mixed, False)


if __name__ == "__main__":
    unittest.main()

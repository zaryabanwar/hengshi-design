"""Private message shape checks only; no worker/publication/authorization proof."""
import json
from pathlib import Path
import unittest

from jsonschema import Draft202012Validator, FormatChecker
from referencing import Registry, Resource

from test_publication_manifest_schema import synthetic_envelope

ROOT = Path(__file__).resolve().parents[2]
CONTRACTS = ROOT / "docs/phase-1-architecture/contracts"


def synthetic_binding():
    """Expected shapes follow the proposed contract, not schema introspection."""
    return {
        "candidate_id": "00000000-0000-0000-0000-000000000001",
        "candidate_revision": 1,
        "release_id": "synthetic_shape_fixture",
        "release_created_at": "2026-10-04T00:00:00Z",
        "content_snapshot_sha256": "1" * 64,
        "route_plan_sha256": "2" * 64,
        "derivative_plan_sha256": "3" * 64,
        "renderer_sha256": "4" * 64,
        "client_build_sha256": "5" * 64,
        "toolchain_lock_sha256": "6" * 64,
        "render_config_sha256": "7" * 64,
        "limits_profile_sha256": "8" * 64,
    }


def synthetic_message(kind):
    message = {
        "schema_version": 1,
        "kind": kind,
        "preparation_id": "00000000-0000-0000-0000-000000000002",
        "attempt_id": "00000000-0000-0000-0000-000000000003",
        "attempt_generation": 1,
        "binding": synthetic_binding(),
    }
    envelope = synthetic_envelope()
    if kind == "prepare":
        message.update({
            "public_snapshot_key": "synthetic/public-snapshot.json",
            "routes": envelope["manifest"]["routes"],
            "expected_artifacts": [
                {key: value for key, value in artifact.items()
                 if key not in ("sha256", "bytes")}
                for artifact in envelope["manifest"]["artifacts"]
            ],
        })
    elif kind == "prepared":
        message["envelope"] = envelope
    elif kind == "failed":
        message["failure"] = {"code": "render_failed"}
    return message


class PublicationPreparationShapeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        resources = []
        for filename in ("publication-preparation.schema.json",
                         "publication-manifest.schema.json"):
            path = CONTRACTS / filename
            schema = json.loads(path.read_text(encoding="utf-8"))
            Draft202012Validator.check_schema(schema)
            resources.append((path.as_uri(), Resource.from_contents(schema)))
        checker = FormatChecker(formats=["uuid", "date-time"])
        for value, format_name in (("not-a-uuid", "uuid"),
                                   ("2026-02-30T00:00:00Z", "date-time")):
            if checker.conforms(value, format_name):
                raise RuntimeError("Required format checking is unavailable")
        cls.validator = Draft202012Validator(
            {"$ref": (CONTRACTS / "publication-preparation.schema.json").as_uri()},
            registry=Registry().with_resources(resources),
            format_checker=checker,
        )

    def assert_shape_valid(self, message):
        self.assertEqual(list(self.validator.iter_errors(message)), [])

    def assert_shape_invalid(self, message):
        self.assertTrue(list(self.validator.iter_errors(message)))

    def test_request_prepared_and_closed_failure_shapes(self):
        for kind in ("prepare", "prepared", "failed"):
            with self.subTest(kind=kind):
                self.assert_shape_valid(synthetic_message(kind))
        codes = ("input_invalid", "authority_unavailable", "candidate_ineligible",
                 "cancelled", "render_failed", "artifact_mismatch",
                 "limit_exceeded", "preparation_unavailable")
        for code in codes:
            with self.subTest(code=code):
                message = synthetic_message("failed")
                message["failure"] = {"code": code, "artifact_id": "html"}
                self.assert_shape_valid(message)

    def test_closed_messages_exclude_authority_payloads_and_diagnostics(self):
        additions = (
            ((), "activate", True),
            ((), "staff_email", "synthetic@example.invalid"),
            (("binding",), "approved", True),
            (("binding",), "provider_secret", "synthetic-only"),
            (("failure",), "exception", "private diagnostic fixture"),
            (("failure",), "retryable", True),
        )
        for path, key, value in additions:
            with self.subTest(path=path, key=key):
                message = synthetic_message("failed")
                target = message
                for part in path:
                    target = target[part]
                target[key] = value
                self.assert_shape_invalid(message)
        message = synthetic_message("prepare")
        message["public_snapshot"] = {"draft": "not a permitted inline input"}
        self.assert_shape_invalid(message)

    def test_variant_payloads_and_required_binding_are_not_interchangeable(self):
        for kind, unexpected, payload in (
            ("prepare", "envelope", synthetic_envelope()),
            ("prepared", "failure", {"code": "render_failed"}),
            ("failed", "envelope", synthetic_envelope()),
        ):
            with self.subTest(kind=kind, unexpected=unexpected):
                message = synthetic_message(kind)
                message[unexpected] = payload
                self.assert_shape_invalid(message)
        for key in ("content_snapshot_sha256", "renderer_sha256",
                    "limits_profile_sha256", "candidate_revision"):
            with self.subTest(missing=key):
                message = synthetic_message("prepare")
                del message["binding"][key]
                self.assert_shape_invalid(message)

    def test_identifier_time_numeric_and_reference_shapes(self):
        changes = (
            (("preparation_id",), "not-a-uuid"),
            (("attempt_generation",), 0),
            (("attempt_generation",), "1"),
            (("binding", "candidate_revision"), 9007199254740992),
            (("binding", "release_created_at"), "2026-02-30T00:00:00Z"),
            (("binding", "release_created_at"), "2026-10-04T00:00:00+00:00"),
            (("binding", "renderer_sha256"), "4" * 64 + "\n"),
            (("public_snapshot_key",), "https://example.invalid/snapshot"),
            (("routes",), []),
            (("expected_artifacts",), []),
            (("expected_artifacts", 0, "streams"), ["UNKNOWN"]),
            (("expected_artifacts", 0, "dependencies"), ["html", "html"]),
        )
        for path, value in changes:
            with self.subTest(path=path, value=value):
                message = synthetic_message("prepare")
                target = message
                for part in path[:-1]:
                    target = target[part]
                target[path[-1]] = value
                self.assert_shape_invalid(message)
        message = synthetic_message("failed")
        message["failure"]["code"] = "unexpected_failure"
        self.assert_shape_invalid(message)
        message = synthetic_message("prepared")
        message["envelope"]["manifest"]["created_at"] = "2026-02-30T00:00:00Z"
        self.assert_shape_invalid(message)


if __name__ == "__main__":
    unittest.main()

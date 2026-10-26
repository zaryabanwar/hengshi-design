"""Definition-level shape tests; not publication approval or runtime conformance."""
import copy
import json
from pathlib import Path
import unittest

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[2]
SCHEMA = ROOT / "docs/phase-1-architecture/contracts/publication-manifest.schema.json"


def synthetic_envelope():
    """No client data, real content, provider settings or public release."""
    kinds = ("html", "metadata", "structured_data", "sitemap", "redirects",
             "knowledge", "scene_panels")
    return {
        "manifest_sha256": "0" * 64,
        "manifest": {
            "schema_version": 1,
            "release_id": "synthetic_shape_fixture",
            "created_at": "2026-10-04T00:00:00Z",
            "content_snapshot_sha256": "1" * 64,
            "routes": [{"route_id": "ROUTE_HOME", "canonical_path": "/",
                        "content_revision": "synthetic_revision",
                        "content_sha256": "2" * 64, "indexable": True}],
            "artifacts": [{"artifact_id": kind, "kind": kind,
                           "asset_key": "synthetic/" + kind + ".json",
                           "sha256": "3" * 64, "bytes": 1,
                           "route_ids": ["ROUTE_HOME"], "dependencies": [],
                           "streams": ["S-HIGH", "S-MEDIUM", "S-LOW", "S-SEMANTIC"]}
                          for kind in kinds],
        },
    }


class PublicationEnvelopeShapeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        checker = FormatChecker(formats=["date-time"])
        # A missing optional checker must fail setup, never silently accept dates.
        cls.validator = Draft202012Validator(schema, format_checker=checker)

    def test_closed_public_envelope_rejects_private_fields(self):
        instance = synthetic_envelope()
        self.assertEqual(list(self.validator.iter_errors(instance)), [])
        mutations = [
            ((), "staff_email", "synthetic@example.invalid"),
            (("manifest",), "provider_secret", "fixture_only"),
            (("manifest", "routes", 0), "draft_body", "not public"),
            (("manifest", "artifacts", 0), "conversation", "not public"),
        ]
        for path, key, value in mutations:
            with self.subTest(path=path, key=key):
                changed = copy.deepcopy(instance)
                target = changed
                for part in path:
                    target = target[part]
                target[key] = value
                self.assertTrue(list(self.validator.iter_errors(changed)))

    def test_invalid_identity_and_storage_shapes_rejected(self):
        mutations = [
            (("manifest_sha256",), "bad-digest"),
            (("manifest_sha256",), "0" * 64 + "\n"),
            (("manifest", "release_id"), "synthetic_release\n"),
            (("manifest", "routes", 0, "canonical_path"), "/services\n"),
            (("manifest", "artifacts", 0, "asset_key"), "synthetic/html.json\n"),
            (("manifest", "schema_version"), 2),
            (("manifest", "created_at"), "not-a-date"),
            (("manifest", "created_at"), "2026-02-30T00:00:00Z"),
            (("manifest", "created_at"), "2026-10-04T25:00:00Z"),
            (("manifest", "created_at"), "2026-10-04T00:00:00"),
            (("manifest", "routes", 0, "canonical_path"), "https://example.invalid"),
            (("manifest", "artifacts", 0, "asset_key"), "https://example.invalid/private"),
            (("manifest", "artifacts", 0, "asset_key"), "assets/%2e%2e/private"),
            (("manifest", "artifacts", 0, "bytes"), 0),
            (("manifest", "artifacts", 0, "streams"), ["UNDECLARED"]),
        ]
        for path, value in mutations:
            with self.subTest(path=path):
                changed = synthetic_envelope()
                target = changed
                for part in path[:-1]:
                    target = target[part]
                target[path[-1]] = value
                self.assertTrue(list(self.validator.iter_errors(changed)))


if __name__ == "__main__":
    unittest.main()

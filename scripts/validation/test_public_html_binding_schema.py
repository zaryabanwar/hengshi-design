"""Closed binding shape evidence only; no HTML/parser/build/runtime proof."""
from copy import deepcopy
import json
from pathlib import Path
import unittest

from jsonschema import Draft202012Validator
from referencing import Registry, Resource


ROOT = Path(__file__).resolve().parents[2]
SCHEMA = ROOT / "docs/phase-1-architecture/contracts/public-html-binding.schema.json"
PUBLICATION = ROOT / "docs/phase-1-architecture/contracts/publication-manifest.schema.json"


def synthetic_binding():
    return {
        "schema_version": 1, "release_id": "synthetic-release",
        "route_id": "synthetic-route", "canonical_path": "/services",
        "html_artifact_id": "synthetic-html", "client_build_sha256": "a" * 64,
    }


class PublicHtmlBindingShapeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        resources = []
        for path in (SCHEMA, PUBLICATION):
            schema = json.loads(path.read_text(encoding="utf-8"))
            Draft202012Validator.check_schema(schema)
            resources.append((path.as_uri(), Resource.from_contents(schema)))
        cls.validator = Draft202012Validator(
            {"$ref": SCHEMA.as_uri()}, registry=Registry().with_resources(resources),
        )

    def assert_shape(self, record, valid):
        self.assertEqual(not list(self.validator.iter_errors(record)), valid)

    def test_valid_closed_document_context_shapes(self):
        self.assert_shape(synthetic_binding(), True)
        for path in ("/", "/services/cloud-platforms", "/work/example-1"):
            record = synthetic_binding()
            record["canonical_path"] = path
            self.assert_shape(record, True)
        record = synthetic_binding()
        for field in ("release_id", "route_id", "html_artifact_id"):
            record[field] = "A" + "_-0" * 31 + "zZ"
        self.assert_shape(record, True)  # domain only, not real registered identities

    def test_required_fields_and_extra_authority_are_rejected(self):
        for field in synthetic_binding():
            record = synthetic_binding()
            del record[field]
            self.assert_shape(record, False)
        for field in ("manifest_sha256", "html_sha256", "candidate_id", "attempt_id",
                      "script_url", "unit_ids", "selected_stream", "consent", "options"):
            record = synthetic_binding()
            record[field] = "synthetic-extra"
            self.assert_shape(record, False)
        for record in (None, [], "{}", {"binding": synthetic_binding()}):
            self.assert_shape(record, False)

    def test_scalar_domains_exclude_url_control_and_script_payloads(self):
        for field, value in (("schema_version", True), ("schema_version", 2),
                             ("client_build_sha256", "A" * 64),
                             ("client_build_sha256", "a" * 64 + "\n"),
                             ("canonical_path", "/Services"), ("canonical_path", "/a/../b"),
                             ("canonical_path", "/a?x=1"), ("canonical_path", "/a#b"),
                             ("canonical_path", "/a/"), ("canonical_path", "https://example.com/")):
            record = synthetic_binding()
            record[field] = value
            self.assert_shape(record, False)
        for field in ("release_id", "route_id", "html_artifact_id"):
            for value in (None, "", "x" * 97, "../x", "x/y", "x\\y", "x%2Fy",
                          "x\n", "x\0", "é", "</script><script>alert(1)</script>"):
                with self.subTest(field=field, value=value):
                    record = deepcopy(synthetic_binding())
                    record[field] = value
                    self.assert_shape(record, False)


if __name__ == "__main__":
    unittest.main()

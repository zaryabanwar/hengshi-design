"""Common value helper boundary only; no application admission/security proof."""
import json
from pathlib import Path
import unittest

from jsonschema import Draft202012Validator, FormatChecker
from referencing import Registry, Resource
from referencing.exceptions import NoSuchResource, Unresolvable

ROOT = Path(__file__).resolve().parents[2]
CONTRACTS = ROOT / "docs/phase-1-architecture/contracts"


def refuse_unregistered(uri):
    raise NoSuchResource(ref=uri)


class ProcessValueShapeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        resources = []
        for name in ("process-value.schema.json", "publication-preparation.schema.json",
                     "publication-manifest.schema.json"):
            path = CONTRACTS / name
            schema = json.loads(path.read_text(encoding="utf-8"))
            Draft202012Validator.check_schema(schema)
            resources.append((path.as_uri(), Resource.from_contents(schema)))
        cls.registry = Registry(retrieve=refuse_unregistered).with_resources(resources)
        cls.checker = FormatChecker(formats=["uuid"])
        if cls.checker.conforms("not-a-uuid", "uuid"):
            raise RuntimeError("Required UUID format assertion is unavailable")
        cls.module_uri = (CONTRACTS / "process-value.schema.json").as_uri()

    def validator(self, name=None):
        uri = self.module_uri if name is None else f"{self.module_uri}#/$defs/{name}"
        return Draft202012Validator({"$ref": uri}, registry=self.registry,
                                    format_checker=self.checker)

    def test_uuid_representation(self):
        validator = self.validator("uuid")
        valid = "919108f7-52d1-4320-9bac-f847db4148a8"
        self.assertTrue(validator.is_valid(valid))
        for value in (valid.upper(), " " + valid, valid + "\n", "{" + valid + "}",
                      "urn:uuid:" + valid, valid.replace("-", ""), "g" + valid[1:],
                      None, 1):
            with self.subTest(value=value):
                self.assertFalse(validator.is_valid(value))

    def test_uuid_shape_does_not_prove_allocation_or_generation(self):
        validator = self.validator("uuid")
        for value in ("00000000-0000-0000-0000-000000000000",
                      "ffffffff-ffff-ffff-ffff-ffffffffffff",
                      "019f1d32-0000-7000-8000-000000000001"):
            with self.subTest(value=value):
                self.assertTrue(validator.is_valid(value))

    def test_revision_boundaries(self):
        validator = self.validator("positive_revision")
        for value in (1, 9007199254740991):
            self.assertTrue(validator.is_valid(value))
        for value in (0, -1, 9007199254740992, 1.5, True, "1", None):
            with self.subTest(value=value):
                self.assertFalse(validator.is_valid(value))

    def test_integer_shape_is_not_raw_token_validation(self):
        self.assertTrue(self.validator("positive_revision").is_valid(json.loads("1.0")))

    def test_digest_representation(self):
        validator = self.validator("sha256")
        self.assertTrue(validator.is_valid("ab" * 32))
        for value in ("AB" * 32, "a" * 63, "a" * 65, "g" * 64, "a" * 64 + "\n",
                      " " + "a" * 64, None, {}):
            with self.subTest(value=value):
                self.assertFalse(validator.is_valid(value))

    def test_module_is_not_an_envelope(self):
        validator = self.validator()
        for value in ({}, {"uuid": "919108f7-52d1-4320-9bac-f847db4148a8"},
                      "919108f7-52d1-4320-9bac-f847db4148a8", None, 1):
            with self.subTest(value=value):
                self.assertFalse(validator.is_valid(value))

    def test_unregistered_reference_is_denied(self):
        validator = Draft202012Validator({"$ref": "https://invalid.example/schema"},
                                        registry=self.registry)
        with self.assertRaises(Unresolvable):
            validator.validate({})


if __name__ == "__main__":
    unittest.main()

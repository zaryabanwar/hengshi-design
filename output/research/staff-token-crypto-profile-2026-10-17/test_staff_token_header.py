"""Research representation tests only; never a JWT verifier or staff credential."""
import json
from pathlib import Path
import unittest

from jsonschema import Draft202012Validator


class StaffTokenHeaderTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        schema = json.loads(Path(__file__).with_name("staff-token-header.schema.json").read_text())
        Draft202012Validator.check_schema(schema)
        cls.root = Draft202012Validator(schema)
        cls.header = Draft202012Validator(schema["$defs"]["header"])

    def sample(self):
        return {"alg": "RS256", "typ": "hsd-staff+jwt", "kid": "a" * 32}

    def test_root_cannot_be_used_as_a_signed_token_or_header_validator(self):
        for instance in (None, {}, self.sample(), "not-a-token"):
            with self.subTest(instance=instance):
                self.assertFalse(self.root.is_valid(instance))

    def test_exact_closed_header_is_a_valid_candidate_shape(self):
        self.header.validate(self.sample())

    def test_other_or_missing_algorithms_are_denied(self):
        for algorithm in ("none", "HS256", "RS384", "PS256", "ES256", "rs256", None, []):
            with self.subTest(algorithm=algorithm):
                self.assertFalse(self.header.is_valid({**self.sample(), "alg": algorithm}))

    def test_other_token_types_are_not_interchangeable(self):
        for kind in ("JWT", "at+jwt", "hsd-visitor+jwt", "HSD-staff+jwt", None):
            with self.subTest(kind=kind):
                self.assertFalse(self.header.is_valid({**self.sample(), "typ": kind}))

    def test_key_identifier_is_bounded_ascii_and_not_a_url_or_path(self):
        for kid in ("a" * 31, "a" * 33, "A" * 32, "g" * 32, "a" * 32 + "\n",
                    "https://example.invalid/key", "../key", "0" * 31 + "\x00", "０" * 32, 0):
            with self.subTest(kid=kid):
                self.assertFalse(self.header.is_valid({**self.sample(), "kid": kid}))

    def test_embedded_keys_urls_extensions_and_extra_fields_are_denied(self):
        for field, value in (("jwk", {}), ("jku", "https://example.invalid"),
                             ("x5u", "https://example.invalid"), ("x5c", []),
                             ("crit", []), ("b64", False), ("cty", "JWT"), ("zip", "DEF")):
            with self.subTest(field=field):
                self.assertFalse(self.header.is_valid({**self.sample(), field: value}))

    def test_every_required_field_and_object_type_is_enforced(self):
        for field in ("alg", "typ", "kid"):
            value = self.sample()
            del value[field]
            with self.subTest(field=field):
                self.assertFalse(self.header.is_valid(value))
        for value in (None, [], "header", 1):
            self.assertFalse(self.header.is_valid(value))

    def test_shape_does_not_prove_key_registration_or_raw_duplicate_rejection(self):
        # A well-shaped invented selector is not a registered trusted key.
        self.header.validate({**self.sample(), "kid": "0" * 32})
        # A lossy decoder can hide the duplicate. Actual ingress must reject
        # this before schema/library dictionaries, independent of shape PASS.
        lossy = json.loads('{"alg":"HS256","alg":"RS256","typ":"hsd-staff+jwt","kid":"' + "a" * 32 + '"}')
        self.assertTrue(self.header.is_valid(lossy))


if __name__ == "__main__":
    unittest.main()

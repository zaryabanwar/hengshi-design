"""D-070 content-shape fixture checks; no admin/publication runtime proof."""
import copy
import json
from pathlib import Path
import unittest

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
SCHEMA = ROOT / "docs/phase-1-architecture/contracts/company-facts.schema.json"


def synthetic_facts():
    return {
        "schema_version": 1,
        "legal_name": "Synthetic Company — fixture only",
        "registration_jurisdiction": "Synthetic jurisdiction",
        "registrations": {
            "secp_cuin": "0000042",
            "pseb": {
                "identifier": "FIXTURE-42/00",
                "validity": {"precision": "month", "from_month": "2041-02", "through_month": "2042-01"},
            },
        },
        "contacts": {"contact": "contact@example.invalid"},
    }


class CompanyFactsShapeTests(unittest.TestCase):
    def test_identifiers_precision_and_workflow_separation(self):
        # The oracle is D-070's string/month/authority requirements, not schema enumeration.
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(schema)
        facts = synthetic_facts()
        roundtrip = json.loads(json.dumps(facts))
        self.assertEqual(roundtrip["registrations"]["secp_cuin"], "0000042")
        self.assertEqual(roundtrip["registrations"]["pseb"]["identifier"], "FIXTURE-42/00")
        self.assertEqual(list(validator.iter_errors(roundtrip)), [])
        no_validity = copy.deepcopy(facts)
        del no_validity["registrations"]["pseb"]["validity"]
        self.assertEqual(list(validator.iter_errors(no_validity)), [])
        mutations = [
            (("registrations", "secp_cuin"), 42),
            (("registrations", "pseb", "identifier"), 42),
            (("registrations", "pseb", "validity", "precision"), "day"),
            (("registrations", "pseb", "validity", "from_month"), "2026-07-01"),
            (("registrations", "pseb", "validity", "from_month"), "2026-00"),
            (("registrations", "pseb", "validity", "through_month"), "2027-13"),
            (("registrations", "pseb", "validity", "through_month"), "2027-06\n"),
            (("registrations", "secp_cuin"), "0000042\n"),
            (("approved",), True),
            (("registrations", "pseb", "active"), True),
            (("registrations", "pseb", "validity", "expiry_instant"), "2027-07-01T00:00:00Z"),
            (("contacts", "owner_principal"), "synthetic_staff"),
            (("provider_secret",), "fixture_only"),
        ]
        for path, value in mutations:
            with self.subTest(path=path, value=value):
                changed = copy.deepcopy(facts)
                target = changed
                for part in path[:-1]:
                    target = target[part]
                target[path[-1]] = value
                self.assertTrue(list(validator.iter_errors(changed)))
        # Syntax alone intentionally cannot prove month ordering, ownership or valid contact facts.


if __name__ == "__main__":
    unittest.main()

"""D-076 projection representations only; no publication or disclosure enforcement."""
import copy
import json
import unittest

from jsonschema import Draft202012Validator
from referencing import Registry, Resource

from scripts.validation import test_company_facts_schema as fixture
from scripts.validation.test_booking_creation_request_schema import deny_remote


class CompanyPublicProjectionShapeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        schema = json.loads(fixture.SCHEMA.read_text(encoding='utf-8'))
        Draft202012Validator.check_schema(schema)
        registry = Registry(retrieve=deny_remote).with_resource(
            schema['$id'], Resource.from_contents(schema))
        cls.private = Draft202012Validator(schema, registry=registry)
        cls.public = Draft202012Validator(
            {'$ref': schema['$id'] + '#/$defs/public_projection'}, registry=registry)

    def public_facts(self):
        return {'schema_version': 1, 'legal_name': 'Synthetic Company — fixture only',
                'registration_jurisdiction': 'Synthetic jurisdiction',
                'contacts': {'contact': 'contact@example.invalid',
                             'privacy': 'privacy@example.invalid',
                             'security': 'security@example.invalid'}}

    def test_private_facts_cannot_be_used_as_the_public_projection(self):
        private = fixture.synthetic_facts()
        private['registered_address'] = 'Fixture Street — no actual office'
        self.assertTrue(self.private.is_valid(private))
        self.assertFalse(self.public.is_valid(private))
        public = self.public_facts()
        self.assertTrue(self.public.is_valid(public))
        del public['contacts']
        self.assertTrue(self.public.is_valid(public))

    def test_deferred_fields_and_workflow_data_are_rejected_at_the_validator_boundary(self):
        forbidden = {
            'registrations': fixture.synthetic_facts()['registrations'],
            'registered_address': 'Fixture Street', 'secp_cuin': '0000042',
            'pseb_identifier': 'FIXTURE-42/00', 'validity': {'from_month': '2041-02'},
            'source_evidence': 'fixture reference', 'approved': True,
            'owner_principal': 'fixture staff', 'public_disclosure': True,
        }
        for key, value in forbidden.items():
            with self.subTest(key=key):
                self.assertFalse(self.public.is_valid({**self.public_facts(), key: value}))
        for key in ('registered_address', 'registrations', 'owner_principal', 'provider_secret'):
            value = self.public_facts()
            value['contacts'][key] = 'forbidden'
            self.assertFalse(self.public.is_valid(value))

    def test_required_types_and_the_limit_of_shape_validation(self):
        for key in ('schema_version', 'legal_name', 'registration_jurisdiction'):
            value = self.public_facts()
            del value[key]
            self.assertFalse(self.public.is_valid(value))
        for key, invalid in (('schema_version', True), ('schema_version', 2),
                             ('legal_name', ''), ('legal_name', 42),
                             ('registration_jurisdiction', 'fixture\n')):
            value = self.public_facts()
            value[key] = invalid
            self.assertFalse(self.public.is_valid(value))
        # A field allowlist cannot establish eligible contact operation or prevent
        # a forbidden fact being disguised inside an otherwise ordinary string.
        # Those are later preparation/rendering tests, not this schema's proof.
        value = copy.deepcopy(self.public_facts())
        value['legal_name'] = 'Unverified fixture label containing an excluded fact'
        value['contacts']['contact'] = 'not an operational email'
        self.assertTrue(self.public.is_valid(value))


if __name__ == '__main__':
    unittest.main()

"""Booking creation request validator boundary, never actual HTTP/admission proof."""
import copy
import json
from pathlib import Path
import unittest

from jsonschema import Draft202012Validator, FormatChecker
from referencing import Registry, Resource
from referencing.exceptions import NoSuchResource, Unresolvable

ROOT = Path(__file__).resolve().parents[2]
CONTRACTS = ROOT / 'docs/phase-1-architecture/contracts'


def deny_remote(uri):
    raise NoSuchResource(ref=uri)


class BookingCreationRequestShapeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        resources = []
        for name in ('booking-creation-request.schema.json', 'process-value.schema.json',
                     'publication-preparation.schema.json', 'publication-manifest.schema.json'):
            path = CONTRACTS / name
            data = json.loads(path.read_text(encoding='utf-8'))
            Draft202012Validator.check_schema(data)
            resources.append((path.as_uri(), Resource.from_contents(data)))
        cls.registry = Registry(retrieve=deny_remote).with_resources(resources)
        cls.uri = (CONTRACTS / 'booking-creation-request.schema.json').as_uri()
        cls.checker = FormatChecker(formats=['uuid'])
        if cls.checker.conforms('not-a-uuid', 'uuid'):
            raise RuntimeError('UUID assertion unavailable')
        cls.validator = Draft202012Validator({'$ref': cls.uri}, registry=cls.registry,
                                             format_checker=cls.checker)

    def create_request(self):
        return {'phase': 'create', 'provisional_id': '919108f7-52d1-4320-9bac-f847db4148a8',
                'operation_id': '9c3567ad-12bf-4b3a-a76d-7e56b9dfe051'}

    def test_bootstrap_admits_only_explicit_phase(self):
        self.assertTrue(self.validator.is_valid({'phase': 'bootstrap'}))
        for key, value in (('email', 'person@example.invalid'), ('message', 'hello'),
                           ('provisional_id', self.create_request()['provisional_id']),
                           ('operation_id', self.create_request()['operation_id']),
                           ('csrf_token', 'not-a-token'), ('consent', True)):
            with self.subTest(key=key):
                self.assertFalse(self.validator.is_valid({'phase': 'bootstrap', key: value}))

    def test_create_requires_all_nonsecret_references(self):
        request = self.create_request()
        self.assertTrue(self.validator.is_valid(request))
        for key in ('phase', 'provisional_id', 'operation_id'):
            with self.subTest(key=key):
                invalid = copy.deepcopy(request)
                del invalid[key]
                self.assertFalse(self.validator.is_valid(invalid))

    def test_create_does_not_accept_private_or_server_fields(self):
        for key in ('email', 'qualification', 'consent', 'marketing_permission', 'context',
                    'chat_session_id', 'lineage_id', 'staff_id', 'proof', 'csrf_token',
                    'expires_at', 'confirmed', 'provider_result'):
            with self.subTest(key=key):
                request = self.create_request()
                request[key] = 'untrusted'
                self.assertFalse(self.validator.is_valid(request))

    def test_references_reject_coercion_and_noncanonical_text(self):
        for key in ('provisional_id', 'operation_id'):
            valid = self.create_request()[key]
            for value in (None, 1, True, {}, [], valid.upper(), ' ' + valid, valid + '\n',
                          '{' + valid + '}', 'urn:uuid:' + valid, valid.replace('-', ''), 'not-an-id'):
                with self.subTest(key=key, value=value):
                    request = self.create_request()
                    request[key] = value
                    self.assertFalse(self.validator.is_valid(request))

    def test_operation_uuid_version_and_variant_are_specific(self):
        for value in ('019f1d32-0000-7000-8000-000000000001',
                      '9c3567ad-12bf-4b3a-c76d-7e56b9dfe051',
                      '00000000-0000-0000-0000-000000000000',
                      'ffffffff-ffff-ffff-ffff-ffffffffffff'):
            with self.subTest(value=value):
                request = self.create_request()
                request['operation_id'] = value
                self.assertFalse(self.validator.is_valid(request))

    def test_closed_phases_and_root_types(self):
        for value in ({}, {'phase': 'reconcile'}, {'phase': 'Bootstrap'},
                      {'phase': None}, [], None, True, 1, 'bootstrap'):
            with self.subTest(value=value):
                self.assertFalse(self.validator.is_valid(value))

    def test_shape_does_not_establish_allocation_or_distinct_identity(self):
        request = self.create_request()
        request['provisional_id'] = request['operation_id']
        self.assertTrue(self.validator.is_valid(request))
        # A valid shape, even equal texts, still requires separate family/issuer/current-proof checks.
        request['provisional_id'] = '00000000-0000-0000-0000-000000000000'
        self.assertTrue(self.validator.is_valid(request))

    def test_unregistered_reference_cannot_fetch_a_remote_schema(self):
        validator = Draft202012Validator({'$ref': 'https://example.invalid/missing.schema.json'},
                                         registry=self.registry, format_checker=self.checker)
        with self.assertRaises(Unresolvable):
            validator.is_valid(self.create_request())


if __name__ == '__main__':
    unittest.main()

"""Server response schema boundary only; no actual HTTP or proof enforcement."""
import copy
import json
from pathlib import Path
import unittest

from jsonschema import Draft202012Validator
from referencing import Resource

from scripts.validation import test_booking_creation_request_schema as request_fixture

CONTRACTS = Path(__file__).resolve().parents[2] / 'docs/phase-1-architecture/contracts'


class BookingCreationResponseShapeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        fixture = request_fixture.BookingCreationRequestShapeTests
        fixture.setUpClass()
        path = CONTRACTS / 'booking-creation-response.schema.json'
        schema = json.loads(path.read_text(encoding='utf-8'))
        Draft202012Validator.check_schema(schema)
        registry = fixture.registry.with_resource(path.as_uri(), Resource.from_contents(schema))
        cls.validator = Draft202012Validator({'$ref': path.as_uri()}, registry=registry,
                                             format_checker=fixture.checker)
        cls.request = fixture().create_request()

    def provisional(self):
        return {'phase': 'bootstrap', 'state': 'provisional',
                'provisional_id': self.request['provisional_id'],
                'proof_generation': 1, 'csrf_token': 'A' * 43}

    def created(self):
        return {'phase': 'create', 'state': 'created',
                'provisional_id': self.request['provisional_id'],
                'operation_id': self.request['operation_id'],
                'lineage_id': '10286f82-cad4-4b14-a76a-e60d6c09ca09',
                'proof_generation': 2, 'csrf_token': 'A' * 43}

    def pending(self):
        return {'phase': 'create', 'state': 'pending', **{
            key: self.request[key] for key in ('provisional_id', 'operation_id')}}

    def test_three_success_projections_require_their_distinct_fields(self):
        for value in (self.provisional(), self.created(), self.pending()):
            self.assertTrue(self.validator.is_valid(value))
            for key in value:
                with self.subTest(state=value['state'], missing=key):
                    invalid = copy.deepcopy(value)
                    del invalid[key]
                    self.assertFalse(self.validator.is_valid(invalid))

    def test_phase_and_outcome_cannot_be_mixed(self):
        for value in (self.provisional(), self.created(), self.pending()):
            for state in ('confirmed', 'qualified', 'BOOKING_PENDING', 'denied', ''):
                self.assertFalse(self.validator.is_valid({**value, 'state': state}))
            self.assertFalse(self.validator.is_valid({**value, 'phase': 'other'}))
        self.assertFalse(self.validator.is_valid({**self.created(), 'phase': 'bootstrap'}))
        self.assertFalse(self.validator.is_valid({**self.provisional(), 'phase': 'create'}))

    def test_private_payload_and_bearer_echoes_are_closed_out(self):
        for value in (self.provisional(), self.created(), self.pending()):
            for key in ('email', 'qualification', 'history', 'staff', 'secret',
                        'cookie', 'provider_confirmation', 'verified', 'consent'):
                self.assertFalse(self.validator.is_valid({**value, key: 'forbidden'}))
        for key, value in (('lineage_id', self.created()['lineage_id']),
                           ('csrf_token', 'A' * 43), ('proof_generation', 2)):
            self.assertFalse(self.validator.is_valid({**self.pending(), key: value}))

    def test_csrf_canonical_padding_bits_and_no_normalization(self):
        for final in 'AEIMQUYcgkosw048':
            self.assertTrue(self.validator.is_valid({**self.provisional(),
                                                    'csrf_token': 'A' * 42 + final}))
        for token in ('A' * 42, 'A' * 44, 'A' * 43 + '=', 'A' * 42 + 'B',
                      'A' * 42 + '+', 'A' * 42 + '/', 'A' * 43 + '\n',
                      ' ' + 'A' * 42, None, True, 123):
            self.assertFalse(self.validator.is_valid({**self.provisional(), 'csrf_token': token}))

    def test_generation_is_integer_safe_and_separate_from_outcome(self):
        for generation in (2, 9007199254740991):
            self.assertTrue(self.validator.is_valid({**self.created(), 'proof_generation': generation}))
        for generation in (0, 1, -1, 2.5, '2', True, 9007199254740992):
            self.assertFalse(self.validator.is_valid({**self.created(), 'proof_generation': generation}))
        for generation in (0, 2, True, '1'):
            self.assertFalse(self.validator.is_valid({**self.provisional(), 'proof_generation': generation}))

    def test_identifier_representation_not_current_authority(self):
        for key in ('provisional_id', 'lineage_id', 'operation_id'):
            for text in ('not-a-uuid', self.request['operation_id'].upper(),
                         self.request['operation_id'] + '\n'):
                self.assertFalse(self.validator.is_valid({**self.created(), key: text}))
        # Shared UUID shape does not establish issuance; token shape does not prove entropy.
        self.assertTrue(self.validator.is_valid({**self.created(),
            'lineage_id': '00000000-0000-0000-0000-000000000000'}))
        self.assertFalse(self.validator.is_valid({**self.created(),
            'operation_id': '10286f82-cad4-1b14-a76a-e60d6c09ca09'}))

    def test_each_safe_error_pair_is_allowed_and_no_other_pair(self):
        pairs = {'INVALID_REQUEST': 'correct_request', 'BODY_TOO_LARGE': 'correct_request',
                 'UNSUPPORTED_MEDIA': 'correct_request', 'HEADER_TOO_LARGE': 'correct_request',
                 'ACCESS_UNAVAILABLE': 'contact', 'ACTION_DENIED': 'contact',
                 'OPERATION_CONFLICT': 'reconcile', 'CAPACITY_LIMIT': 'wait',
                 'SERVICE_UNAVAILABLE': 'reconcile'}
        for code, recovery in pairs.items():
            value = {'state': 'unavailable', 'code': code, 'recovery': recovery}
            with self.subTest(code=code):
                self.assertTrue(self.validator.is_valid(value))
                for key in ('state', 'code', 'recovery'):
                    invalid = copy.deepcopy(value)
                    del invalid[key]
                    self.assertFalse(self.validator.is_valid(invalid))
                self.assertFalse(self.validator.is_valid({**value, 'recovery': 'retry_all'}))
                for key in ('detail', 'provisional_id', 'operation_id', 'csrf_token', 'cookie'):
                    self.assertFalse(self.validator.is_valid({**value, key: 'forbidden'}))
        self.assertFalse(self.validator.is_valid({'state': 'unavailable',
                                                'code': 'UNKNOWN', 'recovery': 'contact'}))
        self.assertFalse(self.validator.is_valid({'state': 'unavailable',
                                                'code': 'ACCESS_UNAVAILABLE', 'recovery': 'wait'}))

    def test_no_scalar_array_or_arbitrary_object_response(self):
        for value in (None, True, 1, 'created', [], [self.created()], {},
                      {'status': 'ok'}, {'state': 'unavailable', 'code': None, 'recovery': None}):
            self.assertFalse(self.validator.is_valid(value))


if __name__ == '__main__':
    unittest.main()

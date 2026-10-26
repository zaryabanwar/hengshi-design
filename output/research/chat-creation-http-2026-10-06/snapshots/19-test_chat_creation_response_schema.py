"""Chat response validator seam only, never actual consent/HTTP/session proof."""
import copy
import json
import unittest

from jsonschema import Draft202012Validator
from referencing import Resource

from scripts.validation import test_booking_creation_request_schema as request_fixture


class ChatCreationResponseShapeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        fixture = request_fixture.BookingCreationRequestShapeTests
        fixture.setUpClass()
        registry = fixture.registry
        for name in ('booking-creation-response.schema.json', 'chat-creation-request.schema.json',
                     'chat-creation-response.schema.json'):
            path = request_fixture.CONTRACTS / name
            schema = json.loads(path.read_text(encoding='utf-8'))
            Draft202012Validator.check_schema(schema)
            registry = registry.with_resource(path.as_uri(), Resource.from_contents(schema))
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
                'session_id': '10286f82-cad4-4b14-a76a-e60d6c09ca09',
                'proof_generation': 2, 'csrf_token': 'A' * 43,
                'consent': {'state': 'none'}}

    def current_consent(self, choice='grant'):
        return {'state': 'current', 'revision': 1, 'decisions': [
            {'purpose_key': 'SYNTHETIC-PURPOSE', 'decision': choice,
             'notice_reference': {'notice_id': 'SYNTHETIC-NOTICE',
                                  'notice_revision': 'fixture-1', 'notice_sha256': 'b' * 64}}]}

    def pending(self):
        return {'phase': 'create', 'state': 'pending',
                'provisional_id': self.request['provisional_id'],
                'operation_id': self.request['operation_id']}

    def test_distinct_bootstrap_created_pending_projections(self):
        for value in (self.provisional(), self.created(), self.pending()):
            self.assertTrue(self.validator.is_valid(value))
            for key in value:
                invalid = copy.deepcopy(value)
                del invalid[key]
                self.assertFalse(self.validator.is_valid(invalid))
        self.assertFalse(self.validator.is_valid({**self.created(), 'phase': 'bootstrap'}))
        self.assertFalse(self.validator.is_valid({**self.pending(), 'state': 'created'}))

    def test_no_booking_transcript_owner_or_bearer_echo(self):
        for value in (self.provisional(), self.created(), self.pending()):
            for key in ('lineage_id', 'history', 'message', 'staff_id', 'qualification',
                        'secret', 'cookie', 'provider_result', 'confirmed', 'expires_at'):
                self.assertFalse(self.validator.is_valid({**value, key: 'forbidden'}))
        for key in ('session_id', 'proof_generation', 'csrf_token', 'consent'):
            self.assertFalse(self.validator.is_valid({**self.pending(), key: self.created()[key]}))

    def test_explicit_none_and_current_consent_variants(self):
        self.assertTrue(self.validator.is_valid(self.created()))
        for choice in ('grant', 'refuse'):
            self.assertTrue(self.validator.is_valid({**self.created(), 'consent': self.current_consent(choice)}))
        for consent in (None, True, {}, {'state': 'none', 'revision': 1},
                        {'state': 'stored'}, {'state': 'current', 'revision': 1, 'decisions': []}):
            self.assertFalse(self.validator.is_valid({**self.created(), 'consent': consent}))
        for key in ('state', 'revision', 'decisions'):
            consent = self.current_consent()
            del consent[key]
            self.assertFalse(self.validator.is_valid({**self.created(), 'consent': consent}))

    def test_consent_revision_and_notice_binding_are_exact(self):
        for revision in (1, 9007199254740991):
            consent = self.current_consent()
            consent['revision'] = revision
            self.assertTrue(self.validator.is_valid({**self.created(), 'consent': consent}))
        for revision in (0, -1, True, '1', 1.5, 9007199254740992):
            consent = self.current_consent()
            consent['revision'] = revision
            self.assertFalse(self.validator.is_valid({**self.created(), 'consent': consent}))
        for key in ('notice_id', 'notice_revision', 'notice_sha256'):
            consent = self.current_consent()
            del consent['decisions'][0]['notice_reference'][key]
            self.assertFalse(self.validator.is_valid({**self.created(), 'consent': consent}))

    def test_csrf_and_generation_keep_the_common_representations(self):
        for value in ('A' * 42, 'A' * 44, 'A' * 42 + 'B', 'A' * 43 + '=', None, True):
            self.assertFalse(self.validator.is_valid({**self.created(), 'csrf_token': value}))
        for generation in (0, 1, -1, True, '2', 2.5, 9007199254740992):
            self.assertFalse(self.validator.is_valid({**self.created(), 'proof_generation': generation}))
        self.assertTrue(self.validator.is_valid({**self.created(), 'proof_generation': 9007199254740991}))

    def test_safe_unavailable_pairs_have_no_data_or_outcome_echo(self):
        pairs = {'INVALID_REQUEST': 'correct_request', 'BODY_TOO_LARGE': 'correct_request',
                 'UNSUPPORTED_MEDIA': 'correct_request', 'HEADER_TOO_LARGE': 'correct_request',
                 'ACCESS_UNAVAILABLE': 'contact', 'ACTION_DENIED': 'contact',
                 'OPERATION_CONFLICT': 'reconcile', 'CAPACITY_LIMIT': 'wait',
                 'SERVICE_UNAVAILABLE': 'reconcile'}
        for code, recovery in pairs.items():
            value = {'state': 'unavailable', 'code': code, 'recovery': recovery}
            self.assertTrue(self.validator.is_valid(value))
            self.assertFalse(self.validator.is_valid({**value, 'recovery': 'invented'}))
            for key in ('detail', 'session_id', 'operation_id', 'consent', 'csrf_token'):
                self.assertFalse(self.validator.is_valid({**value, key: 'forbidden'}))

    def test_consent_cap_duplicates_and_semantic_limit_are_distinct(self):
        consent = self.current_consent()
        initial = consent['decisions'][0]
        consent['decisions'] = [{**initial, 'purpose_key': f'SYNTHETIC-{i}'} for i in range(8)]
        self.assertTrue(self.validator.is_valid({**self.created(), 'consent': consent}))
        consent['decisions'].append({**initial, 'purpose_key': 'SYNTHETIC-8'})
        self.assertFalse(self.validator.is_valid({**self.created(), 'consent': consent}))
        consent['decisions'] = [initial, copy.deepcopy(initial)]
        self.assertFalse(self.validator.is_valid({**self.created(), 'consent': consent}))
        # Different records with the same purpose still need separate producer/consumer semantic denial.
        consent['decisions'] = [initial, {**initial, 'decision': 'refuse'}]
        self.assertTrue(self.validator.is_valid({**self.created(), 'consent': consent}))

    def test_shape_does_not_prove_real_issued_session_or_consent(self):
        value = {**self.created(), 'session_id': '00000000-0000-0000-0000-000000000000',
                 'consent': self.current_consent()}
        self.assertTrue(self.validator.is_valid(value))
        # UUID/token/notice syntax alone does not prove issuance, randomness or actual policy registration.


if __name__ == '__main__':
    unittest.main()

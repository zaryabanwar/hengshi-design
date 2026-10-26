"""IF-CHAT-02 representation seam only; no HTTP, policy or concurrency proof."""
import json
import unittest

from jsonschema import Draft202012Validator
from referencing import Resource

from scripts.validation import test_booking_creation_request_schema as fixture


class ChatConsentShapeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        base = fixture.BookingCreationRequestShapeTests
        base.setUpClass()
        registry = base.registry
        for name in ('booking-creation-response.schema.json', 'chat-creation-request.schema.json',
                     'chat-consent.schema.json'):
            path = fixture.CONTRACTS / name
            schema = json.loads(path.read_text(encoding='utf-8'))
            Draft202012Validator.check_schema(schema)
            registry = registry.with_resource(path.as_uri(), Resource.from_contents(schema))
        cls.validators = {
            direction: Draft202012Validator({'$ref': path.as_uri() + '#/$defs/' + direction},
                                             registry=registry, format_checker=base.checker)
            for direction in ('request', 'response')
        }
        cls.module = Draft202012Validator({'$ref': path.as_uri()}, registry=registry)

    def decision(self, choice='grant', purpose='SYNTHETIC-PURPOSE'):
        value = {'purpose_key': purpose, 'decision': choice}
        if choice in ('grant', 'refuse'):
            value['notice_reference'] = {'notice_id': 'SYNTHETIC-NOTICE',
                                        'notice_revision': 'fixture-1', 'notice_sha256': 'b' * 64}
        return value

    def request(self):
        return {'operation_id': '9c3567ad-12bf-4b3a-a76d-7e56b9dfe051',
                'consent': {'expected_revision': 1, 'decisions': [self.decision()]}}

    def applied(self):
        return {'state': 'applied', 'operation_id': self.request()['operation_id'],
                'applied_revision': 2, 'proof_generation': 2,
                'consent': {'effective_state': {'revision': 2,
                                               'decisions': [self.decision('withdrawn')]}}}

    def valid(self, direction, value):
        return self.validators[direction].is_valid(value)

    def test_requests_distinguish_notice_acceptance_and_withdrawal(self):
        for choice in ('grant', 'refuse', 'withdraw'):
            value = self.request()
            value['consent']['decisions'] = [self.decision(choice)]
            self.assertTrue(self.valid('request', value))
            if choice == 'withdraw':
                value['consent']['decisions'][0]['notice_reference'] = self.decision()['notice_reference']
            else:
                del value['consent']['decisions'][0]['notice_reference']
            self.assertFalse(self.valid('request', value))
        value = self.request()
        value['consent']['decisions'] = [self.decision('withdrawn')]
        self.assertFalse(self.valid('request', value))

    def test_absent_and_existing_map_revision_shapes_are_explicit(self):
        for revision in (None, 1, 9007199254740991):
            value = self.request()
            value['consent']['expected_revision'] = revision
            self.assertTrue(self.valid('request', value))
        for revision in (0, -1, True, '1', 1.5, 9007199254740992):
            value = self.request()
            value['consent']['expected_revision'] = revision
            self.assertFalse(self.valid('request', value))
        value = self.request()
        del value['consent']['expected_revision']
        self.assertFalse(self.valid('request', value))

    def test_closed_input_has_no_other_process_or_server_authority(self):
        for key in ('session_id', 'lineage_id', 'phase', 'csrf_token', 'cookie', 'proof',
                    'staff_id', 'timestamp', 'effective_state', 'deleted'):
            self.assertFalse(self.valid('request', {**self.request(), key: 'forbidden'}))
        for key in ('operation_id', 'consent'):
            value = self.request()
            del value[key]
            self.assertFalse(self.valid('request', value))
        value = self.request()
        value['consent']['unknown'] = True
        self.assertFalse(self.valid('request', value))
        value = self.request()
        value['operation_id'] = '019f1d32-0000-7000-8000-000000000001'
        self.assertFalse(self.valid('request', value))

    def test_decision_list_is_finite_and_exact_duplicates_are_rejected(self):
        for count in (1, 8):
            value = self.request()
            value['consent']['decisions'] = [self.decision(purpose=f'SYNTHETIC-PURPOSE-{i}')
                                             for i in range(count)]
            self.assertTrue(self.valid('request', value))
        for decisions in ([], [self.decision(purpose=f'SYNTHETIC-PURPOSE-{i}') for i in range(9)],
                          [self.decision(), self.decision()]):
            value = self.request()
            value['consent']['decisions'] = decisions
            self.assertFalse(self.valid('request', value))

    def test_applied_effective_states_keep_withdrawal_direction(self):
        for choice in ('grant', 'refuse', 'withdrawn'):
            value = self.applied()
            value['consent']['effective_state']['decisions'] = [self.decision(choice)]
            self.assertTrue(self.valid('response', value))
        value = self.applied()
        value['consent']['effective_state']['decisions'] = [self.decision('withdraw')]
        self.assertFalse(self.valid('response', value))
        for key in self.applied():
            value = self.applied()
            del value[key]
            self.assertFalse(self.valid('response', value))
        for field in ('applied_revision', 'proof_generation'):
            for revision in (0, True, '2', 2.5, 9007199254740992):
                value = self.applied()
                value[field] = revision
                self.assertFalse(self.valid('response', value))
        value = self.applied()
        value['proof_generation'] = 1
        self.assertFalse(self.valid('response', value))

    def test_pending_and_errors_never_echo_effective_grants_or_deletion(self):
        pending = {'state': 'pending', 'operation_id': self.request()['operation_id']}
        error = {'state': 'unavailable', 'code': 'OPERATION_CONFLICT', 'recovery': 'reconcile'}
        for value in (pending, error):
            self.assertTrue(self.valid('response', value))
            for key in ('consent', 'applied_revision', 'proof_generation', 'csrf_token',
                        'deleted', 'transcript', 'provider_result', 'staff_id'):
                self.assertFalse(self.valid('response', {**value, key: self.applied().get(key, True)}))
        self.assertFalse(self.valid('response', {**error, 'recovery': 'contact'}))

    def test_consumers_must_choose_direction_and_not_the_module_root(self):
        self.assertFalse(self.valid('request', self.applied()))
        self.assertFalse(self.valid('response', self.request()))
        for value in (self.request(), self.applied(), {}, None, [], True):
            self.assertFalse(self.module.is_valid(value))


if __name__ == '__main__':
    unittest.main()

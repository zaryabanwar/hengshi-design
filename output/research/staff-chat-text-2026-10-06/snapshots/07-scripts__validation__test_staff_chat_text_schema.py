"""Staff text schema boundary only; no auth, assignment or delivery enforcement."""
import copy
import json
import unittest

from jsonschema import Draft202012Validator
from referencing import Resource

from scripts.validation import test_booking_creation_request_schema as fixture


class StaffChatTextShapeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        base = fixture.BookingCreationRequestShapeTests
        base.setUpClass()
        registry = base.registry
        for name in ('chat-text.schema.json', 'staff-chat-text.schema.json'):
            path = fixture.CONTRACTS / name
            schema = json.loads(path.read_text(encoding='utf-8'))
            Draft202012Validator.check_schema(schema)
            registry = registry.with_resource(path.as_uri(), Resource.from_contents(schema))
        cls.validators = {
            direction: Draft202012Validator({'$ref': path.as_uri() + '#/$defs/' + direction},
                                             registry=registry, format_checker=base.checker)
            for direction in ('client', 'server')
        }
        cls.module = Draft202012Validator({'$ref': path.as_uri()}, registry=registry)

    channel = '9c3567ad-12bf-4b3a-a76d-7e56b9dfe051'
    stream = '919108f7-52d1-4320-9bac-f847db4148a8'
    operation = 'f0839ee7-708d-4ecb-8cb3-1283c1e2f3aa'
    release = {'release_id': 'synthetic-release', 'manifest_sha256': 'a' * 64}

    def valid(self, direction, value):
        return self.validators[direction].is_valid(value)

    def submit(self):
        return {'protocol_version': 1, 'kind': 'staff_submit_text',
                'channel_id': self.channel, 'stream_id': self.stream,
                'operation_id': self.operation, 'command_revision': 1,
                'expected_ownership_generation': 1, 'expected_consent_revision': 2,
                'payload': {'text': 'SYNTHETIC STAFF MESSAGE'}}

    def reconcile(self):
        value = self.submit()
        value['kind'] = 'staff_reconcile_text'
        del value['payload']
        del value['expected_consent_revision']
        return value

    def admission(self):
        return {'protocol_version': 1, 'kind': 'staff_text_admission',
                'channel_id': self.channel, 'stream_id': self.stream,
                'handoff_id': self.stream, 'ownership_generation': 1,
                'consent_revision': 2, 'release_identity': copy.deepcopy(self.release),
                'operation_id': self.operation, 'command_revision': 1}

    def event(self, kind, payload):
        return {'protocol_version': 1, 'kind': kind, 'stream_id': self.stream,
                'release_identity': copy.deepcopy(self.release), 'event_id': self.operation,
                'sequence': 1, 'payload': payload}

    def result(self, state='admitted', **extra):
        return self.event('staff_command_result', {
            'handoff_id': self.stream, 'ownership_generation': 1,
            'operation_id': self.operation, 'command_revision': 1,
            'state': state, **extra})

    def visitor(self):
        return self.event('visitor_text', {
            'handoff_id': self.stream, 'ownership_generation': 1,
            'operation_id': self.operation, 'command_revision': 1,
            'text': 'SYNTHETIC SHARED VISITOR MESSAGE'})

    def test_direction_and_module_cannot_accept_generic_or_visitor_variants(self):
        for direction, factories in (('client', (self.submit, self.reconcile)),
                                     ('server', (self.admission, self.result, self.visitor))):
            other = 'server' if direction == 'client' else 'client'
            for factory in factories:
                value = factory()
                self.assertTrue(self.valid(direction, value))
                self.assertFalse(self.valid(other, value))
                self.assertFalse(self.module.is_valid(value))
        for kind in ('submit_text', 'staff_text', 'initialize', 'ready', 'accept', 'end'):
            value = self.submit()
            value['kind'] = kind
            self.assertFalse(self.valid('client', value))
        for value in ({}, None, [], {'kind': 'message', 'sender': 'staff', 'text': 'x'}):
            for direction in ('client', 'server'):
                self.assertFalse(self.valid(direction, value))

    def test_commands_cannot_choose_sender_recipient_or_server_authority(self):
        for factory in (self.submit, self.reconcile):
            for field in ('sender', 'staff_id', 'role', 'handoff_id', 'recipient_id',
                          'provider', 'sequence', 'release_identity', 'proof_generation',
                          'csrf_token', 'confirmed'):
                self.assertFalse(self.valid('client', {**factory(), field: 'forbidden'}))
        for field in ('sender', 'html', 'recipient_id', 'booking_id', 'end'):
            value = self.submit()
            value['payload'][field] = 'forbidden'
            self.assertFalse(self.valid('client', value))
        self.assertFalse(self.valid('client', {**self.reconcile(), 'payload': {'text': 'again'}}))

    def test_server_projections_and_nested_contexts_are_closed(self):
        for factory in (self.result, self.visitor):
            for field in ('staff_id', 'sender', 'jwt', 'channel_id', 'proof_generation',
                          'consent_revision', 'confirmed'):
                self.assertFalse(self.valid('server', {**factory(), field: 'forbidden'}))
                value = factory()
                value['payload'][field] = 'forbidden'
                self.assertFalse(self.valid('server', value))
            value = factory()
            value['release_identity']['permission'] = 'forbidden'
            self.assertFalse(self.valid('server', value))
        self.assertFalse(self.valid('server', {**self.admission(), 'staff_id': 'forbidden'}))

    def test_representations_require_fields_exact_revisions_and_uuid_v4(self):
        for direction, factory in (('client', self.submit), ('client', self.reconcile),
                                   ('server', self.admission), ('server', self.visitor)):
            original = factory()
            for field in original:
                value = copy.deepcopy(original)
                del value[field]
                self.assertFalse(self.valid(direction, value))
        for field in ('command_revision', 'expected_ownership_generation'):
            for number in (0, -1, True, '1', 1.5, 9007199254740992):
                self.assertFalse(self.valid('client', {**self.submit(), field: number}))
        for operation in ('not-a-uuid', self.operation.upper(),
                          '019f1d32-0000-7000-8000-000000000001'):
            self.assertFalse(self.valid('client', {**self.submit(), 'operation_id': operation}))
        # Null is an absent-map representation, never evidence of sharing consent.
        self.assertTrue(self.valid('client', {**self.submit(), 'expected_consent_revision': None}))

    def test_text_shape_limits_do_not_claim_scalar_byte_or_rendering_proof(self):
        for direction, factory, maximum in (('client', self.submit, 4000),
                                            ('server', self.visitor, 2000)):
            for text in ('x', 'x' * maximum):
                value = factory()
                value['payload']['text'] = text
                self.assertTrue(self.valid(direction, value))
            for text in ('', 'x' * (maximum + 1), None, [], 1):
                value = factory()
                value['payload']['text'] = text
                self.assertFalse(self.valid(direction, value))
        for text in (' ', '\ud800', '<script>untrusted</script>', '\U0001f333' * 4000):
            value = self.submit()
            value['payload']['text'] = text
            self.assertTrue(self.valid('client', value))

    def test_result_states_require_truthful_fixed_recovery(self):
        for value in (self.result(), self.result('projected'),
                      self.result('pending', recovery='reconcile'),
                      self.result('refused', code='recipient_unavailable', recovery='inspect_conversation'),
                      self.result('unavailable', code='outcome_unavailable', recovery='reconcile')):
            self.assertTrue(self.valid('server', value))
        for value in (self.result('delivered'), self.result('read'), self.result('confirmed'),
                      self.result('pending'), self.result('projected', recovery='reconcile'),
                      self.result('pending', code='outcome_unavailable', recovery='reconcile'),
                      self.result('refused', code='outcome_unavailable', recovery='inspect_conversation'),
                      self.result('unavailable', code='outcome_unavailable', recovery='inspect_conversation')):
            self.assertFalse(self.valid('server', value))


if __name__ == '__main__':
    unittest.main()

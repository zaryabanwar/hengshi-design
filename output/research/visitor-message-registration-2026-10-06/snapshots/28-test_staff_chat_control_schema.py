"""Actual control validator boundary only; no staff/session/stream runtime proof."""
import copy
import json
import unittest

from jsonschema import Draft202012Validator
from referencing import Resource

from scripts.validation import test_booking_creation_request_schema as fixture


class StaffChatControlShapeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        base = fixture.BookingCreationRequestShapeTests
        base.setUpClass()
        registry = base.registry
        for name in ('booking-creation-response.schema.json', 'chat-event-control.schema.json',
                     'staff-handoff-request.schema.json', 'staff-chat-control.schema.json'):
            path = fixture.CONTRACTS / name
            schema = json.loads(path.read_text(encoding='utf-8'))
            Draft202012Validator.check_schema(schema)
            registry = registry.with_resource(path.as_uri(), Resource.from_contents(schema))
        cls.validators = {
            direction: Draft202012Validator(
                {'$ref': path.as_uri() + '#/$defs/' + direction}, registry=registry,
                format_checker=base.checker) for direction in ('client', 'server')}
        cls.module = Draft202012Validator({'$ref': path.as_uri()}, registry=registry)
        visitor = fixture.CONTRACTS / 'chat-event-control.schema.json'
        cls.visitor_client = Draft202012Validator(
            {'$ref': visitor.as_uri() + '#/$defs/client'}, registry=registry,
            format_checker=base.checker)

    def initialize(self):
        return {'protocol_version': 1, 'kind': 'staff_initialize', 'csrf_token': 'A' * 43,
                'expected_handoff': {'handoff_id': '919108f7-52d1-4320-9bac-f847db4148a8',
                                     'handoff_revision': 3, 'ownership_generation': 1},
                'expected_consent_revision': 2, 'resume': None}

    def ready(self):
        return {'protocol_version': 1, 'kind': 'staff_ready',
                'channel_id': '9c3567ad-12bf-4b3a-a76d-7e56b9dfe051',
                'handoff_binding': self.initialize()['expected_handoff'],
                'consent_revision': 2, 'stream_id': 'f0839ee7-708d-4ecb-8cb3-1283c1e2f3aa',
                'head_sequence': 0, 'next_sequence': 1, 'resume_outcome': 'fresh'}

    def receipt(self):
        return {'protocol_version': 1, 'kind': 'staff_receipt',
                'channel_id': self.ready()['channel_id'], 'stream_id': self.ready()['stream_id'],
                'handoff_id': self.initialize()['expected_handoff']['handoff_id'],
                'ownership_generation': 1, 'through_sequence': 0}

    def test_client_server_and_visitor_directions_are_distinct(self):
        for message in (self.initialize(), self.receipt()):
            self.assertTrue(self.validators['client'].is_valid(message))
            self.assertFalse(self.validators['server'].is_valid(message))
            self.assertFalse(self.visitor_client.is_valid(message))
            self.assertFalse(self.module.is_valid(message))
        self.assertTrue(self.validators['server'].is_valid(self.ready()))
        self.assertFalse(self.validators['client'].is_valid(self.ready()))
        visitor = {'protocol_version': 1, 'kind': 'initialize', 'proof_generation': 2,
                   'csrf_token': 'A' * 43, 'resume': None}
        self.assertTrue(self.visitor_client.is_valid(visitor))
        self.assertFalse(self.validators['client'].is_valid(visitor))

    def test_initialize_requires_exact_guards_and_closed_resume(self):
        message = self.initialize()
        for key in message:
            invalid = copy.deepcopy(message)
            del invalid[key]
            self.assertFalse(self.validators['client'].is_valid(invalid))
        message['resume'] = {'stream_id': self.ready()['stream_id'], 'after_sequence': 0}
        self.assertTrue(self.validators['client'].is_valid(message))
        for key, value in (('staff_id', 'forged'), ('handoff_id', 'other'),
                           ('after_sequence', -1), ('after_sequence', True)):
            invalid = copy.deepcopy(message)
            invalid['resume'][key] = value
            self.assertFalse(self.validators['client'].is_valid(invalid))
        for value in (None, True, 0, '2', 1.5, 9007199254740992):
            invalid = self.initialize()
            invalid['expected_consent_revision'] = value
            self.assertFalse(self.validators['client'].is_valid(invalid))

    def test_identity_payload_and_visitor_proof_are_not_controls(self):
        for field in ('staff_id', 'sender', 'role', 'jwt', 'access_token', 'proof_generation',
                      'proof', 'session_id', 'payload', 'text', 'transcript', 'accept', 'end'):
            for message in (self.initialize(), self.ready(), self.receipt()):
                invalid = copy.deepcopy(message)
                invalid[field] = 'untrusted'
                direction = 'server' if message['kind'] == 'staff_ready' else 'client'
                self.assertFalse(self.validators[direction].is_valid(invalid))
        for message in (self.initialize(), self.ready()):
            invalid = copy.deepcopy(message)
            key = 'expected_handoff' if message['kind'] == 'staff_initialize' else 'handoff_binding'
            invalid[key]['staff_id'] = 'forged'
            direction = 'client' if message['kind'] == 'staff_initialize' else 'server'
            self.assertFalse(self.validators[direction].is_valid(invalid))

    def test_required_ready_and_receipt_values_have_safe_boundaries(self):
        for message, direction in ((self.ready(), 'server'), (self.receipt(), 'client')):
            for key in message:
                invalid = copy.deepcopy(message)
                del invalid[key]
                self.assertFalse(self.validators[direction].is_valid(invalid))
            sequence_key = 'head_sequence' if direction == 'server' else 'through_sequence'
            for value in (-1, True, '1', 1.5, 9007199254740992):
                invalid = copy.deepcopy(message)
                invalid[sequence_key] = value
                self.assertFalse(self.validators[direction].is_valid(invalid))
            invalid = copy.deepcopy(message)
            invalid['channel_id'] = 'not-a-uuid'
            self.assertFalse(self.validators[direction].is_valid(invalid))
        for value in (0, None, True):
            invalid = self.ready()
            invalid['next_sequence'] = value
            self.assertFalse(self.validators['server'].is_valid(invalid))
        for value in ('a' * 42, 'a' * 43):
            invalid = self.initialize()
            invalid['csrf_token'] = value
            self.assertFalse(self.validators['client'].is_valid(invalid))

    def test_unavailable_is_fixed_and_has_no_private_or_success_data(self):
        message = {'protocol_version': 1, 'kind': 'staff_unavailable',
                   'code': 'authority_changed', 'recovery': 'inspect_conversation'}
        self.assertTrue(self.validators['server'].is_valid(message))
        self.assertFalse(self.validators['client'].is_valid(message))
        for key, value in (('detail', 'private exception'), ('handoff_id', 'private'),
                           ('accepted', True), ('ended', True), ('recovery', 'retry_submit'),
                           ('recovery', 'reconcile_staff_operations')):
            invalid = copy.deepcopy(message)
            invalid[key] = value
            self.assertFalse(self.validators['server'].is_valid(invalid))

    def test_shape_does_not_prove_sequence_relations_or_current_authority(self):
        ready = self.ready()
        ready['next_sequence'] = 17
        # Numeric representation cannot prove the required coordinated next/head relation.
        self.assertTrue(self.validators['server'].is_valid(ready))
        receipt = self.receipt()
        receipt['through_sequence'] = 9007199254740991
        self.assertTrue(self.validators['client'].is_valid(receipt))
        # A well-shaped unbound CSRF token and arbitrary generation are not actual grants.
        self.assertTrue(self.validators['client'].is_valid(self.initialize()))


if __name__ == '__main__':
    unittest.main()

"""Directional chat control representations only; no live socket/security proof."""
import copy
import json
import unittest

from jsonschema import Draft202012Validator
from referencing import Resource

from scripts.validation import test_booking_creation_request_schema as fixture


class ChatEventControlShapeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        base = fixture.BookingCreationRequestShapeTests
        base.setUpClass()
        registry = base.registry
        for name in ('booking-creation-response.schema.json', 'chat-event-control.schema.json'):
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

    def initialize(self):
        return {'protocol_version': 1, 'kind': 'initialize', 'proof_generation': 2,
                'csrf_token': 'A' * 43, 'resume': None}

    def receipt(self):
        return {'protocol_version': 1, 'kind': 'receipt', 'channel_id': self.channel,
                'stream_id': self.stream, 'through_sequence': 3}

    def ready(self):
        return {'protocol_version': 1, 'kind': 'ready', 'channel_id': self.channel,
                'proof_generation': 2, 'consent_revision': None, 'stream_id': self.stream,
                'head_sequence': 0, 'next_sequence': 1, 'resume_outcome': 'fresh'}

    def valid(self, direction, value):
        return self.validators[direction].is_valid(value)

    def test_client_and_server_directions_are_distinct_and_explicit(self):
        for value in (self.initialize(), self.receipt()):
            self.assertTrue(self.valid('client', value))
            self.assertFalse(self.valid('server', value))
            self.assertFalse(self.module.is_valid(value))
        for value in (self.ready(), {'protocol_version': 1, 'kind': 'unavailable',
                                    'code': 'replay_unavailable', 'recovery': 'reconcile'}):
            self.assertTrue(self.valid('server', value))
            self.assertFalse(self.valid('client', value))
            self.assertFalse(self.module.is_valid(value))
        for direction in ('client', 'server'):
            for value in ({}, [], None, {'protocol_version': 1, 'kind': 'message',
                                        'text': 'SYNTHETIC, NOT PUBLIC COPY'}):
                self.assertFalse(self.valid(direction, value))

    def test_initialization_requires_closed_csrf_generation_and_resume(self):
        value = self.initialize()
        value['resume'] = {'stream_id': self.stream, 'after_sequence': 0}
        self.assertTrue(self.valid('client', value))
        for key in self.initialize():
            value = self.initialize()
            del value[key]
            self.assertFalse(self.valid('client', value))
        for token in ('', 'A' * 42, 'A' * 44, 'A' * 42 + '=', 'A' * 42 + '\n', None):
            value = self.initialize()
            value['csrf_token'] = token
            self.assertFalse(self.valid('client', value))
        for cursor in ({}, {'stream_id': self.stream},
                       {'stream_id': self.stream, 'after_sequence': 0, 'session_id': self.channel}):
            value = self.initialize()
            value['resume'] = cursor
            self.assertFalse(self.valid('client', value))

    def test_controls_do_not_admit_business_or_private_authority_fields(self):
        for direction, original in (('client', self.initialize()), ('client', self.receipt()),
                                    ('server', self.ready())):
            for key in ('cookie', 'proof', 'bearer', 'session_id', 'staff_id', 'sender',
                        'message', 'payload', 'confirmed', 'deleted', 'provider_result'):
                value = {**original, key: 'forbidden'}
                self.assertFalse(self.valid(direction, value))
        for key in ('csrf_token', 'consent'):
            self.assertFalse(self.valid('server', {**self.ready(), key: 'forbidden'}))

    def test_uuid_assertion_and_version_reject_noncanonical_cursors(self):
        for field in ('channel_id', 'stream_id'):
            for identity in ('not-a-uuid', self.stream.upper(), ' ' + self.stream,
                             '019f1d32-0000-7000-8000-000000000001', None):
                value = self.receipt()
                value[field] = identity
                self.assertFalse(self.valid('client', value))
                value = self.ready()
                value[field] = identity
                self.assertFalse(self.valid('server', value))

    def test_numeric_boundaries_preserve_zero_sequence_and_positive_revision(self):
        for sequence in (0, 1, 9007199254740991):
            value = self.receipt()
            value['through_sequence'] = sequence
            self.assertTrue(self.valid('client', value))
        for invalid in (-1, True, '1', 1.5, 9007199254740992):
            value = self.receipt()
            value['through_sequence'] = invalid
            self.assertFalse(self.valid('client', value))
        for field in ('proof_generation', 'next_sequence', 'consent_revision'):
            for invalid in (0, -1, True, '2', 2.5, 9007199254740992):
                value = self.ready()
                value[field] = invalid
                self.assertFalse(self.valid('server', value))
        value = self.ready()
        value['proof_generation'] = 1
        self.assertFalse(self.valid('server', value))
        for invalid in (True, '1', 2, None):
            value = self.initialize()
            value['protocol_version'] = invalid
            self.assertFalse(self.valid('client', value))

    def test_ready_and_unavailable_have_only_their_own_closed_fields(self):
        resumed = copy.deepcopy(self.ready())
        resumed.update(consent_revision=3, head_sequence=5,
                       next_sequence=4, resume_outcome='resumed')
        self.assertTrue(self.valid('server', resumed))
        for key in resumed:
            value = copy.deepcopy(resumed)
            del value[key]
            self.assertFalse(self.valid('server', value))
        for state in ('pending', 'confirmed', 'unknown'):
            value = {**self.ready(), 'resume_outcome': state}
            self.assertFalse(self.valid('server', value))
        error = {'protocol_version': 1, 'kind': 'unavailable',
                 'code': 'authority_changed', 'recovery': 'contact_or_book'}
        self.assertTrue(self.valid('server', error))
        for extra in ('detail', 'trace', 'channel_id', 'csrf_token', 'confirmed', 'deleted'):
            self.assertFalse(self.valid('server', {**error, extra: 'forbidden'}))
        self.assertFalse(self.valid('server', {**error, 'code': 'raw-secret-error'}))
        self.assertFalse(self.valid('server', {**error, 'recovery': 'retry_business_command'}))


if __name__ == '__main__':
    unittest.main()

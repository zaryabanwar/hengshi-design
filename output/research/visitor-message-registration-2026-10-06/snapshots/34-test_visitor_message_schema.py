"""Visitor-owned event shape only; no actual registration, ownership or consent."""
import copy
import json
import unittest

from jsonschema import Draft202012Validator
from referencing import Resource

from scripts.validation import test_booking_creation_request_schema as fixture


class VisitorMessageShapeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        base = fixture.BookingCreationRequestShapeTests
        base.setUpClass()
        registry = base.registry
        for name in ('chat-text.schema.json', 'visitor-message.schema.json'):
            path = fixture.CONTRACTS / name
            schema = json.loads(path.read_text(encoding='utf-8'))
            Draft202012Validator.check_schema(schema)
            registry = registry.with_resource(path.as_uri(), Resource.from_contents(schema))
        cls.validators = {direction: Draft202012Validator(
            {'$ref': path.as_uri() + '#/$defs/' + direction}, registry=registry,
            format_checker=base.checker) for direction in ('client', 'server')}
        cls.module = Draft202012Validator({'$ref': path.as_uri()}, registry=registry)
        cls.old_server = Draft202012Validator(
            {'$ref': (fixture.CONTRACTS / 'chat-text.schema.json').as_uri() + '#/$defs/server'},
            registry=registry, format_checker=base.checker)

    def event(self):
        return {'protocol_version': 1, 'kind': 'visitor_text_registered',
                'stream_id': 'f0839ee7-708d-4ecb-8cb3-1283c1e2f3aa',
                'event_id': '919108f7-52d1-4320-9bac-f847db4148a8', 'sequence': 1,
                'release_identity': {'release_id': 'SYNTHETIC-RELEASE',
                                     'manifest_sha256': 'b' * 64},
                'payload': {'operation_id': '9c3567ad-12bf-4b3a-a76d-7e56b9dfe051',
                            'command_revision': 1, 'text': 'Synthetic visitor question.'}}

    def test_registered_text_is_an_explicit_server_extension(self):
        event = self.event()
        self.assertTrue(self.validators['server'].is_valid(event))
        self.assertFalse(self.validators['client'].is_valid(event))
        self.assertFalse(self.module.is_valid(event))
        # Earlier reviewed directions remain closed; this extension is not implicit.
        self.assertFalse(self.old_server.is_valid(event))
        for key in event:
            invalid = copy.deepcopy(event)
            del invalid[key]
            self.assertFalse(self.validators['server'].is_valid(invalid))
        for key in event['payload']:
            invalid = copy.deepcopy(event)
            del invalid['payload'][key]
            self.assertFalse(self.validators['server'].is_valid(invalid))

    def test_transport_identity_and_private_authority_fields_stay_out(self):
        for key in ('channel_id', 'proof_generation', 'consent_revision', 'role',
                    'staff_id', 'csrf_token', 'accepted', 'receipt'):
            invalid = self.event()
            invalid[key] = 'untrusted'
            self.assertFalse(self.validators['server'].is_valid(invalid))
        for key in ('handoff_id', 'ownership_generation', 'provider', 'consent',
                    'purpose_key', 'retention', 'html', 'delivered', 'read', 'source_hash'):
            invalid = self.event()
            invalid['payload'][key] = 'untrusted'
            self.assertFalse(self.validators['server'].is_valid(invalid))
        for kind in ('visitor_text', 'staff_text', 'command_result', 'text_admission'):
            invalid = self.event()
            invalid['kind'] = kind
            self.assertFalse(self.validators['server'].is_valid(invalid))

    def test_text_scalar_and_identifier_boundaries(self):
        for text in ('x' * 2000, '\U0001f331' * 2000):
            event = self.event()
            event['payload']['text'] = text
            self.assertTrue(self.validators['server'].is_valid(event))
        for text in ('', 'x' * 2001, None, ['text']):
            event = self.event()
            event['payload']['text'] = text
            self.assertFalse(self.validators['server'].is_valid(event))
        for key, value in (('event_id', 'not-a-uuid'), ('stream_id', 'not-a-uuid'),
                           ('sequence', True), ('sequence', 0), ('sequence', 1.5),
                           ('sequence', 9007199254740992)):
            event = self.event()
            event[key] = value
            self.assertFalse(self.validators['server'].is_valid(event))
        for key, value in (('operation_id', 'not-a-uuid'), ('command_revision', True),
                           ('command_revision', 0), ('command_revision', 1.5)):
            event = self.event()
            event['payload'][key] = value
            self.assertFalse(self.validators['server'].is_valid(event))

    def test_shape_cannot_prove_correspondence_or_text_safety(self):
        # A valid event can still claim the wrong accepted intent or ownership.
        event = self.event()
        event['payload']['operation_id'] = event['event_id']
        event['payload']['text'] = '<script>untrusted text</script>'
        self.assertTrue(self.validators['server'].is_valid(event))
        # Raw scalar validity and whitespace-only refusal are actual admission duties.
        event['payload']['text'] = '\ud800'
        self.assertTrue(self.validators['server'].is_valid(event))
        event['payload']['text'] = ' '
        self.assertTrue(self.validators['server'].is_valid(event))


if __name__ == '__main__':
    unittest.main()

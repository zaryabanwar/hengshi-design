"""Chat text directional shapes only; no live admission, routing or delivery proof."""
import copy
import json
import unittest

from jsonschema import Draft202012Validator
from referencing import Resource

from scripts.validation import test_booking_creation_request_schema as fixture


class ChatTextShapeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        base = fixture.BookingCreationRequestShapeTests
        base.setUpClass()
        path = fixture.CONTRACTS / 'chat-text.schema.json'
        schema = json.loads(path.read_text(encoding='utf-8'))
        Draft202012Validator.check_schema(schema)
        registry = base.registry.with_resource(path.as_uri(), Resource.from_contents(schema))
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
        return {'protocol_version': 1, 'kind': 'submit_text', 'channel_id': self.channel,
                'stream_id': self.stream, 'operation_id': self.operation, 'command_revision': 1,
                'expected_consent_revision': None, 'payload': {'text': 'SYNTHETIC INPUT'}}

    def reconcile(self):
        value = self.submit()
        value['kind'] = 'reconcile_text'
        del value['payload']
        del value['expected_consent_revision']
        return value

    def admission(self):
        return {'protocol_version': 1, 'kind': 'text_admission', 'channel_id': self.channel,
                'stream_id': self.stream, 'proof_generation': 2, 'consent_revision': None,
                'release_identity': copy.deepcopy(self.release), 'operation_id': self.operation,
                'command_revision': 1}

    def event(self, kind, payload):
        return {'protocol_version': 1, 'kind': kind, 'stream_id': self.stream,
                'release_identity': copy.deepcopy(self.release), 'event_id': self.operation,
                'sequence': 1, 'payload': payload}

    def result(self, state='admitted', **extra):
        return self.event('command_result', {'operation_id': self.operation,
                                             'command_revision': 1, 'state': state, **extra})

    def answer(self):
        return self.event('ai_answer', {'operation_id': self.operation, 'command_revision': 1,
                                       'answer': 'SYNTHETIC ANSWER',
                                       'outcome': 'nonbinding_grounded_guidance',
                                       'sources': [{'document_id': 'synthetic-document',
                                                    'route_key': 'synthetic-route',
                                                    'document_sha256': 'b' * 64}]})

    def staff(self):
        return self.event('staff_text', {'handoff_id': self.stream, 'ownership_generation': 1,
                                        'text': 'SYNTHETIC STAFF PROJECTION'})

    def test_directions_are_explicit_without_generic_sender_fallback(self):
        for value in (self.submit(), self.reconcile()):
            self.assertTrue(self.valid('client', value))
            self.assertFalse(self.valid('server', value))
            self.assertFalse(self.module.is_valid(value))
        for value in (self.admission(), self.result(), self.answer(), self.staff()):
            self.assertTrue(self.valid('server', value))
            self.assertFalse(self.valid('client', value))
            self.assertFalse(self.module.is_valid(value))
        for value in ({}, [], None, True, {'kind': 'message', 'sender': 'staff', 'text': 'x'}):
            for direction in ('client', 'server'):
                self.assertFalse(self.valid(direction, value))

    def test_ticket_and_current_projection_require_all_fields(self):
        for direction, original in (('client', self.submit()), ('client', self.reconcile()),
                                    ('server', self.admission()), ('server', self.answer()),
                                    ('server', self.staff())):
            for key in original:
                value = copy.deepcopy(original)
                del value[key]
                self.assertFalse(self.valid(direction, value), key)
        for original, key, direction in ((self.submit(), 'expected_consent_revision', 'client'),
                                         (self.admission(), 'consent_revision', 'server')):
            for revision in (None, 1, 9007199254740991):
                self.assertTrue(self.valid(direction, {**original, key: revision}))
            for revision in (0, -1, True, '1', 1.5, 9007199254740992):
                self.assertFalse(self.valid(direction, {**original, key: revision}))

    def test_uuid_and_exact_integer_bounds_reject_coercion(self):
        for field in ('channel_id', 'stream_id', 'operation_id'):
            for value in (None, self.operation.upper(), ' ' + self.operation, 'not-a-uuid',
                          '019f1d32-0000-7000-8000-000000000001'):
                self.assertFalse(self.valid('client', {**self.submit(), field: value}))
        for field in ('command_revision',):
            for value in (0, -1, True, '1', 1.5, 9007199254740992):
                self.assertFalse(self.valid('client', {**self.submit(), field: value}))
        for field in ('sequence',):
            for value in (0, -1, True, '2', 2.5, 9007199254740992):
                self.assertFalse(self.valid('server', {**self.answer(), field: value}))
        self.assertFalse(self.valid('server', {**self.admission(), 'proof_generation': 1}))

    def test_text_character_bounds_are_independent_of_actual_wire_bytes(self):
        for direction, factory, field, maximum in (('client', self.submit, 'text', 2000),
                                                   ('server', self.answer, 'answer', 4000),
                                                   ('server', self.staff, 'text', 4000)):
            for text in ('x', 'x' * maximum, '\U0001f333' * maximum):
                value = factory()
                value['payload'][field] = text
                self.assertTrue(self.valid(direction, value))
            for text in ('', 'x' * (maximum + 1), None, 1, [], {}):
                value = factory()
                value['payload'][field] = text
                self.assertFalse(self.valid(direction, value))
        # JSON shape does not establish scalar validity, whitespace policy or encoded byte size.
        for text in (' ', '\ud800', '<script>untrusted</script>'):
            value = self.submit()
            value['payload']['text'] = text
            self.assertTrue(self.valid('client', value))

    def test_composed_events_and_nested_payloads_are_closed(self):
        for factory in (self.result, self.answer, self.staff):
            original = factory()
            for field in ('sender', 'provider', 'staff_id', 'csrf_token', 'confirmed',
                          'channel_id', 'proof_generation', 'consent_revision'):
                self.assertFalse(self.valid('server', {**original, field: 'forbidden'}))
                value = copy.deepcopy(original)
                value['payload'][field] = 'forbidden'
                self.assertFalse(self.valid('server', value))
            value = copy.deepcopy(original)
            value['release_identity']['grant'] = True
            self.assertFalse(self.valid('server', value))
        for factory in (self.submit, self.reconcile):
            for field in ('sender', 'provider', 'staff_id', 'sequence', 'proof_generation'):
                self.assertFalse(self.valid('client', {**factory(), field: 'forbidden'}))
        self.assertFalse(self.valid('client', {**self.reconcile(), 'payload': {'text': 'replay'}}))

    def test_result_states_require_their_exact_safe_recovery(self):
        accepted = (self.result(), self.result('forwarded'),
                    self.result('pending', recovery='reconcile'),
                    self.result('refused', code='source_unavailable', recovery='human_or_book'),
                    self.result('unavailable', code='outcome_unavailable', recovery='reconcile'))
        for value in accepted:
            self.assertTrue(self.valid('server', value))
        rejected = (self.result('complete'), self.result('pending'),
                    self.result('admitted', recovery='reconcile'),
                    self.result('forwarded', code='outcome_unavailable'),
                    self.result('pending', code='guidance_unavailable', recovery='reconcile'),
                    self.result('refused', code='outcome_unavailable', recovery='contact_or_book'),
                    self.result('unavailable', code='outcome_unavailable', recovery='human_or_book'))
        for value in rejected:
            self.assertFalse(self.valid('server', value))

    def test_answers_require_bounded_closed_source_references(self):
        for count in (1, 8):
            value = self.answer()
            value['payload']['sources'] = [
                {'document_id': f'document-{i}', 'route_key': f'route-{i}', 'document_sha256': 'b' * 64}
                for i in range(count)]
            self.assertTrue(self.valid('server', value))
        for count in (0, 9):
            value = self.answer()
            value['payload']['sources'] *= count
            self.assertFalse(self.valid('server', value))
        value = self.answer()
        value['payload']['sources'] *= 2
        self.assertFalse(self.valid('server', value))
        for field, content in (('url', 'https://example.invalid'), ('document_sha256', 'B' * 64),
                               ('document_sha256', 'not-a-digest')):
            value = self.answer()
            value['payload']['sources'][0][field] = content
            self.assertFalse(self.valid('server', value))
        value = self.answer()
        value['payload']['outcome'] = 'binding_quote'
        self.assertFalse(self.valid('server', value))

    def test_shape_cannot_prove_ticket_issuance_sources_staff_or_safety(self):
        # Well-shaped but unissued/stale/fabricated claims still need the actual admission boundary.
        value = self.submit()
        value['operation_id'] = self.channel
        self.assertTrue(self.valid('client', value))
        self.assertTrue(self.valid('server', self.answer()))
        self.assertTrue(self.valid('server', self.staff()))


if __name__ == '__main__':
    unittest.main()

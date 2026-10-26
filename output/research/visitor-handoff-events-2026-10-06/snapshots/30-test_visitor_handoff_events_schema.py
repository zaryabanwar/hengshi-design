"""Preview/status schema boundary; no actual preparation, digest, consent or lifecycle proof."""
import copy
import json
import unittest

from jsonschema import Draft202012Validator
from referencing import Resource

from scripts.validation import test_booking_creation_request_schema as fixture


class VisitorHandoffEventShapeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        base = fixture.BookingCreationRequestShapeTests
        base.setUpClass()
        registry = base.registry
        for name in ('chat-creation-request.schema.json', 'chat-text.schema.json',
                     'staff-handoff-request.schema.json', 'staff-handoff-response.schema.json',
                     'visitor-handoff.schema.json', 'visitor-handoff-events.schema.json'):
            path = fixture.CONTRACTS / name
            schema = json.loads(path.read_text(encoding='utf-8'))
            Draft202012Validator.check_schema(schema)
            registry = registry.with_resource(path.as_uri(), Resource.from_contents(schema))
        cls.validators = {direction: Draft202012Validator(
            {'$ref': path.as_uri() + '#/$defs/' + direction}, registry=registry,
            format_checker=base.checker) for direction in ('client', 'server')}
        cls.module = Draft202012Validator({'$ref': path.as_uri()}, registry=registry)

    event_id = '919108f7-52d1-4320-9bac-f847db4148a8'
    operation_id = '9c3567ad-12bf-4b3a-a76d-7e56b9dfe051'
    stream_id = 'f0839ee7-708d-4ecb-8cb3-1283c1e2f3aa'

    def selected(self):
        return [{'stream_id': self.stream_id, 'event_id': self.event_id, 'sequence': 1}]

    def prepare(self):
        return {'protocol_version': 1, 'kind': 'prepare_handoff_preview',
                'channel_id': self.event_id, 'stream_id': self.stream_id,
                'operation_id': self.operation_id, 'expected_consent_revision': 2,
                'context': {'release_id': 'SYNTHETIC-RELEASE', 'manifest_sha256': 'b' * 64,
                            'wing_key': 'ROUTE-WING-DIGITAL'}, 'selected_events': self.selected()}

    def event(self, kind, payload):
        return {'protocol_version': 1, 'kind': kind, 'stream_id': self.stream_id,
                'event_id': self.event_id, 'sequence': 2,
                'release_identity': {'release_id': 'SYNTHETIC-RELEASE', 'manifest_sha256': 'b' * 64},
                'payload': payload}

    def preview(self):
        projection = {'projection_id': self.event_id, 'projection_revision': 1,
                      'context': self.prepare()['context'], 'consent_revision': 2,
                      'purpose_key': 'SYNTHETIC-NOT-APPROVED',
                      'notice_reference': {'notice_id': 'SYNTHETIC-NOTICE',
                                           'notice_revision': 'SYNTHETIC-REVISION',
                                           'notice_sha256': 'c' * 64},
                      'selected_events': self.selected(), 'text': 'Visitor: synthetic question.'}
        return self.event('handoff_preview', {'operation_id': self.operation_id, 'state': 'prepared',
                          'projection_reference': {'projection_id': self.event_id,
                                                   'projection_revision': 1, 'projection_sha256': 'a' * 64},
                          'projection': projection})

    def test_directions_module_and_closed_client_intents(self):
        prepare = self.prepare()
        self.assertTrue(self.validators['client'].is_valid(prepare))
        self.assertFalse(self.validators['server'].is_valid(prepare))
        self.assertFalse(self.module.is_valid(prepare))
        reconcile = {k: v for k, v in prepare.items()
                     if k in ('protocol_version', 'channel_id', 'stream_id', 'operation_id')}
        reconcile['kind'] = 'reconcile_handoff_preview'
        self.assertTrue(self.validators['client'].is_valid(reconcile))
        for key in ('context', 'selected_events', 'expected_consent_revision'):
            invalid = copy.deepcopy(reconcile)
            invalid[key] = prepare[key]
            self.assertFalse(self.validators['client'].is_valid(invalid))
        inspect = {k: v for k, v in reconcile.items() if k != 'operation_id'}
        inspect.update(kind='inspect_handoff', handoff_id=self.event_id)
        self.assertTrue(self.validators['client'].is_valid(inspect))
        self.assertTrue(self.validators['server'].is_valid(self.preview()))
        self.assertFalse(self.validators['client'].is_valid(self.preview()))

    def test_selected_events_are_bounded_closed_references(self):
        boundary = self.prepare()
        boundary['selected_events'] = [
            {'stream_id': self.stream_id, 'event_id': f'919108f7-52d1-4320-9bac-f847db41{n:04x}',
             'sequence': n + 1} for n in range(16)]
        self.assertTrue(self.validators['client'].is_valid(boundary))
        boundary['selected_events'].append({
            'stream_id': self.stream_id, 'event_id': '919108f7-52d1-4320-9bac-f847db410010',
            'sequence': 17})
        self.assertFalse(self.validators['client'].is_valid(boundary))
        for value in ([], self.selected() * 2, self.selected() * 17, [{'text': 'untrusted'}]):
            invalid = self.prepare()
            invalid['selected_events'] = value
            self.assertFalse(self.validators['client'].is_valid(invalid))
        for key, value in (('sequence', True), ('event_id', 'not-a-uuid'), ('role', 'staff')):
            invalid = self.prepare()
            invalid['selected_events'][0][key] = value
            self.assertFalse(self.validators['client'].is_valid(invalid))
        for key in self.prepare():
            invalid = self.prepare()
            del invalid[key]
            self.assertFalse(self.validators['client'].is_valid(invalid))

    def test_no_identity_consent_or_raw_history_can_be_injected(self):
        for field in ('staff_id', 'owner', 'role', 'proof', 'csrf_token', 'consent', 'transcript',
                      'text', 'provider', 'accepted', 'expires_at'):
            invalid = self.prepare()
            invalid[field] = 'untrusted'
            self.assertFalse(self.validators['client'].is_valid(invalid))
        for field in ('staff_id', 'role', 'approval', 'projection_sha256', 'html', 'provider'):
            invalid = self.preview()
            invalid['payload']['projection'][field] = 'untrusted'
            self.assertFalse(self.validators['server'].is_valid(invalid))
        invalid = self.preview()
        invalid['payload']['projection']['text'] = 'x' * 8001
        self.assertFalse(self.validators['server'].is_valid(invalid))

    def test_pending_and_unavailable_cannot_include_prepared_context(self):
        pending = self.event('handoff_preview', {'operation_id': self.operation_id,
                             'state': 'pending', 'recovery': 'reconcile_same_operation'})
        self.assertTrue(self.validators['server'].is_valid(pending))
        for key, value in (('projection', self.preview()['payload']['projection']),
                           ('projection_reference', self.preview()['payload']['projection_reference']),
                           ('recovery', 'retry_apply')):
            invalid = copy.deepcopy(pending)
            invalid['payload'][key] = value
            self.assertFalse(self.validators['server'].is_valid(invalid))
        unavailable = self.event('handoff_preview', {'operation_id': self.operation_id,
                                'state': 'unavailable', 'code': 'sharing_unavailable',
                                'recovery': 'review_or_contact_book'})
        self.assertTrue(self.validators['server'].is_valid(unavailable))
        unavailable['payload']['detail'] = 'private reason'
        self.assertFalse(self.validators['server'].is_valid(unavailable))

    def test_status_is_minimal_and_cannot_invent_parallel_outcomes(self):
        for state in ('requested', 'queued', 'accepted', 'text_active', 'declined', 'ended', 'expired'):
            event = self.event('handoff_status', {'handoff_id': self.event_id,
                               'handoff_revision': 1, 'state': state})
            self.assertTrue(self.validators['server'].is_valid(event))
            for key in ('staff_id', 'reason_reference', 'transcript', 'media_consent',
                        'booking_confirmed', 'deleted', 'callback_promised'):
                invalid = copy.deepcopy(event)
                invalid['payload'][key] = 'untrusted'
                self.assertFalse(self.validators['server'].is_valid(invalid))
        event = self.event('handoff_status_unavailable', {
            'state': 'unavailable', 'recovery': 'preserve_known_state_contact_or_book'})
        self.assertTrue(self.validators['server'].is_valid(event))
        event['payload']['handoff_id'] = self.event_id
        self.assertFalse(self.validators['server'].is_valid(event))

    def test_shape_cannot_prove_digest_selection_or_status_truth(self):
        preview = self.preview()
        # A fabricated digest or unbound source reference can be well-shaped.
        preview['payload']['projection_reference']['projection_id'] = self.operation_id
        self.assertTrue(self.validators['server'].is_valid(preview))
        # Shape cannot detect one event ID repeated with a changed sequence.
        prepare = self.prepare()
        prepare['selected_events'].append(dict(prepare['selected_events'][0], sequence=2))
        self.assertTrue(self.validators['client'].is_valid(prepare))
        # No authoritative transaction/state is exercised by an accepted-state representation.
        status = self.event('handoff_status', {'handoff_id': self.event_id,
                            'handoff_revision': 9007199254740991, 'state': 'accepted'})
        self.assertTrue(self.validators['server'].is_valid(status))


if __name__ == '__main__':
    unittest.main()

"""Exercise proposed request validators; never HTTP, permission or transition proof."""
import copy
import json
import unittest

from jsonschema import Draft202012Validator
from referencing import Resource

from scripts.validation import test_booking_creation_request_schema as fixture


class StaffHandoffRequestShapeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        base = fixture.BookingCreationRequestShapeTests
        base.setUpClass()
        path = fixture.CONTRACTS / 'staff-handoff-request.schema.json'
        schema = json.loads(path.read_text(encoding='utf-8'))
        Draft202012Validator.check_schema(schema)
        registry = base.registry.with_resource(path.as_uri(), Resource.from_contents(schema))
        cls.validators = {
            endpoint: Draft202012Validator(
                {'$ref': path.as_uri() + '#/$defs/' + endpoint + '_request'},
                registry=registry, format_checker=base.checker)
            for endpoint in ('accept', 'decline', 'end')
        }
        cls.module = Draft202012Validator({'$ref': path.as_uri()}, registry=registry)

    intents = {'accept': 'accept_text_handoff', 'decline': 'decline_text_handoff',
               'end': 'end_text_consultation'}

    def request(self, endpoint, phase='apply'):
        request = {
            'phase': phase, 'intent': self.intents[endpoint],
            'operation_id': 'f0839ee7-708d-4ecb-8cb3-1283c1e2f3aa',
            'expected': {'handoff_id': '919108f7-52d1-4320-9bac-f847db4148a8',
                         'handoff_revision': 2, 'ownership_generation': 1}}
        if phase == 'apply' and endpoint == 'accept':
            request['expected_consent_revision'] = 3
        if phase == 'apply' and endpoint == 'decline':
            request['reason_reference'] = {
                'reason_key': 'SYNTHETIC-NOT-A-PERMITTED-REASON',
                'catalogue_revision': 'synthetic-revision', 'catalogue_sha256': 'a' * 64}
        return request

    def test_endpoint_and_phase_are_explicit_and_module_denies(self):
        for endpoint in self.validators:
            for phase in ('apply', 'reconcile'):
                request = self.request(endpoint, phase)
                self.assertTrue(self.validators[endpoint].is_valid(request))
                self.assertFalse(self.module.is_valid(request))
                for other in self.validators:
                    if other != endpoint:
                        self.assertFalse(self.validators[other].is_valid(request))
                for value in (None, [], True, 'apply', {}, {'phase': 'apply'}):
                    self.assertFalse(self.validators[endpoint].is_valid(value))

    def test_authority_and_unrelated_private_fields_cannot_be_smuggled(self):
        fields = ('staff_id', 'sender', 'role', 'assignment', 'session_id', 'target',
                  'consent', 'expires_at', 'text', 'transcript', 'provider_result',
                  'deleted', 'cancel_booking', 'availability', 'proof', 'csrf_token')
        for endpoint, validator in self.validators.items():
            for field in fields:
                for level in ('root', 'expected'):
                    with self.subTest(endpoint=endpoint, field=field, level=level):
                        request = self.request(endpoint)
                        target = request if level == 'root' else request['expected']
                        target[field] = 'untrusted'
                        self.assertFalse(validator.is_valid(request))

    def test_reconciliation_carries_no_new_intent_payload(self):
        for endpoint, validator in self.validators.items():
            request = self.request(endpoint, 'reconcile')
            for field, value in (
                    ('expected_consent_revision', 9), ('reason_reference', {}),
                    ('text', 'new payload'), ('expected', None)):
                invalid = copy.deepcopy(request)
                invalid[field] = value
                self.assertFalse(validator.is_valid(invalid))
            invalid = copy.deepcopy(request)
            invalid['phase'] = 'replay_then_apply'
            self.assertFalse(validator.is_valid(invalid))

    def test_references_and_revision_boundaries_are_not_coerced(self):
        request = self.request('end')
        validator = self.validators['end']
        for field in ('handoff_revision', 'ownership_generation'):
            for value in (0, -1, True, '2', None, 1.5, 9007199254740992):
                invalid = copy.deepcopy(request)
                invalid['expected'][field] = value
                self.assertFalse(validator.is_valid(invalid))
            valid = copy.deepcopy(request)
            valid['expected'][field] = 9007199254740991
            self.assertTrue(validator.is_valid(valid))
        for field, target in (('operation_id', request), ('handoff_id', request['expected'])):
            original = target[field]
            for value in (original.upper(), original + '\n', 'not-a-uuid', None, 42):
                invalid = copy.deepcopy(request)
                replacement = invalid if field == 'operation_id' else invalid['expected']
                replacement[field] = value
                self.assertFalse(validator.is_valid(invalid))
        invalid = copy.deepcopy(request)
        invalid['operation_id'] = '019f1d32-0000-7000-8000-000000000001'
        self.assertFalse(validator.is_valid(invalid))

    def test_decline_reason_reference_is_closed_and_complete(self):
        request = self.request('decline')
        validator = self.validators['decline']
        for key in ('reason_key', 'catalogue_revision', 'catalogue_sha256'):
            invalid = copy.deepcopy(request)
            del invalid['reason_reference'][key]
            self.assertFalse(validator.is_valid(invalid))
        for key, value in (('note', 'private free text'), ('approved', True),
                           ('catalogue_sha256', 'A' * 64), ('catalogue_sha256', 'a' * 64 + '\n')):
            invalid = copy.deepcopy(request)
            invalid['reason_reference'][key] = value
            self.assertFalse(validator.is_valid(invalid))

    def test_required_fields_and_shape_limitations_are_explicit(self):
        for endpoint, validator in self.validators.items():
            request = self.request(endpoint)
            for key in list(request):
                invalid = copy.deepcopy(request)
                del invalid[key]
                self.assertFalse(validator.is_valid(invalid))
            for key in list(request['expected']):
                invalid = copy.deepcopy(request)
                del invalid['expected'][key]
                self.assertFalse(validator.is_valid(invalid))
        # Schema cannot establish whether this expected consent revision grants acceptance.
        request = self.request('accept')
        request['expected_consent_revision'] = None
        self.assertTrue(self.validators['accept'].is_valid(request))
        # An arbitrary well-shaped reference does not make a reason catalogue approved.
        self.assertTrue(self.validators['decline'].is_valid(self.request('decline')))


if __name__ == '__main__':
    unittest.main()

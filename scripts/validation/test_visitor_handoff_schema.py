"""Visitor handoff validator boundary, never permission, persistence or routing proof."""
import copy
import json
import unittest

from jsonschema import Draft202012Validator
from referencing import Resource

from scripts.validation import test_booking_creation_request_schema as fixture


class VisitorHandoffShapeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        base = fixture.BookingCreationRequestShapeTests
        base.setUpClass()
        registry = base.registry
        for name in ('chat-creation-request.schema.json', 'staff-handoff-response.schema.json',
                     'staff-handoff-request.schema.json', 'visitor-handoff.schema.json'):
            path = fixture.CONTRACTS / name
            schema = json.loads(path.read_text(encoding='utf-8'))
            Draft202012Validator.check_schema(schema)
            registry = registry.with_resource(path.as_uri(), Resource.from_contents(schema))
        cls.validators = {
            direction: Draft202012Validator(
                {'$ref': path.as_uri() + '#/$defs/' + direction},
                registry=registry, format_checker=base.checker)
            for direction in ('request', 'response')
        }
        cls.module = Draft202012Validator({'$ref': path.as_uri()}, registry=registry)

    def request(self, reviewed=False):
        sharing = {'kind': 'reviewed_projection', 'projection_reference': {
            'projection_id': '919108f7-52d1-4320-9bac-f847db4148a8',
            'projection_revision': 2, 'projection_sha256': 'a' * 64}} if reviewed else {
            'kind': 'no_prior_context'}
        return {'phase': 'apply', 'intent': 'request_text_handoff',
                'operation_id': 'f0839ee7-708d-4ecb-8cb3-1283c1e2f3aa',
                'context': {'release_id': 'SYNTHETIC-RELEASE', 'manifest_sha256': 'b' * 64,
                            'wing_key': 'ROUTE-WING-STRATEGY'},
                'expected_consent_revision': 3, 'sharing': sharing}

    def response(self, pending=False):
        result = {'state': 'pending', 'recovery': 'reconcile_same_operation'} if pending else {
            'state': 'requested', 'applied_binding': {
                'handoff_id': '9c3567ad-12bf-4b3a-a76d-7e56b9dfe051', 'handoff_revision': 1},
            'sharing': self.request()['sharing']}
        return {'intent': 'request_text_handoff',
                'operation_id': self.request()['operation_id'], 'result': result}

    def test_directions_and_apply_or_reconcile_are_explicit(self):
        for reviewed in (False, True):
            request = self.request(reviewed)
            self.assertTrue(self.validators['request'].is_valid(request))
            self.assertFalse(self.validators['response'].is_valid(request))
            self.assertFalse(self.module.is_valid(request))
        reconcile = {'phase': 'reconcile', 'intent': 'request_text_handoff',
                     'operation_id': self.request()['operation_id']}
        self.assertTrue(self.validators['request'].is_valid(reconcile))
        for key in ('context', 'expected_consent_revision', 'sharing'):
            invalid = copy.deepcopy(reconcile)
            invalid[key] = self.request()[key]
            self.assertFalse(self.validators['request'].is_valid(invalid))
        for pending in (False, True):
            response = self.response(pending)
            self.assertTrue(self.validators['response'].is_valid(response))
            self.assertFalse(self.validators['request'].is_valid(response))
            self.assertFalse(self.module.is_valid(response))

    def test_authority_and_private_payload_cannot_be_injected(self):
        for field in ('session_id', 'staff_id', 'owner', 'role', 'availability', 'transcript',
                      'contact', 'consent', 'csrf_token', 'proof', 'expires_at', 'queue'):
            for level in ('root', 'context', 'sharing', 'projection_reference'):
                with self.subTest(field=field, level=level):
                    invalid = self.request(True)
                    target = (invalid if level == 'root' else invalid['context'] if level == 'context'
                              else invalid['sharing'] if level == 'sharing'
                              else invalid['sharing']['projection_reference'])
                    target[field] = 'untrusted'
                    self.assertFalse(self.validators['request'].is_valid(invalid))

    def test_apply_requires_explicit_department_consent_and_sharing(self):
        request = self.request(True)
        for key in request:
            invalid = copy.deepcopy(request)
            del invalid[key]
            self.assertFalse(self.validators['request'].is_valid(invalid))
        for key in request['context']:
            invalid = copy.deepcopy(request)
            del invalid['context'][key]
            self.assertFalse(self.validators['request'].is_valid(invalid))
        for value in (None, True, 0, '3', 1.5, 9007199254740992):
            invalid = copy.deepcopy(request)
            invalid['expected_consent_revision'] = value
            self.assertFalse(self.validators['request'].is_valid(invalid))
        invalid = copy.deepcopy(request)
        invalid['context']['wing_key'] = 'ROUTE-RECEPTION'
        self.assertFalse(self.validators['request'].is_valid(invalid))
        for value in (True, None, {'kind': 'full_history'}, {'kind': 'no_prior_context', 'text': 'old'}):
            invalid = copy.deepcopy(request)
            invalid['sharing'] = value
            self.assertFalse(self.validators['request'].is_valid(invalid))

    def test_reviewed_projection_has_exact_closed_reference(self):
        request = self.request(True)
        projection = request['sharing']['projection_reference']
        for key in projection:
            invalid = copy.deepcopy(request)
            del invalid['sharing']['projection_reference'][key]
            self.assertFalse(self.validators['request'].is_valid(invalid))
        for key, value in (('projection_id', 'not-a-uuid'), ('projection_revision', True),
                           ('projection_sha256', 'A' * 64), ('projection_sha256', 'a' * 64 + '\n')):
            invalid = copy.deepcopy(request)
            invalid['sharing']['projection_reference'][key] = value
            self.assertFalse(self.validators['request'].is_valid(invalid))
        for value in (None, [], True, {}, {'phase': 'apply'}):
            self.assertFalse(self.validators['request'].is_valid(value))

    def test_requested_cannot_claim_acceptance_or_current_ownership(self):
        response = self.response()
        for key in response:
            invalid = copy.deepcopy(response)
            del invalid[key]
            self.assertFalse(self.validators['response'].is_valid(invalid))
        for state in ('queued', 'accepted', 'text_active', 'connected', 'alert_delivered', 'ended'):
            invalid = copy.deepcopy(response)
            invalid['result']['state'] = state
            self.assertFalse(self.validators['response'].is_valid(invalid))
        for field in ('staff_id', 'ownership_generation', 'available', 'media_consent', 'transcript'):
            for level in ('root', 'result', 'binding'):
                invalid = copy.deepcopy(response)
                target = (invalid if level == 'root' else invalid['result'] if level == 'result'
                          else invalid['result']['applied_binding'])
                target[field] = 'untrusted'
                self.assertFalse(self.validators['response'].is_valid(invalid))

    def test_pending_and_errors_cannot_claim_success_or_redispatch(self):
        pending = self.response(True)
        for key, value in (('applied_binding', self.response()['result']['applied_binding']),
                           ('sharing', self.request()['sharing']), ('recovery', 'retry_apply')):
            invalid = copy.deepcopy(pending)
            invalid['result'][key] = value
            self.assertFalse(self.validators['response'].is_valid(invalid))
        error = {'error': {'code': 'staff_unavailable', 'recovery': 'contact_or_book'}}
        self.assertTrue(self.validators['response'].is_valid(error))
        for key, value in (('detail', 'private reason'), ('staff_id', 'some-owner'),
                           ('recovery', 'retry_apply'), ('code', 'session_does_not_exist')):
            invalid = copy.deepcopy(error)
            invalid['error'][key] = value
            self.assertFalse(self.validators['response'].is_valid(invalid))
        invalid = copy.deepcopy(error)
        invalid.update(self.response())
        self.assertFalse(self.validators['response'].is_valid(invalid))
        reason_error = {'error': {'code': 'reason_unavailable',
                                  'recovery': 'inspect_authorized_current_state'}}
        self.assertFalse(self.validators['response'].is_valid(reason_error))

    def test_valid_shapes_do_not_prove_preview_consent_or_effect(self):
        # A syntactically valid arbitrary reference does not establish a real approved preview.
        self.assertTrue(self.validators['request'].is_valid(self.request(True)))
        # The schema cannot correlate these synthetic response fields to an awaited operation.
        response = self.response()
        response['operation_id'] = '919108f7-52d1-4320-9bac-f847db4148a8'
        response['result']['sharing'] = self.request(True)['sharing']
        self.assertTrue(self.validators['response'].is_valid(response))


if __name__ == '__main__':
    unittest.main()

"""Response validator boundary only; no actual HTTP, transition or suppression proof."""
import copy
import json
import unittest

from jsonschema import Draft202012Validator
from referencing import Resource

from scripts.validation import test_booking_creation_request_schema as fixture


class StaffHandoffResponseShapeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        base = fixture.BookingCreationRequestShapeTests
        base.setUpClass()
        registry = base.registry
        for name in ('staff-handoff-request.schema.json', 'staff-handoff-response.schema.json'):
            path = fixture.CONTRACTS / name
            schema = json.loads(path.read_text(encoding='utf-8'))
            Draft202012Validator.check_schema(schema)
            registry = registry.with_resource(path.as_uri(), Resource.from_contents(schema))
        cls.validators = {
            endpoint: Draft202012Validator(
                {'$ref': path.as_uri() + '#/$defs/' + endpoint + '_response'},
                registry=registry, format_checker=base.checker)
            for endpoint in ('accept', 'decline', 'end')
        }
        cls.module = Draft202012Validator({'$ref': path.as_uri()}, registry=registry)
        request_path = fixture.CONTRACTS / 'staff-handoff-request.schema.json'
        cls.end_request_validator = Draft202012Validator(
            {'$ref': request_path.as_uri() + '#/$defs/end_request'},
            registry=registry, format_checker=base.checker)

    def outcome(self, endpoint, pending=False):
        intents = {'accept': 'accept_text_handoff', 'decline': 'decline_text_handoff',
                   'end': 'end_text_consultation'}
        states = {'accept': 'accepted', 'decline': 'declined', 'end': 'ended'}
        result = {'state': 'pending', 'recovery': 'reconcile_same_operation'} if pending else {
            'state': states[endpoint],
            'applied_binding': {'handoff_id': '919108f7-52d1-4320-9bac-f847db4148a8',
                                'handoff_revision': 3, 'ownership_generation': 1}}
        if endpoint == 'decline' and not pending:
            result['reason_reference'] = {
                'reason_key': 'SYNTHETIC-NOT-APPROVED', 'catalogue_revision': 'synthetic',
                'catalogue_sha256': 'a' * 64}
        return {'operation_id': 'f0839ee7-708d-4ecb-8cb3-1283c1e2f3aa',
                'intent': intents[endpoint], 'result': result}

    def test_endpoint_outcomes_and_direction_are_closed(self):
        for endpoint, validator in self.validators.items():
            for pending in (False, True):
                outcome = self.outcome(endpoint, pending)
                self.assertTrue(validator.is_valid(outcome))
                self.assertFalse(self.module.is_valid(outcome))
                self.assertFalse(self.end_request_validator.is_valid(outcome))
                for other in self.validators:
                    if other != endpoint:
                        self.assertFalse(self.validators[other].is_valid(outcome))
            for state in ('text_active', 'connected', 'deleted', 'cancelled', 'confirmed'):
                invalid = self.outcome(endpoint)
                invalid['result']['state'] = state
                self.assertFalse(validator.is_valid(invalid))

    def test_no_unrelated_private_or_success_fields_can_be_added(self):
        for endpoint, validator in self.validators.items():
            for field in ('staff_id', 'current_owner', 'transcript', 'csrf_token', 'provider_result',
                          'deleted', 'booking_cancelled', 'socket_closed', 'media_consent'):
                for level in ('root', 'result', 'binding'):
                    with self.subTest(endpoint=endpoint, field=field, level=level):
                        invalid = self.outcome(endpoint)
                        target = (invalid if level == 'root' else invalid['result'] if level == 'result'
                                  else invalid['result']['applied_binding'])
                        target[field] = 'untrusted'
                        self.assertFalse(validator.is_valid(invalid))

    def test_pending_cannot_claim_terminal_binding_or_dispatch_recovery(self):
        for endpoint, validator in self.validators.items():
            pending = self.outcome(endpoint, True)
            for key, value in (('applied_binding', self.outcome(endpoint)['result']['applied_binding']),
                               ('reason_reference', {}), ('recovery', 'retry_apply'),
                               ('recovery', 'create_new_operation'), ('state', 'ended')):
                invalid = copy.deepcopy(pending)
                invalid['result'][key] = value
                self.assertFalse(validator.is_valid(invalid))

    def test_errors_have_fixed_recovery_and_no_private_projection(self):
        for validator in self.validators.values():
            valid = {'error': {'code': 'outcome_unresolved', 'recovery': 'reconcile_same_operation'}}
            self.assertTrue(validator.is_valid(valid))
            for key, value in (('recovery', 'retry_apply'), ('detail', 'private exception'),
                               ('current_binding', {}), ('operation_id', 'private-id'),
                               ('code', 'handoff_does_not_exist')):
                invalid = copy.deepcopy(valid)
                invalid['error'][key] = value
                self.assertFalse(validator.is_valid(invalid))
            invalid = copy.deepcopy(valid)
            invalid.update(self.outcome('end'))
            self.assertFalse(validator.is_valid(invalid))
        reason_error = {'error': {'code': 'reason_unavailable',
                                  'recovery': 'inspect_authorized_current_state'}}
        self.assertTrue(self.validators['decline'].is_valid(reason_error))
        self.assertFalse(self.validators['accept'].is_valid(reason_error))
        self.assertFalse(self.validators['end'].is_valid(reason_error))

    def test_required_values_and_nested_boundaries(self):
        for endpoint, validator in self.validators.items():
            valid = self.outcome(endpoint)
            for key in valid:
                invalid = copy.deepcopy(valid)
                del invalid[key]
                self.assertFalse(validator.is_valid(invalid))
            for key in valid['result']:
                invalid = copy.deepcopy(valid)
                del invalid['result'][key]
                self.assertFalse(validator.is_valid(invalid))
            for key in valid['result']['applied_binding']:
                invalid = copy.deepcopy(valid)
                del invalid['result']['applied_binding'][key]
                self.assertFalse(validator.is_valid(invalid))
            for value in (0, True, '3', 1.5, 9007199254740992):
                invalid = copy.deepcopy(valid)
                invalid['result']['applied_binding']['handoff_revision'] = value
                self.assertFalse(validator.is_valid(invalid))

    def test_well_shaped_response_does_not_prove_effect_or_correlation(self):
        outcome = self.outcome('end')
        # A validator cannot know that this UUID differs from the actual awaited request.
        outcome['operation_id'] = '9c3567ad-12bf-4b3a-a76d-7e56b9dfe051'
        self.assertTrue(self.validators['end'].is_valid(outcome))
        # Neither an arbitrary applied revision nor a reason reference establishes a real transition.
        outcome['result']['applied_binding']['handoff_revision'] = 9007199254740991
        self.assertTrue(self.validators['end'].is_valid(outcome))
        self.assertTrue(self.validators['decline'].is_valid(self.outcome('decline')))


if __name__ == '__main__':
    unittest.main()

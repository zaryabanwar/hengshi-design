"""Proposed chat request schema boundary; no application/consent enforcement proof."""
import copy
import json
import unittest

from jsonschema import Draft202012Validator, FormatChecker
from referencing import Registry, Resource

from test_booking_creation_request_schema import CONTRACTS, deny_remote


class ChatCreationRequestShapeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        resources = []
        for name in ('chat-creation-request.schema.json', 'booking-creation-request.schema.json',
                     'process-value.schema.json', 'publication-preparation.schema.json',
                     'publication-manifest.schema.json'):
            path = CONTRACTS / name
            schema = json.loads(path.read_text(encoding='utf-8'))
            Draft202012Validator.check_schema(schema)
            resources.append((path.as_uri(), Resource.from_contents(schema)))
        checker = FormatChecker(formats=['uuid'])
        if checker.conforms('not-a-uuid', 'uuid'):
            raise RuntimeError('UUID assertion unavailable')
        cls.validator = Draft202012Validator(
            {'$ref': (CONTRACTS / 'chat-creation-request.schema.json').as_uri()},
            registry=Registry(retrieve=deny_remote).with_resources(resources),
            format_checker=checker)

    def request(self):
        return {'phase': 'create',
                'provisional_id': '919108f7-52d1-4320-9bac-f847db4148a8',
                'operation_id': '9c3567ad-12bf-4b3a-a76d-7e56b9dfe051',
                'context': {'release_id': 'SYNTHETIC-RELEASE', 'manifest_sha256': 'a' * 64}}

    def decision(self, choice='grant'):
        return {'purpose_key': 'SYNTHETIC-PURPOSE',
                'notice_reference': {'notice_id': 'SYNTHETIC-NOTICE',
                                     'notice_revision': 'fixture-1', 'notice_sha256': 'b' * 64},
                'decision': choice}

    def test_bootstrap_is_payload_free(self):
        self.assertTrue(self.validator.is_valid({'phase': 'bootstrap'}))
        for key, value in (('context', self.request()['context']), ('consent', True),
                           ('message', 'hello'), ('proof', 'secret'), ('phase_typo', 'bootstrap')):
            with self.subTest(key=key):
                self.assertFalse(self.validator.is_valid({'phase': 'bootstrap', key: value}))

    def test_reception_and_each_canonical_wing(self):
        self.assertTrue(self.validator.is_valid(self.request()))
        for wing in ('ROUTE-WING-STRATEGY', 'ROUTE-WING-DIGITAL', 'ROUTE-WING-AI-DATA',
                     'ROUTE-WING-IMMERSIVE', 'ROUTE-WING-CLOUD-TRUST'):
            request = self.request()
            request['context']['wing_key'] = wing
            self.assertTrue(self.validator.is_valid(request))
        for wing in (None, '', 'RECEPTION', 'ROUTE-WING-UNKNOWN', [], 1):
            request = self.request()
            request['context']['wing_key'] = wing
            self.assertFalse(self.validator.is_valid(request))

    def test_required_fields_and_closed_objects(self):
        for key in ('phase', 'provisional_id', 'operation_id', 'context'):
            request = self.request()
            del request[key]
            self.assertFalse(self.validator.is_valid(request))
        for key in ('release_id', 'manifest_sha256'):
            request = self.request()
            del request['context'][key]
            self.assertFalse(self.validator.is_valid(request))
        for key in ('message', 'history', 'session_id', 'staff_id', 'csrf_token', 'expires_at'):
            request = self.request()
            request[key] = 'untrusted'
            self.assertFalse(self.validator.is_valid(request))
        request = self.request()
        request['context']['url'] = 'https://example.invalid'
        self.assertFalse(self.validator.is_valid(request))

    def test_reference_shapes_reject_coercion_and_wrong_operation_version(self):
        for key in ('provisional_id', 'operation_id'):
            value = self.request()[key]
            for bad in (None, 1, True, value.upper(), ' ' + value, value + '\n',
                        '{' + value + '}', 'not-a-uuid'):
                request = self.request()
                request[key] = bad
                self.assertFalse(self.validator.is_valid(request))
        request = self.request()
        request['operation_id'] = '019f1d32-0000-7000-8000-000000000001'
        self.assertFalse(self.validator.is_valid(request))

    def test_consent_refusal_and_grant_are_explicit_per_notice(self):
        for choice in ('grant', 'refuse'):
            request = self.request()
            request['consent'] = {'decisions': [self.decision(choice)]}
            self.assertTrue(self.validator.is_valid(request))
        for bad in (None, True, {}, {'decisions': []}, {'decisions': [True]},
                    {'decisions': [self.decision()], 'marketing': True}):
            request = self.request()
            request['consent'] = bad
            self.assertFalse(self.validator.is_valid(request))
        for key in ('purpose_key', 'notice_reference', 'decision'):
            request = self.request()
            decision = self.decision()
            del decision[key]
            request['consent'] = {'decisions': [decision]}
            self.assertFalse(self.validator.is_valid(request))

    def test_notice_binding_and_decision_are_closed(self):
        for key in ('notice_id', 'notice_revision', 'notice_sha256'):
            decision = self.decision()
            del decision['notice_reference'][key]
            request = self.request()
            request['consent'] = {'decisions': [decision]}
            self.assertFalse(self.validator.is_valid(request))
        for choice in (True, None, 'yes', 'withdraw', 'Grant'):
            request = self.request()
            request['consent'] = {'decisions': [self.decision(choice)]}
            self.assertFalse(self.validator.is_valid(request))
        decision = self.decision()
        decision['notice_reference']['text'] = 'caller notice'
        request = self.request()
        request['consent'] = {'decisions': [decision]}
        self.assertFalse(self.validator.is_valid(request))

    def test_consent_cap_and_whole_record_duplicates(self):
        request = self.request()
        decisions = []
        for i in range(8):
            decision = self.decision()
            decision['purpose_key'] = f'SYNTHETIC-{i}'
            decisions.append(decision)
        request['consent'] = {'decisions': decisions}
        self.assertTrue(self.validator.is_valid(request))
        decisions.append(self.decision())
        self.assertFalse(self.validator.is_valid(request))
        request['consent'] = {'decisions': [self.decision(), self.decision()]}
        self.assertFalse(self.validator.is_valid(request))

    def test_shape_explicitly_does_not_prove_policy_or_key_uniqueness(self):
        request = self.request()
        request['consent'] = {'decisions': [self.decision('grant'), self.decision('refuse')]}
        # Whole-record uniqueness is insufficient; semantic admission must deny repeated purposes.
        self.assertTrue(self.validator.is_valid(request))
        # All fixture notice/purpose/release references are synthetic, not approved policy.
        request['consent'] = {'decisions': [self.decision()]}
        self.assertTrue(self.validator.is_valid(request))


if __name__ == '__main__':
    unittest.main()

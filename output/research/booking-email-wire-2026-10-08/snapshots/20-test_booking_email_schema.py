"""Directional email schema boundary only; no auth, comparison or mail proof."""
import copy
import json
from pathlib import Path
import unittest

from jsonschema import Draft202012Validator, FormatChecker
from referencing import Resource
from scripts.validation import test_process_value_schema as common_fixture

CONTRACTS = Path(__file__).resolve().parents[2] / 'docs/phase-1-architecture/contracts'
OPERATION = '10286f82-cad4-4b14-a76a-e60d6c09ca09'
CHALLENGE = '20000000-0000-4000-8000-0000000000ab'


class BookingEmailShapeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        fixture = common_fixture.ProcessValueShapeTests
        fixture.setUpClass()
        registry = fixture.registry
        for name in ('booking-creation-request.schema.json', 'chat-creation-request.schema.json',
                     'booking-qualification.schema.json', 'booking-status-response.schema.json',
                     'booking-email.schema.json'):
            path = CONTRACTS / name
            schema = json.loads(path.read_text(encoding='utf-8'))
            Draft202012Validator.check_schema(schema)
            registry = registry.with_resource(path.as_uri(), Resource.from_contents(schema))
        checker = FormatChecker(formats=['uuid', 'date-time'])
        if checker.conforms('2026-02-30T00:00:00.000Z', 'date-time'):
            raise RuntimeError('Required calendar format assertion is unavailable')
        uri = (CONTRACTS / 'booking-email.schema.json').as_uri()
        cls.validators = {name: Draft202012Validator({'$ref': uri + '#/$defs/' + name},
            registry=registry, format_checker=checker)
            for name in ('challenge_request', 'verification_request', 'challenge_response',
                         'verification_response', 'current_controls')}
        cls.root = Draft202012Validator({'$ref': uri}, registry=registry, format_checker=checker)

    def request(self, kind):
        value = {'kind': kind, 'operation_id': OPERATION}
        if not kind.startswith('reconcile_'):
            value['expected_revision'] = 7
        if kind in ('resend_challenge', 'extend_challenge', 'verify_email'):
            value['challenge_ref'] = CHALLENGE
        if kind == 'verify_email':
            value['code'] = '01234567'
        return value

    def current(self):
        return {'state': 'known', 'revision': 8, 'challenge': {'state': 'active',
            'challenge_ref': CHALLENGE, 'expires_at': '2026-10-08T12:10:00.000Z', 'can_extend': True}}

    def applied(self, family):
        value = {'state': 'applied', 'operation_id': OPERATION, 'applied_revision': 8}
        if family == 'challenge':
            value['current'] = self.current()
        return value

    def test_closed_commands_are_directional(self):
        for kind in ('issue_challenge', 'resend_challenge', 'extend_challenge', 'reconcile_challenge'):
            value = self.request(kind)
            self.assertTrue(self.validators['challenge_request'].is_valid(value), kind)
            self.assertFalse(self.validators['verification_request'].is_valid(value), kind)
            self.assertFalse(self.root.is_valid(value))
        for kind in ('verify_email', 'reconcile_verification'):
            value = self.request(kind)
            self.assertTrue(self.validators['verification_request'].is_valid(value), kind)
            self.assertFalse(self.validators['challenge_request'].is_valid(value), kind)
            self.assertFalse(self.root.is_valid(value))

    def test_reconciliation_cannot_repeat_secret_or_mutation_metadata(self):
        for family, kind in (('challenge', 'reconcile_challenge'), ('verification', 'reconcile_verification')):
            for key, value in [('code', '01234567'), ('challenge_ref', CHALLENGE),
                               ('expected_revision', 7), ('email', 'synthetic@example.org'),
                               ('consent', {'decision': 'grant'})]:
                changed = dict(self.request(kind), **{key: value})
                self.assertFalse(self.validators[family + '_request'].is_valid(changed), (kind, key))

    def test_all_declared_request_members_are_required(self):
        for kind in ('issue_challenge', 'resend_challenge', 'extend_challenge', 'verify_email',
                     'reconcile_challenge', 'reconcile_verification'):
            family = 'verification' if kind in ('verify_email', 'reconcile_verification') else 'challenge'
            value = self.request(kind)
            for key in value:
                changed = copy.deepcopy(value)
                del changed[key]
                self.assertFalse(self.validators[family + '_request'].is_valid(changed), (kind, key))

    def test_server_and_personal_fields_cannot_be_injected(self):
        for kind in ('issue_challenge', 'verify_email'):
            family = 'verification' if kind == 'verify_email' else 'challenge'
            for key in ('email', 'qualification', 'consent', 'verified', 'expires_at',
                        'extension_seconds', 'attempts', 'proof', 'csrf_token', 'provider_id'):
                value = dict(self.request(kind), **{key: 'untrusted'})
                self.assertFalse(self.validators[family + '_request'].is_valid(value), key)
        self.assertFalse(self.validators['challenge_request'].is_valid(dict(self.request('issue_challenge'), challenge_ref=CHALLENGE)))

    def test_ascii_code_preserves_leading_zeroes_and_rejects_rewriting(self):
        for code in ('00000000', '01234567', '99999999'):
            value = dict(self.request('verify_email'), code=code)
            self.assertTrue(self.validators['verification_request'].is_valid(value))
        for code in ('1234567', '123456789', '01234567\n', ' 01234567', '0123 4567',
                     '\uff10\uff11\uff12\uff13\uff14\uff15\uff16\uff17',
                     '\u0660\u0661\u0662\u0663\u0664\u0665\u0666\u0667', 12345678, None):
            value = dict(self.request('verify_email'), code=code)
            self.assertFalse(self.validators['verification_request'].is_valid(value), repr(code))

    def test_uuid_v4_and_safe_revision_boundaries(self):
        for key in ('operation_id', 'challenge_ref'):
            for invalid in (CHALLENGE.upper(), ' '+CHALLENGE, CHALLENGE+'\n',
                            '00000000-0000-0000-0000-000000000000', '20000000-0000-7000-8000-000000000001'):
                value = dict(self.request('verify_email'), **{key: invalid})
                self.assertFalse(self.validators['verification_request'].is_valid(value), (key, invalid))
        for revision in (1, 9007199254740991):
            self.assertTrue(self.validators['verification_request'].is_valid(dict(self.request('verify_email'), expected_revision=revision)))
        for revision in (0, -1, 9007199254740992, True, '7', 1.5):
            self.assertFalse(self.validators['verification_request'].is_valid(dict(self.request('verify_email'), expected_revision=revision)), repr(revision))

    def test_current_projection_is_explicit_and_closed(self):
        validator = self.validators['current_controls']
        self.assertTrue(validator.is_valid({'state': 'unavailable'}))
        for challenge in ({'state': 'none'}, {'state': 'inactive', 'challenge_ref': CHALLENGE}, self.current()['challenge']):
            self.assertTrue(validator.is_valid({'state': 'known', 'revision': 8, 'challenge': challenge}))
        for value in ({'state': 'known'}, {'state': 'known', 'revision': 8},
                      {'state': 'unavailable', 'revision': 8},
                      {'state': 'known', 'revision': 8, 'challenge': {'state': 'none', 'challenge_ref': CHALLENGE}}):
            self.assertFalse(validator.is_valid(value), value)

    def test_inactive_cannot_retain_an_action_or_expiry(self):
        for key, value in (('expires_at', '2026-10-08T12:10:00.000Z'), ('can_extend', True),
                           ('remaining_guesses', 3), ('reason', 'used'), ('code', '01234567')):
            current = {'state': 'known', 'revision': 8, 'challenge': {'state': 'inactive', 'challenge_ref': CHALLENGE, key: value}}
            self.assertFalse(self.validators['current_controls'].is_valid(current), key)

    def test_expiry_has_calendar_and_canonical_utc_assertions(self):
        for stamp in ('2024-02-29T12:10:00.000Z', '2026-10-08T12:10:00.999Z'):
            value = self.current()
            value['challenge']['expires_at'] = stamp
            self.assertTrue(self.validators['current_controls'].is_valid(value))
        for stamp in ('2026-02-30T12:10:00.000Z', '2026-10-08T12:10:60.000Z',
                      '2026-10-08T12:10:00Z', '2026-10-08T12:10:00.000+00:00',
                      '2026-10-08T12:10:00.000Z\n'):
            value = self.current()
            value['challenge']['expires_at'] = stamp
            self.assertFalse(self.validators['current_controls'].is_valid(value), stamp)

    def test_extension_affordance_is_boolean_and_not_a_grant(self):
        for can_extend in (True, False):
            value = self.current()
            value['challenge']['can_extend'] = can_extend
            self.assertTrue(self.validators['current_controls'].is_valid(value))
        for can_extend in (1, 'true', None):
            value = self.current()
            value['challenge']['can_extend'] = can_extend
            self.assertFalse(self.validators['current_controls'].is_valid(value))

    def test_receipts_do_not_cross_response_directions(self):
        for family in ('challenge', 'verification'):
            applied = self.applied(family)
            self.assertTrue(self.validators[family+'_response'].is_valid(applied))
            other = 'verification' if family == 'challenge' else 'challenge'
            self.assertFalse(self.validators[other+'_response'].is_valid(applied))
            self.assertFalse(self.root.is_valid(applied))
            self.assertFalse(self.validators[family+'_request'].is_valid(applied))

    def test_pending_cannot_assert_applied_revision(self):
        for family in ('challenge', 'verification'):
            value = {'state': 'pending', 'operation_id': OPERATION}
            if family == 'challenge':
                value['current'] = {'state': 'unavailable'}
            self.assertTrue(self.validators[family+'_response'].is_valid(value))
            self.assertFalse(self.validators[family+'_response'].is_valid(dict(value, applied_revision=8)))

    def test_rejection_is_fixed_and_verification_only(self):
        value = {'state': 'rejected', 'code': 'VERIFICATION_UNAVAILABLE', 'recovery': 'refresh_status'}
        self.assertTrue(self.validators['verification_response'].is_valid(value))
        self.assertFalse(self.validators['challenge_response'].is_valid(value))
        for key in ('operation_id', 'code_value', 'email', 'remaining_guesses', 'reason'):
            self.assertFalse(self.validators['verification_response'].is_valid(dict(value, **{key: 'untrusted'})), key)

    def test_error_pairs_are_fixed_without_secret_echo(self):
        pairs = [('INVALID_REQUEST', 'correct_request'), ('ACCESS_UNAVAILABLE', 'contact'),
                 ('ACTION_DENIED', 'contact'), ('REVISION_CONFLICT', 'refresh_status'),
                 ('OPERATION_CONFLICT', 'reconcile'), ('STATE_CONFLICT', 'refresh_status'),
                 ('RATE_LIMIT', 'wait'), ('CAPACITY_LIMIT', 'wait'),
                 ('SERVICE_UNAVAILABLE', 'reconcile'), ('BODY_TOO_LARGE', 'correct_request'),
                 ('UNSUPPORTED_MEDIA', 'correct_request'), ('HEADER_TOO_LARGE', 'correct_request')]
        for family in ('challenge', 'verification'):
            validator = self.validators[family+'_response']
            for code, recovery in pairs:
                value = {'state': 'unavailable', 'code': code, 'recovery': recovery}
                self.assertTrue(validator.is_valid(value), code)
                self.assertFalse(validator.is_valid(dict(value, recovery='retry_automatically')), code)
                self.assertFalse(validator.is_valid(dict(value, payload='01234567')), code)

    def test_schema_does_not_establish_current_authority_or_cross_revision_truth(self):
        # Deliberately shaped, historically stale/inconsistent values remain schema-valid.
        request = self.request('verify_email')
        request['expected_revision'] = 1
        self.assertTrue(self.validators['verification_request'].is_valid(request))
        value = self.applied('challenge')
        value['current']['revision'] = 1
        value['current']['challenge']['expires_at'] = '2000-01-01T00:00:00.000Z'
        self.assertTrue(self.validators['challenge_response'].is_valid(value))


if __name__ == '__main__':
    unittest.main()

"""Proposed IF-BOOK-02 validator boundary only; no handler/business proof."""
import copy
import json
from pathlib import Path
import unittest

from jsonschema import Draft202012Validator
from referencing import Resource

from scripts.validation import test_process_value_schema as common_fixture

CONTRACTS = Path(__file__).resolve().parents[2] / 'docs/phase-1-architecture/contracts'
OPERATION = '10286f82-cad4-4b14-a76a-e60d6c09ca09'


class BookingQualificationShapeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        fixture = common_fixture.ProcessValueShapeTests
        fixture.setUpClass()
        registry = fixture.registry
        for name in ('booking-creation-request.schema.json', 'chat-creation-request.schema.json',
                     'booking-qualification.schema.json'):
            path = CONTRACTS / name
            schema = json.loads(path.read_text(encoding='utf-8'))
            Draft202012Validator.check_schema(schema)
            registry = registry.with_resource(path.as_uri(), Resource.from_contents(schema))
        uri = (CONTRACTS / 'booking-qualification.schema.json').as_uri()
        cls.request = Draft202012Validator({'$ref': uri + '#/$defs/request'},
                                          registry=registry, format_checker=fixture.checker)
        cls.response = Draft202012Validator({'$ref': uri + '#/$defs/response'},
                                           registry=registry, format_checker=fixture.checker)
        cls.root = Draft202012Validator({'$ref': uri}, registry=registry, format_checker=fixture.checker)

    def submission(self):
        return {'kind': 'set_qualification', 'operation_id': OPERATION, 'expected_revision': 7,
                'qualification': {'email': 'demo@example.org', 'organization': 'Synthetic Organization',
                                  'role': 'Technology lead', 'desired_outcome': 'Assess a synthetic prototype',
                                  'wing_key': 'ROUTE-WING-AI-DATA',
                                  'timing': {'description': 'Exploring options; timing undecided'}},
                'consent': {'purpose_key': 'synthetic_booking_purpose', 'decision': 'grant',
                            'notice_reference': {'notice_id': 'synthetic_notice', 'notice_revision': 'r1',
                                                 'notice_sha256': 'a' * 64}}}

    def applied(self):
        return {'state': 'applied', 'operation_id': OPERATION, 'applied_revision': 8}

    def test_submission_and_payload_free_reconciliation(self):
        self.assertTrue(self.request.is_valid(self.submission()))
        reconcile = {'kind': 'reconcile_qualification', 'operation_id': OPERATION}
        self.assertTrue(self.request.is_valid(reconcile))
        for key in ('qualification', 'consent', 'expected_revision', 'applied_revision', 'email'):
            changed = dict(reconcile, **{key: self.submission().get(key, 'demo@example.org')})
            self.assertFalse(self.request.is_valid(changed), key)

    def test_directional_contracts_and_rejecting_module_root(self):
        for request in (self.submission(), {'kind': 'reconcile_qualification', 'operation_id': OPERATION}):
            self.assertFalse(self.response.is_valid(request))
            self.assertFalse(self.root.is_valid(request))
        for response in (self.applied(), {'state': 'pending', 'operation_id': OPERATION}):
            self.assertTrue(self.response.is_valid(response))
            self.assertFalse(self.request.is_valid(response))
            self.assertFalse(self.root.is_valid(response))

    def test_six_fields_and_separate_consent_are_required(self):
        for field in ('email', 'organization', 'role', 'desired_outcome', 'wing_key', 'timing'):
            changed = self.submission()
            del changed['qualification'][field]
            self.assertFalse(self.request.is_valid(changed), field)
        changed = self.submission()
        del changed['consent']
        self.assertFalse(self.request.is_valid(changed))
        changed = self.submission()
        changed['qualification']['consent'] = changed.pop('consent')
        self.assertFalse(self.request.is_valid(changed))

    def test_budget_and_server_authority_cannot_be_injected(self):
        for field in ('budget', 'phone', 'name', 'upload', 'account_id', 'verified', 'owner_id',
                      'selected_slot', 'provider_event_ref', 'expires_at', 'consent'):
            changed = self.submission()
            changed['qualification'][field] = 'untrusted'
            self.assertFalse(self.request.is_valid(changed), field)
        for field in ('lineage_id', 'proof', 'csrf_token', 'proof_generation', 'state'):
            changed = self.submission()
            changed[field] = 'untrusted'
            self.assertFalse(self.request.is_valid(changed), field)

    def test_proposed_literal_field_bounds(self):
        # Fixed oracles from the wire proposal, never read from schema internals.
        for field, maximum in (('email', 320), ('organization', 200), ('role', 200),
                               ('desired_outcome', 2000)):
            changed = self.submission()
            changed['qualification'][field] = 'x' * maximum
            self.assertTrue(self.request.is_valid(changed), field)
            changed['qualification'][field] += 'x'
            self.assertFalse(self.request.is_valid(changed), field)
        changed = self.submission()
        changed['qualification']['timing']['description'] = 'x' * 500
        self.assertTrue(self.request.is_valid(changed))
        changed['qualification']['timing']['description'] += 'x'
        self.assertFalse(self.request.is_valid(changed))

    def test_unicode_codepoints_and_nonblank_are_distinct_from_utf16_and_graphemes(self):
        changed = self.submission()
        changed['qualification']['role'] = '\U0001f331' * 200
        self.assertTrue(self.request.is_valid(changed))
        changed['qualification']['role'] += '\U0001f331'
        self.assertFalse(self.request.is_valid(changed))
        changed = self.submission()
        changed['qualification']['role'] = 'e\u0301' * 100
        self.assertTrue(self.request.is_valid(changed))
        changed['qualification']['role'] += 'e\u0301'
        self.assertFalse(self.request.is_valid(changed))
        blanks = ('', ' ', '\t\n\r', '\u0085', '\u00a0', '\u1680', '\u2000\u200a',
                  '\u2028\u2029', '\u202f', '\u205f', '\u3000')
        for field in ('organization', 'role', 'desired_outcome'):
            for value in blanks:
                changed = self.submission()
                changed['qualification'][field] = value
                self.assertFalse(self.request.is_valid(changed), (field, repr(value)))

    def test_timing_is_one_description_without_calendar_or_delivery_claims(self):
        for value in ('soon', None, {}, {'description': ''}, {'description': '\u00a0'},
                      {'description': 'Undecided', 'deadline': '2041-01-01'},
                      {'start': '2041-01-01', 'timezone': 'Europe/Paris'}):
            changed = self.submission()
            changed['qualification']['timing'] = value
            self.assertFalse(self.request.is_valid(changed), value)

    def test_wings_are_the_same_five_keys_not_staff_assignments(self):
        for key in ('ROUTE-WING-STRATEGY', 'ROUTE-WING-DIGITAL', 'ROUTE-WING-AI-DATA',
                    'ROUTE-WING-IMMERSIVE', 'ROUTE-WING-CLOUD-TRUST'):
            changed = self.submission()
            changed['qualification']['wing_key'] = key
            self.assertTrue(self.request.is_valid(changed))
        for key in ('RECEPTION', 'ROUTE-WING-OTHER', 'route-wing-digital', 'owner-1', None):
            changed = self.submission()
            changed['qualification']['wing_key'] = key
            self.assertFalse(self.request.is_valid(changed))

    def test_grant_is_closed_and_references_exact_notice_shape(self):
        for decision in ('refuse', 'withdraw', True, None):
            changed = self.submission()
            changed['consent']['decision'] = decision
            self.assertFalse(self.request.is_valid(changed))
        for field in ('purpose_key', 'decision', 'notice_reference'):
            changed = self.submission()
            del changed['consent'][field]
            self.assertFalse(self.request.is_valid(changed))
        for field in ('notice_id', 'notice_revision', 'notice_sha256'):
            changed = self.submission()
            del changed['consent']['notice_reference'][field]
            self.assertFalse(self.request.is_valid(changed))
        changed = self.submission()
        changed['consent']['recorded_at'] = '2041-01-01'
        self.assertFalse(self.request.is_valid(changed))

    def test_operation_and_revision_metadata_use_existing_strict_shapes(self):
        for revision in (0, -1, True, '7', 1.5, 9007199254740992, None):
            changed = self.submission()
            changed['expected_revision'] = revision
            self.assertFalse(self.request.is_valid(changed), revision)
        for revision in (1, 9007199254740991):
            changed = self.submission()
            changed['expected_revision'] = revision
            self.assertTrue(self.request.is_valid(changed))
        for operation in (OPERATION.upper(), OPERATION + '\n', OPERATION.replace('-4b14-', '-7b14-'),
                          'not-a-uuid', None):
            changed = self.submission()
            changed['operation_id'] = operation
            self.assertFalse(self.request.is_valid(changed), operation)

    def test_minimal_applied_and_pending_results(self):
        self.assertTrue(self.response.is_valid(self.applied()))
        for key in ('operation_id', 'applied_revision', 'state'):
            changed = self.applied()
            del changed[key]
            self.assertFalse(self.response.is_valid(changed))
        for key in ('qualification', 'email', 'lineage', 'consent', 'csrf_token', 'proof', 'provider'):
            changed = self.applied()
            changed[key] = 'private'
            self.assertFalse(self.response.is_valid(changed), key)
        pending = {'state': 'pending', 'operation_id': OPERATION}
        self.assertTrue(self.response.is_valid(pending))
        pending['applied_revision'] = 8
        self.assertFalse(self.response.is_valid(pending))

    def test_field_errors_are_nonempty_closed_keys_and_fixed_reasons(self):
        rejected = {'state': 'rejected', 'code': 'INVALID_QUALIFICATION',
                    'recovery': 'correct_request', 'errors': {'email': 'invalid', 'consent': 'not_current'}}
        self.assertTrue(self.response.is_valid(rejected))
        for errors in ({}, [], {'name': 'required'}, {'email': 'demo@example.org'},
                       {'email': {'value': 'demo@example.org'}}, {'consent': 'too_long'},
                       {'wing_key': 'too_long'}):
            changed = dict(rejected, errors=errors)
            self.assertFalse(self.response.is_valid(changed), errors)
        changed = dict(rejected, operation_id=OPERATION)
        self.assertFalse(self.response.is_valid(changed))

    def test_unavailable_error_pairs_do_not_allow_arbitrary_diagnostics(self):
        pairs = (('INVALID_REQUEST', 'correct_request'), ('ACCESS_UNAVAILABLE', 'contact'),
                 ('ACTION_DENIED', 'contact'), ('REVISION_CONFLICT', 'refresh_status'),
                 ('OPERATION_CONFLICT', 'reconcile'), ('STATE_CONFLICT', 'refresh_status'),
                 ('CAPACITY_LIMIT', 'wait'), ('SERVICE_UNAVAILABLE', 'reconcile'),
                 ('BODY_TOO_LARGE', 'correct_request'), ('UNSUPPORTED_MEDIA', 'correct_request'),
                 ('HEADER_TOO_LARGE', 'correct_request'))
        for code, recovery in pairs:
            value = {'state': 'unavailable', 'code': code, 'recovery': recovery}
            self.assertTrue(self.response.is_valid(value))
            self.assertFalse(self.response.is_valid(dict(value, recovery='retry_forever')))
            self.assertFalse(self.response.is_valid(dict(value, detail='private')))

    def test_shape_explicitly_does_not_prove_mailbox_or_current_authority(self):
        changed = self.submission()
        changed['qualification']['email'] = 'not-an-email'
        self.assertTrue(self.request.is_valid(changed))
        changed['consent']['purpose_key'] = 'unapproved_purpose'
        self.assertTrue(self.request.is_valid(changed))
        self.assertTrue(self.response.is_valid(self.applied()))  # Historical revision, not current-state proof.


if __name__ == '__main__':
    unittest.main()

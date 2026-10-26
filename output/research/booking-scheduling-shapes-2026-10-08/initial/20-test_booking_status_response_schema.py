"""Booking status validator boundary only; never HTTP, provider or authorization proof."""
import copy
import json
from pathlib import Path
import unittest

from jsonschema import Draft202012Validator, FormatChecker
from referencing import Resource
from referencing.exceptions import Unresolvable

from scripts.validation import test_process_value_schema as common_fixture

CONTRACTS = Path(__file__).resolve().parents[2] / 'docs/phase-1-architecture/contracts'


class BookingStatusResponseShapeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        fixture = common_fixture.ProcessValueShapeTests
        fixture.setUpClass()
        path = CONTRACTS / 'booking-status-response.schema.json'
        schema = json.loads(path.read_text(encoding='utf-8'))
        Draft202012Validator.check_schema(schema)
        cls.registry = fixture.registry.with_resource(path.as_uri(), Resource.from_contents(schema))
        checker = FormatChecker(formats=['uuid', 'date-time'])
        if checker.conforms('not-a-uuid', 'uuid') or checker.conforms('2041-02-31T04:05:06.125Z', 'date-time'):
            raise RuntimeError('Required UUID/calendar assertion unavailable')
        cls.validator = Draft202012Validator({'$ref': path.as_uri()}, registry=cls.registry,
                                            format_checker=checker)

    def occurrence(self):
        return {'basis': 'last_reconciled', 'starts_at_utc': '2041-02-03T04:05:06.125Z',
                'ends_at_utc': '2041-02-03T04:35:06.125Z'}

    def snapshot(self, state='BOOKING_PENDING', occurrence=None):
        return {'lineage_id': '10286f82-cad4-4b14-a76a-e60d6c09ca09',
                'lineage': {'revision': 7, 'state': state},
                'booking': {'current_occurrence': occurrence}}

    def test_unconfirmed_and_cancelled_states_cannot_carry_an_occurrence(self):
        # Fixed BF-01 proposal oracles, not values read out of the schema.
        states = ('BOOKING_STARTED', 'VALIDATION_ERROR', 'QUALIFICATION_COMPLETE',
                  'EMAIL_PENDING', 'EMAIL_EXPIRED', 'EMAIL_UNDELIVERABLE', 'VERIFIED',
                  'NO_AVAILABILITY', 'SLOT_SELECTED', 'BOOKING_PENDING',
                  'RECONCILIATION_ERROR', 'CANCELLED')
        for state in states:
            with self.subTest(state=state):
                self.assertTrue(self.validator.is_valid(self.snapshot(state)))
                self.assertFalse(self.validator.is_valid(self.snapshot(state, self.occurrence())))

    def test_confirmed_and_pending_change_states_require_last_reconciled_occurrence(self):
        for state in ('CONFIRMED_QUALIFIED', 'RESCHEDULE_PENDING', 'CANCEL_PENDING'):
            with self.subTest(state=state):
                self.assertTrue(self.validator.is_valid(self.snapshot(state, self.occurrence())))
                self.assertFalse(self.validator.is_valid(self.snapshot(state)))
                changed = self.occurrence()
                changed['basis'] = 'currently_active'
                self.assertFalse(self.validator.is_valid(self.snapshot(state, changed)))

    def test_projection_requires_all_fields_and_exact_states(self):
        value = self.snapshot('CONFIRMED_QUALIFIED', self.occurrence())
        for keys in (('lineage_id',), ('lineage',), ('booking',), ('lineage', 'revision'),
                     ('lineage', 'state'), ('booking', 'current_occurrence'),
                     ('booking', 'current_occurrence', 'basis'),
                     ('booking', 'current_occurrence', 'starts_at_utc'),
                     ('booking', 'current_occurrence', 'ends_at_utc')):
            changed = copy.deepcopy(value)
            cursor = changed
            for key in keys[:-1]:
                cursor = cursor[key]
            del cursor[keys[-1]]
            self.assertFalse(self.validator.is_valid(changed), keys)
        for state in ('confirmed', 'pending', 'EXPIRED', 'DELETED', 'cancelled', None, ''):
            self.assertFalse(self.validator.is_valid(self.snapshot(state)))

    def test_private_details_and_cross_direction_fields_are_excluded(self):
        value = self.snapshot('CONFIRMED_QUALIFIED', self.occurrence())
        for keys in ((), ('lineage',), ('booking',), ('booking', 'current_occurrence')):
            for key in ('email', 'qualification', 'consent', 'cookie', 'csrf_token',
                        'proof_generation', 'provider_event_ref', 'provider_meeting_ref',
                        'meeting_url', 'staff_id', 'operation_id', 'diagnostic'):
                with self.subTest(path=keys, forbidden=key):
                    changed = copy.deepcopy(value)
                    cursor = changed
                    for part in keys:
                        cursor = cursor[part]
                    cursor[key] = 'forbidden'
                    self.assertFalse(self.validator.is_valid(changed))

    def test_calendar_assertion_and_exact_utc_millisecond_profile(self):
        for instant in ('2040-02-29T04:05:06.000Z', '2041-02-03T04:05:06.125Z'):
            occurrence = self.occurrence()
            occurrence['starts_at_utc'] = instant
            self.assertTrue(self.validator.is_valid(self.snapshot('CONFIRMED_QUALIFIED', occurrence)))
        invalid = ('2041-02-29T04:05:06.125Z', '2041-02-31T04:05:06.125Z',
                   '2041-02-03T24:05:06.125Z', '2041-02-03T04:05:60.125Z',
                   '2041-02-03T04:05:06Z', '2041-02-03T04:05:06.1Z',
                   '2041-02-03T04:05:06.1250Z', '2041-02-03T04:05:06.125+00:00',
                   '2041-02-03t04:05:06.125z', '2041-02-03T04:05:06.125Z\n', None, 123)
        for field in ('starts_at_utc', 'ends_at_utc'):
            for instant in invalid:
                occurrence = self.occurrence()
                occurrence[field] = instant
                self.assertFalse(self.validator.is_valid(self.snapshot('CONFIRMED_QUALIFIED', occurrence)))

    def test_references_and_revisions_do_not_coerce(self):
        for revision in (1, 9007199254740991):
            value = self.snapshot()
            value['lineage']['revision'] = revision
            self.assertTrue(self.validator.is_valid(value))
        for revision in (0, -1, 1.5, 9007199254740992, '7', True, None):
            value = self.snapshot()
            value['lineage']['revision'] = revision
            self.assertFalse(self.validator.is_valid(value))
        for selector in ('not-a-uuid', '10286F82-CAD4-4B14-A76A-E60D6C09CA09',
                         '10286f82-cad4-4b14-a76a-e60d6c09ca09\n', None, 1):
            value = self.snapshot()
            value['lineage_id'] = selector
            self.assertFalse(self.validator.is_valid(value))

    def test_three_error_pairs_are_minimal_and_cannot_echo_object_information(self):
        for code, recovery in (('INVALID_REQUEST', 'correct_request'),
                               ('ACCESS_UNAVAILABLE', 'contact'),
                               ('SERVICE_UNAVAILABLE', 'refresh_status')):
            value = {'state': 'unavailable', 'code': code, 'recovery': recovery}
            self.assertTrue(self.validator.is_valid(value))
            for field in value:
                changed = dict(value)
                del changed[field]
                self.assertFalse(self.validator.is_valid(changed))
            self.assertFalse(self.validator.is_valid({**value, 'recovery': 'resubmit'}))
            for field in ('lineage_id', 'revision', 'state_detail', 'cookie', 'exists', 'detail'):
                self.assertFalse(self.validator.is_valid({**value, field: 'forbidden'}))
            self.assertFalse(self.validator.is_valid({**self.snapshot(), **value}))

    def test_shape_does_not_prove_duration_ordering_or_booking_truth(self):
        # No cross-field comparison/current authority exists in JSON Schema here.
        # These pass shape and must be denied by the future semantic boundary.
        for end in ('2041-02-03T04:05:06.125Z', '2041-02-03T04:04:06.125Z',
                    '2041-02-03T04:36:06.125Z'):
            occurrence = self.occurrence()
            occurrence['ends_at_utc'] = end
            self.assertTrue(self.validator.is_valid(self.snapshot('CONFIRMED_QUALIFIED', occurrence)))
        value = self.snapshot()
        value['lineage_id'] = '00000000-0000-0000-0000-000000000000'
        value['lineage']['revision'] = 1.0
        self.assertTrue(self.validator.is_valid(value))  # Shape is not raw-token/issuer validation.

    def test_scalar_array_and_arbitrary_response_is_denied(self):
        for value in (None, True, 1, 'CONFIRMED_QUALIFIED', [], [self.snapshot()], {},
                      {'state': 'unavailable'}, {'status': 'ok'}):
            self.assertFalse(self.validator.is_valid(value))

    def test_unregistered_remote_schema_is_not_retrieved(self):
        validator = Draft202012Validator({'$ref': 'https://invalid.example/private-schema'},
                                        registry=self.registry)
        with self.assertRaises(Unresolvable):
            validator.validate({})


if __name__ == '__main__':
    unittest.main()

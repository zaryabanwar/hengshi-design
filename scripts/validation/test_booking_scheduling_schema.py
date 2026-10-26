"""Scheduling representation boundary only; no handler, calendar or authority proof."""
import copy
import json
from pathlib import Path
import unittest

from jsonschema import Draft202012Validator, FormatChecker
from referencing import Resource

from scripts.validation import test_process_value_schema as common_fixture
from scripts.validation import test_booking_qualification_schema as qualification_fixture

CONTRACTS = Path(__file__).resolve().parents[2] / 'docs/phase-1-architecture/contracts'
OP = '10286f82-cad4-4b14-a76a-e60d6c09ca09'
REF = '919108f7-52d1-4320-9bac-f847db4148a8'
START = '2041-02-03T04:05:06.125Z'
END = '2041-02-03T04:35:06.125Z'


class BookingSchedulingShapeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        fixture = common_fixture.ProcessValueShapeTests
        fixture.setUpClass()
        registry = fixture.registry
        for name in ('booking-creation-request.schema.json', 'chat-creation-request.schema.json',
                     'booking-qualification.schema.json', 'booking-status-response.schema.json',
                     'booking-scheduling.schema.json'):
            path = CONTRACTS / name
            schema = json.loads(path.read_text(encoding='utf-8'))
            Draft202012Validator.check_schema(schema)
            registry = registry.with_resource(path.as_uri(), Resource.from_contents(schema))
        cls.registry = registry
        cls.checker = FormatChecker(formats=['uuid', 'date-time', 'date'])
        for value, fmt in (('not-a-uuid', 'uuid'), ('2041-02-31', 'date'),
                           ('2041-02-31T04:05:06.125Z', 'date-time')):
            if cls.checker.conforms(value, fmt):
                raise RuntimeError('Required UUID/calendar assertion unavailable')
        cls.uri = (CONTRACTS / 'booking-scheduling.schema.json').as_uri()

    def validator(self, name=None):
        ref = self.uri if name is None else self.uri + '#/$defs/' + name
        return Draft202012Validator({'$ref': ref}, registry=self.registry,
                                    format_checker=self.checker)

    def command(self, kind):
        value = {'kind': kind, 'operation_id': OP}
        if kind.startswith('reconcile_'):
            return value
        value['expected_revision'] = 7
        if kind.startswith('prepare_'):
            value['visitor_timezone'] = 'UTC'
            if kind != 'prepare_cancellation':
                value['slot_ref'] = REF
        else:
            value['review_ref'] = REF
        return value

    def query(self):
        return {'kind': 'window', 'purpose': 'initial', 'expected_revision': 7,
                'visitor_timezone': 'Europe/Berlin', 'from_utc': START, 'until_utc': END}

    def slots(self):
        return {'state': 'slots', 'lineage_id': OP, 'lineage_revision': 7,
                'purpose': 'initial', 'visitor_timezone': 'UTC',
                'window': {'from_utc': START, 'until_utc': END}, 'observed_at': START,
                'view_ref': REF, 'slots': [{'slot_ref': REF, 'starts_at_utc': START,
                                           'ends_at_utc': END}], 'continuation_ref': None}

    def occurrence(self):
        return {'starts_at_utc': START, 'ends_at_utc': END,
                'local_start': {'date': '2041-02-03', 'time': '04:05:06.125', 'utc_offset_seconds': 0},
                'local_end': {'date': '2041-02-03', 'time': '04:35:06.125', 'utc_offset_seconds': 0}}

    def prepared(self, purpose):
        review = {'purpose': purpose, 'review_ref': REF, 'visitor_timezone': 'UTC'}
        if purpose == 'cancel':
            review.update(wing_key='ROUTE-WING-AI-DATA', current_occurrence=self.occurrence())
        else:
            qualification = qualification_fixture.BookingQualificationShapeTests().submission()
            review.update(qualification=qualification['qualification'], consent=qualification['consent'],
                          proposed_occurrence=self.occurrence())
            if purpose == 'reschedule':
                review['current_occurrence'] = self.occurrence()
        return {'state': 'applied', 'receipt_kind': 'prepared', 'operation_id': OP,
                'applied_revision': 8, 'current': {'state': 'known', 'revision': 8, 'review': review}}

    def test_each_endpoint_has_separate_request_and_response_directions(self):
        for endpoint, purpose, kinds in (
            ('submission', 'book', ('prepare_selection', 'submit_booking', 'reconcile_submission')),
            ('reschedule', 'reschedule', ('prepare_reschedule', 'submit_reschedule', 'reconcile_reschedule')),
            ('cancellation', 'cancel', ('prepare_cancellation', 'cancel_booking', 'reconcile_cancellation')),
        ):
            for kind in kinds:
                value = self.command(kind)
                self.assertTrue(self.validator(endpoint + '_request').is_valid(value), kind)
                self.assertFalse(self.validator(endpoint + '_response').is_valid(value), kind)
                self.assertFalse(self.validator().is_valid(value))
                for other in ('submission', 'reschedule', 'cancellation'):
                    if other != endpoint:
                        self.assertFalse(self.validator(other + '_request').is_valid(value))
            value = self.prepared(purpose)
            self.assertTrue(self.validator(endpoint + '_response').is_valid(value))
            self.assertFalse(self.validator(endpoint + '_request').is_valid(value))
            self.assertFalse(self.validator().is_valid(value))
        self.assertTrue(self.validator('availability_query').is_valid(self.query()))
        self.assertFalse(self.validator('availability_response').is_valid(self.query()))
        self.assertTrue(self.validator('availability_response').is_valid(self.slots()))
        self.assertFalse(self.validator('availability_query').is_valid(self.slots()))

    def test_prepare_and_submit_require_their_own_fields(self):
        for kind in ('prepare_selection', 'submit_booking', 'prepare_reschedule',
                     'submit_reschedule', 'prepare_cancellation', 'cancel_booking'):
            value = self.command(kind)
            for key in value:
                changed = dict(value)
                del changed[key]
                self.assertFalse(self.validator(kind).is_valid(changed), (kind, key))
            for key in ('qualification', 'consent', 'email', 'owner_id', 'provider_event_ref',
                        'csrf_token', 'proof', 'state', 'starts_at_utc', 'reason'):
                changed = dict(value, **{key: 'untrusted'})
                self.assertFalse(self.validator(kind).is_valid(changed), (kind, key))

    def test_reconciliation_contains_only_operation_identity(self):
        for kind in ('reconcile_submission', 'reconcile_reschedule', 'reconcile_cancellation'):
            value = self.command(kind)
            self.assertTrue(self.validator(kind).is_valid(value))
            for key in ('expected_revision', 'slot_ref', 'review_ref', 'email', 'visitor_timezone', 'qualification'):
                self.assertFalse(self.validator(kind).is_valid(dict(value, **{key: REF})))

    def test_uuid_and_revision_boundaries_do_not_coerce(self):
        value = self.command('submit_booking')
        for key in ('operation_id', 'review_ref'):
            for invalid in (OP.upper(), ' ' + OP, OP + '\n', '00000000-0000-0000-0000-000000000000',
                            '019f1d32-0000-7000-8000-000000000001', None, 1):
                changed = dict(value, **{key: invalid})
                self.assertFalse(self.validator('submission_request').is_valid(changed), (key, invalid))
        for revision in (1, 9007199254740991):
            self.assertTrue(self.validator('submission_request').is_valid(dict(value, expected_revision=revision)))
        for revision in (0, -1, 9007199254740992, 1.5, True, '7', None):
            self.assertFalse(self.validator('submission_request').is_valid(dict(value, expected_revision=revision)))

    def test_page_query_cannot_override_view_filters(self):
        value = {'kind': 'page', 'expected_revision': 7, 'page_ref': REF}
        self.assertTrue(self.validator('availability_query').is_valid(value))
        for key in ('purpose', 'visitor_timezone', 'from_utc', 'until_utc', 'owner_id', 'limit', 'offset'):
            self.assertFalse(self.validator('availability_query').is_valid(dict(value, **{key: 'untrusted'})))
        for key in self.query():
            changed = self.query()
            del changed[key]
            self.assertFalse(self.validator('availability_query').is_valid(changed))

    def test_timezone_is_bounded_spelling_not_database_membership(self):
        for zone in ('UTC', 'Europe/Berlin', 'America/Argentina/Buenos_Aires', 'Etc/GMT+4', 'US/Eastern', 'A' * 128):
            self.assertTrue(self.validator('timezone').is_valid(zone), zone)
        for zone in ('', 'A' * 129, '../Europe/Berlin', 'Europe/../Berlin', '/Europe/Berlin',
                     'Europe//Berlin', 'Europe/Berlin/', 'Europe/Berlin\n', ' Europe/Berlin', None, 7):
            self.assertFalse(self.validator('timezone').is_valid(zone), zone)
        self.assertTrue(self.validator('timezone').is_valid('Invented/Zone'))

    def test_complete_empty_and_nonempty_pages_are_distinct(self):
        value = self.slots()
        self.assertTrue(self.validator('availability_response').is_valid(value))
        value['continuation_ref'] = OP
        self.assertTrue(self.validator('availability_response').is_valid(value))
        empty = dict(value, state='empty', slots=[], continuation_ref=None)
        self.assertTrue(self.validator('availability_response').is_valid(empty))
        self.assertFalse(self.validator('availability_response').is_valid(dict(empty, continuation_ref=OP)))
        self.assertFalse(self.validator('availability_response').is_valid(dict(empty, slots=value['slots'])))
        self.assertFalse(self.validator('availability_response').is_valid(dict(value, slots=[])))
        for key in ('complete', 'provider_calendar', 'attendees', 'diagnostic', 'meeting_url'):
            self.assertFalse(self.validator('availability_response').is_valid(dict(value, **{key: 'untrusted'})))

    def test_slot_page_bound_and_duplicate_items(self):
        value = self.slots()
        value['slots'] = [{'slot_ref': f'{n:08x}-52d1-4320-9bac-f847db4148a8',
                           'starts_at_utc': START, 'ends_at_utc': END} for n in range(1, 97)]
        self.assertTrue(self.validator('availability_response').is_valid(value))
        value['slots'].append({'slot_ref': OP, 'starts_at_utc': START, 'ends_at_utc': END})
        self.assertFalse(self.validator('availability_response').is_valid(value))
        value = self.slots()
        value['slots'].append(copy.deepcopy(value['slots'][0]))
        self.assertFalse(self.validator('availability_response').is_valid(value))
        # Different references to the same interval remain a semantic deduplication duty.
        value['slots'][1]['slot_ref'] = OP
        self.assertTrue(self.validator('availability_response').is_valid(value))

    def test_calendar_format_and_exact_utc_milliseconds(self):
        for invalid in ('2041-02-31T04:05:06.125Z', '2041-02-29T04:05:06.125Z',
                        '2041-02-03T04:05:60.125Z', '2041-02-03T04:05:06Z',
                        '2041-02-03T04:05:06.125+00:00', START + '\n', None):
            for key in ('from_utc', 'until_utc'):
                self.assertFalse(self.validator('availability_query').is_valid(dict(self.query(), **{key: invalid})))
        self.assertTrue(self.validator('utc_instant').is_valid('2040-02-29T04:05:06.000Z'))

    def test_local_labels_require_real_dates_and_closed_clocks(self):
        value = self.occurrence()['local_start']
        for date in ('2041-02-31', '2041-02-29', '2041-2-03', '2041-02-03\n'):
            self.assertFalse(self.validator('local_clock').is_valid(dict(value, date=date)))
        for time in ('24:00:00.000', '04:60:00.000', '04:05:60.000', '04:05:06', '04:05:06.125\n'):
            self.assertFalse(self.validator('local_clock').is_valid(dict(value, time=time)))
        for offset in (-86400, 86400, 0):
            self.assertTrue(self.validator('local_clock').is_valid(dict(value, utc_offset_seconds=offset)))
        for offset in (-86401, 86401, True, '0', 0.5):
            self.assertFalse(self.validator('local_clock').is_valid(dict(value, utc_offset_seconds=offset)))

    def test_prepared_reviews_are_endpoint_specific(self):
        for endpoint, purpose in (('submission', 'book'), ('reschedule', 'reschedule'), ('cancellation', 'cancel')):
            value = self.prepared(purpose)
            self.assertTrue(self.validator(endpoint + '_response').is_valid(value))
            for other in ('submission', 'reschedule', 'cancellation'):
                if other != endpoint:
                    self.assertFalse(self.validator(other + '_response').is_valid(value))
            for key in ('current', 'applied_revision', 'operation_id', 'receipt_kind'):
                changed = copy.deepcopy(value)
                del changed[key]
                self.assertFalse(self.validator(endpoint + '_response').is_valid(changed))
            value['current'] = {'state': 'unavailable'}
            self.assertTrue(self.validator(endpoint + '_response').is_valid(value))
            value['current']['review'] = self.prepared(purpose)['current']['review']
            self.assertFalse(self.validator(endpoint + '_response').is_valid(value))

    def test_cancellation_review_does_not_copy_brief_or_consent(self):
        value = self.prepared('cancel')
        for key in ('qualification', 'consent', 'email', 'reason', 'proposed_occurrence', 'provider_event_ref'):
            changed = copy.deepcopy(value)
            changed['current']['review'][key] = 'forbidden'
            self.assertFalse(self.validator('cancellation_response').is_valid(changed), key)
        value['current']['review']['wing_key'] = 'invented'
        self.assertFalse(self.validator('cancellation_response').is_valid(value))

    def test_booking_review_reuses_six_fields_and_separate_consent(self):
        for purpose, endpoint in (('book', 'submission'), ('reschedule', 'reschedule')):
            value = self.prepared(purpose)
            for key in ('qualification', 'consent', 'proposed_occurrence'):
                changed = copy.deepcopy(value)
                del changed['current']['review'][key]
                self.assertFalse(self.validator(endpoint + '_response').is_valid(changed))
            value['current']['review']['qualification']['budget'] = 'untrusted'
            self.assertFalse(self.validator(endpoint + '_response').is_valid(value))

    def test_accepted_and_pending_are_not_calendar_outcomes_or_review_grants(self):
        for endpoint in ('submission', 'reschedule', 'cancellation'):
            for value in ({'state': 'applied', 'receipt_kind': 'accepted', 'operation_id': OP, 'applied_revision': 8},
                          {'state': 'pending', 'operation_id': OP}):
                self.assertTrue(self.validator(endpoint + '_response').is_valid(value))
                for key in ('current', 'review_ref', 'provider_event_ref', 'meeting_url', 'confirmed', 'cancelled'):
                    self.assertFalse(self.validator(endpoint + '_response').is_valid(dict(value, **{key: REF})))

    def test_error_pairs_are_fixed_closed_and_directional(self):
        for endpoint, code, recovery in (('availability', 'VIEW_CHANGED', 'refresh_availability'),
                                        ('submission', 'REVIEW_CHANGED', 'prepare_review'),
                                        ('reschedule', 'OPERATION_CONFLICT', 'reconcile'),
                                        ('cancellation', 'STATE_CONFLICT', 'refresh_status')):
            value = {'state': 'unavailable', 'code': code, 'recovery': recovery}
            validator = self.validator(endpoint + '_response')
            self.assertTrue(validator.is_valid(value))
            self.assertFalse(validator.is_valid(dict(value, recovery='retry_write')))
            self.assertFalse(validator.is_valid(dict(value, diagnostic='private')))
        self.assertFalse(self.validator('availability_response').is_valid(
            {'state': 'unavailable', 'code': 'REVIEW_CHANGED', 'recovery': 'prepare_review'}))

    def test_shapes_do_not_prove_cross_field_business_bindings(self):
        value = self.prepared('book')
        value['current']['revision'] = 9
        occurrence = value['current']['review']['proposed_occurrence']
        occurrence['ends_at_utc'] = START  # Zero duration remains structurally valid.
        occurrence['local_start']['utc_offset_seconds'] = 3600  # UTC label mismatch.
        self.assertTrue(self.validator('submission_response').is_valid(value))
        query = self.query()
        query['until_utc'] = '2041-02-02T04:05:06.125Z'
        self.assertTrue(self.validator('availability_query').is_valid(query))


if __name__ == '__main__':
    unittest.main()

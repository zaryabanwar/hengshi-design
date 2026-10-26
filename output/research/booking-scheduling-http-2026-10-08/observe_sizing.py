"""Synthetic representation sizing; no HTTP, business or load qualification."""
import copy
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from scripts.validation.test_booking_scheduling_schema import BookingSchedulingShapeTests, OP, START, END


def observe():
    BookingSchedulingShapeTests.setUpClass()
    fixture = BookingSchedulingShapeTests()
    cases = []
    value = fixture.slots()
    value['visitor_timezone'] = 'A' * 128
    value['lineage_revision'] = 9007199254740991
    value['slots'] = [{'slot_ref': f'{n:08x}-52d1-4320-9bac-f847db4148a8',
                       'starts_at_utc': START, 'ends_at_utc': END} for n in range(1, 97)]
    cases.append(('96_slots_spelling_only', 'availability_response', value))
    for purpose, endpoint in (('book', 'submission'), ('reschedule', 'reschedule'), ('cancel', 'cancellation')):
        value = fixture.prepared(purpose)
        value['applied_revision'] = 9007199254740991
        value['current']['revision'] = 9007199254740991
        review = value['current']['review']
        review['visitor_timezone'] = 'A' * 128
        if purpose != 'cancel':
            q = review['qualification']
            for field, length in (('email', 320), ('organization', 200), ('role', 200), ('desired_outcome', 2000)):
                # Six-byte escaped controls maximize compact JSON expansion here;
                # this is intentionally not a semantically valid mailbox/content example.
                q[field] = 'x' + '\x00' * (length - 1)
            q['timing']['description'] = 'x' + '\x00' * 499
            consent = review['consent']
            consent['purpose_key'] = 'A' * 96
            consent['notice_reference']['notice_id'] = 'A' * 96
            consent['notice_reference']['notice_revision'] = 'A' * 96
        cases.append((purpose + '_review_escaped_controls', endpoint + '_response', value))
    results = []
    for name, direction, value in cases:
        valid = fixture.validator(direction).is_valid(value)
        assert valid, name
        count = len(json.dumps(value, ensure_ascii=False, separators=(',', ':')).encode('utf-8'))
        assert count <= 32768, (name, count)
        results.append({'case': name, 'direction': direction, 'shape_valid': valid,
                        'compact_utf8_bytes': count, 'proposal_response_ceiling': 32768})
    # Mutation maximum spelling uses bounded ASCII keys/references/zone/revision.
    for kind in ('prepare_selection', 'prepare_reschedule', 'prepare_cancellation',
                 'submit_booking', 'submit_reschedule', 'cancel_booking',
                 'reconcile_submission', 'reconcile_reschedule', 'reconcile_cancellation'):
        value = fixture.command(kind)
        if 'visitor_timezone' in value:
            value['visitor_timezone'] = 'A' * 128
        if 'expected_revision' in value:
            value['expected_revision'] = 9007199254740991
        assert fixture.validator(kind).is_valid(value)
        count = len(json.dumps(value, ensure_ascii=False, separators=(',', ':')).encode('utf-8'))
        ceiling = 1024 if kind.startswith('reconcile_') else 2048
        assert count <= ceiling
        results.append({'case': kind, 'shape_valid': True, 'compact_utf8_bytes': count,
                        'proposal_request_ceiling': ceiling})
    return {'scope': 'Representative synthetic sizing only, not exhaustive maximum proof, compliant transport or measured capacity',
            'python': sys.version.split()[0], 'observations': results}


if __name__ == '__main__':
    result = observe()
    (Path(__file__).parent / 'synthetic-sizing.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2))

"""Replace stale missing-definition navigation with current scoped successors."""
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
catalogue = ROOT / 'docs/phase-1-architecture/contracts/INTERFACE_CATALOG.md'
data = ROOT / 'docs/phase-1-architecture/contracts/DATA_CONTRACT.md'
if (HERE / 'INTERFACE_CATALOG.before.md').exists():
    raise SystemExit('Refuse repeat scheduling reference alignment')
paths = [
    ROOT / 'output/research/booking-scheduling-lifecycle-2026-10-08/final-independent-review.json',
    ROOT / 'output/research/booking-scheduling-shapes-2026-10-08/final-independent-review.json',
    ROOT / 'output/research/booking-scheduling-http-review-2026-10-08/correction-1/independent-review-correction-1-v1.json']
for path in paths:
    receipt = json.loads(path.read_bytes())
    assert any(receipt.get(key) == 'PASS' for key in ('result', 'review_verdict', 'bounded_verdict'))
for path in (catalogue, data):
    (HERE / (path.stem + '.before.md')).write_bytes(path.read_bytes())
raw = catalogue.read_bytes()
old = b'acceptance. IF-BOOK-05/06 availability, slot review and calendar submission, and\r\nIF-BOOK-08/09 rescheduling/cancellation still need their exact definitions. Actual\r\nrequest/store/job/browser enforcement belongs to later approved implementation.'
assert raw.count(old) == 1
new = '''acceptance. The later [scheduling lifecycle](BOOKING_SCHEDULING.md),
[directional representations](BOOKING_SCHEDULING.md#directional-representation-proposal--2026-10-08)
and [HTTP/resource proposal](BOOKING_SCHEDULING.md#scheduling-http-and-finite-resource-proposal--2026-10-08)
now define IF-BOOK-05/06/08/09 availability, review/submission, rescheduling and
cancellation. Their separate frozen logical, shape and HTTP correction receipts
are linked in that controlling document; no earlier catalogue PASS expands to
this later reference or accepts the whole scheduling package. Operating-policy/
resource bindings, actual provider capability, wire freeze and integrated
acceptance remain. Request/store/job/browser enforcement and capacity measurement
belong to later approved implementation, before production promotion.'''.replace('\n', '\r\n').encode()
catalogue.write_bytes(raw.replace(old, new))
raw = data.read_bytes()
anchor = b'## Booking and provider transactions\r\n'
assert raw.count(anchor) == 1
addition = '''
The [scheduling lifecycle](BOOKING_SCHEDULING.md) and its later directional/HTTP
profiles refine these existing logical records for IF-BOOK-05/06/08/09. Use that
controlling source for purpose-bound offers/reviews, guarded admissions, same-
operation reconciliation, provider uncertainty and reschedule/cancel lineage.
Its logical, representation and HTTP correction receipts each retain their exact
frozen scope; this later navigation reference changes no record or transaction
invariant and inherits no PASS. Exact operating policy and resource bindings,
account capability, physical schema, actual PostgreSQL/provider enforcement and
integrated/founder acceptance remain separate.
'''.replace('\n', '\r\n').encode()
data.write_bytes(raw.replace(anchor, anchor + addition))
print('Two controlling navigation references reconciled; no schemas, behavior, tests or app changes.')

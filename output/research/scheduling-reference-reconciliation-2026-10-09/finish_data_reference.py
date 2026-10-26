"""Finish only the unmodified data-reference insertion after a newline guard stop."""
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
data = ROOT / 'docs/phase-1-architecture/contracts/DATA_CONTRACT.md'
raw = data.read_bytes()
assert raw == (HERE / 'DATA_CONTRACT.before.md').read_bytes()
heading = b'## Booking and provider transactions'
assert raw.count(heading) == 1
start = raw.index(heading)
position = raw.index(b'\n', start) + 1
ending = '\r\n' if raw[position-2:position] == b'\r\n' else '\n'
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
'''.replace('\n', ending).encode()
data.write_bytes(raw[:position] + addition + raw[position:])
print('Remaining data reference inserted with existing section newline style; catalogue not rewritten.')

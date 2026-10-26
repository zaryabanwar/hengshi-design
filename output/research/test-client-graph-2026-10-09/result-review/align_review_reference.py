"""Link the inspected result review and separate producer advisory observation."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
receipt = HERE / 'independent-review-native-notices-v1.json'
assert hashlib.sha256(receipt.read_bytes()).hexdigest() == '00f6b34840473e24150d1d8f8560bb1c609ef47dafeb8fcddedf58791fdc5f1d'
assert json.loads(receipt.read_bytes())['review_decision'] == 'PASS'
backend = ROOT / 'docs/phase-1-compatibility/backend-evidence-2026-10-04.md'
readme = ROOT / 'docs/phase-1-compatibility/README.md'
if (HERE / 'backend.before-review-reference.md').exists():
    raise SystemExit('Refuse repeat review reference alignment')
for path in (backend, readme):
    (HERE / (path.stem + '.before-review-reference.md')).write_bytes(path.read_bytes())
addition = '''
The [299-input independent result/notice review](../../output/research/test-client-graph-2026-10-09/result-review/independent-review-native-notices-v1.json)
passes the exact new execution helpers, retained wheels/installed metadata,
18 cases, warning admission, disk arithmetic, discovered notice bytes and bounded
appendix claims with no findings. The [frozen reviewed document](../../output/research/test-client-graph-2026-10-09/result-review/backend.proposed.md)
remains preserved. This later receipt link does not rewrite its inputs or expand
the PASS to actual Hengshi behavior, complete licences/provenance, advisories,
production graph selection or integrated acceptance.

### Separate dated advisory observation

The [producer-only OSV capture](../../output/research/test-client-advisories-2026-10-09/receipt.json)
queried all 48 frozen PyPI package names and exact versions in one successful
batch. All 48 positional results were returned, with no advisory IDs and no
next-page tokens. [Saved request/response mapping](../../output/research/test-client-advisories-2026-10-09/package-results.json)
and [HTTP capture](../../output/research/test-client-advisories-2026-10-09/query-captures.json)
record the dated response. The capture is outside the 299-input review. It follows
the [official querybatch contract](https://google.github.io/osv.dev/post-v1-querybatch/)
and preserves retrieved guidance, full response bytes and protected-input checks.
No-match means only that this database returned no matching published records
at capture time. It does not identify every embedded/native/OS library, establish
application exploitability or provide security/advisory clearance. Fresh checks
against the eventual delivered graph, complete native components and required
triage remain necessary before separately approved adoption.
'''
backend.write_bytes(backend.read_bytes() + addition.encode())
addition = '''

The [299-input independent preferred-client result/notice review](../../output/research/test-client-graph-2026-10-09/result-review/independent-review-native-notices-v1.json)
has bounded PASS with no findings. Its frozen snapshots retain exact scope;
this later reference and the [separate dated OSV observation](backend-evidence-2026-10-04.md#separate-dated-advisory-observation)
are outside those inputs. The producer OSV query returned no exact-PyPI matches,
which establishes no security clearance or embedded/native coverage. Actual
Hengshi behavior, full supply-chain/graph selection and adoption remain held.
'''
raw = readme.read_bytes()
anchor = b'## Current authority and dated evidence'
position = raw.index(anchor) + len(anchor)
readme.write_bytes(raw[:position] + addition.encode() + raw[position:])
print('Inspected PASS and separately scoped OSV observation linked in two compatibility documents.')

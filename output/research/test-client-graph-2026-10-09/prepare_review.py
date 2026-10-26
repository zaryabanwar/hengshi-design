"""Freeze one scoped graph/qualification proposal, changing two owning docs only."""
import ast
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
if (HERE / 'review-inputs.json').exists():
    raise SystemExit('Refuse repeat preparation')
observations = json.loads((HERE / 'closure-observations.json').read_bytes())
assert observations['package_count'] == 48 and observations['edge_count'] == 57
assert observations['previous_45_package_records_unchanged'] and observations['protected_inputs_unchanged']
plan = json.loads((HERE / 'qualification-plan.json').read_bytes())
assert not plan['execution_authorized'] and plan['expected_case_count'] == 18
for entry in plan['probe_files']:
    raw = (ROOT / entry['path']).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == entry['sha256']
    ast.parse(raw)
backend = ROOT / 'docs/phase-1-compatibility/backend-evidence-2026-10-04.md'
before = backend.read_bytes()
(HERE / 'backend.before.md').write_bytes(before)
appendix = '''
## Preferred HTTPX2 client graph and prospective qualification — 2026-10-09

Status: DOING. Evaluate the supported preferred HTTPX2 path before accepting the
deprecated fallback observed in the isolated 43-package trial. The [metadata-only
resolver](../../output/research/test-client-graph-2026-10-09/receipt.json) adds
HTTPX2 2.13.1, HTTPcore2 2.13.1 and Truststore 0.10.4 to the earlier 45-package
identity candidate. All previous package metadata and wheel identities remain
unchanged. The [48-package/57-active-edge closure](../../output/research/test-client-graph-2026-10-09/closure-observations.json)
checks target Python, wheel tags, markers/extras, exact constraints and non-yanked
stable-looking versions. The three added exact/latest registry observations agree;
their classifications are Production/Stable. HTTPX2's exact release is non-draft/
non-prerelease. These are metadata/source observations, not whole-graph selection,
publisher verification, native execution or installed-footprint proof.

Starlette's preserved TestClient source prefers HTTPX2. The [exact Authlib wheel
source](../../output/research/test-client-graph-2026-10-09/authlib-import-source.json)
also prefers HTTPX2 through its compatibility shim and deprecates HTTPX fallback.
Its AsyncOAuth2Client uses the selected shim's AsyncClient; it must not be assumed
to retain HTTPX classes when HTTPX2 is present. No Authlib client was imported or
instantiated during this inspection. The [tagged migration guidance](https://github.com/pydantic/httpx2/blob/d91c9f4236523eb5978ca800944fa0078f17409f/docs/migration.md)
allows coexistence but keeps client/request/response/exception families distinct.
Recommend qualifying each actual consumer's type ownership; do not replace
imports process-wide or mix exception families. The [tagged TLS guidance](https://github.com/pydantic/httpx2/blob/d91c9f4236523eb5978ca800944fa0078f17409f/docs/advanced/ssl.md)
uses system trust stores by default and still respects explicit SSL contexts and
certificate environment settings. This changes no selected production TLS policy;
never disable verification to make a probe pass. No global alias/injection ran.

The [prospective isolated plan](../../output/research/test-client-graph-2026-10-09/qualification-plan.json)
retains the reviewed 256 MiB admission/1 GiB free-floor/180-second command pattern
with measured expanded-wheel reservation, no existing-environment changes and no
automatic cleanup. It proposes the original 14 offline library cases plus four
new namespace/client-lifecycle cases, with both fallback warnings treated as
errors. None of these 18 cases has run against the enlarged candidate. Authlib/
joserfc coverage is limited to import/type/client lifecycle, not OIDC verification,
callbacks, PKCE/nonce, grants, TLS, database or actual Hengshi behavior. The old
43-package environment and its PASS remain separate protected evidence. Independent
proposal review and fresh explicit execution approval are required; the earlier
43-package permission does not expand. Complete candidate rights/provenance/
advisories, stable graph/locks, runtime platform qualification and integrated/
founder adoption remain held. The evaluation pins are not a production lock.
'''
(HERE / 'backend-appendix.md').write_bytes(appendix.encode())
backend.write_bytes(before + appendix.encode())
(HERE / 'backend.proposed.md').write_bytes(backend.read_bytes())
readme = ROOT / 'docs/phase-1-compatibility/README.md'
before = readme.read_bytes()
(HERE / 'README.before.md').write_bytes(before)
anchor = b'## Current authority and dated evidence'
position = before.index(anchor) + len(anchor)
addition = '''

The [preferred HTTPX2 graph and prospective qualification](backend-evidence-2026-10-04.md#preferred-httpx2-client-graph-and-prospective-qualification--2026-10-09)
addresses deprecated TestClient/Authlib fallback without suppressing it. The
metadata-only 48-package candidate adds three stable-classified records while
preserving all prior 45 identities. Consumer type/TLS boundaries and a separate
bounded native plan remain proposals. No enlarged installation, package selection,
whole-graph acceptance or production-client migration is authorized; independent
proposal review and fresh execution permission remain separate.
'''
readme.write_bytes(before[:position] + addition.encode() + before[position:])
(HERE / 'README.proposed.md').write_bytes(readme.read_bytes())
paths = [x for x in HERE.iterdir() if x.is_file()]
paths += [backend, readme,
          ROOT / 'output/research/staff-identity-graph-2026-10-08/pip-report.json',
          ROOT / 'output/research/staff-identity-graph-2026-10-08/closure-observations.json',
          ROOT / 'output/research/staff-identity-graph-2026-10-08/candidate-roots.txt',
          ROOT / 'output/research/staff-identity-distribution-2026-10-09/authlib/wheel.gz',
          ROOT / 'output/research/backend-crypto-graph-2026-10-08/qualification-plan.json',
          ROOT / 'output/research/backend-crypto-graph-2026-10-08/proposal.json',
          ROOT / 'output/research/backend-crypto-graph-2026-10-08/native-probes/test_libraries.py',
          ROOT / 'output/research/backend-crypto-graph-2026-10-08/native-result-review/installed-starlette-testclient.py',
          ROOT / 'output/research/backend-crypto-graph-2026-10-08/native-result-review/independent-review-native-result-v1.json']
manifest = {'product_release': 'v1', 'status': 'DOING', 'review_authorized': False,
            'scope': 'Read-only 48-package metadata/source observation, prospective 18-case isolated qualification plan and exact two-document amendments; no script/probe execution, installs, network, app, provider, Figma, model or Git actions required.',
            'inputs': [{'path': p.relative_to(ROOT).as_posix(), 'bytes': p.stat().st_size,
                        'sha256': hashlib.sha256(p.read_bytes()).hexdigest()} for p in paths]}
(HERE / 'review-inputs.json').write_text(json.dumps(manifest, indent=2) + '\n')
print(json.dumps({'input_count': len(paths), 'changed_canonical_documents': 2,
                  'prospective_cases': 18, 'native_execution_authorized': False}))

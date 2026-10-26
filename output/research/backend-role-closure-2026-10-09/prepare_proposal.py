"""Append one role proposal in two owners; freeze inputs for separate review."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
if (HERE / 'review-inputs.json').exists():
    raise SystemExit('Refuse repeat proposal preparation')
profiles = json.loads((HERE / 'profiles.json').read_bytes())
assert profiles['protected_inputs_unchanged']
assert [p['package_count'] for p in profiles['profiles'].values()] == [30, 35, 5, 48]
backend = ROOT / 'docs/phase-1-compatibility/backend-evidence-2026-10-04.md'
readme = ROOT / 'docs/phase-1-compatibility/README.md'
before = backend.read_bytes()
(HERE / 'backend.before.md').write_bytes(before)
appendix = '''
## Proposed backend dependency roles — 2026-10-09

Status: DOING. The 48-package trial is a combined qualification environment,
not an instruction to ship every tested package inside the serving application.
The [producer role derivation](../../output/research/backend-role-closure-2026-10-09/profiles.json)
uses only the frozen exact wheel metadata, target environment and selected extras.
It makes no new resolution, installation, package selection or source change.
The [package/root ancestry table](../../output/research/backend-role-closure-2026-10-09/package-roles.csv)
preserves all 48 identities and the roots that make each reachable.

| Proposed profile | Direct evaluated roots | Metadata-reachable packages |
|---|---|---|
| API base candidate | FastAPI, Uvicorn[standard], SQLAlchemy, Psycopg[binary], bcrypt, PyJWT[crypto], email-validator, python-dotenv | 30 |
| API with conditional identity candidate | API base plus Authlib and HTTPX2 | 35 |
| Migration tool candidate | Alembic and its required dependencies | 5 |
| Combined qualification basis | All above plus pytest, pytest-asyncio and HTTPX | 48 |

These closures overlap; counts must not be added as independent copies. Authlib/
HTTPX2 remains the leading evaluated identity option, not an accepted OIDC adapter.
The profile is conditional on its eventual separate qualification/selection.
HTTPX and HTTPX2 remain separate libraries. HTTPX, HTTPcore, certifi, colorama,
iniconfig, packaging, pluggy, Pygments, pytest and pytest-asyncio are outside both
the proposed identity-capable application closure and migration closure in this
specific saved Windows metadata graph. That classification is not proof that
they can never be needed by a future consumer or are absent from shipped artifacts.

Recommended eventual packaging keeps serving, migration and test-tool purposes
explicit. Shared required libraries remain in every profile that actually needs
them; do not prune by package name or dev labels. Validate each separately selected
profile under its actual extras/platform, resolve and reproducibly lock it, then
inspect built/delivered contents and public-boundary behavior before adoption.
Migration tooling needs separately authorized database access and reviewed
execution/rollback; its small metadata closure supplies neither. Test dependencies
must not silently become serving requirements merely because a combined fixture
installed them. Existing protected requirements stay unchanged for later waves.

The [PyPA dependency specification](https://packaging.python.org/en/latest/specifications/dependency-specifiers/)
defines marker conditions and optional-extra dependency union. Its [dependency
group specification](https://packaging.python.org/en/latest/specifications/dependency-groups/)
distinguishes local test/tool requirements from distribution metadata. The
[captured primary guidance](../../output/research/backend-role-closure-2026-10-09/primary-guidance.json)
and Context7 response are retained. This proposal does not select a dependency-group
format, package manager or new build tool. The producer uses installed packaging
26.2 as an analysis tool, not evidence of newest-compatible toolchain selection.

The combined derived profile reproduces all 48 identities and 57 active edges
of the reviewed basis. The 18 native cases tested that combined environment;
they did not qualify separately installed profiles, all consumers or actual
Hengshi behavior. Metadata reachability is neither runtime-use nor deployed-
exclusion proof. Source/wheel provenance, licences/advisories, final locks,
other-platform/native-linked inventories and integrated/founder selection remain
separate. Hosting-specific profiles still follow D-068's deferred provider/OS
decision. Independent review of this new role proposal is pending; no earlier
result or notice PASS acquires this scope.
'''
(HERE / 'backend-appendix.md').write_bytes(appendix.encode())
backend.write_bytes(before + appendix.encode())
(HERE / 'backend.proposed.md').write_bytes(backend.read_bytes())
before = readme.read_bytes()
(HERE / 'README.before.md').write_bytes(before)
anchor = b'## Current authority and dated evidence'
position = before.index(anchor) + len(anchor)
addition = '''

The [proposed backend dependency roles](backend-evidence-2026-10-04.md#proposed-backend-dependency-roles--2026-10-09)
separate API, conditional identity, migration and test-tool reachability within
the exact evaluated graph. This is producer-only classification, not a selected
production split, separately qualified environments or deployed-exclusion proof.
Its independent review is pending; no installation or earlier PASS is expanded.
'''
readme.write_bytes(before[:position] + addition.encode() + before[position:])
(HERE / 'README.proposed.md').write_bytes(readme.read_bytes())
paths = [p for p in HERE.iterdir() if p.is_file()]
paths += [backend, readme,
          ROOT / 'output/research/test-client-graph-2026-10-09/pip-report.json',
          ROOT / 'output/research/test-client-graph-2026-10-09/closure-observations.json',
          ROOT / 'output/research/test-client-graph-2026-10-09/receipt.json',
          ROOT / 'output/research/test-client-graph-2026-10-09/candidate-roots.txt',
          ROOT / 'output/research/test-client-graph-2026-10-09/candidate-hashed-requirements.txt',
          ROOT / 'output/research/test-client-graph-2026-10-09/native-trial/receipt.json',
          ROOT / 'output/research/test-client-graph-2026-10-09/result-review/independent-review-native-notices-v1.json',
          ROOT / 'output/research/staff-identity-client-options-2026-10-08/review/independent-review-identity-client-options-v1.json',
          ROOT / 'output/research/backend-wheel-notice-inventory-2026-10-09/observations.json']
manifest = {
    'product_release': 'v1', 'status': 'DOING', 'review_authorized': False,
    'scope': 'Read-only proposed dependency-role closure and two bounded document amendments; no profile installation/import, package/tool selection, app/Figma/account/Git action.',
    'inputs': [{'path': p.relative_to(ROOT).as_posix(), 'bytes': p.stat().st_size,
                'sha256': hashlib.sha256(p.read_bytes()).hexdigest()} for p in sorted(set(paths))]
}
(HERE / 'review-inputs.json').write_bytes((json.dumps(manifest, indent=2) + '\n').encode())
print(json.dumps({'input_count': len(manifest['inputs']),
                  'manifest_sha256': hashlib.sha256((HERE / 'review-inputs.json').read_bytes()).hexdigest()}, indent=2))

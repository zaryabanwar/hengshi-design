"""Freeze the authorized native-result/notice review without repeating producers."""
import hashlib
import json
from pathlib import Path
import xml.etree.ElementTree as ET

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
TRIAL = HERE / 'native-trial'
OUT = HERE / 'result-review'
NOTICES = ROOT / 'output/research/backend-wheel-notice-inventory-2026-10-09'
if OUT.exists():
    raise SystemExit('Refuse repeat result preparation')
receipt = json.loads((TRIAL / 'receipt.json').read_bytes())
assert receipt['qualification'] == 'PASS_synthetic_library_boundaries'
assert receipt['package_count'] == 48 and receipt['protected_inputs_unchanged']
tests = ET.parse(TRIAL / 'library-probes.xml').getroot().find('testsuite')
assert tests is not None and tests.attrib['tests'] == '18'
assert all(tests.attrib[key] == '0' for key in ('errors', 'failures', 'skipped'))
assert not (TRIAL / '07-library-probes.stderr.txt').read_bytes()
warning = json.loads((TRIAL / 'warning-filter-admission.json').read_bytes())
assert warning['both_error_filters_exercised'] and warning['authlib_initialization_preceded_filters']
inventory = json.loads((NOTICES / 'observations.json').read_bytes())
assert inventory['package_count'] == 48 and inventory['notice_file_count'] == 60
assert inventory['protected_inputs_unchanged']
OUT.mkdir()
backend = ROOT / 'docs/phase-1-compatibility/backend-evidence-2026-10-04.md'
readme = ROOT / 'docs/phase-1-compatibility/README.md'
before = backend.read_bytes()
(OUT / 'backend.before.md').write_bytes(before)
appendix = '''
## Preferred client native result and wheel notices — 2026-10-09

Status: DOING. The founder approved the separate 48-package trial and one results/
notice review in “Approve trial and results review”. The [terminal native receipt](../../output/research/test-client-graph-2026-10-09/native-trial/receipt.json)
records a new pip-less research environment, exact hashed binary-wheel download,
offline install, clean pip check and all 48 normalized installed identities
matching the frozen candidate. The earlier 43-package environment and its
preserved comparison failure/correction were neither changed nor reused.

All [18 public-library cases](../../output/research/test-client-graph-2026-10-09/native-trial/library-probes.xml)
passed with zero failures, errors or skips. The original 14 cases are unchanged;
four additional cases establish synthetic TestClient HTTPX2 response ownership,
distinct HTTPX/HTTPX2 exception families, unconfigured Authlib HTTPX2 async-client
ownership/closure and joserfc decoder import. [Warning-filter admission](../../output/research/test-client-graph-2026-10-09/native-trial/warning-filter-admission.json)
initialized Authlib's deprecation module before setting both error filters and
exercised each through a caught synthetic warning. Both remained required pytest
error filters; the recorded test output contains no warning summary and stderr
is empty. This qualifies the preferred client path only at these boundaries;
it does not establish every consumer's migration, real OIDC callback/PKCE/nonce/
ID-token validation, TLS trust, staff permissions or Hengshi session behavior.

The [command/admission records](../../output/research/test-client-graph-2026-10-09/native-trial/commands.json)
retain all eight successful steps, measured expanded-wheel reservation and
post-command checks. Final retained trial size was 84,080,658 bytes with
5,271,166,976 free disk bytes at that observation, within the 256 MiB admission
budget and 1 GiB free-space floor. These are dated measurements and a conservative
boundary-check budget, not an OS hard quota. Psycopg again reports binary
implementation and build/runtime libpq 180004 without connecting to a database.
All six protected inputs remain unchanged. No application source, dependency
manifest/lock, database, provider or original native environment was upgraded.

The separate [exact-wheel notice inventory](../../output/research/backend-wheel-notice-inventory-2026-10-09/observations.json)
preserves metadata and all 60 discovered notice files across the 48 exact Windows
wheels. Every metadata-declared License-File has a unique saved archive-path
binding; no package lacks a discovered notice. Eleven packages contain recorded
binary members. Full notice bytes were saved, not excerpts, and no package was
installed or imported for that inventory. Filename/path discovery can miss
embedded notices; metadata expressions and discovered files do not establish
complete linked/bundled-library coverage, legal applicability or delivered-release
attribution. Hash/CRC matching is not cryptographic publisher/build provenance.

This appendix and the exact results/notices need their authorized independent
review. The earlier 47-input proposal PASS remains scoped to its frozen proposal;
it does not cover these later helpers, execution or notices. Complete newest-
compatible stable graph/platform qualification, advisories, licence applicability,
verified provenance, reproducible production locks and integrated/founder adoption
remain held. These evaluation pins and synthetic cases select no production
dependency and prove no actual Hengshi API, PostgreSQL transaction, account,
authorization, concurrency, recovery or deployment behavior.
'''
(OUT / 'backend-appendix.md').write_bytes(appendix.encode())
backend.write_bytes(before + appendix.encode())
(OUT / 'backend.proposed.md').write_bytes(backend.read_bytes())
before = readme.read_bytes()
(OUT / 'README.before.md').write_bytes(before)
anchor = b'## Current authority and dated evidence'
position = before.index(anchor) + len(anchor)
addition = '''

The [preferred-client native result and exact-wheel notices](backend-evidence-2026-10-04.md#preferred-client-native-result-and-wheel-notices--2026-10-09)
record the separately authorized 48-package trial: all 18 offline library cases
passed with both fallback warnings required as errors. The saved notice inventory
covers 60 discovered files, with declared-path bindings and explicit embedded/
legal/provenance limits. Independent results/notice review is authorized and
pending; complete graph/locks, supply-chain and integrated/adoption gates remain.
Earlier prospective descriptions below retain their dated scope; current results
do not retroactively expand any frozen review or authorize production upgrades.
'''
readme.write_bytes(before[:position] + addition.encode() + before[position:])
(OUT / 'README.proposed.md').write_bytes(readme.read_bytes())
metadata = OUT / 'installed-metadata'
metadata.mkdir()
for path in sorted((TRIAL / 'environment/Lib/site-packages').glob('*.dist-info/METADATA')):
    (metadata / (path.parent.name + '.txt')).write_bytes(path.read_bytes())
assert len(list(metadata.iterdir())) == 48
# Prior reviewed inputs are retained; canonical files have intentional later links.
prior = json.loads((HERE / 'review-inputs.json').read_bytes())
canonical = {backend.relative_to(ROOT).as_posix(), readme.relative_to(ROOT).as_posix()}
paths = {ROOT / entry['path'] for entry in prior['inputs'] if entry['path'] not in canonical}
paths.update([backend, readme, Path(__file__).resolve(), HERE / 'review-inputs.json',
              HERE / 'independent-review-client-graph-v1.json', HERE / 'execution-preparation.json',
              HERE / 'run_native_trial.py', HERE / 'run_probes.py'])
paths.update(p for p in TRIAL.iterdir() if p.is_file())
paths.update(p for p in (TRIAL / 'wheelhouse').iterdir() if p.is_file())
paths.update(p for p in NOTICES.rglob('*') if p.is_file())
paths.update(p for p in OUT.rglob('*') if p.is_file())
old = ROOT / 'output/research/backend-crypto-graph-2026-10-08/native-trial'
paths.update(old / name for name in ('receipt.json', 'continuation-receipt.json',
                                  'continuation-correction.json', 'commands.json',
                                  'continuation-commands.json', 'library-probes.xml'))
paths.add(ROOT / 'output/research/staff-identity-distribution-2026-10-09/joserfc/wheel.gz')
manifest = {
    'product_release': 'v1', 'status': 'DOING', 'review_authorized': True,
    'founder_approval': 'Approve trial and results review',
    'scope': 'Read-only exact 48-wheel native execution, 18 cases, effective warning admission, saved full discovered notice inventory and bounded two-document result appendix. No helper/test/import execution, installation, network, application, Figma, account, Git or dependency adoption.',
    'inputs': [{'path': p.relative_to(ROOT).as_posix(), 'bytes': p.stat().st_size,
                'sha256': hashlib.sha256(p.read_bytes()).hexdigest()}
               for p in sorted(paths)],
    'limits': ['Earlier frozen proposal receipts retain exact scope; later live canonical references differ intentionally.',
               'Read installed metadata snapshots and saved source/command/results as data only; do not execute native environment.',
               'Inventory heuristic and binary members are not complete embedded/linked licence or legal/provenance clearance.']
}
(OUT / 'review-inputs.json').write_bytes((json.dumps(manifest, indent=2) + '\n').encode())
print(json.dumps({'input_count': len(manifest['inputs']),
                  'manifest_sha256': hashlib.sha256((OUT / 'review-inputs.json').read_bytes()).hexdigest(),
                  'modified_canonical_documents': [str(backend), str(readme)]}, indent=2))

"""Freeze native evidence and reconcile only its owning document and Figma brief."""
import gzip
import hashlib
import json
from pathlib import Path
import urllib.request
import xml.etree.ElementTree as ET

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
TRIAL = HERE / 'native-trial'
PACKET = HERE / 'native-result-review'
if PACKET.exists() and any(PACKET.iterdir()):
    raise SystemExit('Refuse repeat outcome capture')
receipt = json.loads((TRIAL / 'continuation-receipt.json').read_bytes())
suite = ET.parse(TRIAL / 'library-probes.xml').getroot()[0]
assert receipt['qualification'] == 'PASS_synthetic_library_boundaries' and receipt['protected_inputs_unchanged']
assert suite.attrib['tests'] == '14' and all(suite.attrib[x] == '0' for x in ('errors', 'failures', 'skipped'))
distribution = ROOT / 'output/research/staff-identity-distribution-2026-10-09'
review = json.loads((distribution / 'independent-review-distributions-v1.json').read_bytes())
assert review['result'] == 'PASS' and not review['findings']
manifest = json.loads((distribution / 'review-inputs.json').read_bytes())
for item in manifest['inputs']:
    raw = (ROOT / item['path']).read_bytes()
    assert len(raw) == item['bytes'] and hashlib.sha256(raw).hexdigest() == item['sha256'], item['path']
PACKET.mkdir(exist_ok=True)
sources = []
for name, url in [
    ('name-normalization.rst', 'https://raw.githubusercontent.com/pypa/packaging.python.org/main/source/specifications/name-normalization.rst'),
    ('starlette-testclient.py', 'https://raw.githubusercontent.com/Kludex/starlette/1.7.0/starlette/testclient.py'),
    ('httpx2-registry.json', 'https://pypi.org/pypi/httpx2/json'),
]:
    request = urllib.request.Request(url, headers={'User-Agent': 'Hengshi-Phase1-Evidence/1.0'})
    with urllib.request.urlopen(request, timeout=30) as response:
        raw = response.read(300001)
        assert len(raw) <= 300000
        (PACKET / (name + '.gz')).write_bytes(gzip.compress(raw, mtime=0))
        sources.append({'url': url, 'file': name + '.gz', 'raw_bytes': len(raw),
                        'raw_sha256': hashlib.sha256(raw).hexdigest(), 'http_status': response.status})
(PACKET / 'sources.json').write_text(json.dumps(sources, indent=2) + '\n')
installed_source = TRIAL / 'environment/Lib/site-packages/starlette/testclient.py'
raw_source = installed_source.read_bytes()
(PACKET / 'installed-starlette-testclient.py').write_bytes(raw_source)
published_source = gzip.decompress((PACKET / 'starlette-testclient.py.gz').read_bytes())
assert raw_source.replace(b'\r\n', b'\n') == published_source.replace(b'\r\n', b'\n')
httpx2 = json.loads(gzip.decompress((PACKET / 'httpx2-registry.json.gz').read_bytes()))
warning = {'product_release': 'v1', 'status': 'DOING',
           'installed_source_matches_tag_ignoring_newlines': True,
           'httpx2_registry_latest_observed': httpx2['info']['version'],
           'observation_not_selection': True,
           'finding': 'Starlette 1.7.0 TestClient uses httpx2 when present and falls back to deprecated httpx; 14 probes passed on the frozen HTTPX 0.28.1 path.',
           'next_boundary': 'Evaluate supported stable HTTPX/test-tool graph before adoption; no package added, warning suppressed or exception approved.'}
(PACKET / 'test-client-observation.json').write_text(json.dumps(warning, indent=2) + '\n')
backend = ROOT / 'docs/phase-1-compatibility/backend-evidence-2026-10-04.md'
before = backend.read_bytes()
(PACKET / 'backend.before.md').write_bytes(before)
addition = '''
The [29-input independent distribution review](../../output/research/staff-identity-distribution-2026-10-09/independent-review-distributions-v1.json)
passes the exact saved two-wheel/licence/publishing observations and appendix.
Its [frozen reviewed document](../../output/research/staff-identity-distribution-2026-10-09/backend.proposed.md)
remains preserved. This later reference is outside those inputs; no signature,
complete-candidate licence, legal, native, sign-in or integrated acceptance follows.

## Isolated native library qualification — 2026-10-09

Status: DOING. The founder approved the existing 43-package frozen trial in
“approve all three and resume”. Exact hashed binary wheels were downloaded once
and installed offline into a separate pip-less research environment. All 43
normalized package names and exact versions match; pip check reports no broken
requirements. The [original stopped receipt](../../output/research/backend-crypto-graph-2026-10-08/native-trial/receipt.json)
is retained: the harness initially compared lowercased names without Python's
required separator normalization. The [explicit correction](../../output/research/backend-crypto-graph-2026-10-08/native-trial/continuation-correction.json)
applies the [PyPA name rule](https://packaging.python.org/en/latest/specifications/name-normalization/)
to both inventories and rejects collisions or any real name/version difference.
Only the remaining approved probes continued; no download or install repeated.

The [14 public-library probes](../../output/research/backend-crypto-graph-2026-10-08/native-trial/library-probes.xml)
pass with zero failures/errors/skips. They exercise RSA token rejection, strict
synthetic HTTP input/output, SQLite rollback/reuse, offline Alembic PostgreSQL
DDL, bcrypt boundaries, Uvicorn configuration and the actual async pytest plugin.
Psycopg reports binary client implementation and build/runtime libpq 180004;
no database connection, actual Hengshi route, Entra/OIDC or provider was exercised.
The [continuation receipt](../../output/research/backend-crypto-graph-2026-10-08/native-trial/continuation-receipt.json)
records 81,648,527 retained trial bytes and 5,390,553,088 free disk bytes at its
measurement, within the 256 MiB admission budget/1 GiB floor. These are dated
observations, not current free space or an OS hard quota. Six protected inputs
remain unchanged; Authlib/joserfc were not part of this 43-package execution.

One warning remains: Starlette 1.7.0 TestClient's HTTPX 0.28.1 fallback is
deprecated. The [saved installed/tagged source and registry observation](../../output/research/backend-crypto-graph-2026-10-08/native-result-review/test-client-observation.json)
identify the coupling question; passing probes do not approve this path for the
selected test-tool graph. No HTTPX2 package, warning suppression or exception
was added. Evaluate the mutually compatible stable graph before adoption.
Independent native-result review, full candidate licences/provenance/advisories,
reproducible locks and integrated/founder acceptance remain required. This
qualification selects no production package and authorizes no application upgrade.
'''
(PACKET / 'backend-appendix.md').write_bytes(addition.encode())
backend.write_bytes(before + addition.encode())
(PACKET / 'backend.proposed.md').write_bytes(backend.read_bytes())
brief = ROOT / 'docs/phase-1-ui-reference-production/B01_EXECUTION_BRIEF.md'
brief_raw = brief.read_bytes()
(PACKET / 'B01_EXECUTION_BRIEF.before.md').write_bytes(brief_raw)
replacements = [
    (b'without correcting originals. It is unexecuted and requires fresh per-call approval.',
     b'without correcting originals. Approved attempt20 returned a reauthentication error and no images/design receipt; source changes were not verified. Reconnect and obtain fresh per-call permission before a retry. See the [failed attempt receipt](../../output/research/b01-directory-full-resolution-2026-10-08/attempt20-2026-10-09/receipt.json).'),
    (b'October attempts 19, conservatively metered 16.', b'October attempts 20, conservatively metered 17; actual debit/balance remains unknown.'),
    (b'separate pending approval; no new call number or monthly debit is assigned here.',
     b'separate reauthentication/fresh-retry gate after attempt20; this recovery preparation assigns no additional call number or monthly debit.'),
    (b'ran; the separately prepared directory pixel export still requires fresh approval.',
     b'ran in this coverage reconciliation; the later directory export attempt20 failed authentication and a retry requires fresh approval.'),
]
for old, new in replacements:
    assert brief_raw.count(old) == 1, old
    brief_raw = brief_raw.replace(old, new)
brief.write_bytes(brief_raw)
(PACKET / 'B01_EXECUTION_BRIEF.proposed.md').write_bytes(brief_raw)
paths = [HERE / name for name in ('qualification-plan.json', 'candidate-hashed-requirements.txt',
         'closure-observations.json', 'proposal.json', 'run_native_trial.py', 'continue_native_trial.py',
         'runner-preflight-correction.json', 'native-probes/test_libraries.py',
         'review/correction-1/review-inputs.json', 'review/correction-1/independent-review-correction-1-v1.json')]
paths += [p for p in TRIAL.iterdir() if p.is_file()]
paths += [p for p in PACKET.iterdir() if p.is_file() and not p.name.startswith('B01')]
paths += [backend]
installed_metadata = PACKET / 'installed-metadata'; installed_metadata.mkdir()
for meta in sorted((TRIAL / 'environment/Lib/site-packages').glob('*.dist-info/METADATA')):
    target = installed_metadata / (meta.parent.name + '.txt')
    target.write_bytes(meta.read_bytes()); paths.append(target)
assert len(list(installed_metadata.iterdir())) == 43
items = [{'path': p.relative_to(ROOT).as_posix(), 'bytes': p.stat().st_size,
          'sha256': hashlib.sha256(p.read_bytes()).hexdigest()} for p in paths]
packet = {'product_release': 'v1', 'status': 'DOING',
          'scope': 'Read-only native-result evidence and exact appended backend claims; verify preserved harness failure/canonical-name correction, 43 identities/hashes, commands, 14 probe results, warning, budget/protected inputs. No rerun, install, socket or provider.',
          'reviewer_authorization': False, 'inputs': items}
(PACKET / 'review-inputs.json').write_text(json.dumps(packet, indent=2) + '\n')
print(json.dumps({'input_count': len(items), 'tests': suite.attrib['tests'], 'warning': warning,
                  'canonical_documents_changed': ['backend-evidence-2026-10-04.md', 'B01_EXECUTION_BRIEF.md']}))

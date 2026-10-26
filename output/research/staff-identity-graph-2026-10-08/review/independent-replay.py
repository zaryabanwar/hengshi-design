"""Read-only frozen metadata replay; writes only reviewer evidence beside this file."""
import difflib, gzip, hashlib, json, sys
from pathlib import Path
from urllib.parse import unquote, urlsplit
from packaging.markers import default_environment
from packaging.requirements import Requirement
from packaging.specifiers import SpecifierSet
from packaging.tags import sys_tags
from packaging.utils import canonicalize_name as canonical, parse_wheel_filename
from packaging.version import Version

sys.stdout.reconfigure(encoding='utf-8')
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
INPUT = HERE / 'inputs'
BASE = INPUT / 'output/research/staff-identity-graph-2026-10-08'
PRIOR = INPUT / 'output/research/backend-crypto-graph-2026-10-08'
sha = lambda b: hashlib.sha256(b).hexdigest()
read = lambda p: json.loads(p.read_text(encoding='utf-8'))
manifest_raw = (HERE/'review-inputs.json').read_bytes()
assert sha(manifest_raw) == '42b66cfa2c017e09ff1862dedfb920a208846e9fa221fd2c0eb569287d3879d3'
manifest = json.loads(manifest_raw)
assert len(manifest['inputs']) == 82
for i in manifest['inputs']:
    frozen = (ROOT/i['snapshot']).read_bytes()
    assert len(frozen) == i['bytes'] and sha(frozen) == i['sha256'], i['path']
    assert (ROOT/i['path']).read_bytes() == frozen, i['path']
receipt, producer, report = [read(BASE/n) for n in ('receipt.json','closure-observations.json','pip-report.json')]
old_report = read(PRIOR/'pip-report.json')
assert sha((BASE/'pip-report.json').read_bytes()) == receipt['report_sha256'] == producer['report_sha256']
assert sha((PRIOR/'pip-report.json').read_bytes()) == receipt['basis_report_sha256']
assert receipt['exit_code'] == 0 and receipt['installation_performed'] is False
assert '--dry-run' in receipt['command'] and '--only-binary=:all:' in receipt['command']
records = {canonical(x['metadata']['name']): x for x in report['install']}
old = {canonical(x['metadata']['name']): x for x in old_report['install']}
assert len(records) == len(report['install']) == 45 and len(old) == 43
assert set(records)-set(old) == {'authlib','joserfc'} and set(old) <= set(records)
for n,r in old.items():
    assert records[n]['metadata'] == r['metadata'] and records[n]['download_info'] == r['download_info'], n
env = report['environment']
assert all(default_environment()[k] == v for k,v in env.items())
roots_raw = (BASE/'candidate-roots.txt').read_bytes()
assert sha(roots_raw) == receipt['roots_sha256']
parse_roots = lambda raw: [Requirement(x) for x in raw.decode().splitlines() if x and not x.startswith('#')]
roots = {canonical(x.name): x for x in parse_roots(roots_raw)}
prior_roots = {canonical(x.name): x for x in parse_roots((PRIOR/'candidate-roots.txt').read_bytes())}
assert len(roots) == 13 and len(prior_roots) == 12
assert set(roots) == {n for n,r in records.items() if r['requested']}
assert set(roots)-set(prior_roots) == {'authlib'}
assert all(str(roots[n]) == str(r) for n,r in prior_roots.items())
extras = {n:set() for n in records}
for n,r in roots.items():
    assert r.url is None and r.specifier == SpecifierSet('=='+records[n]['metadata']['version'])
    assert set(r.extras) == set(records[n].get('requested_extras',[]))
    extras[n].update(r.extras)
edges, changed = set(), True
while changed:
    changed = False
    for n,r in records.items():
        for declaration in r['metadata'].get('requires_dist',[]):
            req = Requirement(declaration)
            if req.marker and not any(req.marker.evaluate({**env,'extra':e}) for e in extras[n]|{''}):
                continue
            target = canonical(req.name)
            assert req.url is None and target in records, (n,declaration)
            assert req.specifier.contains(records[target]['metadata']['version'], prereleases=False)
            edges.add((n,target,declaration))
            if set(req.extras)-extras[target]:
                extras[target].update(req.extras); changed = True
assert len(edges) == 51 and sorted(map(list,edges)) == producer['active_edges']
reachable = set(roots)
while True:
    expanded = reachable | {b for a,b,_ in edges if a in reachable}
    if expanded == reachable: break
    reachable = expanded
assert reachable == set(records)
assert extras['pyjwt'] == {'crypto'} and extras['uvicorn'] == {'standard'} and extras['psycopg'] == {'binary'}
assert not extras['joserfc'] and not extras['authlib'] and 'pycryptodome' not in records
tags, observations, pins, wheel_bytes = set(sys_tags()), [], {}, 0
new_classifiers = {}
for n,r in sorted(records.items()):
    metadata, info = r['metadata'], r['download_info']
    version = Version(metadata['version'])
    assert not version.is_prerelease and not version.is_devrelease and not r['is_yanked']
    assert SpecifierSet(metadata.get('requires_python') or '').contains(env['python_full_version'])
    url = urlsplit(info['url'])
    assert url.scheme == 'https' and url.hostname == 'files.pythonhosted.org'
    filename = unquote(url.path.rsplit('/',1)[-1])
    wn,wv,_,wt = parse_wheel_filename(filename)
    assert canonical(wn) == n and wv == version and wt & tags
    if n in {'authlib','joserfc'}:
        registry_path = f'output/research/staff-identity-graph-2026-10-08/{n}-exact.json.gz'
    elif n in {'cffi','cryptography','pycparser'}:
        registry_path = f'output/research/backend-crypto-graph-2026-10-08/new-registry/{n}-exact.json.gz'
    else:
        rel = 'core-recovery/pydantic-core-project.json.gz' if n == 'pydantic-core' else f'primary/{n}-project.json.gz'
        registry_path = 'output/research/backend-hash-inputs-2026-10-08/'+rel
    packed = (INPUT/registry_path).read_bytes()
    registry = json.loads(gzip.decompress(packed))
    assert canonical(registry['info']['name']) == n and Version(registry['info']['version']) == version
    norm = lambda vals: sorted(str(Requirement(x)) for x in vals or [])
    assert norm(registry['info'].get('requires_dist')) == norm(metadata.get('requires_dist')), n
    assert SpecifierSet(registry['info'].get('requires_python') or '') == SpecifierSet(metadata.get('requires_python') or '')
    artifacts = registry['urls'] if '-exact' in registry_path else registry['releases'][str(version)]
    match = [f for f in artifacts if f['filename'] == filename and f['url'] == info['url']]
    assert len(match) == 1
    wheel = match[0]; digest = info['archive_info']['hashes']['sha256']
    assert wheel['digests']['sha256'] == digest and wheel['packagetype'] == 'bdist_wheel' and not wheel['yanked']
    assert SpecifierSet(wheel.get('requires_python') or '').contains(env['python_full_version'])
    wheel_bytes += wheel['size']
    pins[n] = (str(version),sorted(extras[n]),digest)
    observations.append({'name':n,'version':str(version),'extras':sorted(extras[n]),'wheel':filename,'sha256':digest,
                         'bytes':wheel['size'],'registry_snapshot':registry_path,'registry_snapshot_sha256':sha(packed)})
    if n not in old:
        new_classifiers[n] = [x for x in registry['info']['classifiers'] if x.startswith('Development Status')]
        assert registry['info']['requires_python'] == '>=3.10'
assert observations == producer['package_records'] and wheel_bytes == producer['archive_bytes'] == 18439402
assert any('Production/Stable' in x for x in new_classifiers['joserfc'])
pin_raw = (BASE/'candidate-hashed-requirements.txt').read_bytes()
assert sha(pin_raw) == producer['hashed_requirements_sha256']
actual_pins = {}
for line in pin_raw.decode().splitlines():
    if not line or line.startswith('#'): continue
    text,digest = line.split(' --hash=sha256:'); req = Requirement(text); n = canonical(req.name)
    assert req.url is None and req.marker is None and n not in actual_pins
    actual_pins[n] = (next(iter(req.specifier)).version,sorted(req.extras),digest)
assert actual_pins == pins
assert len(receipt['protected_inputs_before']) == 6 and receipt['protected_inputs_before'] == receipt['protected_inputs_after']
for p,h in receipt['protected_inputs_before'].items():
    assert sha((INPUT/p).read_bytes()) == sha((ROOT/p).read_bytes()) == h
sources = read(BASE/'registry-sources.json')
for s in sources:
    packed = (INPUT/s['snapshot']).read_bytes(); raw = gzip.decompress(packed)
    assert len(raw) == s['raw_bytes'] and sha(raw) == s['raw_sha256'] and sha(packed) == s['snapshot_sha256']
release_obs = read(BASE/'joserfc-release-observations.json')
assert len(release_obs) == 2 and release_obs[0]['http_status'] == 404 and release_obs[0]['url'].endswith('/v1.7.5')
s = release_obs[1]; packed = (BASE/s['snapshot']).read_bytes(); raw = gzip.decompress(packed); release = json.loads(raw)
assert s['http_status'] == 200 and s['url'].endswith('/1.7.5') and sha(raw) == s['raw_sha256'] and sha(packed) == s['snapshot_sha256']
assert release['tag_name'] == s['tag_name'] == '1.7.5' and release['draft'] is s['draft'] is False and release['prerelease'] is s['prerelease'] is False
before = (BASE/'before/backend-evidence-2026-10-04.md').read_bytes()
after = (INPUT/'docs/phase-1-compatibility/backend-evidence-2026-10-04.md').read_bytes()
assert after.startswith(before)
old_map = (BASE/'before/04-reconciliation-map.md').read_text(encoding='utf-8').splitlines(keepends=True)
new_map = (INPUT/'docs/software-definition/04-reconciliation-map.md').read_text(encoding='utf-8').splitlines(keepends=True)
changes = [x for x in difflib.SequenceMatcher(a=old_map,b=new_map,autojunk=False).get_opcodes() if x[0]!='equal']
assert len(changes)==1 and changes[0] == ('replace',241,242,241,242)
assert new_map[241].startswith(old_map[241].removesuffix(' |\n'))
plan = read(PRIOR/'qualification-plan.json')
assert plan['execution_authorized'] is False
assert plan['candidate_sha256'] == read(PRIOR/'closure-observations.json')['hashed_requirements_sha256'] != sha(pin_raw)
assert plan['archive_bytes_from_registry'] == 18107329
result = {'status':'DOING','metadata_replay_verdict':'PASS','manifest_sha256':sha(manifest_raw),'frozen_live_inputs':82,
          'roots':13,'packages':45,'active_marker_extra_edges':51,'previous_43_complete_metadata_and_download_info_equal':True,
          'additions':{'authlib':'1.8.0','joserfc':'1.7.5'},'all_packages_root_reachable':True,'required_extras_retained':True,
          'joserfc_drafts_and_pycryptodome_excluded':True,'registry_declared_compressed_distribution_wheel_bytes':wheel_bytes,
          'two_exact_registry_and_one_release_compressed_raw_hash_pairs':True,'joserfc_wrong_prefix_404_and_actual_release_200_preserved':True,
          'protected_inputs':6,'backend_prefix_preserved_bytes':len(before),'map_diff':'One appended sentence within row242',
          'prior_43_trial_unapproved_and_unchanged':True,'package_records':observations,'active_edges':sorted(map(list,edges)),
          'limits':'Saved metadata/tags/hash associations only. No wheel content/download verification, source provenance, install, native/OIDC/Entra/security tests, licence clearance, production selection or expanded trial permission.'}
(HERE/'independent-replay-results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:result[k] for k in ('metadata_replay_verdict','frozen_live_inputs','roots','packages','active_marker_extra_edges','registry_declared_compressed_distribution_wheel_bytes')}))

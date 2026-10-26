"""Derive proposed role closures from frozen metadata; no resolution or imports."""
import csv
import hashlib
import json
from pathlib import Path
import packaging
from packaging.requirements import Requirement
from packaging.utils import canonicalize_name

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
BASIS = ROOT / 'output/research/test-client-graph-2026-10-09'
OUT = HERE / 'profiles.json'
if OUT.exists():
    raise SystemExit('Refuse repeat profile derivation')
sha = lambda value: hashlib.sha256(value).hexdigest()
report_raw = (BASIS / 'pip-report.json').read_bytes()
assert sha(report_raw) == 'e81b7570efc6903d4074151a61cfdca9060c02f5da59236bee353eddb1831462'
report = json.loads(report_raw)
records = {canonicalize_name(p['metadata']['name']): p for p in report['install']}
assert len(records) == len(report['install']) == 48
environment = report['environment']
protected = json.loads((BASIS / 'receipt.json').read_bytes())['protected_inputs_before']
assert all(sha((ROOT / p).read_bytes()) == digest for p, digest in protected.items())
groups = {
    'api_families': ['fastapi', 'uvicorn[standard]', 'sqlalchemy', 'psycopg[binary]',
                     'bcrypt', 'pyjwt[crypto]', 'email-validator', 'python-dotenv'],
    'conditional_identity_evaluation': ['authlib', 'httpx2'],
    'migration_tooling': ['alembic'],
    'test_tooling': ['pytest', 'pytest-asyncio', 'httpx'],
}
requested = {name: set(p.get('requested_extras', [])) for name, p in records.items() if p['requested']}
seeds = {canonicalize_name(Requirement(text).name): set(Requirement(text).extras)
         for texts in groups.values() for text in texts}
assert len(seeds) == 14 and seeds == requested
profile_groups = {
    'api_base_candidate': ['api_families'],
    'api_with_identity_candidate': ['api_families', 'conditional_identity_evaluation'],
    'migration_tool_candidate': ['migration_tooling'],
    'combined_qualification_basis': list(groups),
}
def closure(texts):
    reached = set()
    extras = {}
    direct = []
    for text in texts:
        req = Requirement(text)
        name = canonicalize_name(req.name)
        reached.add(name)
        extras.setdefault(name, set()).update(req.extras)
        direct.append(name)
    edges = set()
    changed = True
    while changed:
        changed = False
        for parent in sorted(reached):
            for clause in records[parent]['metadata'].get('requires_dist', []):
                req = Requirement(clause)
                active = not req.marker or any(req.marker.evaluate({**environment, 'extra': extra})
                            for extra in {''} | extras.get(parent, set()))
                if not active:
                    continue
                child = canonicalize_name(req.name)
                assert req.url is None and child in records
                assert req.specifier.contains(records[child]['metadata']['version'], prereleases=False)
                edges.add((parent, child, clause))
                if child not in reached:
                    reached.add(child)
                    changed = True
                added = set(req.extras) - extras.setdefault(child, set())
                if added:
                    extras[child].update(added)
                    changed = True
    return {'direct_roots': sorted(set(direct)), 'package_count': len(reached),
            'packages': sorted(reached), 'active_edges': [list(edge) for edge in sorted(edges)],
            'extras': {name: sorted(extras.get(name, set())) for name in sorted(reached)}}
profiles = {name: closure([text for group in names for text in groups[group]])
            for name, names in profile_groups.items()}
assert set(profiles['combined_qualification_basis']['packages']) == set(records)
basis_closure = json.loads((BASIS / 'closure-observations.json').read_bytes())
assert profiles['combined_qualification_basis']['active_edges'] == basis_closure['edges']
ancestry = {canonicalize_name(Requirement(text).name): closure([text])['packages']
            for texts in groups.values() for text in texts}
inventory = json.loads((ROOT / 'output/research/backend-wheel-notice-inventory-2026-10-09/observations.json').read_bytes())
binaries = set(inventory['packages_with_binary_members'])
rows = []
for name, package in sorted(records.items()):
    rows.append({'name': name, 'version': package['metadata']['version'],
                 'profiles': [key for key, profile in profiles.items() if name in profile['packages']],
                 'reachable_from_roots': [root for root, nodes in sorted(ancestry.items()) if name in nodes],
                 'observed_binary_members': name in binaries,
                 'sha256': package['download_info']['archive_info']['hashes']['sha256']})
app = set(profiles['api_with_identity_candidate']['packages'])
test_only = sorted(set(records) - app - set(profiles['migration_tool_candidate']['packages']))
result = {
    'product_release': 'v1', 'status': 'DOING',
    'scope': 'Producer-only proposed role reachability on the evaluated exact Windows graph; no selected production packaging',
    'report_sha256': sha(report_raw), 'analysis_packaging_version': packaging.__version__,
    'environment': environment, 'proposed_root_roles': groups,
    'profiles': profiles, 'package_records': rows,
    'outside_application_and_migration_candidates': test_only,
    'protected_inputs_unchanged': all(sha((ROOT / p).read_bytes()) == digest for p, digest in protected.items()),
    'limits': ['Reachability in saved Requires-Dist metadata is not a resolver result for independent profiles, import/use evidence or final packaging.',
               'Authlib/HTTPX2 are conditional evaluated identity candidates, not selected staff adapters or production requirements.',
               'The 18-case native result tested the combined graph, not each derived profile in a separate environment.',
               'Shared/transitive membership does not grant exclusive role ownership or prove exclusion from delivered artifacts.',
               'Other Python, platform, extras, OS/native-linked, tools/build and actual deployment graphs need their own qualification under D-068.',
               'No installation, candidate package import, lock, app, provider, account, Git or deployment change.'],
}
OUT.write_bytes((json.dumps(result, indent=2) + '\n').encode())
with (HERE / 'package-roles.csv').open('w', encoding='utf-8', newline='') as handle:
    writer = csv.writer(handle)
    writer.writerow(['package', 'version', 'profiles', 'reachable_from_roots', 'observed_binary_members', 'wheel_sha256'])
    for row in rows:
        writer.writerow([row['name'], row['version'], ';'.join(row['profiles']),
                         ';'.join(row['reachable_from_roots']), row['observed_binary_members'], row['sha256']])
print(json.dumps({'profile_counts': {key: value['package_count'] for key, value in profiles.items()},
                  'combined_edges': len(profiles['combined_qualification_basis']['active_edges']),
                  'outside_application_and_migration_candidates': test_only,
                  'protected_inputs_unchanged': result['protected_inputs_unchanged']}, indent=2))

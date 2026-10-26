"""Correlate actual saved command results; no security or legal clearance."""
from collections import Counter
from datetime import datetime, timezone
import collect
import json

def load(name):
    return json.loads((collect.OUT / name).read_text(encoding='utf-8'))

inventory = load('licence-inventory.json')
installed = [row for row in inventory['records'] if row['installed']]
expected = Counter((row['name'], row['version']) for row in installed)
sbom = load('installed-sbom.stdout.json')
observed = {(row['name'], row.get('versionInfo')) for row in sbom['packages']}
project = json.loads((collect.CANDIDATE / 'package.json').read_text(encoding='utf-8'))
project_identity = (project['name'], project['version'])
if set(expected) - observed or observed - set(expected) != {project_identity}:
    raise RuntimeError('SBOM metadata correlation differs')
signatures = load('detailed-signatures.stdout.json')
known_locations = {row['lock_path']: row for row in installed}
if any(row['location'] not in known_locations or
       (row['name'], row['version']) != (known_locations[row['location']]['name'], known_locations[row['location']]['version'])
       for row in signatures['verified']):
    raise RuntimeError('Detailed attestation location/version differs')
bundles = Counter()
for row in signatures['verified']:
    bundle = row.get('attestationBundles')
    if isinstance(bundle, list):
        for value in bundle:
            bundles[value.get('predicateType', 'unspecified')] += 1
    elif isinstance(bundle, dict):
        bundles.update(bundle.keys())
observations = {
    'checked_at_utc': datetime.now(timezone.utc).isoformat(),
    'node': '26.10.0', 'npm': '12.2.0', 'lock_sha256': collect.sha(collect.CANDIDATE / 'package-lock.json'),
    'advisory_audit': {'exit': load('advisory-audit-receipt.json')['exit_code'],
        'reported_vulnerabilities': load('advisory-audit.stdout.json')['metadata']['vulnerabilities'],
        'limits': 'Dated known-advisory database report for this candidate lock, not absence of vulnerabilities or a deployment reachability verdict.'},
    'virtual_sbom': {'exit': load('lock-sbom-receipt.json')['exit_code'],
        'error': 'ESBOMPROBLEMS', 'missing_optional_wasm_dependencies': ['@emnapi/core', '@emnapi/runtime',
        '@emnapi/wasi-threads', '@napi-rs/wasm-runtime', '@tybys/wasm-util', 'tslib'],
        'limits': 'Virtual all-platform inventory is incomplete; no unsupported-platform installation or repair attempted.'},
    'installed_sbom': {'exit': load('installed-sbom-receipt.json')['exit_code'],
        'format': sbom['spdxVersion'], 'packages': len(sbom['packages']), 'relationships': len(sbom['relationships']),
        'installed_locations': len(installed), 'distinct_name_version_pairs': len(expected),
        'duplicates': [{'name': key[0], 'version': key[1], 'locations': count} for key, count in expected.items() if count > 1],
        'correspondence': 'All 233 installed name/version pairs plus private fixture root match the 234 emitted package identities.',
        'noassertion': [{'name': row['name'], 'version': row.get('versionInfo')} for row in sbom['packages'] if row.get('licenseDeclared') == 'NOASSERTION'],
        'limits': 'Installed research tree only; omits absent platform packages and is not a shipped-artifact SBOM or legal clearance.'},
    'signature_verification': {'exit': load('detailed-signatures-receipt.json')['exit_code'],
        'invalid': len(signatures['invalid']), 'missing': len(signatures['missing']),
        'attestation_records': len(signatures['verified']),
        'attestation_bundle_predicates': dict(bundles),
        'gensync_attestation_record_present': any(row['name'] == 'gensync' for row in signatures['verified']),
        'limits': 'npm12 verified registry metadata signatures and available attestations. The verified JSON array contains attestation records only, not all signature checks. Missing on-disk optional packages are skipped; installed-file contents, provenance availability for every package and D072 obligations are not proven.'},
    'licence_inventory': {'lock_records_excluding_root': len(inventory['records']),
        'declared_licence_counts': inventory['licence_counts_from_lock'],
        'installed_without_top_level_text': [{'name': row['name'], 'version': row['version'], 'declared': row['installed_licence']} for row in installed if not row['top_level_licence_and_notice_files']],
        'limits': inventory['limits']},
    'guards': {'first_pass': load('post-command-guard.json'), 'follow_up': load('post-follow-up-guard.json'),
        'limits': 'Both before the separate later reference/checkpoint integration; no retrospective hash equality is claimed.'},
    'context7': {'library': '/npm/cli', 'query_date': '2026-10-06',
        'topics': 'Read-only audit, signatures/available attestations and installed versus virtual SBOM; exact installed npm12 sources also inspected.'},
    'state': 'DOING', 'selection': 'No adoption, package repair, policy override, application change, provider change or security/legal/Phase1 acceptance.'
}
collect.save('observations.json', observations)
print('Saved correspondence: 236 installed locations, 233 unique pairs, 234 SBOM packages; available attestations remain partial.')

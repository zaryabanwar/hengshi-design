"""Append two canonical evidence summaries and freeze this independent material slice."""
from pathlib import Path
import collect
import json

README = collect.ROOT / 'docs/phase-1-compatibility/README.md'
REFRESH = collect.ROOT / 'docs/phase-1-compatibility/refresh-evidence-2026-10-04.md'
if (collect.OUT / 'review-inputs.json').exists():
    raise RuntimeError('Refusing overwrite')
observations = json.loads((collect.OUT / 'observations.json').read_text(encoding='utf-8'))
if observations['signature_verification']['invalid'] or observations['signature_verification']['missing']:
    raise RuntimeError('Unexpected signature finding; revise summary before recording')
for path in (README, REFRESH):
    (collect.OUT / (path.name + '.before')).write_bytes(path.read_bytes())

readme = '''
## Matched-candidate supply-chain follow-up — 2026-10-06

The [separate read-only follow-up](refresh-evidence-2026-10-04.md#matched-candidate-supply-chain-observations--2026-10-06)
records zero reported known advisories, an installed-tree SPDX inventory matching
233 package/version pairs plus the private fixture root, and npm12 signature/
available-attestation verification with no reported invalid or missing entries.
Only 78 attestation records are emitted; gensync has no emitted attestation record.
These observations do not clear all provenance, installed-file integrity or D-072.

The all-platform virtual SBOM fails on six missing dependencies beneath optional
oxide WASM; the successful installed-tree inventory does not replace that failure.
Licence declarations include non-MIT terms and one missing declaration; retained
top-level licence texts are evidence, not legal clearance or complete bundled
notice coverage. No dependency repair or production selection is made. Separate
independent review, complete graph and founder acceptance remain required; this
follow-up is outside the preceding compiler/build/browser receipt.
'''
refresh = '''
## Matched-candidate supply-chain observations — 2026-10-06

This [separate read-only investigation](../../output/research/frontend-supply-chain-2026-10-06/observations.json)
uses the unchanged research candidate lock
`fa903a8d901357aacf80863524e0e00ae2ece69126daf218256cdd2656b2da4c`
and portable Node26.10.0/npm12.2.0. Commands use explicit empty configs, public
registry, a new research-only metadata cache and disabled lifecycle scripts.
No audit fix, installation, dependency/lock patch, credential or machine setting
change occurs. Both post-command guards match all 2,668 then-frozen inputs;
the later reference/checkpoint integration is separate and does not retroactively
change those observations. This material lies outside the preceding independent
compiler/build/browser review and requires its own review.

### Known-advisory report and inventory boundaries

Actual [npm audit --json --package-lock-only](../../output/research/frontend-supply-chain-2026-10-06/advisory-audit-receipt.json)
exits 0 with zero vulnerabilities reported by the registry: no informational,
low, moderate, high or critical entries. This is a dated known-advisory observation,
not proof of vulnerability absence, executable reachability or deployment security.

Actual [virtual SPDX SBOM](../../output/research/frontend-supply-chain-2026-10-06/lock-sbom-receipt.json)
exits 1, ESBOMPROBLEMS. The optional @tailwindcss/oxide-wasm32-wasi entry requires
six absent virtual-tree dependencies: @emnapi/core, @emnapi/runtime,
@emnapi/wasi-threads, @napi-rs/wasm-runtime, @tybys/wasm-util and tslib. Preserve
the failure; the candidate lock is not a complete validated all-platform inventory.
No unsupported-platform install or lock repair is attempted.

The separate actual [installed-tree SPDX SBOM](../../output/research/frontend-supply-chain-2026-10-06/installed-sbom-receipt.json)
exits 0 and emits SPDX-2.3 with 234 packages and 398 relationships. All 233 distinct
installed name/version pairs plus the private fixture root correspond. There are
236 installed locations: semver6.3.1 appears twice and eslint-visitor-keys5.0.1
three times, accounting for the package-identity deduplication. Both root Three
0.184.0 and nested Three0.170.0 remain visible, as do the two checker paths and
gensync beta. This inventory covers the installed research tree, not missing
optional platforms or the eventual shipped browser/server/images. The private
fixture root and webgl-constants1.1.1 emit NOASSERTION for declared licence.

### Registry signatures, available attestations and licence evidence

Both actual [signature commands](../../output/research/frontend-supply-chain-2026-10-06/detailed-signatures-receipt.json)
exit 0 with empty invalid/missing arrays. The detailed --include-attestations
result emits 78 verified attestation records, each corresponding to its installed
package location/version. Installed npm12 source adds a verified JSON record only
when an attestation is present; this array is not the total signature-check count.
gensync has no emitted attestation record. The verifier skips missing on-disk
optional dependencies and verifies published registry metadata and available
attestations; it does not compare every installed file to an archive, establish
provenance availability for all packages or certify safe publisher/source behavior.
Keep D-072 integrity/provenance/execution/exclusion/conformance obligations open.

The [licence inventory](../../output/research/frontend-supply-chain-2026-10-06/licence-inventory.json)
retains each of 301 non-root lock records, installed metadata hashes and available
top-level licence/notice text copies with identities. Lock declarations include
MIT207, ISC13, Apache-2.0 44, CC-BY-4.0 1, BSD-2-Clause6, BSD-3-Clause3,
MPL-2.0 24, BlueOak-1.0.0 1, one GSAP standard licence declaration and one absent
declaration. These counts include optional platform entries and are declarations,
not independently established rights. Eleven installed packages have no top-level
licence/notice file under the collector's narrow rule; this does not establish
that their distribution contains no terms. Existing scoped GSAP/WASM notice
evidence retains its own exact inputs. Recursive bundled notices, source/archive
correspondence, legal interpretation, attribution assembly, platform-specific
inventory and deployed-artifact SBOM still require evidence before adoption.

Primary guidance checked 2026-10-06: Context7 `/npm/cli` for audit/signatures and
actual versus virtual inventory, official [npm12 audit](https://docs.npmjs.com/cli/v12/commands/npm-audit/)
and [npm12 SBOM](https://docs.npmjs.com/cli/v12/commands/npm-sbom/) pages, and retained
installed npm12 audit/SBOM/signature/SPDX command sources. Audit checks known
registry advisories; fix would mutate dependencies and was not used. Available
attestations are distinct from signatures; installed and lockfile inventory modes
cover different trees. These sources do not select a project graph or grant legal
clearance. Full graph, D-069 exceptions/rollback/recheck, D-072 conformance,
MA-013 and integrated founder acceptance remain held.
'''
for path, value in ((README, readme), (REFRESH, refresh)):
    with path.open('ab') as file:
        file.write(value.replace('\n', '\r\n').encode('utf-8'))
    (collect.OUT / (path.name + '.reviewed')).write_bytes(path.read_bytes())
protected = json.loads((collect.BASE / 'protected-before.json').read_text(encoding='utf-8'))
protected = [{'path': row['path'], 'sha256': collect.sha(collect.ROOT / row['path'])} for row in protected]
collect.save('protected-before.json', protected)
paths = {README, REFRESH, collect.ROOT / 'DECISIONS.md', collect.ROOT / 'TASKS.md'}
for row in protected:
    paths.add(collect.ROOT / row['path'])
for path in collect.OUT.rglob('*'):
    if path.is_file() and 'metadata-cache' not in path.parts and '__pycache__' not in path.parts:
        paths.add(path)
for row in json.loads((collect.OUT / 'licence-inventory.json').read_text(encoding='utf-8'))['records']:
    path = collect.CANDIDATE / row['lock_path'] / 'package.json'
    if path.exists():
        paths.add(path)
    for text in row['top_level_licence_and_notice_files']:
        paths.add(collect.ROOT / text['path'])
for relative in ('candidate/package.json', 'candidate/package-lock.json'):
    paths.add(collect.BASE / relative)
for relative in ('node.exe', 'package/package.json', 'package/lib/commands/audit.js',
                 'package/lib/commands/sbom.js', 'package/lib/utils/verify-signatures.js',
                 'package/lib/utils/sbom-spdx.js'):
    paths.add(collect.RUNTIME / relative)
packet = [{'path': path.relative_to(collect.ROOT).as_posix(), 'sha256': collect.sha(path)}
          for path in sorted(paths, key=lambda path: path.as_posix())]
collect.save('review-inputs.json', packet)
print(f'Canonical slice recorded; {len(packet)} review inputs SHA256 {collect.sha(collect.OUT / "review-inputs.json")}')

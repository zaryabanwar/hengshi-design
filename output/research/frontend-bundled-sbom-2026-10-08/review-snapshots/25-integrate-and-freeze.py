from pathlib import Path
import hashlib, json, shutil

root=Path.cwd(); out=root/'output/research/frontend-bundled-sbom-2026-10-08'
readme=root/'docs/phase-1-compatibility/README.md'
evidence=root/'docs/phase-1-compatibility/refresh-evidence-2026-10-04.md'
assert not (out/'README.before.md').exists()
shutil.copyfile(readme,out/'README.before.md'); shutil.copyfile(evidence,out/'refresh-evidence.before.md')
summary='''The [supplemented candidate metadata inventory](refresh-evidence-2026-10-04.md#supplemented-virtual-bundled-inventory--2026-10-08)
now represents the six previously missing archive-owned nodes using npm's own
in-memory dependency model and SPDX exporter. This is a separate producer
supplement, not a passing original npm CLI result or repaired lock. It retains
all platform metadata in the candidate lock and explicitly lists absent optional
peers; actual platform artifacts, embedded code, licence/provenance/advisory
coverage, D-072 isolation, complete graph selection and adoption remain held.
Independent review of this new packet is required; earlier receipts retain scope.

'''.replace('\n','\r\n').encode('utf-8')
data=readme.read_bytes(); needle=b'## Current authority and dated evidence\r\n\r\n'; assert data.count(needle)==1
readme.write_bytes(data.replace(needle,needle+summary))
appendix='''

## Supplemented virtual bundled inventory — 2026-10-08

Status: DOING. Metadata-only isolated evidence under D-069, D-072 and D-077;
no application/runtime/lock/provider changes or production adoption.

The original virtual `npm sbom` result still fails `ESBOMPROBLEMS`; its receipt,
empty stdout, six missing edges and exact candidate lock remain unchanged. The
separate successful Windows installed-tree inventory still excludes optional
platform locations. Neither historical result is relabelled here.

The [new inventory](../../output/research/frontend-bundled-sbom-2026-10-08/supplemented.spdx.json)
starts with npm12.2.0 Arborist's actual `loadVirtual` result: 302 locations including
the private fixture root. The preserved candidate lock SHA256 remains
`fa903a8d901357aacf80863524e0e00ae2ece69126daf218256cdd2656b2da4c`.
The producer rechecked the saved optional oxide archive against that lock's SHA512
integrity and all seven named package manifests against the earlier inspected
manifest hashes. Six declared bundled children are attached through Arborist's
Node model in memory only. No `reify`, ideal-tree resolution, save, install,
script, source patch or lock serialization occurs.

The [location/edge inventory](../../output/research/frontend-bundled-sbom-2026-10-08/graph.json)
retains 308 locations: the original 302 plus six archive-owned occurrences. Npm's
dependency resolution changes the six originally missing required edges to
valid targets; no required missing or invalid edge remains in this supplemented
metadata model. The twelve declared edges across the bundle's seven manifests
resolve through that model. Twenty-one absent references are all optional peers
and remain explicitly recorded, including Expo/React Native, optional Babel/
compiler paths, Vite extensions and Immer. No capability or execution support
for those absent paths is inferred.

The producer invokes npm's installed SPDX exporter directly, with an added
supplement creator and scope comment; this is not another successful `npm sbom`
command. It emits 305 name/version package records and 483 unique relationships,
including six explicit `CONTAINS` relationships. Occurrence locations remain in
the separate graph because npm merges equal name/version identities. None of
these six bundled identities collides with an original name/version record.
Their child download locations remain `NOASSERTION` and no parent archive
checksum is assigned to a child. `filesAnalyzed=false` remains explicit.

[Validation observations](../../output/research/frontend-bundled-sbom-2026-10-08/validation.json)
record zero errors against the saved official SPDX2.3 JSON schema, unique IDs,
resolving relationship endpoints, exact bundled containment correlations and
the absent optional peers. A deliberately unsupported relationship type fails
the schema; a dangling endpoint passes its shape but fails the independent
endpoint correlation. This illustrates the distinct evidence layers. Schema
acceptance does not validate every SPDX semantic requirement or licence
expression: npm's declared labels, including the GSAP custom label, remain raw
metadata and are not licence clearance or a claim of fully compliant attribution.

The initial producer guard incorrectly treated all 78 historical 6 October inputs
as current. Its failed observation is preserved. The corrected comparison
explicitly reports later changes to DECISIONS, PROJECT_STATE and TASKS; the other
75 earlier input identities still match, including their protected application,
asset and candidate inputs. Current authority is separately frozen for review.
This does not claim that the older checkpoint files stayed unchanged.

Context7 `/npm/cli`, [official npm12 SBOM guidance](https://docs.npmjs.com/cli/v12/commands/npm-sbom/),
the [official SPDX schema](https://raw.githubusercontent.com/spdx/spdx-spec/v2.3/schemas/spdx-schema.json)
and [SPDX containment/dependency guidance](https://spdx.github.io/spdx-spec/v2.3.1/relationships-between-SPDX-elements/)
were consulted, alongside installed Arborist/Node/flag/exporter source. Npm's
reader and exporter define this observed model; no custom package-range resolver
or inferred published child archive substitutes for the verified bundled bytes.

This supplements the named missing metadata occurrences and provides a portable
candidate inventory. It does not inspect every other platform archive or embedded
component, prove publisher/source-to-binary provenance, assemble applicable
notices, cover current advisories or package safety, or establish D-072 deployed
exclusion/conformance. Complete compatible selection, exact production locks,
rollback/recheck, MA-013, legal/adoption and integrated Phase 1 acceptance remain
held. Later build/platform/deployed artifact inventories must be based on their
actual delivered bytes; this research supplement cannot stand in for them.
'''.replace('\n','\r\n').encode('utf-8')
evidence.write_bytes(evidence.read_bytes()+appendix)
paths=[
 'docs/phase-1-compatibility/README.md','docs/phase-1-compatibility/refresh-evidence-2026-10-04.md',
 'AGENTS.md','.specify/memory/constitution.md','PROJECT.md','DECISIONS.md','PROJECT_STATE.yaml','TASKS.md',
 'output/research/frontend-three-remedy-evaluation-2026-10-06/candidate/package.json',
 'output/research/frontend-three-remedy-evaluation-2026-10-06/candidate/package-lock.json',
 'output/research/optional-wasm-contents-2026-10-06/contents.json',
 'output/research/frontend-supply-chain-2026-10-06/lock-sbom-receipt.json',
 'output/research/frontend-supply-chain-2026-10-06/lock-sbom.stderr.txt',
 'output/research/frontend-supply-chain-2026-10-06/protected-before.json',
 'docs/phase-1-compatibility/reviews/optional-wasm-contents-v1-2026-10-06.md'
]
runtime=root/'output/research/frontend-build-evaluation-2026-10-06/runtime/package'
paths += [(runtime/p).relative_to(root).as_posix() for p in ['package.json','node_modules/@npmcli/arborist/lib/node.js','node_modules/@npmcli/arborist/lib/calc-dep-flags.js','node_modules/@npmcli/arborist/lib/arborist/load-virtual.js','lib/utils/sbom-spdx.js','lib/commands/sbom.js']]
paths += [p.relative_to(root).as_posix() for p in out.iterdir() if p.is_file() and p.name not in ['review-inputs.json']]
snapshot=out/'review-snapshots'; snapshot.mkdir(exist_ok=False)
inputs=[]
for i,p in enumerate(paths):
    src=root/p; dest=snapshot/f'{i:02d}-{src.name}'; shutil.copyfile(src,dest); raw=src.read_bytes()
    inputs.append({'source':p,'snapshot':dest.relative_to(root).as_posix(),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()})
archive='output/research/optional-wasm-bundle-2026-10-06/oxide-wasm32-wasi-4.3.3.tgz'
raw=(root/archive).read_bytes()
inputs.append({'source':archive,'snapshot':archive,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'preservation':'Existing frozen archive retained in place to avoid duplicate storage'})
manifest=out/'review-inputs.json'
manifest.write_text(json.dumps({'product':'Hengshi Design v1','status':'DOING','scope':'Supplemented candidate metadata model/export and appended evidence only; not repaired npm lock/CLI/deployed SBOM','inputs':inputs},indent=2)+'\n',encoding='utf-8')
print(json.dumps({'inputs':len(inputs),'manifest_sha256':hashlib.sha256(manifest.read_bytes()).hexdigest()}))

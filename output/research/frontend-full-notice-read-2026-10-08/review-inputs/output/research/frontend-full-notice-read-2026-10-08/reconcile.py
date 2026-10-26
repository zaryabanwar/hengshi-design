from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil
root=Path(__file__).resolve().parents[3]
out=Path(__file__).resolve().parent
refresh=root/'docs/phase-1-compatibility/refresh-evidence-2026-10-04.md'
entry=root/'docs/phase-1-compatibility/README.md'
for file in [refresh,entry]:shutil.copyfile(file,out/(file.name+'.before'))
sources={'product':'Hengshi Design v1','status':'DOING','checked_at_utc':datetime.now(timezone.utc).isoformat(),
 'primary_sources':[{'url':'https://docs.npmjs.com/cli/v12/configuring-npm/package-json/#license',
  'observation':'Official npm12 documentation identifies common-licence SPDX declarations and directs custom declarations to a named supplied licence file; metadata is not publisher/source-build proof.'},
 {'url':'https://docs.npmjs.com/cli/v12/configuring-npm/package-json/#files',
  'observation':'Official npm12 documentation distinguishes package files, README and LICENSE/LICENCE inclusion; this does not establish that a particular binary distribution contains all third-party notices.'}],
 'no_legal_interpretation':'Sources explain metadata/file handling only; no package licence applicability or clearance is decided'}
(out/'primary-source-observations.json').write_text(json.dumps(sources,indent=2)+'\n',encoding='utf-8')
with refresh.open('a',encoding='utf-8',newline='') as stream:
    stream.write('''

## Full installed notice reads and broader root inventory — 2026-10-08

Status: DOING. This follows the [bounded eleven-package discovery review](reviews/installed-notice-discovery-v1-2026-10-08.md)
and removes its prefix/excerpt limits in a new isolated read-only study. No candidate,
application, lock, package script, setting, model, Git or provider change occurs.
The original candidate lock remains
`fa903a8d901357aacf80863524e0e00ae2ece69126daf218256cdd2656b2da4c`.

### Complete reads and notice candidates

[Full observations](../../output/research/frontend-full-notice-read-2026-10-08/observations.json)
re-enumerate and initially/finally verify all 394 own-file identities of the same
eleven packages. There are 387 complete strict UTF-8 file reads, including all
31 formerly excluded JSON source maps; seven other files remain outside the text
allowlist. The maps contain 44 embedded source strings. No source path is resolved
or fetched and no vendor code executes. Raw full-text term locations are retained
without the former 8,192-byte / twelve-match / 240-character caps. The study retains
256 complete README/comment-shaped candidates, not 256 applicable licence notices.
The regex is deliberately not a language parser: it may match comment syntax in
JSON strings, templates or examples. Nonmatching clauses, binary interpretation,
other packages and actual deployed/bundled attribution remain outside this scope.

A concrete new candidate is `maath 0.10.8`'s Quaternion Damp comment in three
`dist/easing-*` files, beginning at character offsets 8,336 / 8,384 / 8,386.
The identical text SHA256 is
`2fda481f5dc33e4f7d0e7c09d238796646adb689e7abaf47c61e262559c86a09`.
It includes the Max Kaufmann copyright and permission/condition/disclaimer text;
the earlier prefix scan missed it. This is embedded third-party evidence, not a
substitute for the whole package's own declaration or complete applicability review.

### Root-name omission repaired across the installed candidate

[Broader root inventory](../../output/research/frontend-full-notice-read-2026-10-08/root-notice-name-inventory.json)
checks the same 236 installed locations and metadata identities, matching notice,
licence, copying, copyright and third-party terms anywhere in immediate filenames.
It retains 229 unchanged full text copies: all previous 227 and two new files,
`@typescript/old/ThirdPartyNoticeText.txt` (37,824 bytes) and
`rolldown/THIRD-PARTY-LICENSE` (2,209 bytes). The previous starts-with collector
missed both. The latter accompanies the existing Rolldown MIT text and identifies
additional Rollup/Evan Wallace notices. A sibling Rolldown package's notices do
not establish all Rust/native-binding component rights. This remains an immediate
filename inventory, not a recursive licence classifier or whole-binary audit.

### Published source associations

[Eleven exact-version registry responses](../../output/research/frontend-full-notice-read-2026-10-08/registry-source-associations.json)
match the installed names/versions and prior declared distribution integrity
strings. They preserve licence declarations and six Git revision pointers.
That correlation does not verify signatures/attestations, installed-file/archive
identity, publisher/source builds or safety.
[Pinned notice requests](../../output/research/frontend-full-notice-read-2026-10-08/pinned-upstream-notice-associations.json)
retain two root notice candidates at those declared revisions: Fiber (1,072 bytes)
and Draco (13,898 bytes). These are upstream source candidates, not silently
substituted installed package files or default-branch licences.

Finite root-filename requests returned 404 for the other four pointed repositories.
Separate [revision-tree observations](../../output/research/frontend-full-notice-read-2026-10-08/revision-tree-observations.json)
returned complete non-truncated trees at all four requested revisions: Humanfs has
licence files for seven other sibling packages but none at `packages/types`;
esrecurse, Natural Compare and stats-gl have no notice-name path in those trees.
This reports name/path coverage only, never absence of licensing terms in source.
MediaPipe, the Rolldown binding, GSAP, imurmurhash and maath supplied no Git pointer
in these version metadata responses. No guessed source revision is promoted.

[Official npm metadata/file guidance](https://docs.npmjs.com/cli/v12/configuring-npm/package-json/#license)
is recorded in [primary observations](../../output/research/frontend-full-notice-read-2026-10-08/primary-source-observations.json).
Metadata declarations, complete copied text, embedded notices and source pointers
remain distinct evidence types. Earlier GSAP/pinned vendor archive reviews retain
their own scopes; no earlier receipt is reinterpreted as whole-graph clearance.

Independent review of these new full-read, root-inventory and pointer associations
is pending. Applicable licence interpretation/attribution assembly, other embedded
components, all-platform/deployed coverage, provenance, D-072 isolation, complete
compatible graph/locks, MA-013 and integrated Phase1 acceptance remain held.
''')
needle='The [exact synthetic client module inventory]'
raw=entry.read_bytes().decode('utf-8')
assert raw.count(needle)==1
raw=raw.replace(needle,'''The later [full notice reads and broader root inventory](refresh-evidence-2026-10-04.md#full-installed-notice-reads-and-broader-root-inventory--2026-10-08)
remove the eleven-package prefix/excerpt limits, inspect all31 source maps and
retain previously omitted TypeScript/Rolldown third-party files across236 installed
locations. Exact-version public source associations are separate from publisher
provenance and licence applicability. Independent review of this new evidence is
pending; complete attribution, graph selection and adoption remain held.

'''+needle)
entry.write_bytes(raw.encode('utf-8'))
print(json.dumps({'canonical_documents_changed':2,'new_evidence_scope':'full reads/root-name repair/exact-version source pointers','independent_review':'pending','candidate_changed':False}))

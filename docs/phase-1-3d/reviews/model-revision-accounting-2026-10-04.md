# Campus model revision accounting review — v1

Date: 2026-10-04. Independent bounded governance review.
Disposition: **REVISE** for the current accounting statements; **one final third model revision cycle is available under the known sequence**, without a new revision-limit exception.

## Scope and authority

This receipt checks the existing campus prototype's creation/revision count only. It does not review geometry, approve a new model design, accept appearance, authorize production modelling or amend canonical status.

`AGENTS.md:29–31` separates create from revise and allows at most three revision cycles for 3D. The constitution at lines 99–102 and 185–191 repeats that sequence and requires escalation once revisions are exhausted. An accepted counting precedent appears in **D-047**, `DECISIONS.md:245–252`: initial amendment plus revision 2 consumed one revision cycle. D-046 commissioned that amendment; D-047 records its accepted count. This supports excluding initial creation from the revision allowance. It does not transfer unused UI cycles into the campus or reset any other workstream.

## Finding

**MODEL-COUNT-MED-001 — Medium — current records imply exhausted revisions without the required count.**

`docs/phase-1-3d/SPATIAL_STORYBOARD.md:126` says the assessment does not permit a “fourth substantial model revision”. `PROJECT_STATE.yaml:31` carries `fourth_correction_exception` as a held condition. The known campus sequence contains an initial creation and two subsequent substantial attempts, rather than three completed revision cycles. Counting the stopped refinement conservatively as one cycle still leaves the third revision cycle available.

Required correction: replace the exhaustion/exception implication with explicit accounting: initial blockout creation, revision cycle 1 stopped refinement, revision cycle 2 composition rebuild, revision cycle 3 remaining and bounded. Retain applicable design, inspection, independent review and founder appearance/production acceptance gates; after that third revision, unresolved material changes require a founder decision rather than another silent revision. Preserve the exact reviewed records and this receipt when correcting references.

This is an accounting correction supported by existing governance, not a request to waive the limit. No ambiguity in the supplied known sequence prevents that bounded correction.

## Known model sequence

The founder conversation supplied in this chat records rejection of the initial blockout, a refinement attempt then stopped when the architectural composition was clarified, and a composition rebuild subsequently described as better. The retained README at lines 12–17 identifies the same sequence. This conversation is contextual evidence, not a separately retained timestamped machine execution log.

| Known event | Evidence | Conservative revision accounting |
|---|---|---|
| Initial blockout | `build_blockout.py` creates the generic pavilion arrangement/flat terrain and saves `nature-campus-blockout.blend` at line 83. Both are retained. | Initial create; consumes zero revision cycles. |
| Refined attempt | `build_refined.py` keeps that arrangement while changing roofs, foliage and ridge geometry; line 124 would save a refined master and line 128 would export the shared GLB if reached. README explicitly calls it stopped/superseded. | Revision cycle 1, counted even though stopped. The source alone does not prove which instructions completed. |
| Composition rebuild | `build_composition.py:33` introduces continuous valley geometry, line 52 defines larger reception/varied wings, and lines 131–133 save the composition master/export. README identifies these as current. | Revision cycle 2. |
| Next bounded model correction | Not built or reviewed by this receipt. | Final revision cycle 3 remains; no new numerical-limit exception is required for it. |

The inspected directory contains the blockout and composition masters and current GLB. A refined master is not present in that directory inventory. **Its absence does not prove that the attempt never ran, establish its stopping point or exclude hidden/deleted revisions.** The supplied conversation/README establish the known stopped attempt; counting it consumes a cycle rather than erasing it.

Recorded filesystem last-write times put the blockout script/master before the refinement script and then the composition script/master/export. They are consistent with the supplied sequence. Timestamps are observations, not authenticated execution receipts, and cannot establish an exhaustive revision history or production acceptance. Exact script/master/export identities are below.

## Certainty and retained limits

The conclusion is sufficient for the known scope: conservative counting of the stopped attempt gives two consumed revision cycles, so the remaining third cycle is justified. It is not proof that no other revision ever existed. If additional contradictory execution/revision evidence is found, reconcile the count before further model changes; do not infer new attempts from file absence or silently reset the allowance.

“Better” in the founder dialogue is not acceptance of complete appearance or a connected usable production model. The README expressly retains those limits. Existing geometry defects, transfer/loading budgets, safe walking, collision, streaming and all complete Phase 1/production gates remain separate. Inspection/storyboard work that did not change campus geometry does not itself consume a model revision; this receipt makes no count ruling for revisions of other documentation or design contracts.

No scripts or Blender model were executed or changed in this review. No producer record, earlier review, protected Atlanta asset, application, credentials, process, provider, commit or canonical status was modified. Hashes and timestamps establish artifact identity and observed chronology only.

## Exact reviewed input identities

SHA256 covers exact bytes. UTC last-write timestamps are the filesystem observations at inspection.

| Input | Bytes | SHA256 | Last write UTC |
|---|---:|---|---|
| `AGENTS.md` | 7686 | `55405CB02A96D05F7F6D68E56A588D743F83877FB2691A5A9F2C736126ADBCC5` | 2026-10-04T00:46:39.9867577Z |
| `.specify/memory/constitution.md` | 16234 | `33EC0BB02B0D0D9A55D0971589BD19F7242F5D56DA130F8F496BC1D31A8B5D23` | 2026-10-04T00:39:30.1121823Z |
| `DECISIONS.md` | 70865 | `C843AE17EE0AA7B9E5DD0BE39595310B5B25C31BEA2B97ECE4E6EBD34C2DADBF` | 2026-10-04T00:41:20.3629849Z |
| `docs/phase-1-3d/SPATIAL_STORYBOARD.md` | 15611 | `1B87273B24949F0191A077C88B289B5ED9CA0664DEAB8491C7CAA5D8E7D926A9` | 2026-10-04T13:09:51.4634640Z |
| `PROJECT_STATE.yaml` | 3057 | `88BE0E9544EE076A4A108FB42BAA27BF7464FBC42B4D3DB3AE9C481AA3516E04` | 2026-10-04T13:48:21.7755576Z |
| `artifacts/nature-campus-prototype/README.md` | 3681 | `633292D485E88CEC936A775212B9F77763458579D2C5D194B34C3E98E115805F` | 2026-10-04T01:10:04.6039017Z |
| `artifacts/nature-campus-prototype/build_blockout.py` | 6151 | `68CC36E3407C1563EB02EE0C387511C492035E6EBEEE1B2247858C040B18E778` | 2026-10-03T22:33:06.2698876Z |
| `artifacts/nature-campus-prototype/build_refined.py` | 8687 | `FECC917F2F028BC2A282B1376205D1D70F827E3967FB866FEE9538B38366A11B` | 2026-10-03T22:40:28.8062282Z |
| `artifacts/nature-campus-prototype/build_composition.py` | 10182 | `8A2A8E6814A3EDBA881B1B9807B2837638BC6B5B3C3E56AA25413C57F5198972` | 2026-10-03T22:48:25.9326912Z |
| `artifacts/nature-campus-prototype/nature-campus-blockout.blend` | 328579 | `9E12D7D42C3DA0A21EAA6CAEDA7537AB526D8CCFCA37DC895E54441A0016732E` | 2026-10-03T22:33:43.2302767Z |
| `artifacts/nature-campus-prototype/nature-campus-composition.blend` | 4971900 | `2B2E05259DFE2BA66849448246D56A475A8D1EB6C77C0DCB90E200CC43E15AB0` | 2026-10-03T22:48:41.7590754Z |
| `artifacts/nature-campus-prototype/nature-campus.glb` | 8945052 | `7AD9EE472B2E0F51A7E5E2107A88060258E43D87A9DDEDCEB887B6EBBA0B94D8` | 2026-10-03T22:48:50.2766631Z |

## Disposition

**REVISE** for MODEL-COUNT-MED-001 in the current storyboard/state statements. The supported correction is to reserve the final third model revision cycle, not invent a fourth-revision exception. This receipt leaves the existing producers unchanged and grants no model or production acceptance.


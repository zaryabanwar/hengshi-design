# D-076 feature reconciliation independent review — 2026-10-07

Status: DOING; uncommitted. Verdict: **REVISE — initial bounded feature-consistency review.** One P2 staff-session scope ambiguity and P3 review-status wording need reconciliation. Correction has not been applied or re-reviewed; zero correction cycles consumed. No runtime defect was observed or inferred from this definition review.

Scope: only D-076 additions/changed requirements/scenarios in security feature 001 and content feature 004, plus existing producer-checklist consistency against frozen decisions/contracts and the three later scoped receipts. AGENTS and constitution govern. The earlier complete feature definitions, legal correctness of the privacy recommendation, implementation, schema enforcement and whole-feature acceptance were not reviewed anew. This receipt records the initial disposition, not a current-source-wide verdict.

## Exact frozen identities

Packet: `output/research/feature-d076-reconciliation-2026-10-07/`. Manifest `review-inputs.json` SHA-256: `37d2a4d021e906e4889a77fb8bf9fa211532848f44bae616a096589f89925863`. Twenty records use `source`, packet-relative `snapshot`, `bytes` and `sha256`; each snapshot is the corresponding source below the packet's `snapshots/` directory.

| Source / snapshot suffix | Bytes | SHA-256 |
| --- | --- | --- |
| AGENTS.md | 7686 | 55405cb02a96d05f7f6d68e56a588d743f83877fb2691a5a9f2c736126adbcc5 |
| .specify/memory/constitution.md | 16234 | 33ec0bb02b0d0d9a55d0971589bd19f7242f5d56da130f8f496bc1d31a8b5d23 |
| DECISIONS.md | 84370 | f38b6f5930b51cae9188db8df6bc9fe458b0df907a3f6eab10fc6b956a0b50da |
| specs/001-platform-security-hardening/spec.md | 30531 | 88cd499685d95a0d9499ffab6e6606cf4d0ce87ba2c6fb812af4ca9a834f46e7 |
| specs/001-platform-security-hardening/checklists/requirements.md | 3473 | 6f92b3c648a6948a10564a81c814a7d51c9c9b906a1dde616f1ef9c89d84fb14 |
| specs/004-design-services-content/spec.md | 27848 | e23e6a25ec3b5aa6896f21fddb7bdfecaeb1cdd792995d8479c1b548c3d6bd0c |
| specs/004-design-services-content/checklists/requirements.md | 3958 | b84dab8f61339df8d5c23bad402d26f1eeb47cf1ed152ffb8dd75417f4052e5b |
| specs/001-platform-security-hardening/reviews/security-feature-v1-2026-10-04.md | 10080 | 26166b97feee585d524c682fe00a5b1c50aeb5278e71bf98d5edc96fb8ed2960 |
| specs/004-design-services-content/reviews/content-feature-v1-2026-10-04.md | 8350 | c7fb841bf13e5f7a4654b2bccde5af5b40e3efbacd8a7dc0e4d56724dea7147c |
| docs/phase-1-architecture/contracts/PRIVATE_PROCESS_PROOF.md | 108274 | f247fd4c72d2e79cd03d77cd9d0e5287f2266c85bf4cefd129742bb2a9f639a2 |
| docs/phase-1-architecture/contracts/HANDOFF_LIFECYCLE.md | 89614 | 40a3779f56737725bb2c5e5d5a5ee34b44ad27030adc16cc374fdb9b04266a12 |
| docs/phase-1-architecture/contracts/CHAT_EVENT_PROTOCOL.md | 49954 | b2f2b08e52569a7fa50a6e0a00eb71fc2ddd56d50f2033c9c9fa0bd75a282d64 |
| docs/phase-1-architecture/contracts/SECURITY_PRIVACY_CONTRACT.md | 68608 | 3d61c735d00c47d907814f193be4b35669ad950bdf27d8f0f8112f57a8fa6774 |
| docs/phase-1-architecture/contracts/PUBLICATION_CONTRACT.md | 71036 | 9bd9d0d291926ec783f19f84fba18785f4bb476e260d6447e9bde02e111fd9a2 |
| docs/software-definition/06-entity-and-public-contact.md | 15443 | 5e4f5fb9aa35ff2d5165383fb051f3dca2520df088cc2de20fe2c0bab8f40e47 |
| docs/phase-1-architecture/contracts/DATA_CONTRACT.md | 35916 | 1959e28b6be31c3e660d89790612144bd32769d992d554d6b9ec026e898cf8d6 |
| docs/phase-1-architecture/contracts/data-classification.csv | 5615 | c8793ebfb401178b4175f0f6c7b9cfb14edcd606f370090883cbe2be94f0cd6e |
| docs/phase-1-architecture/contracts/reviews/visitor-lifetime-controls-v1-2026-10-07.md | 6106 | a54f91d14cc9b32ca5cb4caff1bbbe90235f4c0b75ed73554ce5e29187008adc |
| docs/phase-1-architecture/contracts/reviews/company-public-projection-v1-2026-10-07.md | 5748 | 7222bc92b7dd3e846ba6faea9383f8d027c362ec6b38a19a26f9107d588da245 |
| docs/phase-1-architecture/contracts/reviews/eu-privacy-retention-v1-2026-10-07.md | 8708 | b02ef22854693fd3f59581be855bd7e1b04e5387bec283aae3dbc63e91a5a200 |

Initial and final review verification on 2026-10-07 matched the manifest and all twenty snapshot hashes/byte counts. Read-only PowerShell parsed each exact packet-relative snapshot, compared `Get-FileHash -Algorithm SHA256` and file length with its record, and repeated the comparison before reporting. Hash/byte equality establishes identity only. No prose tests or runtime/schema tests were run; no external call was required for this consistency review.

## Findings and minimal remedies

All paths and line numbers below refer to the frozen snapshots in this packet, not moving canonical sources.

**D076-F01 — P2: explicitly bind the absolute timeout to staff sessions.** `specs/001-platform-security-hardening/spec.md:144` defines FSC-04 using unqualified "browser sessions" and 30-minute idle/eight-hour absolute limits. Acceptance case 5 at `:237` supplies a controlled clock but no actor or session kind. Read independently as implementation/test oracles, they can impose eight-hour expiry on visitor conversation authority, contrary to FSC-14 at `:154` and visitor cases 17–18 at `:250–251`. The staff-focused title, preceding case 4 and amendment at `:41–44` show the intended distinction, but the two normative statements should carry it themselves. Frozen `SECURITY_PRIVACY_CONTRACT.md:116–119` expressly scopes JWT/absolute clocks to staff; `DECISIONS.md:1006–1011` and `PRIVATE_PROCESS_PROOF.md:846–852` prohibit recreating an absolute visitor cap through proof/cookie lifetime.

Minimal remedy: name **staff JWT browser sessions** in FSC-04 and make case 5 begin with a staff session under controlled time. Explicitly exclude visitor conversation proof/access from that eight-hour absolute clock, retaining FSC-14 and its current activity/End semantics. This requires no new timeout, schema, cryptography or actor grant, and no founder reconsideration of D-076. It is a consequential scope ambiguity in the draft, not evidence of a runtime bug.

**D076-F02 — P3: distinguish completed bounded definition reviews from held legal/physical mechanisms.** Security spec `:47–48,251` retains review-pending language without distinguishing the later visitor-control definition/representation review from still-held mechanism acceptance. Content spec `specs/004-design-services-content/spec.md:46` calls the new legal periods/mappings unreviewed, while the frozen EU receipt `docs/phase-1-architecture/contracts/reviews/eu-privacy-retention-v1-2026-10-07.md:5–6,27–41` records bounded engineering-recommendation PASS and explicitly withholds adoption/legal clearance. `PUBLICATION_CONTRACT.md:931` likewise remains "unreviewed" despite the company-projection receipt `:5–6,19–24,39–40` covering that exact definition/schema seam. These are stale or insufficiently qualified status statements; the later receipts do not clear live mechanisms or counsel review.

Minimal remedy: reference the three later exact-input receipts and label the relevant definition/representation or engineering recommendation as **bounded independently reviewed**, while retaining pending legal clearance, exact physical mechanisms/record bindings, operational contacts, runtime enforcement and founder/integrated acceptance. Keep earlier feature PASS explicitly limited to its preserved inputs; do not transfer it to D-076 or rewrite frozen receipts. Shared-contract reference/status reconciliation can be a separately bounded slice rather than broadening the feature correction.

## Consistent boundaries and prior authority

- Security spec `:43–59,151,182–200,229` preserves staff versus visitor clocks, mapped consented-record expiry without resume/restore reset, separate booking/provider/audit/suppression classes, policy nonadoption, undecided aliases, Entra and verified Azure Europe private-AI routing. D-068 hosting deferral does not authorize weaker private-AI fallback. `PRIVATE_PROCESS_PROOF.md:854–915` preserves deliberate activity, terminal fencing, retained-record separation, uncertain work and no inferred booking cancellation/deletion.
- Content spec `:33–47,129,138,276–284` retains private typed facts and string/month precision, excludes registration/validity/supplied address from public derivatives, keeps mandatory operator/contact assessment and quarantines synthetic local records. `PUBLICATION_CONTRACT.md:936–975` requires allowlisted same-candidate projection, prevents disguising excluded facts in allowed fields and forbids fixtures establishing real company/contact/live-staff truth. Entity definition `:39–63` preserves notice assessment and later verified disclosure without requesting real records for current Phase 1 definition.
- Security checklist `specs/001-platform-security-hardening/checklists/requirements.md:34–37,49–51` and content checklist `specs/004-design-services-content/checklists/requirements.md:33–35,46–51` honestly bind prior PASS to preserved exact feature inputs and retain final evidence/acceptance holds. They do not automatically cover the D-076 additions. Unchecked readiness items are not evidence of completed planning, implementation or approval.
- The earlier security/content receipts retain their exact-input limits. The later visitor, projection and privacy receipts retain representation/engineering scope and no runtime/legal/founder acceptance. In particular, visitor receipt `:26–42` retains stolen-valid-proof exposure, shared-clock/fencing, physical settlement, warning/progress and accessibility limits; company receipt `:35–40` retains semantic exclusion/contact/publication enforcement; EU receipt `:39–42` retains period adoption, exact policy/copy/provider/legal/operational bindings. This review adds no stronger assurance.

## Disposition and preservation

Apply the narrow staff-scope correction and review-status qualification, then freeze a separately identifiable correction packet for bounded re-review. The correction is not yet applied; this initial REVISE remains historical evidence after any later superseding disposition. No further consequential inconsistency was established within the requested amendment/checklist scope.

No actual processing, auth, session, publication, controller/model or provider boundary was exercised. No whole-feature re-review, legal clearance, accessibility/security certification, feature/integrated acceptance, planning permission or launch readiness follows. The feature review changed no files; subsequent authorized preservation creates only this one DOING/uncommitted receipt. Feature/contract/checklist sources, snapshots, state, code, external systems, Git history and goal remain unchanged in this preservation slice. PASS/DONE is not claimed; the producer/parent owns the separate correction cycle and checkpoint.

## Correction 1 disposition — superseding bounded PASS, 2026-10-07

Status: DOING; uncommitted. Verdict: **PASS for the exact correction-1 scope only.** D076-F01 (P2) and D076-F02 (P3) are resolved; no residual consequential finding established. One correction cycle used. This supersedes the initial findings only at the exact correction packet below; it does not replace the historical initial review or accept either whole feature.

The entire original REVISE receipt remains an exact byte prefix, with original SHA-256 `6a5fbc98289fa8572768913d62a8f461e8fe8e3657e9ed3106ba25f7f97c724e`. The initial manifest `37d2a4d021e906e4889a77fb8bf9fa211532848f44bae616a096589f89925863` and all twenty initial frozen identities remain preserved and matched at review completion.

Correction packet: `output/research/feature-d076-reconciliation-2026-10-07/correction-1/`. Its `review-inputs.json` SHA-256 is `b80c43d0d60995761ed9b7b6ea14a997718c16cef118223c478a14d28b1148bb`. Twenty directory-relative snapshots use `source`, `snapshot`, `bytes` and `sha256`; each is the source path beneath this packet's `snapshots/`. All twenty corrected snapshot hashes and byte counts matched initially and finally.

| Corrected source / snapshot suffix | Bytes | SHA-256 |
| --- | --- | --- |
| AGENTS.md | 7686 | 55405cb02a96d05f7f6d68e56a588d743f83877fb2691a5a9f2c736126adbcc5 |
| .specify/memory/constitution.md | 16234 | 33ec0bb02b0d0d9a55d0971589bd19f7242f5d56da130f8f496bc1d31a8b5d23 |
| DECISIONS.md | 84370 | f38b6f5930b51cae9188db8df6bc9fe458b0df907a3f6eab10fc6b956a0b50da |
| specs/001-platform-security-hardening/spec.md | 31323 | 2f7066eef33f89f8600587e7778d70e80538b82d49709c5516cac91f63371747 |
| specs/001-platform-security-hardening/checklists/requirements.md | 3473 | 6f92b3c648a6948a10564a81c814a7d51c9c9b906a1dde616f1ef9c89d84fb14 |
| specs/004-design-services-content/spec.md | 28074 | d95a6fa419135cbc1774a3f5bff5e141ec9ba0a8ae8a108e752b890e96df7a34 |
| specs/004-design-services-content/checklists/requirements.md | 3958 | b84dab8f61339df8d5c23bad402d26f1eeb47cf1ed152ffb8dd75417f4052e5b |
| specs/001-platform-security-hardening/reviews/security-feature-v1-2026-10-04.md | 10080 | 26166b97feee585d524c682fe00a5b1c50aeb5278e71bf98d5edc96fb8ed2960 |
| specs/004-design-services-content/reviews/content-feature-v1-2026-10-04.md | 8350 | c7fb841bf13e5f7a4654b2bccde5af5b40e3efbacd8a7dc0e4d56724dea7147c |
| docs/phase-1-architecture/contracts/PRIVATE_PROCESS_PROOF.md | 108274 | f247fd4c72d2e79cd03d77cd9d0e5287f2266c85bf4cefd129742bb2a9f639a2 |
| docs/phase-1-architecture/contracts/HANDOFF_LIFECYCLE.md | 89614 | 40a3779f56737725bb2c5e5d5a5ee34b44ad27030adc16cc374fdb9b04266a12 |
| docs/phase-1-architecture/contracts/CHAT_EVENT_PROTOCOL.md | 49954 | b2f2b08e52569a7fa50a6e0a00eb71fc2ddd56d50f2033c9c9fa0bd75a282d64 |
| docs/phase-1-architecture/contracts/SECURITY_PRIVACY_CONTRACT.md | 68608 | 3d61c735d00c47d907814f193be4b35669ad950bdf27d8f0f8112f57a8fa6774 |
| docs/phase-1-architecture/contracts/PUBLICATION_CONTRACT.md | 71338 | ee78c1b0b35549cf2a4a2647726d3080874b14bc57e86934b422a1e959b2a4c8 |
| docs/software-definition/06-entity-and-public-contact.md | 15443 | 5e4f5fb9aa35ff2d5165383fb051f3dca2520df088cc2de20fe2c0bab8f40e47 |
| docs/phase-1-architecture/contracts/DATA_CONTRACT.md | 35916 | 1959e28b6be31c3e660d89790612144bd32769d992d554d6b9ec026e898cf8d6 |
| docs/phase-1-architecture/contracts/data-classification.csv | 5615 | c8793ebfb401178b4175f0f6c7b9cfb14edcd606f370090883cbe2be94f0cd6e |
| docs/phase-1-architecture/contracts/reviews/visitor-lifetime-controls-v1-2026-10-07.md | 6106 | a54f91d14cc9b32ca5cb4caff1bbbe90235f4c0b75ed73554ce5e29187008adc |
| docs/phase-1-architecture/contracts/reviews/company-public-projection-v1-2026-10-07.md | 5748 | 7222bc92b7dd3e846ba6faea9383f8d027c362ec6b38a19a26f9107d588da245 |
| docs/phase-1-architecture/contracts/reviews/eu-privacy-retention-v1-2026-10-07.md | 8708 | b02ef22854693fd3f59581be855bd7e1b04e5387bec283aae3dbc63e91a5a200 |

Exactly three sources changed: security spec, content spec and the company-projection review label in PUBLICATION_CONTRACT. Seventeen sources remain byte-identical to the initial packet, including both producer checklists, founder decisions, other contracts/classification and all five prior receipts. Checklist PASS remains scoped to its earlier preserved feature inputs; no checked item becomes D-076 or whole-feature acceptance through this correction.

### Finding resolution at frozen correction lines

All paths below refer to correction-1's exact snapshots, not moving canonical files.

- **D076-F01 resolved:** `specs/001-platform-security-hardening/spec.md:80,143,236` explicitly names staff authentication in the outcome, FSC-04 and case 5. FSC-04/case 5 expressly exclude visitor conversation proof/access from the staff absolute clock. FSC-14 at `:153` and visitor cases 17–18 at `:249–250` retain 30-minute inactivity/authorized End and no absolute visitor duration. Accepted staff 30-minute idle/eight-hour absolute limits are unchanged; no new timeout, credential mechanism or permission was introduced.
- **D076-F02 resolved:** security spec `:47,50–52,250` acknowledges the later 26-input visitor control-definition and eight-input privacy recommendation reviews while retaining concrete credential/store/fencing, complete-process accessibility, policy adoption, legal clearance and actual enforcement holds. The earlier feature PASS expressly does not cover D-076. Content spec `specs/004-design-services-content/spec.md:46–47` acknowledges the later eight-input recommendation PASS without adopting periods or exact operational/legal mappings. `docs/phase-1-architecture/contracts/PUBLICATION_CONTRACT.md:931` now acknowledges the separate thirteen-input definition/schema-seam PASS at its frozen inputs, labels the later reference outside those inputs and retains semantic exclusion, legal/contact verification, actual enforcement and acceptance holds.

### Complete diff and preservation evidence

The three saved patches were inspected, and full initial-to-correction snapshot differences were independently derived. Security spec has six replacement blocks: initial lines 47–48 to corrected 47; 51 to 50; 81 to 80; 144 to 143; 237 to 236; and 251 to 250. Content spec changes only line 46. Publication contract changes only line 931. All other source content and the seventeen unchanged inputs are preserved. The diffs are limited to session-scope clarification and review-reference/status qualification; duration, permissions, substantive visitor activity/End behavior, retention, disclosure, synthetic quarantine, alias ownership and approved identity/private-AI routes remain unchanged.

| Saved correction patch | SHA-256 |
| --- | --- |
| 001-platform-security-hardening-spec.md.patch | ab1aec22fdfe3065804ac950594c9a05f32a3f66f298684b68d0dfe5e80b2795 |
| 004-design-services-content-spec.md.patch | 2d9728e8497327b981038ba9b39b635876d82ae3b071230d85df6418c4e8a5be |
| contracts-PUBLICATION_CONTRACT.md.patch | 34951128068b2934fe3d816f37c494e168e56f30948edcc002d9ddc44574fdbd |

No prose/runtime/schema tests, controller/model probes, compiler/build/browser runs or external checks/calls were performed. Read-only hash/byte comparison and diff inspection establish artifact identity and the bounded correction scope only. No review of the whole earlier feature definitions, legal merits of the privacy policy or production enforcement was repeated.

Concrete mechanisms and record/purpose/policy/copy/provider bindings, legal clearance, operational contacts, stolen-valid-proof exposure, actual auth/session/publication/deletion behavior, complete-process accessibility, runtime evidence, full graph and feature/integrated/founder acceptance remain held. The initial finding was a definition ambiguity, not an observed runtime defect; this correction PASS supplies no runtime fix evidence, implementation permission or release readiness.

Only this append was authored in the preservation slice. The initial receipt prefix, initial/correction snapshots, feature/contract/checklist sources, other canonical/state documents, code/models, external systems, Git history and goal remain untouched. DOING/uncommitted remains; neither PASS nor one completed correction cycle implies DONE, whole-feature acceptance or launch readiness.

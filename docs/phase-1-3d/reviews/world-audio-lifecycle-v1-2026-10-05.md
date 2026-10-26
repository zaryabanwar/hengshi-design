# World audio lifecycle and ownership — bounded independent review

Date: 2026-10-05. Reviewer: independent Codex review agent, separate from the proposal producer.
Verdict: **PASS** for the new audio lifecycle/ownership proposal and its review-coverage notice only. No actionable finding remains within this bounded definition review. This is not founder acceptance, implementation permission or runtime certification.

## Scope and authority

Reviewed `WORLD_EXPERIENCE.md:237–411`, the review-coverage notice at lines 7–19, and the date change against the preserved predecessor. The comparison contains only that date update, the notice extension and the new audio subsection; the preceding World definition and later build contract remain unchanged. Existing sound/release clauses are context, not newly certified inputs.

Read the root `AGENTS.md`, constitution, `PROJECT.md`, `DECISIONS.md`, `PROJECT_STATE.yaml`, `TASKS.md` and `docs/software-definition/README.md`. Applied current founder/governance authority, F3D-12/13, the campus loading/residency contract, browser-resource security proposal, accepted brand sound principles and media/recovery obligations. The feature specification remains proposed; its requirements trace to the controlling upstream decisions and definitions, rather than supplying new approval.

This is the first completed bounded review receipt for this audio proposal. The coordinator reports two earlier interrupted reviewer sessions that produced no receipt or verdict; neither is a REVISE cycle. D-071's accepted composition and its three consumed model revision cycles are unchanged. The visual walkthrough is outside these inputs and was not reviewed here.

## Exact inspected inputs

Manifest: `output/research/world-audio-lifecycle-2026-10-05/review-inputs.json`, SHA256 `1c27d8c5a5446f05d86542fef707ba9c4baabd9f8b2ffe1725fd22f63d72cd62`.

Independently recomputed SHA256 and byte length for all nine entries before review; every value matched. The current World and frozen reviewed copy are identical. Hash/length checks establish artifact identity only.

| Input path | Bytes | SHA256 |
|---|---:|---|
| `docs/phase-1-3d/WORLD_EXPERIENCE.md` | 31724 | `cc84b06883a91e3d1d79dbeb0586854d5cba6c27314bdef028cfde0f6a015801` |
| `output/research/world-audio-lifecycle-2026-10-05/WORLD_EXPERIENCE.reviewed.md` | 31724 | `cc84b06883a91e3d1d79dbeb0586854d5cba6c27314bdef028cfde0f6a015801` |
| `output/research/world-audio-lifecycle-2026-10-05/WORLD_EXPERIENCE.pre-audio-lifecycle.md` | 18238 | `77987ae5ee1c0f31f0252e30ea8ff38403d82ae2ed6ff21abe3a549413512d84` |
| `output/research/world-audio-lifecycle-2026-10-05/source-receipt.json` | 2190 | `401a784aff46f2a06620f666dc8c946636601f1df760181e42fc7ee61fda340f` |
| `docs/phase-1-3d/CAMPUS_ASSET_BUILD_SPEC.md` | 41027 | `6bd0c2e95df6d227a34c0611e4c957501b1c368cd4f6d460f42b530559d0b228` |
| `docs/phase-1-architecture/contracts/SECURITY_PRIVACY_CONTRACT.md` | 24722 | `74ab420b5bec9f0aad72f59178f4ea7c626bd14edfa9d4ba02f3aa1dd0a1a254` |
| `specs/003-3d-experience-completion/spec.md` | 25605 | `2aceefa18e51bd11a450d79b2c75d0a2f3a0783baac785de12e56956fa03d4f9` |
| `docs/phase-1-brand-identity/06-motion-sound-and-3d.md` | 4872 | `df6de88bed6afe56b1d4a8f78b1839815f4215886f0176e0bec32137f305ca61` |
| `docs/phase-1-ux-architecture/STATES_AND_RECOVERY.md` | 22804 | `3c723eeaf583cd5e5ba79b147e3af1fd0d764efa3097cf708d269f41cdd79ba6` |

## Findings and bounded checks

No actionable correction is required for the reviewed proposal. The following are definition-coherence findings, not observations of implemented behavior.

| Boundary | Finding and evidence |
|---|---|
| Intent versus browser state | PASS. World lines 248–280 keep intent, eligibility and engine state independent; a new document stays silent despite restored preferences. Playback additionally requires unmuted nonzero gain, visible active World, eligible ready assets, current attempt and usable context. Unrelated movement, booking or browser heuristics cannot opt in. This preserves F3D-12/13 and the brand's informed-choice rule. |
| Pending starts, mute and visibility | PASS. World lines 266–275 and 308–313 fence delayed resume/fetch/decode work, suppress new work on mute/zero/hidden/Exit and recheck the gate after settlement. Browser interruption does not mandate a nonportable enum or retry loop. Same-document restoration retains intent without authorizing hidden or withdrawn playback. |
| Human media and process lineage | PASS. World lines 259–262 keep separately consented speech/human media outside the ambience bus. Exit/failure cannot indiscriminately close another owner's media or alter handoff/booking lineage; this agrees with F3D scenario 15 and campus lines 469–497. Existing media alternatives and activation holds in `STATES_AND_RECOVERY.md:84` remain binding, including applicable audio description. |
| Context and source ownership | PASS. World lines 284–306 specify coordinator/lease ownership, no per-room contexts or duplicate effect setup, one-shot source retirement, and attempt-specific `ended` cleanup. Bus silence does not depend on suspending another owner's shared context; close completion and retained references are separately accounted for. Three's global context is explicitly identified as a sharing hazard, not assumed to be World-local. |
| Draining work and finite capacity | PASS. World lines 308–313 and 341–354 inherit campus lines 365–371, 427–450 and 460–467: cancellation cannot release non-cancellable work's reservation early, stale completion cannot admit sound, shared/cached owners remain charged, and missing finite limits hold admission. This is a coherent proposal to prevent abort/retry or pending close/resume from hiding unbounded work. Actual enforcement is unproven. |
| Zone changes and crossfades | PASS. World lines 317–331 bind sound to admitted destinations, eligibility and reviewed boundary hysteresis. Turns, prefetch and tile reloads do not choose rooms. Complete overlap must fit; obsolete gain automation is replaced on reversals. Mute, visibility, withdrawal and other gates override fades. No physically simulated occlusion or universal fade formula is claimed. |
| Release identity and resource admission | PASS. World lines 273–275 and 333–349 bind exact bytes, eligible release, provenance, zone use and format/sample/loop metadata to existing publication/asset authority. Unknown eligibility is silent; a tail cannot continue withdrawn presentation. Visitor/AI strings cannot supply arbitrary media/decoder URLs. Browser resource policy remains independently required. |
| Optional delivery and failure parity | PASS. World lines 266–268, 337–339 and 351–357 forbid optional transfer/decode/scheduling before enablement and eager page/World preloads or precaches. Existing in-flight work still drains under reservations. Audio has lower priority than safety and essential journeys; budget/failure cannot evict supporting collision, change graphics stream or substitute an unapproved track. No new telemetry, microphone, provider audio transfer or retention authority is created. |
| Review and acceptance precision | PASS. World lines 7–19 and 359–411 separate prior hashes, this proposal, source observations and future boundary proof. No new package, codec, sound asset, numeric profile, preference store or implementation is selected. D-071 appearance/composition authority and the full Phase 1 gate are preserved. |

## Independent primary-source check

Reopened the cited primary/reference pages on 2026-10-05. These limited observations agree with the proposal; the ownership, consent and safety requirements themselves are Hengshi recommendations derived from project authority.

- [W3C Web Audio 1.0 Recommendation](https://www.w3.org/TR/webaudio-1.0/) supports graph/gain automation and one-shot source starts. Its AudioBuffer/sample definitions support channels × frames × four-byte exposed float payload accounting; that formula excludes implementation overhead, copies and other owners. The standard does not certify this product or its browser matrix.
- [Chrome autoplay guidance](https://developer.chrome.com/blog/autoplay/) describes activation and suspended/resumed contexts. It supplies no product opt-in or universal browser permission guarantee; the proposal deliberately applies stricter intent gates.
- [MDN Page Visibility](https://developer.mozilla.org/en-US/docs/Web/API/Page_Visibility_API) distinguishes hidden-document state from focus/blur; [context state](https://developer.mozilla.org/en-US/docs/Web/API/BaseAudioContext/state) describes operational state and interruption differences, not speaker audibility or visitor consent.
- [MDN buffer decoding](https://developer.mozilla.org/en-US/docs/Web/API/BaseAudioContext/decodeAudioData) requires complete file data and resamples to context rate. Its documented signature supplies no transfer-abort cancellation guarantee for an already-started decode. [Context closure](https://developer.mozilla.org/en-US/docs/Web/API/AudioContext/close) separately describes creation-blocking system resources, promise completion and still-retained objects. [Buffer sources](https://developer.mozilla.org/en-US/docs/Web/API/AudioBufferSourceNode) confirm new sources are required for another playback while buffers may be reused.
- [Three Audio](https://threejs.org/docs/pages/Audio.html) documents playback/source controls; [Three AudioContext](https://threejs.org/docs/pages/AudioContext.html) documents a global native context. Current online documentation does not establish exact package/archive behavior or source-to-binary identity. The frozen producer receipt records Context7 library ID `/websites/threejs` and its ownership/control query; this review did not independently replay that Context7 query.
- [MDN AudioSession](https://developer.mozilla.org/en-US/docs/Web/API/AudioSession) remains marked experimental and limited availability. It is excluded from production requirements here.

## Unproven obligations and next gate

- Select and reproducibly resolve/test/lock the latest mutually compatible stable graph only through its authorized compatibility process, including any Three adapter and exact browser support. These online observations do not select a release, package or wrapper configuration.
- Supply provenance/rights-cleared exact sound bytes, approved zones/loop metadata, supported codec/container/MIME evidence and conservative finite transfer/decode/context/cache/source/automation/overlap profiles. Account for resampled decoded frames and transient peaks; compressed length or the sample payload formula alone cannot prove memory safety. No numeric defaults or long-media delivery path are accepted by this review.
- Obtain the required production-screen reference and specialist/founder acceptance for accessible enable/retry/mute/volume/waiting/Exit states. Verify actual keyboard, focus, assistive-technology and applicable speech/media alternatives. The review preserves existing alternatives; it does not establish WCAG conformance.
- After implementation approval, exercise the real public controls, network/decode boundary and graph: never-enable/decline; pending resume/decode followed by mute/zero/Exit/withdrawal; stale `ended`; remounts; shared owners; pending close/resume; rapid reversals; release overlap; denial/corrupt/unsupported/over-budget assets; visibility/interruption/renderer recovery; and final cleanup. Measure actual output, reservations and prolonged-session memory on named computers and physical phones. Browser mocks, screenshots, schemas and documentation checks cannot substitute for these tests.
- Preserve authoritative eligibility and private process lineage throughout; verify no arbitrary media URLs, unsolicited microphone/provider traffic, new storage/telemetry/retention or automatic stream change. Complete integrated Phase 1 review and founder acceptance remain required before application work.

Artifact validation performed: input byte/hash reproduction and bounded predecessor comparison. Audio/browser/application runtime tests performed: **none**. Geometry, appearance, full Phase 1, visual walkthrough, exact compatibility, phone behavior and production readiness are outside this verdict. Only this receipt was written; application/source/assets/dependencies/accounts/configuration and the frozen inputs were not changed. Commits and pushes remain deferred.

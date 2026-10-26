# World measurement profile proposal review — 2026-10-06

Verdict: **REVISE — one bounded measurement-definition ambiguity.** Initial review, correction cycle 0 of the three permitted for this new 3D definition slice. Numerical target plausibility is not measured device fitness; this receipt approves no target, model, implementation, compatible graph or complete Phase 1 package.

Scope: the new `WORLD_MEASUREMENT_PROFILE.md` and only the `Numerical measurement profile proposal — 2026-10-06` appendix in `CAMPUS_ASSET_BUILD_SPEC.md`. Review follows current AGENTS, constitution, PROJECT/DECISIONS/PROJECT_STATE, software definition and TASKS authority; approved NFR-002/006/007, D-064 streams/movement and D-071 composition govern. Earlier specification and model studies were not reviewed anew.

## Exact frozen identities

Packet: `output/research/world-measurement-profile-2026-10-06/`. All identities are SHA256.

| Input | Identity |
| --- | --- |
| review-inputs.json, 98 inputs | `66f39681ce75fe268a198e5fcfda0df54ee4f663d667965586cea9a1da53bbf3` |
| protected-before.json, 78 inputs | `053bf224797d6c3afe0fd297b839fab4cabfd52f8d4b5cd96e2e17d7536fd923` |
| WORLD_MEASUREMENT_PROFILE.md reviewed/current | `01b6e8eb7085d346838a8d9877ca3b1ce1f557665e457d963cf5ea6b752a3288` |
| CAMPUS_ASSET_BUILD_SPEC.md.before | `42b0d89074b968704fa44d7ae40803ab4f5fab3f39c64a671ee75b2da66ba9e3` |
| CAMPUS_ASSET_BUILD_SPEC.md reviewed/current | `c014e2baf705bbd5c2f072557cd8eea2b9798e43ad9077ebe690d4fc6df148e2` |
| context7-three.json | `1d9204d8b040f3ff4d4056172d5c974283f2ad7e9be7ce356ca670870280eef3` |
| source-observations.json | `9fbf422b26bdc35a8a076a6058d53cbc1b9b69293000f93a5e35d4477dd51d8d` |
| webgl-best-practices.html | `50c2e29ce77d2620c91c9e3909a75dafa8feeddbdae2e407f13ee9a167424169` |
| request-animation-frame.html | `b97434d7e6cfcaac4e64c4061602712fd3c3944a7dead3419571d649a4f44315` |
| encoded-body-size.html | `7c46f08055016e2b9ce6998d371c1087ea642c1e899757282ce1c7c3f2d5467d` |
| transfer-size.html | `1c661f77156bed44132b28387d6b49e370e298f42d09ff67183a755bb3a639f4` |
| three-renderer.html | `0d6f74e9590ca30c45945fc9c3dbb315e64d8b0c8f662bbe7aaf39f46c119dc4` |

The current specification equals its reviewed snapshot, with its entire predecessor retained as an exact byte prefix (+993 bytes). The new profile equals its reviewed snapshot. All 98 packet identities and all 78 protected current identities match before and after this review. Only the authorized receipt was written; no producer, app, lock, accepted study/model or machine setting changed. This is a two-canonical-document definition slice and performs no additional D-071 composition revision.

## Required correction

**[P2] Define the frame observation population.** `WORLD_MEASUREMENT_PROFILE.md:77–83` defines frame intervals as timestamp deltas and supplies a correct nearest-rank percentile rule, but does not identify the events whose timestamps form those intervals. At a preferred 30 Hz cadence, recording every 60 Hz `requestAnimationFrame` callback can report smooth intervals while the World skips submissions or does no render work. The sustained p95 ratio and three-five-second runtime guard inherit the same ambiguity.

State which active World-frame event population is measured, how deliberate cadence skipping differs from missed/late expected World frames, and how a no-progress active window is recorded rather than passing through an empty or callback-only sample. Preserve loading/decoding/upload/control/resize stalls. Exact candidate instrumentation and representative workloads may remain held; defining the population does not require claiming GPU execution or physical presentation measurement. No application or phrase test is requested for this prose correction.

## Other bounded observations

The proposed table retains finite stream-specific frame, pixel/scale, complete-frame draw/triangle, CPU/GPU reservation, transfer/decode/GPU-work and queue ceilings. Every value, the three-cold/three-warm minimum, 30-minute traversal, 125% sustained ratio and three-five-second guard is expressly an unmeasured starting proposal requiring acceptance. Preferred 60/30 Hz cadence is not an asserted achieved rate. No source is represented as establishing these numbers.

Approved initial 8 MB/4 MB and incremental 5 MB/2.5 MB ceilings remain unchanged; decimal MB is a proposed clarification and memory uses MiB. Encoded body, headers, decoded residency, actual attempted bytes and cached bodies are separated; started-before-readiness transfers cannot escape by completing later. Incremental demand includes dependencies/prefetch and cumulative visit totals. Shared already-resident dependencies are visible in sample ownership; they must not be interpreted as a new network transfer when no body was received. Warm success cannot erase cold failure; retries/partials retain attempted accounting without certifying successful-path fit. Unknown resource-timing values require independent ledger evidence, not zero-as-pass.

Matched first/final five-minute route/camera/interaction/resource state, separately recorded shader/cache warm-up, both absolute and relative p95 limits, and unavailable status for an unmatched baseline prevent unlike-window degradation claims. Physical constrained/mainstream phones and integrated/discrete computers are coverage categories, not selected machines. Named settings, supported deliberate overrides, latest-two-release coverage and the Safari/iOS 16.4 floor remain qualification inputs. All required successful samples must pass, rather than averaging away failures.

CPU reservations include optional audio, workers/decoder state, collision and old/new overlap; GPU estimates include texture levels/layers/faces and intermediate/upload overlap. Shared owners count once, CPU images and GPU textures remain distinct, and running/draining work retains permits/reservations until known cleanup. Hidden queues and unverified zero costs are forbidden; conservative validated reservations or refusal are required. Estimates and renderer object counts are not total browser/process/driver RAM. Optional retirement cannot remove supporting ground; immediate allocation/eligibility/ground failures do not wait for the degradation window. Locked-stream recovery remains deliberate without silent tier changes or travel/audio restart.

Severe/critical OS thermal states hold qualification where exposed, exact platform labels require mapping, missing access stays unknown, and sustained performance is explicitly a proxy rather than temperature or thermal-safety proof. An unknown/failed qualification is not demonstrated suitability. Recovery and instrumentation remain proposed obligations, not executed behavior.

Saved [MDN WebGL guidance](https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API/WebGL_best_practices), [animation scheduling](https://developer.mozilla.org/en-US/docs/Web/API/Window/requestAnimationFrame), [encodedBodySize](https://developer.mozilla.org/en-US/docs/Web/API/PerformanceResourceTiming/encodedBodySize), [transferSize](https://developer.mozilla.org/en-US/docs/Web/API/PerformanceResourceTiming/transferSize), [Three WebGLRenderer reference](https://threejs.org/docs/pages/WebGLRenderer.html) and raw Context7 were inspected. They support nonportable memory estimates, pixel/query costs, callback scheduling/hidden-page pauses, cache/cross-origin size limits and WebGL renderer object/submission counters. Context7 also includes another Info API; that does not bind an installed renderer or portable total-memory probe. These are platform constraints, not numeric-target validation.

Limits: no benchmark, stress test, physical-device/tool calibration, thermal-safety test, rendering/streaming/audio implementation, final device/probe/profile/exporter/decoder binding, rights, production-screen/detail appearance, collision/ground certification, model approval, compatible graph selection or founder acceptance. Definition/measurement/appearance/physical-device and integrated Phase 1 gates remain held. Correction must address the single event-population finding without relaxing targets or reopening the accepted composition.

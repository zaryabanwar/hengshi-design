# World measurement and loading profile — v1 proposal

Status: DOING. Engineering proposal dated 2026-10-06; correction-1 independent
review passes its frozen proposal-coherence scope. Integrated review and founder
acceptance remain pending. These are initial qualification targets,
not measurements, universal browser standards or claims that the accepted study
fits them. No model, application, dependency, renderer, device or hosting changes.
The dated capability/workload amendment below is new, unreviewed material outside
that earlier correction-1 verdict; it does not inherit an independent PASS.

## Scope and authority

This completes a proposed measurement method for the existing asset/scheduler
contract and NFR-007. Retain D-064 movement/streaming, D-071 composition and the
four equivalent delivery streams. Detailed, Balanced and Simplified differ in
visual cost; all retain essential ground, destinations, boards and help/booking.
Quick Access needs no World asset download. Selection, deliberate override and
the visit's stream lock remain under the approved delivery rules.

The approved transfer ceilings stay 8 MB desktop / 4 MB mobile initially and
5 MB desktop / 2.5 MB mobile per incremental room. Proposed unit clarification:
MB means 1,000,000 bytes; memory MiB means 1,048,576 bytes. No larger binary-MB
interpretation is adopted. Device/network/browser/cache classification is recorded
for authorized tests; it does not become a new visitor fingerprint or telemetry.

## Transfer accounting and reproducible samples

Measure encoded HTTP response-body bytes separately from request/response headers,
decoded body bytes and decoded residency. Retain response encoding and exact
artifact identity; file length, gzip estimates and resource counts are not wire
measurements. Account for decoder/WASM code, model data, textures, collision,
required World scripts and any optional World audio fetched in the sample.

For a cold initial entry, count every World transfer started before the first
complete safe movement context is admitted, including work that finishes later.
Moving a request's completion after that boundary cannot hide its cost. Late
prefetch is not free: assign it to the applicable bounded incremental demand.
An incremental sample covers one requested room/connected-area demand and all
additional dependencies and background prefetch triggered by it. Attribute each
newly transferred shared body once to the demand that initiated it; record other
consumers' ownership separately. Already-resident dependencies stay visible once
in the sample's residency inventory, but add no network body bytes without a new
transfer. Report actual cached-body consumption separately from new transfer;
neither resource reuse nor cache revalidation permits fabricated zero-size data.
Also report cumulative visit transfer so repeated traversal is not masked.

Cold means a clean authorized profile with HTTP/application/decoder caches absent.
Warm means precisely identified admitted cached resources and cache policies;
report network bytes and cached bytes separately. A cached response cannot turn
an over-budget cold result into a pass. Failed/partial/retried responses are
included in actual attempted transfer totals and reported separately from the
successful-path ceiling; they cannot be dropped from the sample. Retry scenarios
retain their bounded work/memory rules and do not establish successful-path fit.

Use a controlled HTTP server/adapter byte ledger alongside browser resource timing.
Where timing hides sizes or cache accounting is ambiguous, mark the observation
unavailable and use independent served/received-byte evidence; zero is not proof.
Record desktop/mobile baseline membership explicitly before running; do not infer
it solely from viewport width. Exact named devices and network profiles remain
qualification inputs, not selected machines or hosting regions.

## Initial engineering targets

The following values are proposed starting envelopes for qualification. They
provide finite admission/work limits to test and revise, not a guarantee that a
particular phone or GPU has this capacity. They are intentionally independent of
the building image and do not replace the accepted transfer ceilings.

| Target | Detailed | Balanced | Simplified |
|---|---:|---:|---:|
| Preferred active rendering cadence | 60 Hz | 30 Hz | 30 Hz |
| Foreground active frame interval p95 / p99 | 25 / 50 ms | 40 / 80 ms | 40 / 80 ms |
| Drawing-buffer pixel ceiling | 3,000,000 | 1,500,000 | 800,000 |
| Render scale upper bound relative to CSS pixels | 2 | 1.5 | 1 |
| Submitted draw-call ceiling per complete frame | 400 | 200 | 100 |
| Submitted triangle ceiling per complete frame | 500,000 | 250,000 | 120,000 |
| Accounted peak CPU resource reservations | 320 MiB | 192 MiB | 128 MiB |
| Accounted peak GPU resource reservations | 256 MiB | 128 MiB | 64 MiB |
| Concurrent resource transfers | 4 | 3 | 2 |
| Concurrent decode/transcode work | 2 | 1 | 1 |
| Concurrent GPU preparation admission | 1 | 1 | 1 |
| Queued resource jobs, excluding already-running/draining jobs | 32 | 24 | 16 |

Cadence is a preference; actual display scheduling can differ. The observation
population is completed CPU submission cycles for a complete active World frame,
including every required render pass. Record one monotonic-clock timestamp at the
end of each such cycle; a bare requestAnimationFrame callback, React update or
individual pass is not a frame observation. This measures submission progress,
not GPU completion, physical display presentation or GPU execution duration.

Use timestamp deltas between successive complete cycles. Include the active
sample's start-to-first-cycle and last-cycle-to-end gaps in the raw observations;
the interval containing late or missed cycles is not divided into invented fast
frames. Deliberate callback skipping for a 30 Hz render cadence consequently
measures approximately 33 ms submission intervals on a 60 Hz display, rather than
counting unused 16 ms callbacks. The sample workload must require ongoing World
rendering (for example traversal/camera movement); intentional idle or pause is
identified separately and cannot certify active performance. Do not mark a stall
as idle merely because no new frame was submitted.

Percentiles use sorted interval observations and the nearest-rank rule: rank
ceil(p × n), with p 0.95/0.99. Keep cycle count, sample duration, raw intervals,
boundary-gap labels and any observation loss. Do not remove stalls caused by
loading, decode/upload, controls, board use or resize from an active sample.
A five-second active window with no complete submission is no-progress, not a
passing empty or callback-only sample; it fails qualification and is a failing
window for the degradation guard below. Missing instrumentation makes the result
unavailable, never passing. Report background/pause/reentry periods separately;
they are not fast-frame samples. The sustained comparison uses this same event
population and ongoing-workload requirement in both matched windows.

Count complete-frame submissions across shadow/water/other render passes and all
instances, not just one renderer call. Counts are additional guardrails, not
performance proof: shader cost, overdraw and driver behavior still need measurement.
Apply pixel/scale ceilings together while preserving aspect ratio and readable DOM
panels. Capability limits may require lower within-stream cost; they do not permit
an unsolicited stream switch or removal of essential interactions.

Proposed sustained-degradation ceiling: the p95 frame interval in the final five
minutes must be no more than 125% of the first five-minute active baseline and
must also meet the absolute stream threshold. Repeat the same identified route,
camera/interaction script and resource state in both windows; unlike workloads
cannot establish this ratio. Record shader/cache warm-up separately rather than
making a slower initial baseline hide degradation. Where a matched valid baseline
cannot be established, this criterion remains unavailable, not passing.

This is a performance proxy, not a temperature measurement or thermal-safety
claim. Where named-device OS tooling exposes severe/critical thermal state, such
a state holds qualification and requires investigation; map the platform's exact
labels before execution. Missing sensor/state access is reported as unknown.
Do not invent a browser temperature API or infer a cool device from stable FPS.

For the proposed runtime degradation guard, three consecutive five-second
foreground active windows above the selected stream's p95 limit hold new optional
admission and expose deliberate recovery. Immediate allocation/resource-cap,
eligibility or ground-safety failure follows its existing fail-closed rule without
waiting fifteen seconds. Any within-stream adjustment retains required content
and support; no automatic tier change or unsolicited restart of travel/audio.
Runtime observation details still need the approved candidate's implementation.

## Memory and work admission

CPU reservations include owned compressed bytes, decoded geometry/images/bitmaps,
collision data, resource metadata, worker/decoder workspaces, optional audio
buffers and transient old/new release overlap. GPU reservations include geometry,
textures with mip levels/layers/faces, shadow/render targets, intermediate buffers
and upload overlap. Shared costs count once with explicit valid owners. Decoded
CPU images and uploaded GPU textures are separate costs. Optional audio stays
inside the CPU envelope; it cannot evict current supporting ground.

These are conservative application-accounted estimates and reservations, not
portable readings of total browser RAM or actual driver allocation. Calibrate
estimates against named-device tooling and record browser/process peak separately.
Unknown costs require a validated conservative reservation or refused admission.
Do not count an unverified unknown as zero or present Three object counts as bytes.
If instrumentation cannot establish a resource class, qualification stays open.

Running and draining jobs keep permits and peak reservations until known settlement
and cleanup. The queue ceiling does not include a hidden second queue: defer
unadmitted demand under bounded visit/catalogue ownership. Dependency priority
and deduplication follow the existing scheduler; support/current ground stays
protected. Cancellation cannot instantly free non-interruptible decode capacity.
At pressure, retire eligible optional detail first, stop before an unready edge
and expose truthful retry/semantic access. Reject oversubscription rather than
claiming a safe buffer while allocating outside the envelope.

## Qualification sequence and automatic selection

Proposed test baselines are a constrained physical touch phone, a mainstream
physical touch phone, an integrated-GPU laptop and a discrete-GPU desktop.
Qualify Simplified first on the constrained baseline, Balanced on mainstream/
integrated baselines and Detailed on the higher-capacity baseline, then evaluate
all supported deliberate overrides. These are coverage categories, not a rule
that all phones receive one stream or a claim that an unnamed device fits. Name
actual hardware/OS/display/browser samples before running, retain the accepted
latest-two-release browser coverage and Safari/iOS 16.4 legacy floor, and record
unsupported configurations' equivalent semantic recovery.

After implementation authorization, exercise the actual candidate at named browser,
OS/device/display/network/cache settings. Preserve exact scene/build/profile
identities and selected stream; synthetic development fixtures cannot certify
the campus. Run at least three cold and three identified warm entry/journey samples
per baseline, then a 30-minute foreground sustained traversal. Include arrival,
reception, first eligible wing, board/help/Book, immediate reversal, repeated
eviction/reentry, release overlap and resize. Run fault/context-loss/background
scenarios separately without hiding their costs or safety outcomes.

All required successful samples must fit the applicable transfer and accounted
resource/work ceilings; active samples must fit both frame percentiles and preserve
visual/accessibility equivalence. A median passing run cannot erase a failing
run. Inspect appearance against the accepted composition and future approved
references. Browser console, context loss, resource growth and platform tooling
remain evidence; a draw-call count or emulated phone viewport is insufficient.
Record thermal-state/performance change across the sustained run where tooling
permits, without inventing an unavailable browser temperature reading.

Automatic selection evaluates approved minimal capability/workload evidence in
the browser under the existing consent/privacy and stream-selection rules. Static
WebGL limits are compatibility constraints, not measured speed or available VRAM.
Use supported, bounded capability checks and representative work after explicit
entry; no GPU vendor/device identity or server device profile is introduced here.
Detailed qualification requires demonstrated room in its measured envelope.
Unknown or failed qualification cannot be advertised as proven suitability.
Manual override still follows the accepted support checks; a locked stream's
failure offers recovery rather than changing it silently. The dated amendment
below supplies a finite workload/sampling proposal. Calibrated classification
thresholds, exact devices and implementation still require their own evidence and
adoption; no selector or fingerprinting benchmark is implemented.

## Capability samples and workload registration proposal — 2026-10-17

Status: DOING. New engineering proposal under G06, D-039/040/042/045, D-064/071
and the existing measurement/loading/traversal contracts. Independent review,
calibration and integrated founder adoption remain held; the reviewer last
reported a workspace-credits error. No model correction, application runner,
device inspection, new dependency, graphics stream, collection or benchmark run.

### Three separate decisions and evidence populations

1. **Compatibility:** the existing initial hard context ceiling and compiled
   build's actual required WebGL features determine whether World entry is
   supported. Check only needed features once at initialization, no GPU vendor/
   renderer identity or repeated blocking limit queries. A WebGL1 context cannot
   prove compatibility with a registered renderer requiring WebGL2. No automatic
   alternate renderer, CDN decoder or WebGPU fallback is selected.
2. **Runtime observation:** after explicit entry and actual current safe context,
   observe already-required completed World submission cycles, transferred bytes
   and accounted reservations. Do not create a second context, extra stress scene,
   hidden GPU benchmark, forced camera travel or synthetic successful frames.
   This population characterizes only the actually observed stream/workload.
3. **Qualification/calibration:** run the registered production scene/build/profile
   on named physical devices through the workload matrix below. Only this wider
   evidence can qualify a target stream or validate a predictive promotion rule.
   A faster Simplified sample alone is not proof of Detailed fitness.

Retain the accepted selection order: initial hard ceiling, usable
hardwareConcurrency mapping, unsignalled Simplified default, eligible prior-visit
measurement promotion, then deliberate persisted override. Unsupported/limited
deviceMemory/effectiveType/reduced-data signals do not become mandatory or select
tiers here. U-03 core-count/classification thresholds remain explicitly deferred
to implementation-phase measurements under style-guide8.2.3; no new numeric core
cutoff is invented during Phase1. The semantic first shell and explicit World
entry remain distinct from the in-force delivery stream. This amendment does not
select or implement a pre-JavaScript/initial-paint binding.

### Finite observation and temporal hysteresis candidate

Propose at most one observation attempt per visit, after explicit World entry.
The attempt has a30-second foreground wall-clock budget and uses only naturally
ongoing active work, never movement forced for measurement. It may acquire three
consecutive non-overlapping five-second active windows. Use the existing complete
submission-cycle population, boundary gaps and nearest-rank percentiles, not raw
requestAnimationFrame callbacks. Loading/decode/upload/control stalls stay in the
active sample; five seconds with active demand and no submission is failure.
An idle scene, missing instrumentation or too little active work is unavailable,
not a pass and not a reason to render pointlessly until it passes.

Cap transient interval observations at8192 and reserve at most96KiB for this
instrumentation, including interval storage, fixed metadata and accumulator work.
These are proposed admission bounds inside the selected stream's existing CPU
envelope, not extra memory outside it. An implementation must demonstrate the
reservation; unknown cost/overflow cannot drop slow observations or count as zero.
Use bounded accumulation/sorting at most once per completed five-second window.
No raw timings, hardware attributes, coordinates, scene path or per-frame history
go to analytics or persistent visitor storage. Dispose transient observations
when the attempt settles or the visit/renderer ends.

Visibility loss, context loss, renderer/release/build/profile or stream change,
resize/drawing-buffer change, observation loss and budget exhaustion invalidate
the attempt rather than stitching unlike windows together. Do not pause its
deadline, restart it automatically, catch up on wake or prolong it to fill the
buffer. A later visit under the existing visit-generation rules can obtain its
own attempt; Exit/reentry inside the same visit does not reset this attempt limit.
Existing immediate ground/resource/eligibility failures retain their immediate
recovery; do not wait for a statistical decision before preventing unsafe travel.

For positive promotion evidence propose all three valid windows at or below90%
of the selected stream's existing p95 and p99 limits, with all observed resource/
work/transfer ceilings satisfied. This leaves explicit headroom and is stricter
than ordinary qualification, not a replacement threshold. Three matching good
windows must not be assembled from disconnected bursts or a changed scene.
The existing runtime degradation guard stays three consecutive five-second
failing active windows, holding new optional admission and offering deliberate
recovery. It does not automatically change streams, restart movement/audio,
evict essential ground or mark performance failure as visitor inactivity.

### Evidence-to-next-visit mapping

A registered calibration profile must bind the observed workload/stream, public
scene/build/renderer configuration and drawing-buffer domain to explicit measured
decision bands and a proposed next-visit stream. Include all supported baseline
classes and adverse conditions below, and compare predicted recommendations with
actual target-stream qualification. Any band producing a target-stream failure
on a required sample is not qualified. Keep withheld/unknown/unrepresented bands
explicit; do not extrapolate from CPU core count, one fast frame, object counts
or nominal VRAM. A profile must have an independently reviewed conservative error
and invalid-evidence disposition before it can authorize a promotion suggestion.

No calibrated classifier/profile is supplied by this proposal. Until actual
evidence registers one, an observed successful stream can at most support that
same stream as a positive prior-visit observation; automatic prediction of a
higher unobserved stream remains held. This is a visible remaining calibration
obligation, not a replacement of the intended measured promotion feature with a
permanently restricted selector. Exact bands/thresholds remain U-03 evidence work.

The existing origin-scoped preference/last-measurement facility may hold only one
coarse resulting suggestion and its public profile identity, or an explicit known
no-promotion result, within its already-approved notice/clear/reset rules. No
raw feature vector, device label, user/visit ID, timestamps, source route/history
or server profile is added. Storage failure skips the optimization; requested
preference write failures retain their existing visible explanation. An
unavailable/incomplete attempt supplies no new measurement; a completed valid
no-promotion result is not an instruction to select below the initial base.
Changes of public profile/build invalidate incompatible evidence, not the user's
preference. Exact stored encoding/privacy review remains a registration input.

Snapshot the eligible previous measurement when the visit's stream is resolved.
New measurements are never read back to select the visit that produced them;
storage events or another tab cannot create an automatic in-session tier change.
On the next visit a supported suggestion may raise only within the hard ceiling,
never lower the hardware/default base; a stored deliberate override skips that
optimization and is evaluated last. Local storage is untrusted advice, not proof
of current device safety or object/content access: actual feature/resource/ground
guards remain mandatory. An unknown measurement cannot disable otherwise allowed
overrides or remove destinations. A locked stream failure offers explicit recovery.

### Named qualification recipes and conditions

The [six-workload matrix](qualification-workloads.csv) registers candidate recipe
identities and durations, not actual routes/camera samples. Before execution bind
each action to exact scene anchors, transforms, path/threshold and input steps;
preserve those bytes with the sample. All-around eye-level horizon, connected
ground/river/entrances and readable boards remain inspection criteria, not merely
triangle-count or overview-camera checks. Never use the protected Atlanta asset
or accepted composition study as a falsely qualified production workload.

Run the existing three cold/three identified warm samples per required baseline,
stream and eligible journey, plus the30-minute sustained run. Include all eligible
wings separately; no tested agriculture path opens held defense or another room.
Reversal/reentry timings are requested actions, not permission to cross unready
ground or fabricate completion. Record blocked/deferred attempts and all triggered
prefetch, partial/retried transfers and old/new overlap. The sustained recipe's
first/final five-minute segments must actually match resource/workload conditions;
otherwise the existing degradation ratio remains unavailable.

Proposed controlled network recipes, not runtime device classifiers or claims
about mobile service: N01=50Mbit/s down,10Mbit/s up,20ms added RTT; N02=10/2Mbit/s,
80ms added RTT; N03=1.5/0.75Mbit/s,180ms added RTT with bounded30ms jitter and1%
loss. Record shaping algorithm, whether latency is added or end-to-end, actual
server path/response timing, cache and independent byte ledger. These conditions
are unmeasured candidates and need calibration; do not label real connections by
them or use navigator.connection. Offline, response truncation, context loss,
decode/integrity failure, visibility/wake, resize and release withdrawal are
separate bounded fault recipes; do not average them away or count them as successful
path byte-fit samples. No unlimited automatic retries or artificial background FPS.

Name physical constrained-touch phone, mainstream-touch phone, integrated-GPU
laptop and discrete-GPU desktop samples before qualification. Include actual OS,
browser release, viewport/drawing buffer, display cadence, input mode and available
power/thermal observations under authorized lab recording. Preserve latest-two
stable-release coverage and the accepted Safari/iOS16.4 floor; categories and
emulation do not establish device fit. No hardware purchase or inspection of the
founder's machine is authorized by this recipe. Desktop/mobile transfer-baseline
membership must be preregistered, not inferred from CSS width.

### Profile registration before build/adoption

Require one reviewed exact association among eligible release, public HTML/client
build digest, scene descriptor, visual/collision maps, renderer/exporter/decoder/
controller profiles and this workload/calibration identity. Confirm the full
latest-mutually-compatible stable graph and actual supported browser APIs; current
docs or filenames do not select versions. Register original source/provenance,
licences/credits, metre/Y-up transforms, continuous support/barriers/clearance,
all-around horizon, appearance/control references and required dependency closures.
No descriptor index can fetch every area eagerly or select executable code.

Account code/WASM/decoders, complete rendered passes, collision preparation,
textures/targets/mips, optional audio and peak overlap under the same stream
budgets. Verify drawing-buffer dimensions and per-complete-cycle render counts;
Three geometry/texture counts are not bytes. A missing class/reservation/calibration,
copied hash without controlled build association, unsupported profile or unknown
workload result blocks the affected admission/qualification. It cannot become a
silent safe default or a relaxed budget. Retain the last eligible safe context
and equivalent semantic recovery under its existing authority.

Primary constraints refreshed2026-10-17 through Context7 `/websites/threejs` and
[Three WebGLRenderer](https://threejs.org/docs/pages/WebGLRenderer.html): multi-pass
statistics need complete-frame accounting; reported memory counts are objects,
and drawing-buffer size is physical pixels. [MDN WebGL guidance](https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API/WebGL_best_practices)
supports bounded resource estimates and avoiding blocking queries; it supplies no
portable VRAM reading or Hengshi thresholds. [Frame scheduling](https://developer.mozilla.org/en-US/docs/Web/API/Window/requestAnimationFrame),
[visibility](https://developer.mozilla.org/en-US/docs/Web/API/Page_Visibility_API),
[context loss](https://developer.mozilla.org/en-US/docs/Web/API/WebGLRenderingContext/isContextLost)
and [encoded body size](https://developer.mozilla.org/en-US/docs/Web/API/PerformanceResourceTiming/encodedBodySize)
inform observation limits, not qualification of the campus. None prescribes these
recipes/durations/bands. Full measurement, privacy/accessibility/appearance,
independent review and founder acceptance remain required; no runtime tests ran.

## Primary constraints and remaining acceptance

Checked 2026-10-06: Context7 `/websites/threejs` and the current
[Three renderer reference](https://threejs.org/docs/pages/WebGLRenderer.html)
describe draw/primitive counts and geometry/texture object counts, not total memory.
[MDN WebGL guidance](https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API/WebGL_best_practices)
explains nonportable VRAM queries, estimated budgets, pixel cost and blocking
queries. [requestAnimationFrame](https://developer.mozilla.org/en-US/docs/Web/API/Window/requestAnimationFrame)
depends on display scheduling and can pause in hidden pages. These are platform
constraints; none of the table's values or qualification durations comes from a
standard or an executed benchmark. Exact installed APIs still need the selected
compatible graph; current documentation does not select a renderer version.

The [encodedBodySize](https://developer.mozilla.org/en-US/docs/Web/API/PerformanceResourceTiming/encodedBodySize)
and [transferSize](https://developer.mozilla.org/en-US/docs/Web/API/PerformanceResourceTiming/transferSize)
references distinguish body representation size (which can include cached bodies)
from transferred response size; cross-origin exposure can hide values. Body-size
fields alone do not prove actual network transfer or supply the independent ledger.

Integrated review, founder acceptance, named devices/network/probes,
final exporter/decoder/profile binding, cost calibration, physical-device samples,
rights, controls/screens, continuous ground/collision and detailed appearance remain.
No model/collision, streaming, sound, movement, measurement runner or production
performance is implemented or certified by this document. D-071's accepted layout
and consumed model revision cycles remain untouched. Later qualification can
reject these starting envelopes; changes need their applicable review/approval,
not silent relaxation of an accepted target.

Review reference added 2026-10-06: [correction-1 independent review PASS](reviews/world-measurement-profile-v1-2026-10-06.md#correction-1-disposition--superseding-bounded-pass)
covers the corrected measurement proposal at its exact frozen inputs. The
[inspected profile](../../output/research/world-measurement-profile-2026-10-06/correction-1/WORLD_MEASUREMENT_PROFILE.md.reviewed)
is preserved; this later reference and review-status clarification are outside
those bytes. Numerical values remain
unmeasured engineering targets requiring integrated/founder acceptance, named
workloads/devices and actual qualification. No runtime or appearance proof follows.

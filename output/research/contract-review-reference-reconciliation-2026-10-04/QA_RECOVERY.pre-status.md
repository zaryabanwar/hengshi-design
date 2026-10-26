# Cross-layer QA, release and recovery definition

Status: DOING. Proposed 2026-10-04 under constitution VII, D-020/D-021/D-065,
accepted UXTEST-001–UXTEST-046 and the consolidated Phase 1 scope. No deployment,
migration, test environment provisioning or application implementation.

## Evidence and oracle

Use the [acceptance matrix](acceptance-matrix.csv) to connect responsibilities to
evidence. Approved requirements and current founder decisions are the oracle;
the protected prototype is behavior evidence, not the desired production design.
Proposed gesture or contract details need integrated acceptance before becoming
implementation expectations. A passing shape validator proves neither a truthful
claim nor accessibility, provider behavior, security or a successful release.

Reuse focused synthetic fixtures for each behavior boundary, then run affected
tests and the full relevant suite once per coherent batch. Browser inspection
must cover changed surfaces using the approved scenarios and references. Record
actual tool/runtime versions with evidence; do not select production versions
or silently substitute a different provider merely to make a test pass.

Current D-068 and the [provider scope addendum](PROVIDER_SCOPE_ADDENDUM.md)
supersede exclusive Azure hosting references. Test obligations for fencing,
unknown-effect reconciliation, drain, withdrawal and privacy-safe recovery remain
provider independent. Deployment/provider/region/SKU and cost planning are
explicitly deferred; no QA row selects hosting or requests a budget now. Later
provider evidence must prove the chosen mechanism, including external fencing or
proven terminal serialization. Approved Entra identity and the Azure Europe
personal/confidential AI route remain separate retained restrictions.

## Required test layers

### Product behavior versus artifact integrity

The founder reaffirmed behavior-based testing on 2026-10-04. Tests use approved
requirements as expected outcomes and exercise real code; they must not reproduce
the implementation to generate their own expected results. Follow the frameworks'
[Playwright best practices](https://playwright.dev/docs/best-practices) for
user-visible behavior, isolated tests and controlled third-party boundaries.
Keep a small risk-based suite rather than targeting a count of tests/checks.

Existing `scripts/validation/test-focus-backing-definition.ps1` and parts of
`test-privacy-route-definition.ps1` inspect phrases or definition coverage. These
are historical artifact guards, not accessibility or privacy behavior tests.
Do not extend exact-prose assertions for routine documentation changes. Link,
schema and necessary immutable-asset integrity checks remain separate from
product test results and cannot satisfy runtime acceptance criteria.

`scripts/validation/test_publication_manifest_schema.py` exercises the schema
validator with valid/invalid synthetic envelopes, including impossible dates.
The optional RFC3339 checker supports that local check; it is not evidence that
the application's publication boundary validates a manifest. Once implemented,
exercise that boundary with the same invalid inputs and verify rejection before
persistence or external effects. Likewise, OpenAPI security declarations do not
prove authorization, and a browser journey with a stubbed API is frontend-only
evidence until an integration journey exercises the real backend.

Do not add automated tests merely to confirm this policy's wording. Relevant
application behavior tests, integration failures and browser outcomes provide
the evidence; manual document inspection checks this policy change.

| Layer | Scope and evidence |
|---|---|
| Unit / behavior boundary | State transitions, stream precedence, consent/refusal, time-zone conversion and parsing; positive cases plus invalid inputs and boundary clocks. |
| Contract | Closed public schemas, release identity, source/citation bindings, role-denial cases, booking lineage and WebSocket replay/resume semantics once defined. |
| Integration | Real isolated PostgreSQL and approved derivative/provider adapter fixtures; idempotent intent, concurrency, missing acknowledgements, expiry and deletion. SQLite-only tests cannot prove PostgreSQL behavior. |
| Browser / semantic SEO | Complete meaningful indexable HTML before JS, correct metadata/canonicals/structured data, links, sitemap exclusions and no public draft marker. Test JS disabled and transaction scripting failures separately. |
| Accessibility / media | Keyboard, touch, pointer alternatives, screen reader, focus/400% zoom, reduced motion and meaningful media alternatives across all four streams; automated axe alone is insufficient. |
| 3D / spatial | Same campus composition in overview/arrival/department, correct service destinations, collision readiness, reversing movement, asset loss, eviction/disposal and semantic parity. Compare actual coherent model views with the selected concept. |
| Security / privacy / AI | Server authorization, self-approval denial, CSRF, session expiry/rotation, dormant-account controls, classification/provider denial, injection, redaction, consent boundaries, expiry/deletion and restore suppression. |
| Load / performance | Named phones/computers and browser versions; cold/warm loads, weak connections, frame-time percentiles, peak memory, requests and resource counts, API/WebSocket concurrency and accepted capacity targets. Cost planning remains deferred under D-068. No synthetic desktop result is a phone certification. |
| Migration / release / recovery | Backup/restore, forward/backward compatibility, fenced cutover, missing derivative, concurrent publish/rollback, delayed external effect and safe rollback to an eligible complete release. |

## Deterministic fault scenarios

Exercise failures before the external write, after provider receipt, before
acknowledgement, after durable recording and during restart/reconciliation.
Use the same operation identity across safe retries. Prove no duplicate booking,
notification or publication and no guessed confirmation after an unknown result.
The exact Graph/provider contract must establish what can be reconciled; tests
must not assume all adapters accept idempotency headers or support lookup.

For spatial streaming, vary travel and camera direction independently. Retain
required current/adjacent/recent collision-ready areas under the accepted budget;
reversals must not expose unloaded ground. Force stalled download, checksum
mismatch, corrupt asset, load cancellation and capability loss. Movement stops
safely with a truthful recovery route, while booking and entered values survive.
Do not silently change the session's accepted delivery stream to hide poor load
performance. New movement gestures remain proposed until design acceptance.

For the proposed contextual audio, inspect browser network and playback behavior
before activation and after refusal; optional sound must not download eagerly or
play. Enable sound deliberately, then cross an exterior/reception/department
boundary, reverse direction and reload/evict a nearby chunk. Verify the correct
context without duplicate loops or preference resets. Mute and volume persist;
backgrounding pauses ambience and does not latch movement. Force failed audio
fetch/decode and release withdrawal: retain a silent usable journey and truthful
help/booking state. Test real meaningful-media alternatives where that media is
actually present; do not invent speech just to satisfy a test. Final browser
activation behavior, loop/transition/resource limits and rights remain reviewed
inputs before these proposed details become implementation acceptance criteria.

The 2026-10-04 World material/asset/sound expansion adds these spatial/media
evidence obligations. This QA amendment awaits independent review; prior review
of an earlier QA hash does not cover it. No product tests were written for prose,
and this test plan does not demonstrate that movement or audio is implemented.

For publication, verify exact approved snapshot and artifact bytes, seven required
derivative kinds and all-stream coverage. Interleave generations N and N+1;
prove stale external effects cannot replace a newer release. Unknown cutover
outcomes hold further activation. Warm caches and long-lived AI/World sessions
must obey eligible release pinning and urgent withdrawal. Suppression must not
rewrite immutable bytes. Rollback cannot resurrect withdrawn rights or content.

For privacy, test consent refusal, non-consented durable-store absence, allowed
90-day expiry classes and prohibited retention extensions. Restore into an
isolated quarantine; enforce approved deletion/expiry before publishing or
serving any restored data. Unmapped provider/audit/tombstone classes keep privacy
completion pending, even when the main row was removed successfully.

## Recovery and release sequence

1. Establish the exact candidate source revision, locks, SBOM/license inventory,
   immutable artifact/container digests and pinned workflow actions. Verify
   zero-traffic candidate health without unapproved production writes.
2. Before any authorized migration, verify backup completion and restoration in
   isolation. Define backward compatibility, destructive-step gate and rollback
   feasibility; do not infer rollback from a successful forward migration.
3. Verify candidate data/derivatives, auth, publication, booking and semantic/
   immersive parity using synthetic fixtures and the acceptance matrix.
4. Obtain required independent review and applicable founder promotion approval.
   Gates are evidence, not scripted automatic approval.
5. For an authorized cutover, record durable intent, fenced generations, verified
   health/routing and definitive outcome. Unknown effects enter reconciliation.
6. If recovery is needed, select a still-eligible complete release, preserve
   durable booking/privacy decisions and verify routed identity and operation
   outcomes after restoration. An unsafe old release is not a rollback target.

Retain the accepted NFR-001–NFR-007 targets: Quick Access p75 LCP at most 2.5
seconds, INP at most 200 milliseconds and CLS at most 0.1; initial lazy 3D transfer
at most 8 MB desktop / 4 MB mobile and incremental room transfer at most 5 MB
desktop / 2.5 MB mobile; 25 concurrent visitors and three simultaneous chats;
99.9% monthly availability; RPO at most 24 hours and RTO at most eight hours.
These are unproven targets. Availability numerator/denominator/exclusions and
measurement sources, device/network/cache load profiles, backup/storage layout,
deletion-safe recovery, region and capacity are pending contracts. Device-tier
frame-time, memory and thermal thresholds still need definition, not inherited
prototype FPS values. Support the latest two stable evergreen browser releases
and the accepted Safari/iOS 16.4 legacy floor with semantic unsupported-client
recovery; reverify exact client versions before execution.
Recovery timing includes verification before serving, not only process startup.

## Gates and verdicts

Maintain TODO/DOING/BLOCKED for outstanding work; DONE also requires the applicable
commit under AGENTS.md. Evidence may say PASS for a defined check while the task
remains DOING. No credential, sign-off, provider entitlement or deployment is
inferred from tests. Failed critical behavior holds the affected promotion;
continue unrelated definition work where safe.

Before integrated Phase 1 acceptance, resolve missing interface/retention/provider
rules, approved screen/storyboard coverage, measured budget method, compatibility
and the documented boundary for deferred deployment/operating-envelope work.
Keep exact provider mechanisms as held obligations for later authorized selection;
do not reopen the founder's deferral or claim those mechanisms verified. Full
Phase 1 acceptance still requires its other definitions and reviews. Before
launch, execute the accepted strategy
against the actual candidate and named supported clients. This document supplies
the strategy, not those test results or final sign-off.

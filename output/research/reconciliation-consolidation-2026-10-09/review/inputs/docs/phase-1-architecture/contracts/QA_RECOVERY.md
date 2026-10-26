# Cross-layer QA, release and recovery definition

Status: DOING. Proposed 2026-10-04 under constitution VII, D-020/D-021/D-065,
accepted UXTEST-001–UXTEST-046 and the consolidated Phase 1 scope. No deployment,
migration, test environment provisioning or application implementation.

## Review coverage

The [later independent contract review](reviews/current-definition-amendments-2026-10-04.md)
records bounded PASS for this proposal and its acceptance-matrix amendments at
the receipt's exact hashes. The reviewed
[contract bytes](../../../output/research/contract-review-reference-reconciliation-2026-10-04/QA_RECOVERY.pre-status.md)
are preserved. Only review references were reconciled afterward; test obligations
and approved targets were not changed. This is definition coherence, not test
execution or full Phase 1 acceptance.

The [original QA feature review](../../../specs/002-testing-and-monitoring/reviews/qa-feature-v1-2026-10-04.md)
retains its historical PASS/REVISE. [D-074](../../../DECISIONS.md#d-074--one-word-qa-browser-release-correction-exception)
approved the exact browser families-to-releases repair; its separate
[corrected-input independent PASS](../../../specs/002-testing-and-monitoring/reviews/qa-browser-release-correction-v1-2026-10-06.md)
resolves QA-V1-01 at spec SHA-256
`3afdbd73217090da8980ecddad69ce1c447879f1ee00f90f1db47ee2ebb3548e`.
Do not request the settled exception again. This later reference is outside the
contract review’s frozen bytes; it changes no test obligation or target. Feature,
integrated/founder acceptance and physical-device, performance, recovery and
security runtime evidence remain separate.

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
evidence obligations. The later contract review identified above covers this
logical amendment at its listed hashes; older receipts retain their own scopes.
No product tests were written for prose, and this test plan does not demonstrate
that movement or audio is implemented.

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

## Monthly availability measurement proposal — 2026-10-08

Status: DOING. This supplies the missing NFR-004 accounting definition for the
accepted 99.9% monthly target. The following measurement choices are engineering
recommendations for independent review and integrated founder acceptance. They
are not a measured result, public SLA, hosting decision or monitoring activation.
Older receipts cover their frozen inputs only. D-068's provider/cost deferral and
the existing two-deployable boundaries remain unchanged.

### Outcomes and separate surfaces

Measure four surfaces separately; do not average them into a traffic-weighted
number that lets successful page reads hide an unavailable conversion entry.
For this proposal each surface uses the existing 99.9% target; there is no new
combined target or promise that every downstream service completes a transaction.

| Surface | Required outcome at its existing user boundary | Failure must not be hidden by |
|---|---|---|
| Public semantic site | Applicable approved routes return meaningful initial HTML, correct eligible release context and usable navigation/Contact/Book entry. Check the canonical route inventory, including a rotating representative of each indexable template family. | A process-only health response, empty SPA shell, obsolete withdrawn content, or a successful homepage alone. |
| API | Applicable eligible public and authorized private API operations produce their contract-correct outcomes. The frozen profile maps every applicable operation family from the existing interface catalogue, including qualification, consent changes, own-process status and later booking/chat/staff actions. Server admission, required durable dependencies and eligibility are actually checked where applicable. Unmeasured families keep whole-API accounting unknown. | A live worker, reachable database, generic HTTP 200, or successful reads/entry masking failed follow-up operations. |
| AI entry | An allowed visitor can reach the consent-aware, classified guidance entry and receive its correct admission/result or intentional policy refusal. Authorized ordinary guidance cannot be silently replaced by a provider-outage refusal and called fully available. | A rendered chat launcher, invented answer, or Book fallback after an outage. Report unavailable downstream generation separately as degradation as well. |
| Booking entry | Direct Book remains available without AI, preserves the approved six-field qualification plus separate purpose-specific consent and optional budget, and can admit valid permitted entry. | A visible button whose operation fails, fabricated booking confirmation, or an unrelated Contact link. |

Staff deliberately unavailable, no eligible slots, valid consent refusal and a
correct security/policy denial are normal domain outcomes when their actual
contracts require them. A dependency outage or unsafe unknown operation is an
availability failure for an otherwise valid operation even if its error message
and alternative route work. Keep correct failure handling as separate evidence.
This entry SLO does not certify email delivery, human staffing, meeting creation,
complete AI-answer quality, World frame time or every booking completion.

### Calendar accounting, uncertainty and exclusions

Use calendar months in UTC, split into fixed, non-overlapping one-minute bins.
For each surface, the denominator T includes every bin during the declared
production service period. At first launch report the partial month and its
start timestamp explicitly; never label it a full observed month. A later
release, rollback, maintenance or monitor restart cannot reset that denominator.

The frozen measurement profile identifies the finite mandatory checks, existing
boundaries, probe locations, supported client representatives, outcome predicates
and deadlines before collection. Each good bin requires affirmative, nonempty
coverage of every mandatory outcome obligation for that surface under the frozen
profile. A bin is good G only when this coverage exists, all due mandatory checks
have timely, admissible successful observations, and no admissible observed
failure contradicts them. Zero due checks, no traffic without independently
sufficient approved evidence, omitted operation families, or old successes carried
forward cannot establish G; classify these bins U. A bin is bad B when an
admissible failure is observed; otherwise incomplete, stale or contradictory
measurement is unknown U. T = G + B + U. A measured service failure takes precedence
over simultaneous missing coverage; monitor failure alone establishes U, not B.
Approved profile revisions apply prospectively and remain identified with their
bins; they cannot erase prior failures, exclude elapsed unknown time or reset T.

Report sampled availability lower bound G/T, upper bound (G+U)/T, and observation
coverage (G+B)/T together. Only the lower bound may demonstrate the 99.9% target;
unknown bins never become successful bins or disappear. This is a sampled-bin
SLI, not proof of uninterrupted service between observations. Retain the sampling
limitation with every result; incident evidence can mark additional affected bins
bad, but cannot turn previously missing coverage into assumed success.

Production maintenance, releases, overload within the accepted operating profile,
provider outages and DNS/TLS/edge failures affecting the profiled boundary stay
in the denominator. No planned-downtime or third-party exclusion is inferred.
Confirmed unsupported-client behavior and deliberate malformed/unauthorized probes
belong to separate negative tests, not mandatory success checks; they cannot be
used to relabel an ordinary valid visitor's outage as an exclusion. Pre-launch
isolated tests are not production SLO time. Out-of-profile observations must be
reported separately with their evidence, rather than used to improve the SLI.

For each surface the allowed unavailable/unknown allowance is 0.001*T bins;
consumed allowance is B+U, not failed HTTP requests or money. A 30-day full month
has 43,200 bins and an allowance of 43.2 bins: 44 non-good bins already miss the
target. These are arithmetic examples, not observed performance. Deadline and
coverage alerts distinguish service failure from monitoring failure; accounting
must expose threshold breach and projected exhaustion without silently rounding
a below-target ratio upward. Alert thresholds, recipient and automation need
separate reviewed operating bindings; this does not assign mailbox ownership.

### Measurement sources, privacy and later execution

External observations are needed for failures before the API/application boundary.
Use purpose-approved, payload-free application/adapter outcome counters to detect
failures a public-page probe cannot see. Neither server logs alone nor a reachable
health endpoint certifies these outcomes. Author the profile before execution:
select exact existing reads and, where needed, explicitly isolated synthetic
journeys with disabled live dispatch/provider writes. Local demo-data permission
never authorizes production visitor fabrication, email, meeting or human alerts.
If a required private/provider path cannot be checked under an approved safe
profile, report its bins unknown; do not declare the whole API or entry available.

Keep only necessary bounded labels: surface, approved check/profile revision,
coarse time bin, outcome category and non-personal deployment/release correlation
where safe. Do not add visitor/session IDs, email, conversation bodies, full URLs,
precise movement, IP-derived visitor histories or provider secrets to metrics.
Operational evidence follows the existing privacy/record-purpose contract; no
new retention period, public dashboard or permanent telemetry grant is created.
A profile must also identify its approved evidence store/access/cleanup binding.

Before launch, bind concrete probe/client/location/deadline/cadence execution,
privacy-safe signals and alert recipients to the eventually selected operating
setup. Prove classification at actual boundaries with site/API/entry outage,
maintenance, valid no-slot/offline/policy outcomes, low/no traffic, monitor loss,
late observations, duplicate/out-of-order samples and UTC month transitions.
Verify that retries and release changes do not erase failed bins or reset history.
No new tests assert this prose, and no monitoring/provider package is selected.

This follows the specification-versus-measurement distinction and good/total
accounting in [Google's SLO guidance](https://sre.google/workbook/implementing-slos/),
and its [monitoring guidance](https://sre.google/workbook/monitoring/) on user-impact
signals and bounded metrics. Checked 2026-10-08. The four-surface scope, calendar
bins, conservative unknown accounting and exclusion policy above are Hengshi
engineering proposals, not externally mandated defaults or previously approved
thresholds. Independent review and integrated acceptance remain required.

## Recovery clocks and safe return-to-service proposal — 2026-10-08

Status: DOING. This refines NFR-005's accepted RPO at most 24 hours and RTO at
most 8 hours into measurable outcomes. These are engineering recommendations
requiring independent review and integrated acceptance, not achieved recovery,
a public guarantee or approval to create backups, restore data or switch traffic.
R-014's reassessment of the accepted launch risk remains open. D-068 defers exact
hosting, region, storage, topology, backup service and cost choices.

### Interruption, recovered point and completion

Record UTC instants with their evidence and uncertainty; elapsed timing must
survive process/host restarts. Clock sources and offset checks belong in the
later operating profile. A displayed timestamp or successful command exit does
not prove a recovery boundary.

| Symbol | Meaning and required evidence |
|---|---|
| I | Beginning of the incident's affected service interruption or unsafe operation, supported by actual boundary evidence. Detection, operator declaration and restore-command start are separate later times; none may silently replace I. |
| R | Latest validated consistent recovery point at or before I for each in-scope durable authority. Prove complete recoverable committed meaning through that boundary using the approved recovery method. A backup file's creation/completion timestamp or one newest row cannot establish R. |
| V | Time each affected required service boundary passes the frozen recovery profile after restore/reconciliation, security/privacy verification and actual routing/admission verification. Report per-boundary results. |
| F | Completion time only when every affected required boundary has current, admissible passing evidence under the frozen recovery profile. An earlier V invalidated by regression, expiry, incompatible state or missing current coverage cannot contribute a completed boundary. Reverify it without resetting I. A started process, public homepage, database connection or completed file restore cannot establish F by itself. |

Measured data-loss exposure is max(0,I-R) for each durable authority; report the
worst in-scope value against 24 hours, without averaging good stores over missing
ones. Validate compatible release artifacts and required transaction/intent
history together; unresolved holes or mismatched authorities make R unproven.
The exposure window is not a count of rows actually lost, nor permission to lose
mandatory privacy or authorization decisions. Record any established lost
committed work separately without copying private payloads into evidence.

Measured recovery duration is F-I, compared with 8 hours. Include detection,
response, restore, rebuilding, outcome reconciliation, security/privacy checks
and verified return to service. Waiting for a provider or human authorization
does not pause this clock. A failed attempt followed by another attempt retains
the original I; neither a new incident ticket nor a rollback resets it.

If I is established only within an evidence-supported interval [a,b], calculate
RTO conservatively from the earliest plausible interruption: F-a, or the latest
credible F bound minus a when completion time is also uncertain. For RPO use the
latest plausible interruption and earliest validated recovery-point bound: b-R,
or b-c for a recovery point supported in [c,d]. Record these conservative upper
bounds and their uncertainty separately. The chosen consistent recovery point
must be demonstrably before the actual interruption; timestamp ambiguity that
cannot establish this ordering or complete coverage keeps RPO unproven. Do not
choose favourable correlated clock readings or fabricate a point from an alert.
For example, I between October 8 00:00 and 02:00 with a validated R at October 7
01:00 gives possible exposure of 23 to 25 hours. Report the 25-hour upper bound, which
fails 24 hours; the earliest I cannot justify a 23-hour pass. This is arithmetic,
not measured project recovery. Unbounded interruption, unknown recovered coverage,
missing current passing evidence or unreliable time correlation cannot produce
a passing result. Separate measured results, estimated bounds and unproven
targets. These are duration rules, not a new incident SLA.

The frozen profile defines admissibility/freshness and compatible recovered-state
coverage at F. Earlier passing evidence does not survive a known regression,
expired validity or an incompatible state change. All affected required boundaries
must have current valid passing coverage together at F; no simultaneous-probe
timestamp or arbitrary new soak duration is inferred. For example, A passing at
hour 2 then failing at 3 and B passing at 6 leaves recovery incomplete until A is
reverified and all required evidence is current. Original I still anchors duration.

### Recovery scope and non-negotiable safety

The frozen recovery profile maps the accepted product's affected critical user
and staff boundaries to the existing API/site contracts and artifact inventory.
It includes their dependencies and required durable-authority coverage; a
subset cannot certify full recovery. Correctly permitted domain states such as
no slots, staff unavailable or pending reconciliation remain distinguishable
from an unavailable underlying service. Report any accepted degraded operation
explicitly; Contact fallback or semantic-only delivery cannot silently certify
full restoration of an affected required boundary.

- Restore only into an approved isolated quarantine initially. Prevent restored
  workers, timers, adapters and stale deployments from dispatching, renewing
  credentials, publishing or serving private data before their current authority
  is verified. Isolation and cutover fencing must be proven by the later selected
  mechanism; a naming convention or stopped local process is insufficient.
- Recover authoritative PostgreSQL records, compatible immutable artifacts and
  necessary safe operation evidence as a coherent set. Rebuild Redis/cache/search
  and other derivatives from eligible current authority. A restored derivative
  or immutable checksum does not select an active release or revive withdrawn
  material. Missing assets or incompatible schema/locks keep the affected path held.
- Apply approved deletion, expiry, consent withdrawal, release withdrawal and
  access revocation before serving restored content. Prove that the recovery
  profile has current necessary decisions, not merely the old backup's decisions.
  The 24-hour loss tolerance never authorizes deleted data or revoked access to
  reappear. If current suppression/authority cannot be established, deny the
  affected serving/processing and leave its recovery incomplete.
- Preserve original retention and credential/activity deadlines. Neither restored
  timestamps nor recreated IDs reset them. Ephemeral non-consented conversations,
  disposable derived projections and deliberately deleted data are not missing
  durable history that recovery may reconstruct. Report authorized access loss
  truthfully; do not resurrect old proofs or recreate an owner from email/name.
- Preserve scoped operation identity and known external-effect uncertainty across
  retries. Reconcile with approved authoritative provider evidence before a write
  may be repeated or confirmation changed. A restored database lacking a later
  provider acknowledgement cannot prove that no meeting/alert/calendar effect
  happened. Unknown remains pending; recovery cannot invent success or cancellation.
- Existing uncertain individual operations can remain truthfully pending after
  service recovery only if their fencing, authorized status, reconciliation and
  nonduplication safeguards work. This does not excuse a continuing dependency
  outage, missing intent history or unavailable required API operation. Report
  affected lineages separately from recovered service, without exposing them in
  public metrics or declaring every business operation resolved.

These conditions do not demand restoration of expired personal content to improve
RPO, grant new legal retention, purchase a backup service, choose a storage design
or give an operator publication/access authority. Necessary evidence retention,
suppression binding and actual restore capability remain separate approved inputs.

### Evidence and later drills

Before an authorized drill, freeze the scenario, exact starting release/source/
locks, permitted isolated target, covered authorities and operation families,
known synthetic committed sequence, protected privacy/security decisions, clock
method and required success checks. Include corruption, missing backups/logs,
partial restores, provider acknowledgement loss, late old workers, revoked grants,
expired/deleted content, unavailable derivatives and incompatible rollback assets.
Use supported PostgreSQL recovery and actual eligible artifact/adapter boundaries;
mocked stores or a restored file alone cannot prove recoverable application state.

Record minimal safe timestamps/sequence coverage, result categories, selected
artifact identities, missing/reconciled work and each verified boundary. Do not
retain raw tokens, transcript/email/body copies or fabricated personal fixtures
in operational evidence. Its store/access/cleanup follow approved purpose bindings.
An isolated synthetic drill proves that scenario only; it is not a production
incident or proof of every provider, data size, client, geography or outage class.

Later acceptance must bind exact backup/log coverage and retention, corruption
handling, recovery credentials/keys, current suppression sources, authoritative
provider reconciliation, fenced routing and complete measurement evidence to the
selected operating setup. If that setup cannot satisfy a target, record the
measured gap and R-014 risk for a founder decision; never silently weaken 24 hours,
8 hours, privacy, consent or confirmation integrity to make a drill pass.
No product tests are added to assert this text. No restore or live fault was run.

[NIST SP 800-34 Rev. 1](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-34r1.pdf)
sections 3.2.1 and 4.4, checked 2026-10-08, distinguish recovery-point/time objectives
and recovered-data/functionality validation. They do not prescribe Hengshi's
numbers or require a particular cloud. The I/R/V/F accounting and safeguards above
are project engineering proposals under the existing contracts, not a claim of
NIST certification, legal clearance or achieved recovery. Earlier independent
receipts retain their exact reviewed-input identities; this addition needs review.

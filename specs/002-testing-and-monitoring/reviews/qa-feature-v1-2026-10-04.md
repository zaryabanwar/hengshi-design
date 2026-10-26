# Independent QA/recovery feature review — v1

Date: 2026-10-04. Task status: DOING; commits remain deferred.
Reviewer: nonproducer QA/recovery reviewer commissioned for this bounded scope.
Verdict: **PASS for the inspected feature-definition proposal**.
Actionable findings: Critical 0 / High 0 / Medium 0 / Low 0.
This verdict is not founder acceptance, planning/implementation authorization,
an executed test result, measurement certification or full Phase 1 acceptance.

## Exact reviewed identities

The following SHA-256 values were independently recomputed and match the
commissioned inputs. The producer's two revision cycles are exhausted; no
producer artifact was edited and no third revision was introduced.

| Artifact | SHA-256 |
|---|---|
| [Feature specification](../spec.md) | `1CCEE505C8FEC6B2CEBFC56F9B0DD5A751F57F40EBC11733AD45BC63EAA17AB3` |
| [Producer checklist](../checklists/requirements.md) | `B06BB9CAD8D8ED57C3177123078E55986A183A0EC796A6346C3C0A42A933F8C1` |

Canonical QA input identities also independently match their entries in the
[current-definition amendment review](../../../docs/phase-1-architecture/contracts/reviews/current-definition-amendments-2026-10-04.md):

| Canonical input | SHA-256 |
|---|---|
| [QA_RECOVERY.md](../../../docs/phase-1-architecture/contracts/QA_RECOVERY.md) | `BFD5DE6F37891B38A007D73432E28AFC8D29526EDC43761FC1B1A8FC3288D8C0` |
| [acceptance-matrix.csv](../../../docs/phase-1-architecture/contracts/acceptance-matrix.csv) | `DF3EDD4CB6E2AAD2AF8F6320070312975172350675BA80710A7713E43AFFF8DE` |

## Authority and subject coverage

Applied AGENTS.md, constitution VI–VIII and its authority order, PROJECT.md,
DECISIONS.md, PROJECT_STATE.yaml, TASKS.md and the software-definition entry point.
The accepted foundation remains accepted under D-025; later D-064–D-070 control
their affected scope. Canonical detailed contracts and this feature remain
proposals despite bounded independent review. Source targets below were inspected
directly; previous review verdicts were not substituted for this feature review.

| Canonical subject | Feature binding and scenarios | Source inspected and conclusion |
|---|---|---|
| QA-SEMANTIC | FQA-04; 6–7; SEO section | Foundation SEO-001–013 and QA_RECOVERY:67–68; meaningful no-JS HTML, transaction failures, eligible SEO derivatives and manual accessibility remain required. |
| QA-STREAM | FQA-04; 6–7 | Acceptance matrix:3 and CONTENT_ANALYTICS_TESTS.md:152–165; accepted Apply/precedence and independent stream predicates are referenced, preserving both boundary directions and permitted process state. |
| QA-SPATIAL | FQA-05; 8, 5, 10 | Matrix:4 and WORLD_EXPERIENCE.md:95–181,214–230; same-model three-view evidence, collision-ready ground, reversal, cancellation, resource ownership and eligible refresh remain runtime obligations. |
| QA-AUDIO | FQA-05; 9 | Matrix:5, QA_RECOVERY:91–101 and World:183–212; optional activation/fetch policy, context, mute/volume, failure/withdrawal and silent alternatives are inherited, with no simulated human activity. |
| QA-PUBLICATION | FQA-06; 2–5,12 | PUBLICATION_CONTRACT.md:51–179; preparation/eligibility, stale generations, unknown cutover, withdrawal, warm caches and eligible rollback require authoritative actual-boundary proof. |
| QA-IDENTITY | FQA-07; 3,19 | Matrix:7, SEC-001–010 and SECURITY_PRIVACY_CONTRACT.md:24–99,174–179; server role/object/purpose denial and session/CSRF cases are bound to the canonical identity obligations, including held dormant-account mechanisms. |
| QA-PRIVACY | FQA-07; 12–13,19 | DATA_CONTRACT.md:62–80,176–196 and DATA-003–009; no hidden durable transcript, class-specific expiry/deletion, unchanged clocks and quarantined restore are preserved. |
| QA-AI | FQA-07; 14–15 | AI-001–009 and security contract:101–124; permitted source-bound answers, unsupported/injected refusal, prohibited/unknown classification denial and required-route outage are explicit. Vendor agreement proof remains separate. |
| QA-BOOKING | FQA-08; 4,16 | Foundation FR-004–007/019, FLOWS.md BF-01 and INTERFACE_CATALOG.md:218–244; six qualification fields plus separate consent, optional budget, current challenge, owner/slot/DST and reconciled confirmation are preserved. |
| QA-HANDOFF | FQA-08; 4,17 | FR-009–011, FLOWS.md AF-02/SOF-01 and interface contract:151–159,195–216; stale/unknown availability, ineligible assignment, consent refusal and honest recovery are covered. Alert delivery does not establish human acceptance. |
| QA-PERFORMANCE | FQA-09–10; 10–11 | NFR-001–007, QA_RECOVERY:139–151 and spec:108–158; approved numerical targets are unchanged, while profile/SLI/device acceptance inputs remain held. |
| QA-RECOVERY | FQA-09; 4,12 | NFR-005, QA_RECOVERY:121–151 and data/security restore obligations; isolated verification, retained suppression, private operation reconciliation and eligible complete release are required before serving. |

## Findings and evidence limits

No actionable contradiction was found in the commissioned definition scope.

- Spec:60–70,93–104,218–225 separates independently approved oracles, actual
  behavior boundaries and fixture scope. Schema rejection cannot pass an
  application that still accepts the input. Check counts, mocked browser journeys,
  OpenAPI declarations and protected prototype results do not certify enforcement.
- Spec:79–85,229–234,254–257 retains uncertainty across fault/retry/restart,
  publication concurrency and privacy-safe recovery. Exact external fencing,
  serialization, lookup/deduplication and recovery mechanisms are held; a mock is
  not proof that a provider supports them. The canonical publication/data/interface
  contracts remain the detailed source targets rather than newly invented routes.
- Scenarios 14–19 provide both permitted controls and denial/failure cases for
  AI grounding/routing, booking and handoff, real test-target isolation, sessions,
  retention and restore. Spec:291–297 stops effects against unverified/shared
  targets; SQLite or mocked success cannot pass PostgreSQL integration. This
  specification grants no database, fault, load or external-operation permission.
- Spec:169–191,298–304 keeps consent purpose-specific and versioned through the
  canonical data/process contracts. Chat expiry is not applied indiscriminately
  to booking, provider, consent-proof, audit or suppression records. Diagnostic
  evidence cannot become a movement history, fingerprint or transcript copy.
- Spec:121–158 proposes a measurement method without selecting limits or claiming
  observations. It distinguishes physical/emulated execution, payload/transport,
  manifest attribution and early prefetch, frame distributions versus callback FPS,
  heap/process/resources versus estimated GPU allocation, and sustained behavior
  versus phone thermal proof. Raw bytes and MB/MiB preserve the held accounting
  interpretation instead of relaxing the existing caps.

External statements were rechecked read-only on 2026-10-04 using Context7 resolve
and query for `/microsoft/playwright.dev` plus the
[official Playwright emulation page](https://playwright.dev/docs/emulation).
It describes simulated browser/device parameters; the conclusion that a host
viewport run does not measure a physical phone's GPU or thermals is an inference
about that evidence boundary, not a vendor phone-certification claim.
[Chrome's official frame reference](https://developer.chrome.com/docs/devtools/performance/reference)
supports the available frame-category distinction. The
[W3C Resource Timing text](https://www.w3.org/TR/resource-timing/)
supports encoded/decoded/transfer distinctions and restricted readings. Its
current document is a Candidate Recommendation Draft, and its transfer getter
can use a privacy-preserving header constant; it is not proof of exact transport
octets or a selected production API/tool compatibility graph. The feature holds
accounting and actual-client instrumentation review, so this source limitation
does not create an unsupported benchmark or relax a cap.

Independent read-only CIM discovery confirms i3-1115G4, Intel UHD Graphics,
Windows 11 Home and approximately 19.8 GiB physical RAM, consistent with
spec:153–156. Browser, renderer, performance, power and thermal behavior were
not measured; this host remains only an available lab candidate.

## Held inputs and disposition

Numerical NFR-007 limits; named physical phones and supported-client evidence;
profiles, sample/measurement/transfer accounting; SLI numerator/denominator,
exclusions and breach rules; RPO/RTO anchors; exact identity, consent/retention,
diagnostic policy and isolated environment approval; external contracts and
recovery/suppression mechanisms remain held. These prevent affected execution
or readiness verdicts, not this bounded definition-quality PASS. Operational
privacy/security alias ownership remains explicitly undecided.

D-068 hosting/cost planning stays deferred with Azure/AWS candidates. Outlook/Teams
intent remains without a blanket Microsoft 365 prerequisite; Entra identity and
approved Azure Europe personal/confidential AI routing are retained. No provider,
owner, numeric threshold, fixture runner, instrumentation or operational grant
was introduced. The checklist accurately leaves exact inputs, review/approval
and implementation readiness pending at its reviewed hash; this report does not
silently edit its historical producer assertions.

Only this review file was written. No application test suite, browser journey,
load test, restoration or monitoring system was executed, and no configuration,
installation, account/credential/resource change, commit, push, deployment or
external message occurred. Further material producer revisions require a founder
decision under the exhausted two-cycle rule. Integrated acceptance and specialist
runtime accessibility/SEO/security/performance evidence remain separate gates.

## 2026-10-04 addendum — browser-release coverage correction

Current bounded verdict: **REVISE**, superseding the original PASS for the two
unchanged commissioned hashes above. The original receipt is retained as history.
Current actionable findings: Critical 0 / High 0 / Medium 1 / Low 0.

**QA-V1-01 — Medium: browser families replace the accepted release coverage.**
[spec.md](../spec.md):117, FQA-N06, says "Latest two stable evergreen families".
The accepted [foundation requirement](../../../docs/phase-1-foundation/01-product-requirements.md):254,
NFR-006, requires the latest two stable evergreen **releases**; the canonical
[QA/recovery contract](../../../docs/phase-1-architecture/contracts/QA_RECOVERY.md):148–150
retains that release requirement and dated exact-client verification. Counting
two browser families does not require testing both supported release generations
and can reduce the supported browser matrix. FQA-N06's exact-version verification
column does not restore the omitted release count. This is an actionable source
conflict, not an ordinary prose preference. The original reviewer missed it;
the original no-finding and preserved-browser-target conclusions are superseded
in this affected scope.

Required correction: replace the single word `families` with `releases` in
FQA-N06's measurable target. Preserve the Safari/iOS 16.4 floor, WCAG target,
dated exact-client evidence and all other commissioned requirements. No new
browser family, version, threshold or external test is selected by this finding.

Both commissioned hashes were independently recomputed again before this addendum
and remain unchanged. Neither producer file was edited. The QA producer's two
revision cycles remain exhausted: this report does not authorize a third cycle,
waive that limit or record founder acceptance. Obtain the applicable founder
decision before the affected producer correction, then review its exact new
identity. Other original scope limits and held inputs remain in force; no runtime
tests, configuration, external action, commit or push occurred for this addendum.

## Correction disposition — 2026-10-06

D-074 authorises the exact one-word repair, now applied. The separate
[corrected-input independent re-review](qa-browser-release-correction-v1-2026-10-06.md)
records bounded PASS and resolves QA-V1-01 at the corrected spec/checklist hashes.
This later reference lies outside the original reviewed bytes. Original PASS,
REVISE and exhausted-cycle history above remain preserved; no additional revision,
feature/integrated/founder acceptance or runtime/implementation permission follows.

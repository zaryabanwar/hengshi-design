# Accessibility Audit — UX Architecture Iteration 2

**Audit date:** 2026-07-20  
**Reviewer:** independent `hengshi-accessibility-reviewer` contract  
**Producer iteration:** 2 of maximum 3  
**Audit type:** definition-level verification; no implementation conformance claim  
**Target:** WCAG 2.2 Level AA and approved Hengshi accessible-journey requirements  
**Verdict:** REVISE

## Independence and boundary

The reviewer did not produce or revise the iteration-2 UX package. Producer and
authority artifacts, the iteration-1 design review, and the iteration-1
accessibility audit were inspected read-only. The only write under this contract
is this report. No UI, application, 3D, state, decision, task, risk, manual action,
dependency, data, infrastructure, Git, external service, or publication state was
changed.

This pass verifies definition obligations. It does not assert conformance of any
screen, HTML, browser, assistive technology, media, WebGL experience, form,
third-party provider, integration, or release.

## Frozen scope and integrity

The producer scope is 12 files: the prior 11 producer files plus
`wayfinding-release-map.csv`. Files under `reviews/**` and `accessibility/**` are
excluded from the producer index.

The canonical producer index was recomputed before the verdict using the supplied
serialization: sort by full path; serialize uppercase file SHA-256, two ASCII
spaces, and workspace-relative forward-slash path; join with LF and no terminal
newline; hash the UTF-8 bytes.

- Expected producer SHA-256: `8A454D5BBA909C43CF8701522A20D48514F666143C731B3841E7E97443C3C5FB`
- Actual producer SHA-256: `8A454D5BBA909C43CF8701522A20D48514F666143C731B3841E7E97443C3C5FB`
- Result: exact match; 12 files
- Iteration-1 accessibility-audit expected SHA-256:
  `DCF4F36F8A9C1F9FAD4E6F7E2E65B4EF09C30CBAA2267A64FDD28624C01F2D34`
- Iteration-1 accessibility-audit actual SHA-256:
  `DCF4F36F8A9C1F9FAD4E6F7E2E65B4EF09C30CBAA2267A64FDD28624C01F2D34`
- Result: prior report unchanged

This report is under the excluded `accessibility/**` path and does not alter the
frozen producer index.

## Standard, contexts, and method

The audit applied the W3C Recommendation, [Web Content Accessibility Guidelines
(WCAG) 2.2](https://www.w3.org/TR/WCAG22/), at Level AA; accepted UX-001 through
UX-011 and related FR/AI/DATA/NFR controls; D-025/D-026/D-035; the semantic Quick
Access and optional-World authority; and the supported-browser/assistive contexts
recorded in iteration 1.

Methods:

1. Read the iteration-1 accessibility report completely and inspected the
   overlapping no-JavaScript finding in the independent design review.
2. Read the revised producer package, iteration-2 inspection/validation records,
   wayfinding map, action contracts, test hypotheses, and traceability rows.
3. Recomputed both required hashes.
4. Reran the extended validator read-only. Result: `106 PASS / 0 FAIL`, with 33
   routes, nine exclusions, 15 wayfinding entries, 53 actions, 45 tests, and 123
   trace rows.
5. Manually verified each A11Y-I1 finding in its normative flow and recovery
   context rather than treating phrase assertions as proof.
6. Checked all route/exclusion records for nonempty semantic representation,
   primary actions, and recovery; manually sampled public, immersive, AI/handoff,
   booking, content/trust, and staff paths for regression.
7. Compared the revised prerecorded-media branch directly with WCAG 2.2 success
   criteria 1.2.3 and 1.2.5.

No automated accessibility scanner was applicable because there is no rendered
implementation. Deterministic validation is supporting evidence, not conformance
proof.

## Finding verification

### A11Y-I1-01 — Pointer and touch requirements

**Prior severity:** MEDIUM  
**Status:** CLOSED  
**WCAG 2.2:** 2.5.2, 2.5.3, 2.5.7, 2.5.8  
**Evidence:** `UX_ARCHITECTURE.md:286-292`,
`STATES_AND_RECOVERY.md:136-145`, `CONTENT_ANALYTICS_TESTS.md:141`

The revised contract applies to navigation, search, HUD, consent, AI/handoff,
booking, media, and staff controls. It requires pointer-up activation or equivalent
abort/undo, move-away cancellation, visible label text within the accessible name,
a single-pointer non-drag control plus keyboard equivalent, and a 24 by 24 CSS
pixel target or a specifically recorded WCAG exception/spacing measurement.
UXTEST-039 exercises the same obligations. The prior implementation ambiguity is
closed without inventing a product accommodation.

**Later implementation acceptance:** Measure every representative control family
at 100% zoom; verify any exception calculation; compare visible and accessible
names; cancel before pointer-up; and complete all drag tasks through non-drag and
keyboard alternatives.

### A11Y-I1-02 — Motion and time safeguards

**Prior severity:** MEDIUM  
**Status:** CLOSED  
**WCAG 2.2:** 2.2.1, 2.2.2, 2.3.1  
**Evidence:** `UX_ARCHITECTURE.md:293-301`,
`STATES_AND_RECOVERY.md:128-154`, `CONTENT_ANALYTICS_TESTS.md:142`

The revised definition covers standard and reduced-motion states. Automatic
moving, blinking, scrolling, or updating content over five seconds requires a
keyboard/screen-reader pause, stop, or hide control unless a valid exception is
documented. It caps flashes at three per second. Every user time limit is
removable/adjustable, or provides at least 20 seconds warning and a simple
extension at least ten times, or records a valid exception. Expiry preserves
permitted entered data and authoritative state and offers accessible
reauthentication. Exact security values remain correctly gated rather than
accessibility behavior being conditional.

**Later implementation acceptance:** Inventory and operate automatic updates in
standard/reduced modes, run flash analysis across all states, and use controlled
clocks to verify adjustment/warning/extension or the documented exception plus
state preservation and reauthentication.

### A11Y-I1-03 — Media alternatives

**Prior severity:** MEDIUM  
**Status:** OPEN — partially corrected  
**WCAG 2.2:** 1.2.2, 1.2.3, 1.2.4, 1.2.5  
**Evidence:** `UX_ARCHITECTURE.md:277-282`, `FLOWS.md:81-86`,
`STATES_AND_RECOVERY.md:84`, `CONTENT_ANALYTICS_TESTS.md:143`,
`traceability.csv:122`

Audio-only transcripts, prerecorded captions, live captions, media holding, and
semantic fallback are now correctly distinguished. The remaining branch says
prerecorded synchronized media may use “audio description **or** a complete media
alternative” for meaningful visuals, and UXTEST-041 accepts the same alternative.

That disjunction satisfies the Level-A choice in [SC 1.2.3](https://www.w3.org/TR/WCAG22/#audio-description-or-media-alternative-prerecorded),
subject to its stated exception. It does not fully specify [SC 1.2.5](https://www.w3.org/TR/WCAG22/#audio-description-prerecorded),
which at Level AA requires audio description for prerecorded video content in
synchronized media. A complete media alternative is not the general Level-AA
substitute for audio description. The current definition could therefore permit
publication of an applicable prerecorded synchronized video with a text/media
alternative but no audio description while still passing UXTEST-041.

**User impact:** Blind and low-vision users may be forced out of the synchronized
media experience and can miss time-aligned visual actions, demonstrations,
speaker/status cues, or spatial changes that Level-AA audio description must
convey.

**Required correction:** Separate the criteria. Require prerecorded captions and
the applicable SC 1.2.3 audio-description/media-alternative behavior, and require
SC 1.2.5 audio description for all applicable prerecorded video content in
synchronized media at the AA target. A complete media alternative may supplement
that obligation or satisfy SC 1.2.3 where applicable, but must not be stated as a
general replacement for SC 1.2.5. If no audio description is required for a
specific item because there is no uncommunicated visual information or another
standards-supported applicability determination is made, the inventory must record
that evidence. Missing required audio description continues to hold media only,
without blocking semantic content, text help, or Book.

**Acceptance test:** For every prerecorded synchronized media item, record whether
it contains video content and meaningful visual information; verify accurate
captions for audio; verify audio description conveys every meaningful visual cue
in time with the media for SC 1.2.5; separately verify any complete media
alternative used for SC 1.2.3. The test must fail if an applicable item has only a
complete media alternative but lacks required audio description. Verify missing
requirements hold media activation/publication while the semantic journey remains.

### A11Y-I1-04 — Input purpose, redundant entry, and accessible authentication

**Prior severity:** MEDIUM  
**Status:** CLOSED  
**WCAG 2.2:** 1.3.5, 3.3.2, 3.3.4, 3.3.7, 3.3.8  
**Evidence:** `FLOWS.md:137-149,165-173,211-215`,
`STATES_AND_RECOVERY.md:116-132`, `CONTENT_ANALYTICS_TESTS.md:144-145`

Applicable input purposes are mapped without inventing tokens: email=`email`,
organization=`organization`, and job-title role=`organization-title`; domain
controls remain explicitly labeled. Already supplied qualification, correction,
review, reschedule/cancel, contact, and staff values are auto-populated or
selectable unless a documented 3.3.7 exception applies. Booking verification and
staff authentication/reauthentication allow paste, password managers, assistive
mechanisms, or an equivalent accessible method and forbid an unaided cognitive
test. Third-party process steps remain within the conformance scope. Provider
selection stays correctly gated.

**Later implementation acceptance:** Inspect autocomplete semantics; complete all
re-entry scenarios without redundant input; and complete booking/staff
authentication using paste, password-manager, and applicable assistive paths while
preserving authoritative state across timeout and reauthentication.

### A11Y-I1-05 — No-JavaScript booking claim

**Prior severity:** MEDIUM  
**Status:** CLOSED  
**WCAG 2.2:** conformance requirements 5.2.2-5.2.4; related 3.3.1-3.3.4 and 4.1.3  
**Evidence:** `UX_ARCHITECTURE.md:5-17`, J-01,
`STATES_AND_RECOVERY.md:37,156-163`,
`CONTENT_ANALYTICS_TESTS.md:146`, `traceability.csv:116,124`

The package now consistently limits the approved before-JavaScript guarantee to
complete initial semantic content and direct Book access. It separately requires
the complete booking transaction to be accessible and non-WebGL, while deferring
the exact transactional progressive-enhancement architecture and explicitly
stating that end-to-end completion without JavaScript is not approved. Script
failure reports unavailable/not completed and cannot infer lineage, challenge,
write, pending, or confirmation. This aligns with the iteration-1 design finding
and introduces no unapproved architecture requirement.

**Later implementation acceptance:** Disable JavaScript on representative
indexable routes and verify complete initial content and direct semantic Book
access; simulate transaction-script failure and verify truthful non-completion,
safe context preservation, retry/verified Contact, and no false booking state;
then test the full accessible non-WebGL transaction with its approved scripting
architecture.

## Regression and representative-flow result

| Area | Evidence | Result |
|---|---|---|
| 33 canonical routes | 33/33; semantic representation and primary action cells nonempty; route IDs/paths match authority | No regression found |
| Nine exclusions | 9/9; safe recovery cells nonempty; defense/draft/search/admin remain fail closed | No regression found |
| Wayfinding/release | 15 unique wing/service entries, exact accessible titles, unique rooms/routes, closed/held/opening/open behavior | No accessibility regression found |
| Quick Access/World | Same release/checksum, canonical links, persistent Quick Access/Book/Exit, non-WebGL recovery | No regression found |
| Keyboard/focus/status/forms | Global order, focus move/return, error-summary focus, live/status text, truthful pending/error | No regression found at definition level |
| Reflow/contrast/forced colors | 320 CSS px, 400% zoom, text spacing, table alternatives, non-color state labels, accepted identity contrast obligations | No regression found at definition level |
| AI/handoff/booking | Sources/refusal, explicit availability, text fallback, exact qualification, one lineage, idempotency/reconciliation | No regression found |
| Staff SOF-01A–M / ACT-41–53 | Availability, triage, conversation, alert, assignment, booking, review, knowledge, audit; role negatives and recovery | No regression found |
| Media | Captions/live/holding improved, but SC 1.2.5 branch remains incomplete | Open A11Y-I1-03 |

## New findings

No new CRITICAL, HIGH, MEDIUM, or LOW finding was identified. The only unresolved
barrier is the partially corrected iteration-1 finding A11Y-I1-03.

## Severity summary and gate

| Severity | Unresolved count |
|---|---:|
| CRITICAL | 0 |
| HIGH | 0 |
| MEDIUM | 1 |
| LOW | 0 |

PASS requires all five iteration-1 findings closed and zero unresolved CRITICAL,
HIGH, or MEDIUM finding. The evidence is available, so BLOCKED is not appropriate.
A11Y-I1-03 remains MEDIUM; therefore the verdict is REVISE.

The producer has one remaining audit/fix cycle under the maximum of three. Any
conformance exception, risk acceptance, target change, product-level accommodation,
or final founder approval remains a human decision. The existing manual gates may
remain; none substitutes for the media criterion correction.

## Limitations

- No approved Figma/Stitch screen, rendered build, running URL, or final media
  inventory exists.
- No browser, Safari/iOS, screen-reader, keyboard, touch-device, zoom/reflow,
  forced-colors, contrast, flash, controlled-clock, audio-description, captions,
  or live-media behavior was tested.
- The validator proves selected document invariants and integrity, not accessibility
  or WCAG conformance.
- Exact content, providers, consent/legal wording, people, media rights, time-limit
  values, and integrations remain later gates.
- Later design and implementation must undergo fresh automated and manual checks;
  automated scans alone will not establish conformance.

**Verdict:** REVISE

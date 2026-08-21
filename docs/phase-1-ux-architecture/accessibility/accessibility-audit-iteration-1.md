# Accessibility Audit — UX Architecture Iteration 1

**Audit date:** 2026-07-20  
**Reviewer:** independent `hengshi-accessibility-reviewer` contract  
**Producer iteration:** 1 of maximum 3  
**Audit type:** definition-level accessibility audit; no implementation conformance claim  
**Target:** WCAG 2.2 Level AA and the approved Hengshi accessible-journey requirements  
**Verdict:** REVISE

## Independence and boundary

The reviewer did not produce or edit the 11 frozen producer artifacts. The only
write made under this contract is this report. No product source, design, UI, 3D,
root state, task, decision, risk, manual-action, dependency, data, infrastructure,
Git, external service, or publication state was changed.

This audit asks whether the UX definition is complete enough to guide later design
and implementation without inventing accessibility accommodations. It does not
claim that any UI, HTML, browser, assistive technology, WebGL experience, media,
form, integration, or production release conforms.

## Frozen scope and integrity

The reviewed producer scope is the following 11 files:

1. `README.md`
2. `UX_ARCHITECTURE.md`
3. `FLOWS.md`
4. `STATES_AND_RECOVERY.md`
5. `CONTENT_ANALYTICS_TESTS.md`
6. `route-room-parity.csv`
7. `excluded-surfaces.csv`
8. `traceability.csv`
9. `producer-inspection.md`
10. `validation/validate-ux-architecture.ps1`
11. `validation/validation-report.md`

The canonical package index was recomputed before the verdict by sorting the 11
files by full path, serializing each uppercase SHA-256 plus two spaces plus its
workspace-relative forward-slash path, joining with LF and no terminal newline,
then hashing the UTF-8 bytes.

- Expected SHA-256: `1B44551DDB3004228159582C9234C6AE5F4E6763A2357C1C3F345F9376CA6D0A`
- Actual SHA-256: `1B44551DDB3004228159582C9234C6AE5F4E6763A2357C1C3F345F9376CA6D0A`
- Result: exact match; 11 files

This report is under the excluded `accessibility/` reviewer path, so its creation
does not alter that frozen producer index.

## Authority and tested contexts

The audit applied `AGENTS.md`, Constitution 2.0.0, `PROJECT.md`,
`PROJECT_STATE.yaml`, `TASKS.md`, `DECISIONS.md`, `RISKS.md`,
`MANUAL_ACTIONS.md`, the software-definition boundary, accepted foundation
requirements, D-025/D-026/D-035, the accepted brand accessibility implications,
and CR-001 closure. D-025 controls and `/industries` remains retained.

The definition was evaluated for the latest two stable evergreen browsers with
Safari/iOS 16.4 as the later implementation floor; keyboard-only and screen-reader
use; 200% text resize, 400% zoom and 320 CSS px reflow; text spacing; forced colors
and grayscale; reduced motion; low power; non-WebGL and unsupported browsers;
offline, network, asset, AI/provider, Graph, Redis and session failures; pointer
and touch; captions and media alternatives; and meaningful semantic discovery
without JavaScript.

The standard reference is the W3C Recommendation, [Web Content Accessibility
Guidelines (WCAG) 2.2](https://www.w3.org/TR/WCAG22/). Conformance must cover full
pages and complete processes, including third-party steps relied on by the process.

## Method and evidence

1. Read the authority and all 11 frozen producer files.
2. Recomputed the canonical package hash and checked all 33 routes, nine excluded
   classes, 40 action contracts, and 30 UX test hypotheses.
3. Reran the producer validator read-only. Result: `52 PASS / 0 FAIL`, 33 routes,
   nine exclusions, 40 actions, 30 tests, and 114 trace rows.
4. Manually traced J-01 through J-05, FV-01, RV-01, AF-01, AF-02, BF-01,
   DF-01, PF-01, CF-01, all action/error/recovery rows, and staff permission/session
   branches against applicable WCAG 2.2 AA criteria.
5. Searched the package for explicit touch-size, pointer-cancellation, dragging,
   timeout, pause/stop/hide, flashing, media-description, input-purpose,
   redundant-entry, and accessible-authentication obligations. The reported gaps
   were manually confirmed in context; absence from a text search alone was not
   treated as proof.

The deterministic validator supports completeness and integrity evidence but does
not test WCAG conformance. No automated accessibility scanner was run because no
rendered implementation exists.

## Coverage result

| Area / journey | Definition evidence | Result |
|---|---|---|
| 33 canonical routes and nine exclusions | Complete semantic representation, actions, gates, recovery; no canvas-only route | Pass at definition level |
| Quick Access and optional World | Shared release/checksum, canonical links, persistent Quick Access/Book/Exit, WebGL/asset/offline escape | Pass at definition level |
| Keyboard, focus, names/roles/states/status/errors | Global operability and reading-order rules; focus move/return; live/status intent; linked error summaries; UXTEST-021/022 | Pass with finding A11Y-I1-01 affecting pointer-specific criteria |
| Reflow, zoom, text spacing, responsive order | 320 CSS px, 400% zoom, text spacing, table alternatives, focus/content not obscured | Pass at definition level; implementation evidence deferred |
| Contrast, forced colors and sensory equivalence | Accepted identity contrast obligations; text/redundant state labels; forced-colors/grayscale requirements | Pass at definition level; final combinations require implementation testing |
| Motion, animation and time | Reduced-motion stable states and skip behavior are defined | Revise — A11Y-I1-02 |
| Forms, errors, booking and recovery | Required/optional labels, linked summaries, preserved values, idempotent lineage and truthful pending/error states | Revise — A11Y-I1-04 |
| AI and human handoff | AI identity/sources/refusal, consent boundary, explicit staff availability, text fallback, direct Book | Pass at definition level; product/legal/provider gates remain visible |
| Media | Audio off, explicit media opt-in, captions/transcripts and text fallback | Revise — A11Y-I1-03 |
| Staff author/reviewer/founder/admin | Role separation, server denial, session/error recovery, stale-candidate protection | Revise — A11Y-I1-04 |
| No-JavaScript semantic path | Complete initial route content and links are required | Revise — A11Y-I1-05 for the stronger no-JS booking-completion claim |
| Content and non-text loss | Formal labels, limitations, source order, honest empty states, unavailable images/font/no-CSS-image hypothesis | Pass at definition level; final alt/complex-graphic decisions remain implementation/content gates |

## Findings

### A11Y-I1-01 — Pointer and touch requirements are not testable enough

**Severity:** MEDIUM  
**WCAG 2.2 references:** 2.5.2 Pointer Cancellation (A), 2.5.3 Label in Name (A),
2.5.7 Dragging Movements (AA), 2.5.8 Target Size (Minimum) (AA)  
**Affected flows:** primary/mobile navigation, directory/search, immersive HUD and
point-and-click destinations, consent, AI/handoff, booking, media, and staff actions  
**Exact locations:** `UX_ARCHITECTURE.md:250-251`, `FLOWS.md:188-204`,
`CONTENT_ANALYTICS_TESTS.md:118-122`

**Evidence/reproduction:** Read the touch/pointer rule and UXTEST-021. They require
accessible names and keyboard equivalence, but do not require a minimum 24 by 24
CSS pixel target or qualifying spacing/exception, visible-label text to be
contained in the accessible name, cancellation/undo behavior for pointer
activation, or a non-drag alternative if later controls use dragging. A producer
could therefore satisfy the current tests with undersized or down-event-only
controls.

**User impact:** People with limited dexterity, tremor, low vision, or touch-only
input may activate the wrong control, be unable to cancel an accidental action,
or encounter a gesture with no practical alternative.

**Required revision:** Add a normative cross-surface pointer contract and an
acceptance hypothesis covering target size/spacing and WCAG exceptions, up-event
or equivalent cancellation, label-in-name, and a single-pointer non-drag
alternative. This is a standards implementation obligation, not a new product
accommodation.

**Acceptance test:** On representative compact and full layouts for every control
family, measure each pointer target at 100% CSS pixels and verify it is at least
24 by 24 CSS pixels or satisfies a recorded WCAG exception/spacing calculation;
compare visible labels to accessible names; cancel or move away before pointer-up
without triggering the action; and complete every dragging action using a
non-drag single-pointer control. Keyboard parity must still pass.

### A11Y-I1-02 — Motion and time controls omit standard-mode safeguards

**Severity:** MEDIUM  
**WCAG 2.2 references:** 2.2.1 Timing Adjustable (A), 2.2.2 Pause, Stop, Hide (A),
2.3.1 Three Flashes or Below Threshold (A); related approved UX-004/NFR-008  
**Affected flows:** first-visit arrival, ambient/room animation, AI/session states,
booking challenge and staff session expiry  
**Exact locations:** `UX_ARCHITECTURE.md:243-247`,
`STATES_AND_RECOVERY.md:102-103`, `CONTENT_ANALYTICS_TESTS.md:122`

**Evidence/reproduction:** The package correctly defines a stable reduced-motion
path, but it does not constrain standard-mode moving, blinking, scrolling, or
auto-updating content that starts automatically and lasts more than five seconds;
it contains no flash-threshold rule. Session warning is conditional on whether a
later security design supports it, and no timing-adjustment/extension or recorded
WCAG exception contract is supplied. Reduced motion does not replace these AA
requirements for users in standard mode.

**User impact:** Motion or flashing can prevent safe use or trigger physical
reactions; users who need more time may lose form, booking, AI, or staff work
without a usable warning/extension or preserved-state reauthentication path.

**Required revision:** Define pause/stop/hide behavior for applicable automatic
motion or updates, prohibit content that exceeds the flash threshold, and require
each user time limit to be adjustable/warned or explicitly mapped to a valid WCAG
exception while preserving entered data and authoritative state. Security policy
may set exact challenge/session limits, but cannot leave accessibility behavior
conditional.

**Acceptance test:** In standard and reduced-motion modes, inventory every
automatic animation/update over five seconds and verify a keyboard/screen-reader
operable pause, stop, or hide control unless an applicable exception is documented;
run a flash analysis showing no content exceeds three flashes in any one-second
period; and use controlled clocks to verify each timeout is adjustable with at
least the required warning/extension opportunity or has a documented WCAG
exception, with safe data preservation and reauthentication.

### A11Y-I1-03 — Media alternatives do not cover meaningful visual information

**Severity:** MEDIUM  
**WCAG 2.2 references:** 1.2.2 Captions (Prerecorded) (A), 1.2.3 Audio Description
or Media Alternative (Prerecorded) (A), 1.2.4 Captions (Live) (AA), 1.2.5 Audio
Description (Prerecorded) (AA)  
**Affected flows:** optional World media, service/demo/insight media, and opt-in
human voice/video  
**Exact locations:** `UX_ARCHITECTURE.md:245-246`,
`FLOWS.md:54-56`, `STATES_AND_RECOVERY.md:36,71`,
`CONTENT_ANALYTICS_TESTS.md:122`

**Evidence/reproduction:** The package requires captions/transcripts and a text
fallback, which covers spoken/audio information, but it never requires audio
description or an equivalent media alternative for meaningful visual information
in prerecorded video. It also does not distinguish prerecorded captions from live
caption obligations for synchronized live media.

**User impact:** Blind and low-vision visitors can miss actions, demonstrations,
spatial changes, speaker identification, or other visual-only meaning even when a
speech transcript exists; deaf users may lack captions if live video is offered.

**Required revision:** Extend the media content and publication contract so every
meaningful prerecorded visual has audio description at AA or an approved complete
alternative that satisfies the applicable criterion, and live synchronized media
has captions when offered. Media without its required alternative remains held;
text and booking remain available.

**Acceptance test:** For each representative audio-only, prerecorded video, and
live video type, build a media-alternative inventory and manually compare all
spoken and visual information, speaker/status cues, and actions against captions,
transcript/media alternative, audio description, and live captions as applicable.
No meaningful item may be available only visually or aurally; missing alternatives
must block publication/media activation without blocking the semantic journey.

### A11Y-I1-04 — Input, repeated-entry, and authentication obligations are incomplete

**Severity:** MEDIUM  
**WCAG 2.2 references:** 1.3.5 Identify Input Purpose (AA), 3.3.7 Redundant Entry
(A), 3.3.8 Accessible Authentication (Minimum) (AA); also 3.3.2 Labels or
Instructions (A) and 3.3.4 Error Prevention (Legal, Financial, Data) (AA)  
**Affected flows:** BF-01 qualification, verification, review, reschedule/cancel;
PF-01 staff sign-in/reauthentication; any consent/contact form  
**Exact locations:** `FLOWS.md:123-181,252-268`,
`STATES_AND_RECOVERY.md:37-50,93-103`,
`CONTENT_ANALYTICS_TESTS.md:105-113,118-122`

**Evidence/reproduction:** The package defines strong labels, errors, value
preservation, and booking review, but does not map applicable personal-data fields
to programmatic input-purpose tokens; require previously entered information to
be auto-populated or selectable rather than re-entered across the same process;
or require authentication methods that avoid an unaided cognitive-function test.
The email challenge mechanism is intentionally unselected, and Entra/break-glass
reauthentication is referenced without a copy/paste, password-manager, passkey,
magic-link, or other accessible-authentication obligation. Third-party steps used
by the complete process cannot be treated as outside the later conformance scope.

**User impact:** People with cognitive, memory, reading, motor, or learning
disabilities may have to remember/transcribe codes, repeat data, or identify input
purpose manually, and can be excluded from booking recovery or staff work.

**Required revision:** Define programmatic input-purpose behavior for applicable
fields; forbid redundant re-entry within a process unless an allowed exception
applies; and require booking and staff authentication/reauthentication to satisfy
3.3.8, including support for assistive mechanisms and paste/password-manager or
equivalent operation. Exact provider and challenge choices remain MA-006/security
decisions; the accessibility acceptance boundary does not select one.

**Acceptance test:** Inspect rendered input semantics and verify applicable WCAG
autocomplete tokens; complete qualification, email correction, review,
reschedule/cancel, session expiry, and staff reauthentication while previously
entered information is auto-populated or selectable unless an exception is
recorded; and complete each authentication path without memorizing or transcribing
a code/puzzle, using paste or an approved assistive mechanism. Verify review,
correction, and confirmation remain available before data-changing submissions.

### A11Y-I1-05 — The no-JavaScript booking claim has no complete-process contract

**Severity:** MEDIUM  
**WCAG 2.2 references:** conformance requirements 5.2.2 Full Pages, 5.2.3 Complete
Processes, and 5.2.4 Only Accessibility-Supported Ways of Using Technologies;
related WCAG 2.2 AA criteria 3.3.1-3.3.4 and 4.1.3  
**Affected flows:** J-01 and BF-01 from semantic `/book` through qualification,
email ownership, availability, submission, reconciliation, and recovery  
**Exact locations:** `UX_ARCHITECTURE.md:5-9,125-136`,
`FLOWS.md:96-181`, `CONTENT_ANALYTICS_TESTS.md:86-89,105-113`

**Evidence/reproduction:** The experience thesis states that a visitor can
complete a verified booking through semantic HTML without JavaScript. UXTEST-001
checks complete initial content and Book links with JS/canvas disabled, while
UXTEST-004 checks that Book is reachable. Neither test completes BF-01 without JS,
and no server-round-trip focus, validation, pending-status, back/refresh,
idempotency, or recovery behavior is defined for that mode. Thus the stronger
package claim can pass the current test suite without being specified.

**User impact:** A visitor relying on the semantic/non-script path may reach the
booking page but be unable to finish, understand errors/pending truth, or recover,
contradicting the promised equivalent conversion path.

**Required revision:** Either add a no-JavaScript progressive-enhancement contract
for the complete booking process, including semantic server responses and all
existing error/recovery obligations, or narrow the thesis only through the
applicable founder/product gate. The reviewer does not choose between those
product-level alternatives.

**Acceptance test:** With JavaScript disabled, start from representative routes
and complete the approved BF-01 process against a test double through validation,
email verification, slot selection, durable pending, reconciliation, and confirmed
state. Verify headings, focus target after each response, associated errors,
status text, preserved safe values, back/refresh, duplicate submission, provider
ambiguity, and direct recovery. If the founder narrows the claim instead, approved
authority, journeys, parity statements, and tests must consistently define the
remaining semantic process with no false completion claim.

## Severity summary and gate

| Severity | Count |
|---|---:|
| CRITICAL | 0 |
| HIGH | 0 |
| MEDIUM | 5 |
| LOW | 0 |

PASS requires zero unresolved CRITICAL, HIGH, or MEDIUM findings. The package is
auditable and evidence is available, so BLOCKED is not appropriate. All five
findings are definition gaps that must return to the producer for revision and a
fresh independent audit pass.

The existing MA-002/003/004/005/006/007/008/009/010/011/013 gates can remain. They
do not excuse a missing fail-closed accessibility contract. Human approval is
required for a conformance exception, risk acceptance, target change, or a choice
between product-level accommodations, including whether to retain or narrow the
explicit no-JavaScript booking-completion promise.

## Limitations and future evidence

- No approved Figma/Stitch screen, rendered build, running URL, or final public
  copy exists in scope.
- No browser, Safari/iOS, screen-reader, keyboard, touch-device, zoom/reflow,
  forced-colors, contrast, motion, media, or performance conformance test could be
  run. Those remain mandatory later gates, not reasons to mark this audit BLOCKED.
- No axe/Lighthouse result can establish implementation conformance here.
- Exact consent/legal wording, people, media rights, providers, time limits,
  retention mappings, and production integrations remain human/specialist gates.
- The review assesses the documented obligations, not whether future producers
  will implement them correctly.

**Verdict:** REVISE

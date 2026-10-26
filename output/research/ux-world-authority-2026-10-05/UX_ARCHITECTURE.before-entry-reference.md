# UX Architecture

## 1. Experience thesis

**[APPROVED]** A qualified buyer can understand fit, inspect truthful evidence,
get optional AI or human help, and reach direct Book access from complete initial
semantic HTML before JavaScript. The complete booking process has an equivalent
accessible non-WebGL flow and requires no audio, account, upload, or prior chat.
The optional campus may improve orientation and memorability but never changes
content authority, evidence status, limitations, or conversion access.

**[PROPOSED UX]** The exact transactional progressive-enhancement architecture is
deferred to later technical architecture and UI design. End-to-end transaction
completion without JavaScript is not an approved requirement. If scripting fails,
the semantic route must retain meaningful booking context, a truthful unavailable
status, and Book/Contact/retry choices; it must not claim qualification, submission,
pending acceptance, or confirmation that did not authoritatively occur.

**[PROPOSED UX]** Every public entry exposes three stable choices: explore the
relevant decision content, open the searchable directory, or book. Optional AI,
human help, and `/world` are adjacent assistance/exploration choices, not gates.

## 2. Actors, evidenced goals, and jobs

| Actor | Authority/evidence | Goal | Job statement status |
|---|---|---|---|
| Global English-speaking mid-market/enterprise buyer | BR-002, D-005 | Evaluate service/sector fit and book discovery | **[HYPOTHESIS]** “Help me decide whether Hengshi fits my outcome without making me learn the site or disclose too much.” No interview evidence exists. |
| Agriculture decision-maker | BR-003, route strategy | Evaluate relevant service intersections without invented sector history | **[HYPOTHESIS]** Validate through sector interviews and named reviewer evidence. |
| Mining decision-maker | BR-003, route strategy | Evaluate operational fit and trust before sensitive disclosure | **[HYPOTHESIS]** Validate through sector interviews and legal/security-reviewed content. |
| Trust/technical evaluator | route and conversion foundation | Inspect evidence, experts, privacy/security/AI posture, and limitations | **[HYPOTHESIS]** Validate proof/trust path before treating it as buyer fact. |
| Visitor uncertain about fit | FR-005, FR-008–FR-010 | Ask bounded questions or reach a person while retaining direct booking | **[HYPOTHESIS]** Compare direct and assisted paths without preferring one. |
| Returning visitor | FR-013 | Resume a non-sensitive location or choose Reception, Replay, Quick Access | **[PROPOSED UX]** Local preference only; no identity/account inference. |
| Live staff / room owner / backup | FR-006, FR-009, FR-010 | Receive a consented handoff or reconciled booking | **[APPROVED]** Availability must be explicit; named assignments are **[UNRESOLVED GATE]** MA-003/MA-006. |
| Author | PUB-002, PUB-003 | Draft content with evidence/provenance and submit review | **[APPROVED]** Cannot approve own material. |
| Evidence/SEO reviewer | PUB-002, SEC-001 | Review claims, evidence, rights, discoverability, and completeness | **[PROPOSED UX]** Review queue behavior; exact role membership is MA-006. |
| Founder approver | PUB-002, SEC-001 | Approve/reject a release candidate after specialist review | **[APPROVED]** Founder approval is separate; no self-approval. |
| Administrator | SEC-001, FR-016 | Manage governed assignments/configuration without publishing authority by implication | **[APPROVED]** Server-side authorization; exact privileges await architecture/security contracts. |
| Privacy/security owner | DATA-004–DATA-010, SEC-009 | Minimize collection and verify retention/deletion/refusal | **[HYPOTHESIS]** Named owner and legal mappings remain MA-002. |

No detailed persona names, biographies, quotes, device ownership, organization
sizes, pain-point frequencies, budgets, or response expectations are claimed.

## 3. Experience objects and source-of-truth rules

| Object | Meaning | UX-visible states | Authority rule |
|---|---|---|---|
| Publication release | One immutable public truth set | active; prior-active; candidate/nonpublic; unavailable | Only active approved checksum drives HTML, metadata, search knowledge, and panels. |
| Canonical route | Semantic public document/pattern | planned; approved content; active; empty-held; 404; 410 | Planning does not imply public activation. |
| Wing/service/industry | Approved offer taxonomy or context | open content; visibly closed immersive space; content held | Formal titles remain exact; no delivery proof inferred. |
| Evidence item | Fact/case/demo/source/trust proof | verified; Hengshi-owned demo; pending; held; unavailable | Fail closed; Work and Demos remain separate. |
| Expert | Verified, consented person record | verified public; pending; absent | No profile/name/portrait/claim without MA-003 evidence. |
| AI session | Anonymous bounded conversation | consent choice; ephemeral active; retained consented; resuming; expired; refused; unavailable; handed off | Non-consented content ephemeral; no training; source-bound answers. |
| Handoff | Governed request to explicitly available staff | not offered; offered; requested; queued; accepted; unavailable; failed-alert/retry | Teams alert is not system of record and presence cannot create availability. |
| Booking lineage | One visitor booking journey | started; qualified; email pending/expired/undeliverable/verified; slot selected; pending; confirmed; rescheduled; cancelled; reconciliation error | Verification precedes slot eligibility; retries/reschedules never create a second lineage. |
| Consent record | Purpose/copy-version proof | not asked; declined; granted; stale/mismatched; revoked where approved | Exact copy/legal basis and record retention are MA-002 gates. |
| Local preference | Non-sensitive first/return visit choice | absent; valid; invalid/stale; cleared | Never an account or cross-device identity. |
| Staff session | Authorized staff access | signed out; active role; forbidden; idle expired; absolute expired | Entra role + server enforcement; local break glass separately controlled. |

## 4. Information architecture

### 4.1 Public hierarchy

```mermaid
flowchart TD
  H[Home] --> S[Services]
  S --> W1[Strategy & Transformation]
  S --> W2[Digital Products & Growth]
  S --> W3[AI, Data & Automation]
  S --> W4[Immersive & Creative]
  S --> W5[Cloud, Reliability & Trust]
  W1 --> SV1[1 service]
  W2 --> SV2[3 services]
  W3 --> SV3[2 services]
  W4 --> SV4[2 services]
  W5 --> SV5[2 services]
  H --> I[Industries]
  I --> AG[Agriculture]
  I --> MI[Mining]
  H --> E[Evidence and expertise]
  E --> WO[Verified Work]
  E --> DE[Demos]
  E --> IN[Insights]
  E --> EX[Experts]
  H --> T[Trust]
  H --> A[About]
  H --> C[Contact]
  H --> B[Book]
  H -. optional .-> X[/world - noindex]
  X --> S
  X --> B
```

`route-room-parity.csv` is the complete 33-row route authority for this UX
package; `excluded-surfaces.csv` covers all nine nonindexable/absent classes.

### 4.2 Campus wayfinding and release sequence

**[APPROVED]** `wayfinding-release-map.csv` is the UX authority for five wing and
ten service signs. Every concise sign is unique, and its exact formal title remains
the accessible/semantic name in the directory, DOM, canonical page, and booking
context. A room ID and canonical route ID/path make the association deterministic.

**[APPROVED]** Wing sequence is AI/Data (1), Strategy (2), Immersive/Creative (3),
Digital Products/Growth (4), then Cloud/Reliability/Trust (5). A later ordinal
cannot be `open` unless every earlier ordinal is open in the same or a prior active
approved release. **[PROPOSED UX]** `closed` means not traversable; `held_content`
means prerequisites may be met but evidence/publication is not; `opening` is an
authorized nonpublic candidate and never a public-open claim; `open` requires the
active approved release and its sequence prerequisites. In every state, an active
canonical Quick Access page remains available even when its room is closed; if the
page itself is held, the directory reports that truthfully rather than fabricating
content.

### 4.3 Persistent global navigation

**[PROPOSED UX]** Semantic header/primary navigation includes Home, Services,
Industries, Work, Demos, Insights, Experts, Trust, About, Contact, and Book.
Search/Directory, accessibility/preferences, and the visitor-elected World are
utilities.
On narrow layouts the same destinations move into a labeled disclosure/menu with
predictable focus return; Book remains reachable without opening optional media.

**[PROPOSED UX]** The immersive HUD contains current location, directory/search,
Quick Access, Book, accessibility, quality, audio, and Exit. These controls are
DOM-based, keyboard operable, visible at 400% zoom/reflow, and never canvas-only.

### 4.4 Cross-linking contract

- **[APPROVED]** `/services` links to every wing; each wing to every contained
  service; breadcrumbs link back through the visible hierarchy.
- **[PROPOSED UX]** Each service offers only approved related industry, Work,
  Demo, Insight, Expert, Trust, and Book links; absent proof produces a truthful
  held/empty module, not fabricated filler.
- **[APPROVED]** Industry pages link to relevant formal services and approved
  evidence without implying delivery history.
- **[APPROVED]** Work and Demos use distinct labels, collections, structured data,
  filters (local UI only), analytics classes, and AI evidence language.
- **[PROPOSED UX]** Insights link to named verified reviewer/expert, primary
  sources, relevant service/industry/Trust, and Book only after publication.
- **[PROPOSED UX]** Trust topics link back to services/AI/booking behaviors they
  actually govern; requirements/targets are visually separated from implemented
  evidence.
- **[APPROVED]** Every immersive room/panel links to its canonical semantic route.
  Closed/missing rooms never remove the canonical page.

## 5. Primary public journeys

### J-01 Direct semantic discovery and booking

**Requirements:** BR-001, FR-001, FR-004–FR-007, SEO-001, UX-002–UX-005.

1. **[APPROVED]** Visitor lands on a complete canonical document before JS with a
   direct semantic Book link. This guarantee is access to booking, not a claim that
   the complete transaction runs without scripting.
2. **[PROPOSED UX]** Visible hierarchy identifies location; directory and Book
   are available without overlay obstruction.
3. Visitor opens service/industry/evidence/trust content; every claim shows its
   evidence state or is omitted/held.
4. Visitor selects Book; route context may propose a matched wing but the visitor
   must confirm/change it.
5. Booking follows BF-01 in `FLOWS.md`; success is only reconciled confirmation.

Alternate: visitor books from the first page through the accessible non-WebGL
flow. Error/recovery: canvas, media, search, or AI failure leaves that flow usable.
If scripting required by the later transactional architecture fails, the semantic
page preserves selected non-sensitive context, states that the transaction is
unavailable/not completed, and offers Book retry or a verified Contact route; it
never displays a false successful or pending state.

### J-02 Visitor-elected immersive discovery

**Requirements:** FR-002, FR-003, FR-012–FR-014, UX-002–UX-008, NFR-008.

1. Visitor explicitly selects the World or follows a nonindexable `/world`
   link from semantic content.
2. First visit receives controls/choice onboarding; reduced-motion or Skip Intro
   reaches stable Reception immediately; standard arrival targets approximately
   eight seconds and remains skippable.
3. Reception/atrium shows visibly closed future wings and a persistent directory.
4. Point-and-click directed transition opens a room/panel; free-look is optional;
   WASD, collision walking, gamification, and easter eggs are never required.
5. The panel exposes the same release title, summary, evidence state, limitations,
   source links, canonical page, help, and Book action.
6. Exit opens the corresponding semantic route or Quick Access and transfers only
   safe context (route/wing), never chat or PII.

Failure/recovery: loader timeout, WebGL loss, asset error, memory/thermal downgrade,
offline, or unsupported browser offers immediate Quick Access with location context.

### J-03 Service/industry fit

**Requirements:** BR-003–BR-005, FR-017, SEO-004, SEO-007, UX-008.

Visitor compares exact formal service titles; opens a wing/service or Agriculture/
Mining context; checks scope, limits, approved evidence/Trust; then books, asks
optional help, or leaves. Empty evidence is honest. No fixed price, outcome,
customer, sector-history, certification, or availability claim is inferred.

### J-04 Evidence and due diligence

**Requirements:** BR-007–BR-009, PUB-004–PUB-007, SEO-006, SEO-011.

Visitor chooses Work, Demos, Insights, Experts, or Trust; the collection reports
its truthful availability; published detail exposes label, owner/source, review
date, limitation, and canonical sources; visitor follows related content or Book.
Held/empty collections remain unindexed until the approved release rule is met.
Defense content remains absent and AI cannot surface it.

### J-05 Optional AI or human help

**Requirements:** FR-008–FR-011, AI-001–AI-009, DATA-003–DATA-007.

Visitor may start anonymous text without an account. Consent/retention choices are
clear and purpose-specific; AI identifies itself, cites substantive sources,
refuses unsupported/sensitive/commitment requests, and always preserves Book.
Handoff is offered only for explicit staff availability. Voice/video requires
separate explicit opt-in. Full states are AF-01/AF-02 in `FLOWS.md`.

## 6. First and return visit

### FV-01 First visit

**[PROPOSED UX]** On semantic routes there is no modal gate: content and primary
navigation are immediately usable. If World is selected, a keyboard/screen-reader
accessible choice panel explains navigation, quality, audio-off state, AI, human
help, Skip Intro, Skip Guide, Quick Access, and Exit. Default audio is off. The
visitor may accept standard animation, choose reduced motion/low power, skip to
Reception, or use Quick Access. No consent for analytics/chat is bundled here.

Success: chosen stable state opens with focus at its H1/location announcement.
Error: preference write fails. Recovery: continue session with defaults and do
not imply persistence.

### RV-01 Return visit

**[PROPOSED UX]** When a valid non-sensitive local preference exists, offer
Resume, Reception, Replay, and Quick Access. Resume names the saved public
location; it never implies identity or preserved form/chat data. Invalid, closed,
retired, checksum-mismatched, or unavailable destinations fall back to Reception
or the nearest canonical semantic route with a status message. Clearing storage
simply restores first-visit choices.

## 7. Content-family behavior

| Family | Required decision content | Empty/held behavior | Primary actions |
|---|---|---|---|
| Home | name, approved category/promise, plain explanation, service/sector overview, evidence state | No invented proof strip; omit unsupported social proof | Services, Industries, Book, the visitor-elected World |
| Wing/service | formal title, intended context, scope, boundaries, evidence state, limitations, related Trust | Hold publication when owner/evidence incomplete | Related content, help, Book |
| Industry | reviewed problem context and service intersections | No sector-history claims or generic duplicated copy | Services, evidence, Book |
| Work | verified client classification and claim evidence | Honest empty/held state; do not substitute demos | Services, Book |
| Demos | Hengshi ownership, reproducibility, provenance, limits | Honest empty/held state; do not relabel seeds | Services, Book |
| Insights | buyer question, original value, sources, named review | Useful empty state only if approved; no thin filler | Related expert/service/Trust, Book |
| Experts | verified identity, role, qualifications, consent, evidence | Honest empty/held state; no anonymous invented person | Related content, Book |
| Trust | requirement vs implemented control vs test evidence vs limitation | Never claim target as assurance | Related service, Contact, Book |
| About | verified entity/people/approach | Omit legal/history/location facts until verified | Trust, Contact, Book |
| Contact | verified channels, purpose, consent/privacy, failure route | Do not expose example addresses or promise SLA | Book, available help |
| Book | qualification, email verification, local time, state/recovery | No provider/owner claims before approval | Continue, retry, reschedule/cancel where authorized |

## 8. Responsive and accessibility architecture

- **[APPROVED]** WCAG 2.2 AA is the target, not a current conformance claim.
- **[PROPOSED UX]** DOM and reading order follow full name/title, context, evidence,
  limits, sources, then action. Visual asymmetry never changes reading order.
- Keyboard and screen reader users can discover services, open/close navigation,
  search, inspect sources, operate consent, recover errors, and book. Focus is
  placed on the changed-state heading/error summary and restored to the invoking
  control when a panel closes.
- Status, validation, loading, pending, confirmation, and errors use visible text
  plus appropriate live/status semantics; no meaning depends on color, material,
  depth, glow, sound, animation, or icon alone.
- At 320 CSS px, 400% zoom, landscape mobile, tablet, desktop, text spacing, and
  content enlargement, actions remain in DOM order without two-dimensional scroll
  except genuinely two-dimensional data. Tables gain equivalent lists where needed.
- Forced colors/high contrast preserves boundaries, focus, selected state,
  evidence labels, and error/success distinction. Grayscale retains labels.
- Reduced motion is applied before nonessential travel: stable end states appear
  immediately; no parallax, particles, loops, camera travel, or opacity wait.
- Audio is opt-in/off by default and persistent mute is reachable. Meaningful
  audio-only content has a transcript; prerecorded synchronized media has accurate
  captions. SC 1.2.3's applicable Level-A branch uses one of that criterion's
  permitted options, documented per item and subject to its valid exception. Separately,
  SC 1.2.5 at the AA target requires audio description for every applicable item
  containing prerecorded video content in synchronized media. A complete media
  alternative may supplement that description or satisfy SC 1.2.3 where applicable;
  it is not a substitute for SC 1.2.5. An item treated as not requiring description
  records the standards-supported applicability evidence, such as no uncommunicated
  visual information, rather than silently substituting text. Live synchronized
  media, if offered, has live captions. Missing alternatives hold media activation/
  publication while semantic content, text help, and Book remain usable. Declining
  media does not reduce help.
- Low-power mode reduces quality/lighting/effects and can transition to Quick
  Access. Unsupported browsers (including below the approved floor) get semantic
  Quick Access, not a broken campus.
- Pointer activation uses up-event activation or an equivalent cancel/undo
  mechanism so moving away before release does not trigger an action (WCAG 2.5.2).
  The accessible name contains the visible label text (2.5.3). Every dragging
  operation has a single-pointer non-drag alternative (2.5.7). Pointer targets are
  at least 24 by 24 CSS px or satisfy and document the applicable spacing, inline,
  equivalent-control, user-agent, or essential exception (2.5.8). Point-and-click
  destinations retain keyboard equivalents; hover/drag is never required.
- Any automatic moving, blinking, scrolling, or auto-updating information that
  starts automatically and lasts more than five seconds has a keyboard/screen-
  reader-operable pause, stop, or hide control unless a valid WCAG exception is
  documented. Content never exceeds three flashes in any one-second period.
- Every user time limit is either removable/adjustable before it starts, warned
  with at least 20 seconds to extend by a simple action and extendible at least ten
  times, or mapped to a documented valid WCAG exception. Exact security/session/
  challenge time values remain gated. Timeout preserves entered data and the last
  authoritative state where policy permits, then provides accessible reauthentication.
- Applicable personal-data fields expose correct programmatic input purpose and
  autocomplete semantics. Information already entered in the same process is
  auto-populated or selectable rather than required again unless a documented
  WCAG redundant-entry exception applies. Review/correct/confirm remains available
  before data-changing submission.
- Booking verification and staff authentication/reauthentication do not require an
  unaided cognitive-function test. They support paste, password managers, and
  assistive mechanisms or an equivalent accessible method without blocking those
  mechanisms. Exact Entra/email/challenge provider and proof policy remain gated;
  third-party steps used by the complete process remain in conformance scope.
- English launch is localization-ready: no fixed-width text assumptions,
  concatenated phrases, direction-dependent meaning, or untranslatable canvas text.

## 9. Journey acceptance invariants

1. Every 3D task in this document has a semantic equivalent using the same active
   publication checksum.
2. Every named action has success, error, and recovery in `STATES_AND_RECOVERY.md`.
3. Booking is reachable and completable with AI, human help, WebGL, audio, motion,
   and uploads unavailable.
4. An unsupported claim, missing source, draft marker, or checksum mismatch is held
   or refused; it cannot be replaced by generic confident copy.
5. No visitor account/upload exists; no media activates without explicit opt-in.
6. No slot eligibility or external booking write occurs before email verification.
7. Pending/provider-ambiguous is never presented as confirmed.
8. Empty collections cannot be filled with prototype seeds or cross-classified proof.
9. Defense is absent until MA-011; ordinary visitor routes do not reveal gated detail.
10. Missing legal/provider/owner/retention policy fails closed and keeps the
    affected capability held without blocking unrelated public discovery.

# UI Reference-Design Contract and Foundation-Surface Coverage Plan

**Contract date:** 2026-09-03  
**Revision:** Producer iteration 3 of 3  
**Status:** **[PROPOSED UI CONTRACT]** final producer freeze awaiting fresh
independent design and independent accessibility review before founder decision
at MA-024  
**External Figma/Stitch write authority:** false

## 1. Objective

Define the minimum complete visual-reference evidence that a later, separately
authorized Figma or Stitch producer must create before any Hengshi Design
production UI implementation. The evidence must make the accepted D-036 journeys,
D-035 identity, D-026 strategy, and D-025 route/content boundaries implementable
without changing requirements or fabricating unavailable facts.

The contract covers:

- 33 canonical route definitions and their route-instance obligations;
- semantic navigation, directory/search, first and return visits;
- optional World entry, HUD, room/threshold states, and Quick Access recovery;
- grounded AI, human handoff, media opt-in, direct booking, contact, staff,
  publication, review, audit, authentication, permission, and recovery;
- all 53 accepted `ACT-*` action contracts, nine `EXCL-*` classes, 15 accepted
  wayfinding records, and 45 `UXTEST-*` acceptance predicates; and
- required responsive, accessibility, degraded, content-stress, focus, and
  screen-reader evidence.

This is a design-production contract, not visual production.

## 2. Authority and frozen inputs

### 2.1 Accepted authority

| Authority | Binding effect on this contract |
|---|---|
| D-025 | Retains the exact accepted 33-route foundation including `/industries`; preserves claim and publication gates. |
| D-026 | Requires Evidence in Motion, evidence-led positioning, accountable-delivery promise, exact service taxonomy, proof discipline, and semantic-first expression. |
| D-035 | Requires the frozen Signal Ledger system + Framework Relay logo hybrid and its accepted color, typography, evidence, motion, accessibility, asset, and clearance boundaries. |
| D-036 | Requires the accepted semantic/World parity, journeys, actions, states, recovery, staff operations, wayfinding, and UX tests. |

Frozen accepted inputs are read-only. Their historical draft/pending labels are not
edited here; D-025/D-035/D-036 control current acceptance. No source route is active
or published by this work.

### 2.2 Design-system dependency

Later visual work must use the semantic tokens and primitives defined in:

- `docs/phase-1-ui-reference-design/DESIGN_SYSTEM_IMPLICATIONS.md`; and
- `docs/phase-1-ui-reference-design/component-primitives.csv`.

`PRIM-*` dependencies in `reference-template-inventory.csv` identify the minimum
reusable primitives. A missing variant is a design-system finding; it is not
permission to alter the UX requirement or create an untracked one-off pattern.

### 2.3 Normative accessibility and browser baseline

The future visual and implemented product target is **WCAG 2.2 Level AA for every
applicable full page and complete process, including represented third-party
steps**. This target governs reference production, independent review, handoff,
implementation, and verification. It is not a claim of current visual,
implemented, tested, certified, or production conformance; design references and
annotations alone cannot establish conformance.

The normative `BP-NFR-006` browser/platform profile applies to every public,
interactive, World, Quick Access, and staff route, flow, template, profile, and
B01-B09 batch. It requires:

- the latest two stable release families of Chrome, Edge, Firefox, and Safari
  current at the later dated QA run;
- Safari on iOS 16.4 as the minimum legacy floor;
- mobile Safari layout, touch/input, virtual-keyboard, orientation, and safe-area
  evidence at that floor;
- exact then-current browser versions selected and recorded by dated QA rather
  than invented at this documentation freeze; and
- an equivalent semantic Quick Access journey without WebGL for clients below
  the floor or otherwise unsupported.

## 3. Contract boundary

### 3.1 Included

- Tool-neutral frame/reference names and reusable template definitions.
- Route-instance, flow/action, exclusion, and wayfinding coverage mappings.
- Required viewport, state, mode, responsive, interaction, focus, content-stress,
  asset, and evidence behavior.
- A dependency-ordered production batch plan and later evidence expectations.
- Deterministic coverage validation and producer inspection.

### 3.2 Excluded

- Visual screen production or edits in Figma, Stitch, Canva, image tools, or any
  other external system.
- Application, UI, API, 3D, data, test, dependency, lockfile, migration,
  infrastructure, publication, or deployment changes.
- Final public/legal/consent/privacy/error copy, provider behavior, staff/owner
  identities, response times, live availability, measured outcomes, or
  accessibility-conformance claims.
- New imagery, fonts, icons, production logo files, paid/licensed assets, GLB
  reuse, or generated media.
- Route activation, sitemap membership, DNS, search submission, Git history, or
  complete Phase 1 acceptance.

## 4. Coverage model

### 4.1 Reusable reference template

A reusable reference template defines stable hierarchy, content slots, controls,
responsive rules, state families, modes, focus behavior, and primitive use for a
class of surfaces. Its `TPL-*` ID is not a URL or component implementation. Each
template has one unique representative frame name plus explicit variant evidence.

### 4.2 Route instance

A route instance is one row in `foundation-route-coverage.csv`. It proves that an
accepted route ID/path has:

- one reusable `TPL-*` assignment;
- a unique `INST-*` identifier and tool-neutral route-instantiation name;
- exact family, semantic Quick Access, optional immersive, primary-action, state,
  viewport, mode, and content-gate coverage; and
- a later route-instance sheet showing real slot lengths and route-specific
  differences.

Route-instance sheets may reference a template master and annotate deltas. They
do not require 33 independently composed full-page screens. Pattern paths such as
`/work/{verified-case-slug}` remain pattern instances until truthful content is
approved and atomically released.

### 4.3 Flow/action instance

`foundation-flow-coverage.csv` assigns each flow family, action, exclusion, and
wayfinding record to one or more templates and profiles. Action coverage must show
the accepted success, loading/empty/error/pending condition, recovery, and focus
or announcement implication without changing the source behavior.

## 5. Evidence units and frame economy

Every later reference-production batch must maintain a design evidence ledger.
For each applicable template/instance/state/viewport/mode combination it records
one of these evidence types:

| Evidence type | What it proves |
|---|---|
| `FRAME` | A complete composition at an assigned viewport and state. |
| `FOCUSED_FRAME` | A bounded panel, overlay, state, or component whose geometry/hierarchy materially changes. |
| `VARIANT` | A reusable component/property variant that proves a repeated state without a duplicate page. |
| `ANNOTATION` | Responsive, semantic, focus, screen-reader, pointer, timing, or implementation behavior that is not honestly proven by pixels alone. |
| `PROTOTYPE` | Interaction sequence, focus return, modal/disclosure behavior, pointer cancellation, or transition timing. |
| `ROUTE_INSTANCE_SHEET` | Route-specific content slots, title/action stress, evidence gate, canonical path, and template delta. |
| `TEST_CAPTURE` | Later browser/assistive-technology/forced-colors/zoom/print evidence after implementation; never substituted by a design mockup. |

A unique full-page frame is required when hierarchy, action placement, responsive
structure, or authoritative state changes materially. It is not required for every
cross-product of state, viewport, and mode when a reusable variant plus an explicit
annotation and representative capture proves the behavior. Every combination must
still be accounted for in the later evidence ledger; `not applicable` requires a
written rationale and reviewer acceptance.

Minimum per template:

1. one standard desktop or wide `FRAME`;
2. one 320 CSS px or narrow-mobile `FRAME`;
3. one landscape/tablet responsive evidence item where the grid or control
   placement changes;
4. distinct `FRAME` or `FOCUSED_FRAME` evidence for critical empty, held, error,
   pending, permission, or recovery states named by the template;
5. forced-colors, grayscale, reduced-motion, low-power, non-WebGL, unavailable
   font/image/asset, keyboard, screen-reader, and print evidence as applicable;
6. interaction/focus annotations and a content-stress specimen; and
7. route-instance sheets for every mapped route, including honest zero-content
   and maximum-length cases.

The ledger must additionally record `BP-NFR-006`, its dated browser/platform/input
result, unsupported-client Quick Access recovery, and the assigned `TL-*`
time-limit branch for every covered record. Provider latency or a system-response
timeout is not a user time limit and cannot substitute for that branch decision.

## 6. Tool-neutral naming

Every future reference frame/evidence object uses:

`HSD_UIR_<BATCH>_<TEMPLATE>_<INSTANCE>_<STATE>_<VIEWPORT>_<MODE>_V<NN>`

Rules:

- uppercase ASCII letters, digits, and underscores only;
- `B01` through `B09` match `design-batch-plan.csv`;
- `<TEMPLATE>` is the `TPL-*` ID with hyphens converted to underscores;
- `<INSTANCE>` is `REF`, the normalized `INST-*` ID, or a normalized flow/action
  source ID;
- `<STATE>`, `<VIEWPORT>`, and `<MODE>` use IDs from
  `responsive-state-mode-matrix.csv` with hyphens converted to underscores;
- versions begin at `V01`; revisions increment without renaming the stable
  template/instance source IDs; and
- filenames, page names, and review comments may add human-readable labels, but
  the canonical evidence ID stays unchanged.

Example:

`HSD_UIR_B06_TPL_BOOKING_INST_ROUTE_BOOK_STATE_EMAIL_PENDING_VP_320_MODE_KEYBOARD_V01`

The inventories provide unique baseline names. Later producers generate
additional names deterministically from the same grammar and must reject
duplicates.

## 7. Required viewports and responsive behavior

The authoritative viewport profiles are in
`responsive-state-mode-matrix.csv`. They include at least:

- `VP-320`: exact 320 CSS px reflow evidence;
- `VP-NARROW`: narrow mobile portrait;
- `VP-LANDSCAPE`: landscape mobile;
- `VP-TABLET`: tablet;
- `VP-DESKTOP`: desktop;
- `VP-WIDE`: wide desktop; and
- `VP-ZOOM-400`: 400% browser zoom/reflow with an effective 320 CSS px content
  width.

Responsive decisions are content-driven, not device-status-driven. The accepted
12/6/4-column direction may collapse earlier when content requires it. At every
required viewport:

- DOM, reading, focus, and error-summary order remains meaningful;
- Book and recovery remain reachable without opening optional media;
- persistent/sticky navigation and HUD controls do not obscure focused content;
- controls do not require two-dimensional scrolling, except genuinely
  two-dimensional data with an equivalent list/table;
- long formal service names, visible evidence labels, local date/time/timezone,
  errors, and translated-length stress remain intact;
- tables have equivalent responsive structures; and
- no action depends on hover, drag, color, icon, position, sound, motion, or
  canvas alone.

All viewport evidence is executed against `BP-NFR-006`. At minimum, a Safari/iOS
16.4 specimen proves narrow and landscape reflow, touch/input behavior,
virtual-keyboard avoidance, orientation change, focus visibility, and safe-area
insets; an unsupported-client specimen proves the equivalent semantic Quick
Access route, content, and action recovery.

## 8. Required modes

The mode profiles include:

- standard;
- reduced motion;
- low power;
- non-WebGL / Quick Access;
- forced colors / high contrast;
- grayscale;
- unavailable font;
- unavailable image or asset;
- print where applicable;
- keyboard; and
- screen-reader semantics.

Reduced motion presents stable end states without camera travel, parallax, loops,
particles, or opacity waits. Low-power reductions never remove content or Book.
Forced colors preserves boundaries, focus, selection, status, and evidence labels.
Unavailable fonts must tolerate metric changes and preserve controls. Missing
images/assets use truthful alternatives and never hide a claim, limitation, or
action. Print applies to public decision/evidence/trust/insight/booking-summary and
appropriate staff audit/review evidence; interactive-only controls receive a
documented non-applicable rationale rather than a fake print interaction.

Keyboard evidence includes logical tab order, visible unclipped focus, skip links,
disclosure/dialog focus entry and return, escape/cancel where safe, and no trap.
Screen-reader annotations include landmarks, heading order, names/roles/values,
descriptions, status/live-region priority, error-summary links, table/list
alternatives, media alternatives, and canvas-independent content.

## 9. State coverage and critical variants

State profiles are defined in the matrix and assigned in both coverage files.
Critical variants requiring distinct visual or focused-frame evidence include:

- public collection populated, approved honest empty, held/unindexed, loading,
  derived-index unavailable, offline, 404, and 410;
- source/evidence verified, demo, proposed/requirement, review-needed/conditional,
  unavailable/held, error, and checksum mismatch;
- first visit, valid return, stale/closed/retired return destination, cleared
  preference, and preference-write failure;
- World onboarding, loading, Reception, closed/held/opening/open threshold,
  transition interruption, low-power downgrade, unsupported WebGL, asset failure,
  offline, and Quick Access exit;
- AI consent choice, ephemeral/consented session, connecting/typing, sourced
  answer, cannot verify, refusal, policy/provider unavailable, resume pending,
  expired, handoff, and direct Book;
- human handoff not offered/offered/requested/pending/queued/accepted/text-active/
  ended, staff unavailable, alert failed, expired/declined, media opt-in/active/
  denied/failure;
- the complete booking lineage from `BOOKING_STARTED` through qualification,
  challenge, verification, availability, slot review, `BOOKING_PENDING`,
  reconciliation, confirmation, reschedule, cancellation, and every accepted
  failure/ambiguity state; and
- staff signed-out, authorized, forbidden, idle/absolute expiry, CSRF/session
  failure, queue loading/empty/stale/unavailable, mutation pending/error/success,
  publication draft/review/founder/candidate/activation/prior-release states, and
  read-only audit recovery.

Pending or ambiguous never uses success styling or language. Permission denial
does not reveal protected-object existence. Offline never implies queued PII or a
durable write. Error designs state what happened, what remains preserved, and the
smallest safe next action.

## 10. Interaction and accessibility annotations

Every later reference set must annotate:

1. source-order, landmark, heading, label, description, status, and error
   semantics;
2. initial focus, focus movement, focus containment where necessary, return focus,
   and post-navigation heading focus;
3. pointer-up activation/cancellation, at least 24 by 24 CSS px targets or a
   recorded valid exception, single-pointer non-drag alternatives, and keyboard
   equivalents;
4. loading/pending announcement without focus theft and manual refresh for
   auto-updating authoritative state;
5. pause/stop/hide for automatic content over five seconds, no content over three
   flashes per second, and the exact assigned WCAG 2.2 SC 2.2.1 time-limit branch;
6. input purpose/autocomplete, textual required/optional status, persistent field
   errors, linked error summary, redundant-entry avoidance, review/correct/confirm,
   and accessible authentication without an unaided cognitive test;
7. exact modal/disclosure dismissal and safe escape behavior; and
8. no-JavaScript boundary: complete initial semantic decision content and direct
   Book access, but no invented end-to-end no-JavaScript transaction claim.

The design review evaluates visual hierarchy, comprehension, component
consistency, real-content stress, focus visibility, contrast, and implementation
feasibility. Accessibility conformance is established only by later independent
implementation evidence, not by these references.

### 10.1 Time-limit branches

Every route, flow, reusable template, responsive/state/mode profile, and production
batch has a machine-readable `TL-*` selection:

- `TL-REMOVABLE-ADJUSTABLE`: the user can turn the limit off or adjust it before
  encountering it over the criterion-supported range;
- `TL-WARN-EXTEND`: warn at least **20 seconds** before expiry and provide a
  simple extension of at least **10 times** the default limit;
- `TL-EXCEPTION`: only a documented criterion-supported exception naming the
  affected complete process, rationale, fallback, preservation behavior, and
  independent accessibility-review acceptance; or
- `TL-NOT-APPLICABLE`: the accepted definition introduces no user time limit.

For any applicable branch, preserve permitted data and the last authoritative
state across expiry and return through accessible reauthentication where a
protected session is involved. The warning, extension, pre-start adjustment, and
reauthentication controls must be keyboard and screen-reader operable. Exact
session, challenge, hold, or warning durations remain gated and must not be
invented by reference production. No current record selects `TL-EXCEPTION`; a
standards exception or target change is a human gate.

## 11. Content stress contract

Reference evidence uses realistic but non-public fixture language. Each specimen
is visibly marked `REFERENCE FIXTURE — NOT PUBLIC COPY` and must include:

- the full `Hengshi Design` name, category, promise, longest formal service names,
  and sentence-case labels;
- minimum and maximum-length headings, summaries, source labels, limitations,
  breadcrumbs, menu items, field errors, status messages, and local-time strings;
- zero-item, one-item, and many-item collection/list conditions;
- verified Work and Hengshi-owned Demo labels kept visibly distinct;
- requirement/target, implemented control, test evidence, limitation, owner, and
  review date kept distinct in Trust specimens;
- booking's exact six required data fields plus one separate purpose-specific
  consent record, with budget optional and no name/phone/account/upload/AI gate;
- absent expert/contact/owner/media/provider facts rendered as held or unavailable,
  never filled with examples that resemble real data; and
- plain global English with no culture-specific idiom, agriculture rescue/pastoral
  trope, mining spectacle/extraction claim, AI magic, militarized/defense metaphor,
  or unsupported comparative language.

Exact public/legal/consent/privacy/error wording remains gated. Fixtures cannot be
copied into public content without evidence, legal/privacy review where applicable,
specialist review, and founder publication approval.

## 12. Asset map and evidence constraints

| Asset need | Allowed reference source | Later evidence required | Current rule |
|---|---|---|---|
| Entity/logo treatment | Frozen D-035 Framework Relay family in `docs/phase-1-brand-identity/assets/` | Exact source asset ID/hash, size variant, contrast/background, clearance status, founder visual approval | Internal definition reference only; unregistered and trademark-not-cleared |
| Color/type/evidence grammar | Frozen `semantic-tokens.json` and accepted identity documents | Token mapping, contrast evidence, unavailable-font stress, evidence-label redundancy | No paid/hosted font; system stacks only unless separately approved |
| Icons | Accepted 24-unit/2-unit construction guidance | Original icon source, name, label, forced-colors result, rights/provenance | No third-party icon set or ambiguous icon-only action |
| Documentary or case media | None currently approved | Owner, creator, source, rights, consent, evidence class, caption/alt decision, dimensions/crop, checksum, review and publication state | Hold; no stock or prototype seed presented as proof |
| Illustration or generated media | None in this package | Separate approved asset brief, generator/source provenance, rights, cultural/accessibility/security review, clear illustrative label | Cannot depict a real person/place/client/system/result as evidence |
| Data visualization | Accepted direct-label and evidence-state grammars | Title, unit, period, scope/sample, source, limitation, summary, exact values, narrow/forced/grayscale/print evidence | No invented metric, animated count-up, 3D chart, or color-only meaning |
| Audio/video | None currently approved | Rights, transcript/captions, SC 1.2.3 handling, separate SC 1.2.5 audio description where applicable, live captions, applicability record | Media remains held if an applicable alternative is missing |
| World/3D | Future approved storyboard and project-owned Blender/asset specification | Provenance, scale/origin, LOD, performance, semantic mapping, low-power and non-WebGL evidence | Protected exterior GLB is visual comparison evidence only; no reuse |
| Social/print exports | Future route-specific design | Truthful subject, full name, licensed/versioned assets, safe crops, release checksum, physical/print proof | No current social/public/print asset is authorized |

No asset is accepted merely because it appears in a reference frame. Every
substantive asset needs a manifest identity, provenance, rights/clearance, evidence
class, alternative-text decision, approval state, and release linkage.

## 13. Route and non-route production rules

### 13.1 Public routes

`foundation-route-coverage.csv` is the exact 33-row route coverage authority.
Each later route-instance sheet must show the canonical ID/path, template, dominant
intent, route-specific content slots, evidence gate, actions, semantic/immersive
relationship, required profiles, and pattern-vs-concrete status. D-025 overrides
only the stale planning status for `/industries`; it does not activate the route.

### 13.2 Exclusions

All nine exclusions require an intentional nonindexable/private/absent experience:
World, admin, nonpublic publication, chat/session, internal search, tracking
variants, filter/sort variants, staging/candidate, and defense. A noindex label is
not an authorization control. Defense remains absent. External or private state
must not leak through navigation, error messages, screenshots, or design fixtures.

### 13.3 Wayfinding

All 15 accepted wing/service records retain unique concise signs, exact formal and
accessible titles, route IDs/paths, room IDs, release ordinal/prerequisite, and
closed/held/opening/open behavior. A room can never be the sole path to an active
canonical page. `Opening` remains nonpublic candidate state and cannot use an
unapproved promise such as a date or `coming soon`.

### 13.4 Flows and actions

`foundation-flow-coverage.csv` is the exact mapping authority for navigation,
search, first/return visit, World/HUD/recovery, AI, human/media, booking, contact,
staff/publication/operations, auth/session/permission, and error/offline/recovery.
Every `ACT-01` through `ACT-53` row preserves its source success, alternate, and
recovery semantics.

## 14. Design batches and review evidence

`design-batch-plan.csv` sequences later visual work. A batch may begin only when
its dependencies and input gates pass. The plan establishes:

- exactly one primary owner for every `TPL-*`, route, package `FLOW-*`, accepted
  source journey/flow/subflow, `ACT-*`, `EXCL-*`, and wayfinding ID;
- separately labeled supporting/final-evidence references that never count as
  primary production ownership; and
- only exact semicolon-delimited IDs in executable coverage fields, with hard
  batch prerequisites separated from explanatory held-input text.

B06 booking has one hard visual prerequisite: B01 shared semantic shell and
recovery. It has no prior AI, human handoff, media, World, account, audio, or
upload dependency. B05 consistency inspection is non-blocking. This preserves
direct Book access and independent booking production even while optional-help
inputs remain held.

Every B01-B09 row requires both independent design review and independent
accessibility review against the normative WCAG 2.2 Level AA target for every
applicable full page and complete process, including represented third-party
steps. Passing a design-reference review does not claim current conformance.
Every batch also produces:

- named frames/evidence objects and an evidence-ledger export;
- route/flow/template coverage deltas with no orphan `TPL-*`, `INST-*`, `ACT-*`,
  `EXCL-*`, `UXTEST-*`, or `PRIM-*` reference;
- representative 320, mobile landscape, tablet, desktop/wide, and 400% reflow
  evidence;
- `BP-NFR-006` evidence, including Safari/iOS 16.4 mobile layout/input/safe-area
  behavior, dated then-current evergreen selection, and unsupported-client
  semantic Quick Access recovery;
- its assigned `TL-*` branch evidence, including preservation and accessible
  reauthentication where applicable, while exact durations remain gated;
- critical state and mode evidence with annotations;
- keyboard/focus and screen-reader semantic notes;
- content-stress and missing-asset evidence;
- design-system delta or explicit no-delta decision;
- producer inspection; and
- independent design and accessibility findings.

The final visual-direction gate occurs only after all contracted batches and
evidence exist, independent review passes, and the founder reviews the actual
visual result. This documentation package cannot substitute for that gate.

## 15. Handoff contract for later visual production

The future producer must begin from the frozen MA-024 package and record the
approved external-write authority before opening or changing a Figma/Stitch file.
They must not silently redesign a flow, rename a service, remove a route, simplify
the booking lineage, collapse Work into Demos, infer a provider, or populate
unverified content to make layouts look complete.

The later handoff must include:

- the design-file/file-key and page/frame inventory without credentials;
- the exact frame/evidence ID ledger and exported inspection images;
- component/property mappings to `PRIM-*` IDs and documented deltas;
- responsive/state/mode and route/flow coverage reports;
- interaction, focus, semantics, content, asset, and implementation notes;
- independent design and accessibility reviews and resolved findings;
- a production-ready `docs/ui/UI_SPEC.md`; and
- the founder's final visual-direction decision.

Only after the whole Phase 1 package is accepted may a separately bounded
implementation task use those references.

## 16. Human and unresolved gates

- **MA-024 — Phase 1 UI reference-design contract and foundation-surface coverage
  acceptance:** accept this frozen documentation package or request a bounded
  revision. It does not authorize external design writes.
- **Separate future external-write gate:** required before Figma or Stitch
  production/write; authorization is currently false.
- **Final visual direction:** founder approval after actual reference evidence and
  independent review.
- **MA-002:** exact legal entity, contact, consent, privacy, retention, deletion,
  and public disclosure facts/copy.
- **MA-003:** verified claims, Work, Demos, experts, owners/backups, biographies,
  media rights, and publication consent.
- **MA-004:** protected GLB provenance/reuse and future 3D source.
- **MA-005/MA-006/MA-007/MA-010:** provider capability, mailbox/calendar, roles,
  availability, entitlement, policy, and paid envelopes.
- **MA-008/MA-009:** domain and webmaster ownership/actions.
- **MA-011:** defense remains absent until exact founder/legal/security approval.
- **MA-013:** compatibility inventory acceptance remains separate.
- Paid/licensed assets, fonts, likenesses, trademark clearance, implementation,
  publication, Git, deployment, complete Phase 1 acceptance, and launch remain
  separate gates.

The package may proceed to independent design and independent accessibility review
when deterministic validation and producer inspection pass. Both current reviews
must pass before MA-024. The producer cannot approve their own work.

At the 2026-09-03 producer freeze, MA-024 and the separate external-write gate are
package proposals not yet recorded in root durable manual-action records, so their
trace provenance is package-only. An authorized coordinator may integrate root
durable records only after clean independent design and accessibility reviews;
later integration does not contradict this time-bounded freeze statement.
External Figma/Stitch production/write authorization remains false until its
separate future manual gate is explicitly accepted.

# Content, Data, Analytics, and UX Test Definition

## 1. Content and data needs

| Need ID | Route/surface | Required input before public/operational use | Current evidence state and gate | Fail-closed UX |
|---|---|---|---|---|
| CN-001 | Entity/Home/About/Contact | verified legal/display relationship, public business/privacy/security contacts, jurisdiction and disclosures | Display name/positioning approved direction; legal facts absent; ECL-001/ECL-016/ECL-028; MA-002 | Use approved brand name in definition; hold legal/contact claims and channels |
| CN-002 | Five wings/ten services | specialist scope, boundaries, delivery model, owner/backup, evidence or labeled demo | Taxonomy approved; delivery proof/owners absent; ECL-004/ECL-014/ECL-015/ECL-029; MA-003 | Keep route/room reserved; do not assert delivered capability |
| CN-003 | Agriculture/Mining | named reviewer, sourced problem framing, approved service intersections | Priorities approved; no sector history proof; ECL-003; MA-003 | No client/history/credential claim; hold unsupported module |
| CN-004 | Work | authorized case, claim sources, measurable method if applicable, client consent, media rights | No verified cases; ECL-007–ECL-012/ECL-019/ECL-032; MA-003 | Honest approved empty/held state; never use seeds or Demos |
| CN-005 | Demos | Hengshi ownership, reproducibility, provenance, limitations, security review where relevant | No approved demos; ECL-033; MA-003 | Honest approved empty/held state; do not relabel fictional seeds |
| CN-006 | Insights | six approved briefs, buyer question, original value, primary sources, named qualified reviewer, byline/date/media rights | Requirement only; ECL-023; MA-003 | Hold/unindex thin, anonymous, or unreviewed content |
| CN-007 | Experts | verified identity, role, qualifications, biography, consent, portrait rights | None verified; ECL-017/ECL-018; MA-003 | No profile/byline/Person data; honest empty/held state |
| CN-008 | Trust | implemented/approved control, evidence, scope, owner, date, limitation, legal/security review | Targets/requirements not assurance; ECL-031; MA-002 | Separate requirement from control/evidence; hold certification/compliance claim |
| CN-009 | Booking | mailbox/calendar/provider, owners/backups, availability, timezone source, consent copy, privacy notice, challenge/resend/expiry/rate-limit rules, no-slot, reschedule/cancel policy | Contract direction approved; operational rules absent; MA-002/MA-006 | Define states only; no slot/provider/owner/SLA claim or external write |
| CN-010 | AI | approved knowledge checksum, source display, provider/data policy, refusal language, capability/security/residency/availability evidence | Role required but not operational; ECL-030; MA-005/MA-007 | Cannot verify/unavailable; human/Book; no unsafe provider fallback |
| CN-011 | Human handoff | explicit availability source, console owner/backup, Teams alert recipients/consent, escalation/closure rules | Assignments absent; ECL-029; MA-003/MA-006 | Do not offer live state; Contact/Book without response promise |
| CN-012 | World/3D | project-owned source/provenance, canonical mappings, accessible labels, delivery streams, loader and recovery content | Existing GLB reference-only; ECL-022; MA-004 | Semantic routes and reserved room mapping; no geometry reuse |
| CN-013 | Domain/search ownership | verified canonical-domain control and webmaster accounts | design-time host only; ECL-005/ECL-024; MA-008/MA-009 | Specification only; no verification/submission/public claim |
| CN-014 | Defense | exact scope and independent legal/security/export/control/AI/data review | Not cleared; ECL-025; MA-011 | Absent from routes/search/AI; safe general route only |
| CN-015 | Retention/deletion | record-class matrix for booking, meeting/provider, consent proof, audit, operational copies, tombstone; legal basis/duration/exceptions | 90-day rule applies only to consented chat/brief/lead; other classes unmapped; DATA-005/006; MA-002 | Keep deletion pending/unmapped; never claim provider deletion or tombstone retention |

## 2. Content component requirements

**[PROPOSED UX]** Content structures below describe fields, not final copy or
screen design.

- Decision header: formal title, route type, approved one-sentence context,
  evidence/publication state, limitation, primary Book action.
- Service unit: exact formal service title; intended buyer decision; scope and
  explicit exclusions; delivery/evidence status; approved related Work/Demo/
  Insight/Expert/Trust; owner only when verified; canonical sources.
- Evidence card: classification (`Verified Work` or `Hengshi-owned Demo`), claim,
  owner/source, evidence status, review date, limitation, rights/media status,
  canonical detail. Never show a generic “results” badge.
- Trust unit: requirement/target, implemented control (if evidenced), test evidence,
  limitation/scope/date, owner, legal/security review state.
- AI answer: visible AI identity, answer/refusal, source list, evidence limitation,
  human/Book. No source carousel hidden from screen reader order.
- Booking status: lineage state, action completed/not completed, next safe step,
  local time/timezone where relevant, consent purpose/copy version reference,
  editable qualification summary; no provider internals.
- Media alternative inventory: media kind (`audio_only`, `prerecorded_synchronized`,
  or `live_synchronized`), spoken and meaningful visual information, captions,
  transcript, SC 1.2.3 description/media-alternative handling, separate SC 1.2.5
  audio description for every applicable prerecorded video item, live captions
  when live media is offered, applicability evidence, rights/reviewer/status. A
  complete media alternative may supplement the SC 1.2.5 description or satisfy
  SC 1.2.3 where applicable, but cannot replace required SC 1.2.5 audio description.
  A missing required alternative holds media activation/publication but not
  semantic content or Book.
- Empty state: what collection represents, truthful reason no public entries are
  available, what remains usable, and next action. It cannot market absence as proof.

## 3. Privacy-safe analytics hypotheses

Analytics are **[PROPOSED UX]** measurement definitions until privacy/legal review.
No numerical conversion target, attribution window, event retention, small-cell
threshold, response SLA, or causal claim is approved.

### Minimal event envelope

Allowed candidate dimensions: pseudonymous/session-scoped booking lineage only
where governed; canonical route key/class (not raw URL); active publication
checksum; coarse entry experience (`quick_access`, `3d`, `reduced_motion`,
`low_power`, `non_webgl_or_asset_failure`); coarse entry class (`organic_search`,
`direct`, `referral`, `unknown`); bounded state/action ID; assistance path (`direct`,
`ai_assisted`, `human_assisted`, `mixed`, `none`); bounded outcome/error class;
event time; consent purpose/copy version only on the governed consent record.

Never in aggregate analytics: name, email, organization, role, desired-outcome
text, budget, chat, form message, raw search query, phone, IP, exact location,
full referrer, provider response, credential/secret, unbounded error, fingerprint,
or cross-site/persistent visitor ID. Security network data is separate and governed.

### Hypotheses

| Hypothesis ID | Proposition to test | Evidence | Privacy/interpretation guardrail |
|---|---|---|---|
| HYP-01 | Buyers can identify a relevant formal service and next action from Quick Access without AI or World. | Moderated task success, comprehension, keyboard/AT path, route logs in aggregate | No interview result exists yet; success does not prove purchase intent. |
| HYP-02 | The visitor-elected World improves orientation/memorability for some visitors without reducing semantic completion. | Cohort-sized usability findings and KPI-D06-style aggregate outcomes | No parity threshold/causality claim; never route users to a worse path. |
| HYP-03 | Evidence/limitation labels help evaluators distinguish Work, Demos, requirements, and implemented Trust evidence. | Classification/comprehension tasks | Do not publish fabricated stimuli as real proof. |
| HYP-04 | Route-context wing suggestion reduces effort while remaining understandable and correctable. | Correction rate and qualitative comprehension | Prefill must be confirmed; no hidden scoring or penalty. |
| HYP-05 | Clear cannot-verify/refusal plus sources/human/Book preserves trust better than unsupported completion. | Adversarial usability and trust-reasoning interviews | Trust rating is subjective; refusal must not conceal available approved facts. |
| HYP-06 | Email verification after qualification is understandable when pending/expired/undeliverable states preserve one lineage. | State comprehension, recovery success, duplicate-rate invariant | Expiry/rate policy remains unselected; no production email baseline. |
| HYP-07 | Showing local time with explicit timezone reduces slot-selection errors. | DST/timezone scenario accuracy and participant interpretation | No attendance/conversion causality claim. |
| HYP-08 | Honest empty evidence/expert collections are clearer than omitted labels or placeholder proof. | Findability and credibility interviews | Founder must approve whether/when empty collection is public/indexed. |
| HYP-09 | Persistent Directory, Quick Access, Book and Exit reduce immersive disorientation. | Findability/time-on-task and recovery tasks | Time is diagnostic, not a target or proof of business value. |
| HYP-10 | Stable reduced-motion states preserve comprehension and task completion. | Preference-mode task parity and qualitative comfort | No numerical parity threshold approved; never collect health/disability profiles. |

## 4. UX test hypotheses and acceptance evidence

### Public discovery and parity

| Test ID | Scenario | Required evidence / pass predicate |
|---|---|---|
| UXTEST-001 | JS and canvas disabled on representative indexable routes | Unique title/H1, core decision content, hierarchy, relevant links, help/Book are complete in initial HTML. |
| UXTEST-002 | Enumerate all 33 routes and nine exclusion classes | Route IDs/paths unique; D-025 `/industries` retained; exclusions match controls; zero orphan canonical family. |
| UXTEST-003 | Compare each optional room/panel to canonical route | Same active checksum, formal title, summary meaning, evidence state, limitations, sources, and Book; no 3D-only action. |
| UXTEST-004 | Start from every route family and reach Book | Direct semantic path exists without AI/human/World; selected route/wing context is visible and editable. |
| UXTEST-005 | First World visit standard/reduced/skip | Controls announced before commitment; audio off; approximately 8-second standard target; skip/reduced reaches stable Reception promptly. |
| UXTEST-006 | Return visit with valid/stale/closed/retired saved location | Valid offers Resume/Reception/Replay/Quick Access; invalid safely falls back with status; no identity inference. |
| UXTEST-007 | Loader/WebGL/asset/network/device loss at every transition | Quick Access appears, safe context retained, no blank canvas/loop/content loss. |
| UXTEST-008 | Directory search empty/no-result/index unavailable/offline | Browse categories/static active-release directory/clear/Book remain; clean canonical result links; no raw query analytics. |

### AI, handoff, and booking

| Test ID | Scenario | Required evidence / pass predicate |
|---|---|---|
| UXTEST-009 | Anonymous AI with consent declined | Ephemeral use available; no durable chat/lead/analytics content; browsing and Book remain. |
| UXTEST-010 | Supported/missing/conflicting/stale/private/commitment/sensitive AI prompts | Supported answer cites approved sources; other cases cannot verify/refuse and offer safe human/Book; no draft/defense/secret leakage. |
| UXTEST-011 | AI interruption/resume/expiry/duplicate send | At most one message/request; valid session resumes; expired starts new safely; status truthful. |
| UXTEST-012 | Staff explicit availability vs Teams presence | Presence cannot create availability; stale/unavailable never shows live; durable handoff survives alert failure. |
| UXTEST-013 | Voice/video opt-in declined/denied/unsupported/fails | No media before opt-in; text and Book continue; no automatic re-prompt loop. |
| UXTEST-014 | Booking required and optional elements | Exactly six required data fields—email, organization, role, desired outcome, matched wing, desired timing—plus one purpose-specific consent record: seven required elements total. Budget is optional; no name/phone/account/upload/AI requirement. |
| UXTEST-015 | Invalid form and consent decline | Error summary/field associations/focus work; no challenge/lead; browsing/ephemeral help remain. |
| UXTEST-016 | Email pending/expired/undeliverable/corrected/resend/verified | One lineage; unverified states expose no slots/write/confirmation; only current challenge verifies. |
| UXTEST-017 | Availability timezone/DST/no owner/no slot/stale slot | Correct visitor-local instant/zone; no ineligible slot; honest no-slot and recovery with no promise. |
| UXTEST-018 | Double submit/reload/two tabs/provider timeout | One idempotent booking; ambiguous remains pending; reconcile before retry; exactly one external record. |
| UXTEST-019 | External confirms but alert fails | Confirmation remains valid after reconciliation; alert retry independent; staff console truth preserved. |
| UXTEST-020 | Reschedule/cancel timeout/race/expired authorization | Same lineage; prior truth remains until reconciliation; no false success or duplicate occurrence. |

### Accessibility, responsive, content, and staff

| Test ID | Scenario | Required evidence / pass predicate |
|---|---|---|
| UXTEST-021 | Keyboard-only across nav/search/help/booking/staff decision | Logical order; no trap; visible focus; focus moves/restores predictably; every pointer task equivalent. |
| UXTEST-022 | Screen reader landmarks/headings/status/errors/source list | Meaningful order/names/roles; status announced without focus theft; error summary links; sources accessible. |
| UXTEST-023 | 320 CSS px, 400% zoom, text spacing, landscape mobile/tablet/desktop | No lost content/action or two-dimensional scroll except data; sticky/HUD controls do not obscure focus/content. |
| UXTEST-024 | Forced colors, grayscale, unavailable font/images, no CSS images | Focus/status/evidence/error meaning retained; decorative loss does not remove content. |
| UXTEST-025 | Reduced motion/low power/audio muted | Stable content/actions identical; no camera/parallax/loop requirement; transcripts/text equivalents present. |
| UXTEST-026 | Empty Work/Demos/Insights/Experts and held Trust/About/Contact | Truthful labels and next paths; no prototype seed, invented person/contact, social proof, or assurance claim. |
| UXTEST-027 | Author/reviewer/founder/admin role negatives | Server denies self-approval, skipped review, ambiguous/missing role and admin-as-approver inference. |
| UXTEST-028 | Draft marker seeded across release surfaces | Absent from HTML, metadata, sitemap, notification, AI, directory and 3D; failure keeps previous release. |
| UXTEST-029 | Render/index/activation component failure | No partial/mixed release; previous checksum active; correction returns through workflow. |
| UXTEST-030 | Analytics payload and deletion workflow inspection | No prohibited fields; unknown/small cohorts protected by later policy; unmapped class keeps deletion pending. |
| UXTEST-031 | Staff availability on/off with Teams/Redis failure and role negatives | Only authorized explicit durable action can set available; off/error/pending fails unavailable; Teams presence cannot set on; both transitions are audited. |
| UXTEST-032 | Handoff queue empty/load/stale then accept/decline/end | Empty differs from error; one authorized acceptance; decline/end preserve request/audit; stale/negative roles denied; visitor retains Book. |
| UXTEST-033 | Alert adapter failure after durable handoff/booking | Core state remains authoritative; authorized retry is independently pending/success/error; no duplicate or false conversation/booking outcome. |
| UXTEST-034 | Assignment/reassignment with no eligible assignee and stale tabs | One current eligible assignment; conflict blocks overwrite; hold/recovery visible; actor/from/to/version/reason audited; unauthorized self/admin override denied. |
| UXTEST-035 | Booking reconciliation and exception handling | Local/provider match confirms once; ambiguous/missing/duplicate/no-slot/alert exception remains visible; no unauthorized delete or retry before ambiguity resolves. |
| UXTEST-036 | Evidence/SEO and knowledge review boundaries | Exact candidate/checksum used; self-review/admin-as-reviewer denied; knowledge excludes draft/private/defense/stale sources; neither review activates publication. |
| UXTEST-037 | Audit inspection authorized/empty/index unavailable/integrity gap | Redacted durable event chain remains read-only; inspection audited; derived-index failure recovers to durable retrieval; unauthorized role learns no event existence. |
| UXTEST-038 | Five-wing/ten-service wayfinding and release sequence | Fifteen unique signs/room IDs map one-to-one to exact formal/accessibility titles and canonical routes; ordinals are 1–5 in AI/Data, Strategy, Immersive/Creative, Digital/Growth, Cloud/Trust order; out-of-order open fails while active canonical Quick Access remains. |
| UXTEST-039 | Pointer/touch across every control family | Targets are at least 24x24 CSS px or have recorded exception/spacing; visible label is in accessible name; move-away before pointer-up cancels; every drag has non-drag single-pointer and keyboard alternatives. |
| UXTEST-040 | Standard/reduced motion, auto-updates, flashes, and controlled-clock timeouts | Every automatic motion/update over five seconds has pause/stop/hide or valid exception; no content exceeds three flashes/second; each time limit adjusts or warns/extends per WCAG or records valid exception; state/data and accessible reauth survive. |
| UXTEST-041 | Audio-only, prerecorded synchronized, and live synchronized media inventory | Verify transcript and captions; separately verify SC 1.2.3 description/media-alternative handling and SC 1.2.5 audio description conveys every meaningful visual cue in time for each applicable prerecorded video item; record valid non-applicability evidence; verify live captions. Fail when an applicable item has only a complete media alternative but lacks required SC 1.2.5 audio description. Missing requirements hold media only; semantic content/Book remain. |
| UXTEST-042 | Input purpose and redundant-entry process inspection | Correct autocomplete tokens for applicable fields; no invented tokens; qualification/email correction/review/reschedule/cancel/contact/staff values are auto-populated/selectable unless documented exception; correction/confirmation available. |
| UXTEST-043 | Booking verification and staff authentication/reauthentication | Complete without unaided cognitive test using paste/password manager/assistive mechanism or equivalent; third-party steps included; timeout preserves authoritative state and permitted entered data; exact provider remains gated. |
| UXTEST-044 | JavaScript transaction failure boundary | With JS unavailable, representative indexable routes retain complete initial content and direct semantic Book access; if transaction scripting fails, status says unavailable/not completed and offers Book retry/verified Contact without false lineage, pending, or confirmation. No no-JS end-to-end completion is asserted. |
| UXTEST-045 | Qualification contract deterministic fixture | Fixture accepts only the six named required data fields plus one purpose-specific consent record as seven elements total; budget omission passes; name/phone/account/upload/AI cannot become required. |
| UXTEST-046 | Delivery stream control, boundary crossing, and process-state survival | The control is a native radio group with a separate explicit Apply; arrowing through options changes nothing until Apply is operated. Streams above the capability ceiling are present, disabled, and state the reason; none is hidden. The advisement is **visible text adjacent to the control** and says the same thing as the accessible description. The control is reachable and operable in all four streams, and on `ROUTE-HOME`'s first frame in every stream including `S-HIGH`, where the canvas has not been entered. Applying a change announces politely without interrupting, does not move focus within a shell, and preserves scroll, open panel, and route. Crossing the semantic boundary, focus lands on the destination shell's stream control — the same control by role and name, reporting the new stream — and never on the document body; the outgoing shell leaves the accessibility tree before the incoming shell is added. Booking process state survives every crossing including the semantic one: a held slot, a verified email, and entered values are all still present, with nothing re-entered. Where process state cannot be carried, the change is refused and explained under `ACT-11` and the visitor keeps their work. Fail on any silent reset, any hidden ceiling-excluded option, any advisement available only to assistive technology, and any automatic canvas entry. |

## 5. Research plan and priority

**[PROPOSED UX]** Before visual UI design approval, conduct concept-neutral
journey tests with representatives of the approved buyer roles plus keyboard and
screen-reader users. Prioritize comprehension and recovery over preference:
service/sector fit, proof classification, semantic/World parity, direct booking,
AI refusal/source behavior, email verification states, no-slot/pending recovery,
and staff separation. Sample size, recruitment, compensation, segmentation, and
success thresholds require an approved research plan and are not invented here.

## 6. Human gates and non-decisions

- MA-002: legal/controller/contact, exact consent/privacy wording, analytics
  retention/suppression, legal-record mappings, deletion/tombstone/provider scope.
- MA-003: cases, demos, experts, claims, images, owners/backups, biographies,
  rights, consent and six insight reviewers.
- MA-004: existing GLB provenance/rights; reference only meanwhile.
- MA-005/MA-007/MA-010: provider capability, entitlement, region and paid envelope;
  UX does not select or claim availability.
- MA-006: booking mailbox, calendar/no-slot/reschedule/cancel policy, Entra groups,
  owners/backups, Teams consent, authoritative attendance/status source.
- MA-008/MA-009: domain and webmaster ownership/actions.
- MA-011: defense remains absent, not merely hidden.
- MA-013: compatibility inventory remains a separate awaiting-human gate and does
  not block this UX definition; no dependency version is selected here.
- Numerical conversion/attendance/verification/parity targets, response times,
  attribution windows, lead scoring, sales/CRM qualification, localization rollout,
  and public empty-collection decisions remain unapproved.

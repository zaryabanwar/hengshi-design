# States, Errors, and Recovery

## State language contract

**[APPROVED]** Success is stated only after the authoritative predicate passes.
Pending is not success. Error text identifies what happened, what was preserved,
and the next safe action without exposing secrets, personal data, provider detail,
account existence, or unsupported response promises. **[PROPOSED UX]** Loading
uses a text status and, when content is already valid, preserves readable prior
content instead of replacing it with a blank shell.

## Action contract matrix

Every named visitor/staff action has success, error, and recovery here.

| Action ID / action | Success state | Error/empty/pending state | Recovery |
|---|---|---|---|
| ACT-01 Open primary navigation | Destinations visible; focus enters menu | Control fails/JS absent | Semantic links remain in initial HTML; reload/skip link; focus returns on close |
| ACT-02 Open canonical route | Complete active-release document, H1 and context | loading; offline; 404 unknown; 410 retired; release unavailable | cached/prior truthful content if approved; retry; directory; nearest relevant canonical; Home/Book |
| ACT-03 Open directory/search | Search and browse groups available | index loading/unavailable; focus failure | static active-release directory; Quick Access; restore invoker focus |
| ACT-04 Submit search | Canonical result list | empty query; no results; derived index/checksum failure | browse categories; clear; static directory; never search draft/private data |
| ACT-05 Open result/room | Canonical document or optional directed transition | closed room; missing asset; stale result | canonical semantic route; Quick Access with safe context |
| ACT-06 Enter optional World | onboarding or stable Reception | unsupported WebGL; low power; loader/asset/network error | Quick Access immediately; retain source route/wing context |
| ACT-07 Skip intro/guide | Stable Reception or chosen semantic destination | transition interrupted | jump to stable end state; announce location |
| ACT-08 Navigate immersive destination | Directed point-and-click transition and location update | transition/asset/memory/thermal failure | cancel motion; stable current location; quality downgrade or canonical route |
| ACT-09 Toggle quality | Labeled quality state applied | unsupported tier/change failure | prior stable tier; low power; Quick Access; no content loss |
| ACT-10 Toggle audio | Explicit muted/unmuted state | media unavailable/blocked | remain muted; text/visual equivalent; retry only after interaction |
| ACT-11 Toggle accessibility/reduced motion | Stable authored equivalent | preference cannot persist | apply session state; explain persistence failure without blocking |
| ACT-12 Exit World | Current canonical semantic route opens | missing mapping | Services/Home/Quick Access; report safe fallback |
| ACT-13 Open source/evidence | Accessible active canonical source | source held/retired/unavailable/checksum mismatch | cannot-verify label; related approved source; human/Book |
| ACT-14 Start AI | Identified anonymous session and consent choice | policy/provider/session unavailable | semantic content; available human; Contact; Book |
| ACT-15 Choose AI retention consent | Ephemeral or approved consented state | exact policy unavailable; record write unknown; declined | fail to ephemeral/no-retention; retry consent only when authoritative; browsing/Book |
| ACT-16 Send AI message | Sourced answer or explicit safe refusal | typing/send timeout; duplicate; grounding unavailable | show not-sent/unknown; status-check; safe retry once; human/Book |
| ACT-17 Resume AI | Same valid session resumes once | expired/invalid/checksum/policy mismatch | new ephemeral session; explain old content not resumed; human/Book |
| ACT-18 Request human | One durable handoff request | no explicit availability; duplicate; console outage; alert failure | preserve request if durable; status refresh; Contact/Book; alert retry is staff-side |
| ACT-19 Opt into voice/video | Media begins after explicit permission | declined/denied/unsupported/device failure | text continues; permission guidance; Book; never reactivate automatically |
| ACT-20 Start booking | One booking lineage and accessible non-WebGL qualification flow | transactional scripting/booking entry unavailable | semantic page states not started/not completed; retry Book; verified Contact without promise; preserve non-sensitive route/wing context only |
| ACT-21 Submit qualification | QUALIFICATION_COMPLETE | missing/invalid field; consent declined; offline | linked summary and field correction; browsing/ephemeral help; no retained lead |
| ACT-22 Issue email challenge | EMAIL_PENDING in same lineage | not issued; unknown; provider/Redis/rate-limit failure | status check before retry; bounded later guidance; change address; no slot access |
| ACT-23 Resend challenge | New current challenge, same lineage | too soon/limit/unknown/delivery failure | approved wait guidance; status check; corrected address; no second lineage |
| ACT-24 Correct email | Old challenge invalidated; new challenge pending | invalid syntax; update conflict | correct inline; refresh authoritative lineage; no verified carryover |
| ACT-25 Verify email | VERIFIED | invalid/expired/used/wrong lineage/undeliverable | safe resend/current challenge; corrected address; support path; no slot access |
| ACT-26 Load availability | Eligible 30-minute slots in explicit visitor-local zone | loading; none; stale; owner/provider/Graph unavailable | retry/next period; honest no-slot; approved human/Contact; no promise |
| ACT-27 Select slot | SLOT_SELECTED and review summary | slot no longer available; timezone changes | refresh; reselect; show same instant/zone clearly |
| ACT-28 Submit booking | One BOOKING_PENDING durable request | offline before accept; duplicate; timeout/ambiguous provider state | explicit not-submitted or pending; same idempotency key; reconcile before retry |
| ACT-29 Refresh booking status | CONFIRMED_QUALIFIED or truthful pending/failed | status service unavailable | retain last authoritative state; retry later/approved support; never infer success |
| ACT-30 Reschedule | Same lineage with reconciled replacement occurrence | expired auth; no slots; timeout; race/conflict | reauthenticate; keep old confirmed truth; refresh/reconcile; approved support |
| ACT-31 Cancel | Reconciled CANCELLED | expired auth; provider timeout; conflict | retain last confirmed state; refresh/reconcile; never claim cancelled early |
| ACT-32 Submit contact | One truthful accepted/pending contact record | invalid; offline; duplicate; channel unavailable | correct; same idempotency identity; verified alternate channel/Book; no SLA |
| ACT-33 Staff sign in | Authorized role session | Entra unavailable; no/ambiguous group; local account dormant | deny by default; approved support/break-glass process only; no credential hints |
| ACT-34 Save draft | Durable draft version saved | validation/network/session conflict | retain current text only under approved policy; reauth; merge/version choice without overwrite |
| ACT-35 Submit for review | Immutable review candidate queued | missing evidence/rights/owner/metadata; stale version | linked issue list; return to draft; resubmit new version |
| ACT-36 Reviewer decision | Independent pass or changes requested | unauthorized/self-review/stale candidate/session failure | deny; refresh current candidate; reassign through approved policy |
| ACT-37 Founder decision | Approved/rejected/requested changes on current candidate | unauthorized/stale/not specialist-passed | deny; refresh; return to review queue; do not infer approval |
| ACT-38 Render/index candidate | Valid immutable candidate checksum | render/index/schema/sitemap/AI/3D parity failure | previous release active; correct through workflow; rerun full validation |
| ACT-39 Activate release | One atomic active checksum | partial/timeout/mismatch | no activation or rollback to prior active; reconcile; never mix release surfaces |
| ACT-40 Clear preferences/session | Non-sensitive preferences cleared/session ended | storage unavailable | session state cleared as far as possible; explain local limitation; no account claim |
| ACT-41 Declare staff available | Durable approved-scope availability on | pending/role/eligibility/Redis/Teams issue fails unavailable; no scope empty | status-check; retry; no presence-derived availability |
| ACT-42 Withdraw staff availability | Durable availability off | pending/error/already-off | fail safe to unavailable; idempotent status-check/retry; queued work remains visible |
| ACT-43 Triage handoff queue | Current authorized request detail opened | queue loading/unavailable/stale; truthful empty | refresh authoritative request; reauthenticate; no chat data in analytics |
| ACT-44 Accept text conversation | One authorized operator owns `text_active` | pending/stale/already accepted/consent invalid | reconcile current owner/status; no duplicate acceptance; visitor keeps Book |
| ACT-45 Decline text conversation | Durable declined/reassignment-needed state | pending/stale/unauthorized/already resolved | refresh; approved reassignment/closure later; never delete request |
| ACT-46 End text conversation | Durable ended state once | ending pending/session/retention conflict | status-check; preserve authoritative active/ended truth; Book/Contact remains |
| ACT-47 Retry failed alert | Alert delivered or exception closed without changing core record | adapter unavailable/retry pending/no exceptions empty | retry/escalate under later policy; handoff/booking truth preserved |
| ACT-48 Assign or reassign work | One current eligible assignment | stale/conflict/no eligible assignee/unauthorized | refresh/hold; later approved escalation; no invented availability |
| ACT-49 Reconcile booking | Local/external state agrees truthfully | ambiguous/provider unavailable/mismatch/no exceptions empty | refresh/compare/approved retry after ambiguity; preserve last authoritative state |
| ACT-50 Handle booking exception | Invariant restored or exception held/escalated | pending/unauthorized/unsupported resolution | approved bounded repair or escalation; never hide duplicate/unknown |
| ACT-51 Record evidence/SEO review | Specialist pass or changes requested on exact candidate | self-review/stale/unauthorized/missing evidence/no candidates empty | deny; refresh; return candidate to author; no activation |
| ACT-52 Record knowledge review | Grounding bundle passed or changes requested | draft/private/defense/stale/missing source/unauthorized/no candidate empty | fail closed; return to release workflow; no publication/activation |
| ACT-53 Inspect audit | Authorized redacted event chain visible | index loading/unavailable/integrity gap/no results empty/unauthorized | durable retrieval/refine/retry/escalate; inspection audited; no edit/delete |

## System and dependency state matrix

| Surface/dependency | Loading/empty | Failure/degraded | Integrity/permission concern | Required recovery |
|---|---|---|---|---|
| Semantic public HTML | meaningful server content; skeleton only for optional modules | network/offline/5xx | wrong/missing checksum or draft marker | fail closed; prior approved/cached truth if allowed; retry/Home/directory/Book |
| Collection: Work | approved honest empty only; otherwise held/unindexed | content service failure | prototype seed/unverified case appears | remove/quarantine; previous release; never relabel Demo |
| Collection: Demos | approved honest empty only; otherwise held/unindexed | content service failure | seed/ambiguous client-style item appears | quarantine; previous release; require ownership/provenance |
| Insights/Experts | useful approved empty/held state | derived index missing | anonymous/unverified reviewer/person | block detail/publication; show no invented profile/byline |
| Trust | no approved topics -> held/unindexed | evidence unavailable | requirement/target shown as implemented assurance | block claim; visibly distinguish requirement/control/test/limitation |
| Directory/search | static browse is baseline | Redis/search index unavailable or stale | private/draft/defense result | fall back to static release directory; quarantine mismatched result |
| WebGL renderer | loader with semantic escape | context loss/crash/device loss | room/release content mismatch | Quick Access; retain route/wing; mismatch blocks panel/activation |
| 3D asset | progressive loading and labeled placeholder | 404/decode/license/LOD/material failure | provenance not approved | no geometry reuse; semantic route; visual-reference boundary MA-004 |
| Audio/media | off by default; audio transcript; prerecorded captions; SC 1.2.3 applicable description/media alternative; separate SC 1.2.5 audio description for applicable prerecorded video; live captions when live media offered | autoplay block/device/caption/description failure | missing rights or required alternative; complete media alternative alone cannot replace SC 1.2.5 description | stay muted; hold media activation/publication; record valid applicability evidence; semantic content/text help/Book remain |
| AI session | connecting/typing status | provider timeout/unavailable | no approved provider for data class; grounding mismatch | fail closed; cannot verify; new session/human/Book; never unsafe failover |
| AI answer | sources loading independently | source unavailable | unsupported/conflicting/private source | label cannot verify; omit claim; approved source/human/Book |
| Handoff console | requested/queued/pending | console unavailable | no explicit staff availability | no false live state; Contact/Book; durable retry if request accepted |
| Teams alert/presence | alert pending; presence may suppress | alert/presence unavailable | presence alone implies availability | durable console truth; retry alert; show unavailable |
| Booking qualification | blank form is not empty content | validation/offline | extra required field/hidden scoring | exact fields only; correct/continue browsing; no retained lead |
| Email challenge | pending | issue/delivery/expiry/rate-limit failure | challenge from wrong lineage or stale address | status-check; same-lineage resend/correction; no slot eligibility |
| Availability/Graph | loading with explicit timezone | none/timeout/permission/provider outage | stale/ineligible owner/backup slot | invalidate list; refresh/later/human; no promise |
| Durable booking/outbox | BOOKING_PENDING is truthful | timeout/duplicate/partial write | external/local mismatch | idempotency; reconcile; one lineage; no confirmation until agreement |
| Calendar/meeting | confirmation only after reconcile | ambiguous/duplicate/missing record | unverified email created event | block/flag; reconcile/remediate; never hide duplicate |
| Reschedule/cancel | pending with prior truth visible | timeout/race/expired authorization | second lineage or false cancelled | serialize/reconcile; preserve original lineage and last confirmed state |
| Redis | optional/ephemeral state may be unavailable | presence/rate/cache/lock degraded | used as durable truth | fail closed/degrade; PostgreSQL remains truth; no false availability |
| PostgreSQL/API | bounded loading | unavailable/timeout | fallback to SQLite/mutable cache | no write/success claim; retry/recovery process; no silent alternate truth |
| Offline | prior semantic content may remain readable | actions cannot reach durable acceptance | local PII persistence or hidden queue | explicit not submitted; no local sensitive queue unless later approved |
| Staff auth/session | sign-in/reauth pending | Entra outage/idle/absolute expiry | missing/ambiguous role; CSRF failure | deny; reauth; approved break glass only; no state change on failure |
| Staff review queue | truthful zero-item empty state | query failure | cross-role/self-approval or draft leakage | refresh/deny; preserve separation; no public exposure |
| Staff operations queues | truthful empty by operation; current durable item/version | queue/index/Redis/Teams/Graph unavailable; stale conflict | missing/ambiguous role or derived state presented as truth | deny/degrade to durable retrieval; status-check; hold/escalate under later policy; audit every action |
| Publication render/index | candidate pending | any component fails | mixed checksums/draft marker | previous approved release active; fix through workflow; full rerun |
| Analytics | no baseline is truthful | event pipeline loss | PII/chat/raw query/IP/secret or small cohort leakage | drop/quarantine payload; reporting shows incomplete/unknown; privacy review |
| Retention/deletion | request pending | one in-scope system fails | unmapped provider/record class | remain pending; do not claim completion; MA-002 matrix decision |

## Form, status, and session behavior

- Required indicators are textual and announced before entry; optional budget is
  visibly optional. No required field is represented by color or asterisk alone.
- Error summaries receive programmatic focus after failed submission and link to
  field errors. Errors explain correction, preserve unaffected approved values,
  and never clear a whole form unnecessarily.
- Validation never exposes whether an email/account exists beyond the current
  booking lineage. Verification/rate-limit detail remains bounded by later security policy.
- Pending actions disable only the duplicate action, keep navigation/exit usable,
  expose status, and use idempotency rather than relying on disabled UI alone.
- Applicable booking/contact/consent fields expose correct programmatic input
  purpose and autocomplete tokens. Email=`email`, organization=`organization`,
  and role=`organization-title` when role means job title; domain-specific fields
  do not receive invented tokens.
- Data already supplied in qualification, email correction, review, reschedule,
  cancellation, or staff work is auto-populated/selectable within the same process
  unless a documented WCAG 3.3.7 exception applies. Review/correction/confirmation
  precedes data-changing submission.
- Booking verification and staff authentication/reauthentication allow paste,
  password managers, and assistive mechanisms or an equivalent accessible method;
  no unaided memorization/transcription, puzzle, or cognitive-function test is
  required. Exact provider/challenge selection remains gated.
- Every user time limit is removable/adjustable, or provides at least 20 seconds
  warning and a simple extension available at least ten times, unless a documented
  valid WCAG exception applies. Exact security values remain gated. Expiry denies
  protected action, preserves entered data/last authoritative state where allowed,
  and offers accessible reauthentication; there is no silent extension.
- Browser back/refresh and duplicate tabs retrieve authoritative lineage/candidate
  state. Stale views cannot overwrite or approve a newer version.

## Pointer, motion, update, and timeout behavior

- All control families—including navigation, search, HUD, consent, AI/handoff,
  booking/media, and staff actions—activate on pointer up or provide equivalent
  abort/undo. Moving away before release cancels without the action firing.
- Accessible names contain visible label text. Every drag interaction has a
  single-pointer non-drag control and keyboard equivalent.
- Targets measure at least 24 by 24 CSS px at 100% zoom, or the implementation
  records the exact WCAG spacing, inline, equivalent-control, user-agent, or
  essential exception and its measurement.
- Automatic moving, blinking, scrolling, or auto-updating content that begins
  automatically and lasts more than five seconds provides pause, stop, or hide
  through keyboard and assistive technology unless a documented valid exception
  applies. Pausing never falsifies authoritative status; a manual refresh remains.
- No content exceeds three flashes in any one-second period. Flash analysis covers
  all standard/reduced modes, media, loading, errors, focus, and immersive effects.
- Controlled-clock tests inventory every arrival, AI/session, challenge, booking,
  media, and staff timeout; prove adjust/warn/extend or record the valid exception;
  preserve entered data/authoritative state and complete accessible reauthentication.

## JavaScript failure boundary

Complete initial semantic content and a direct Book link are available before
JavaScript. The complete transaction is accessible and non-WebGL, but the exact
progressive-enhancement transaction architecture is deferred. If required script
fails, no lineage/challenge/write/pending/confirmation is inferred: the semantic
page reports booking unavailable or not completed, preserves only approved
non-sensitive route/wing context, and offers Book retry or verified Contact.

## Recovery priority

1. Protect data, publication, claim, permission, and booking integrity.
2. State the last authoritative truth: not submitted, pending, confirmed, held,
   unavailable, cancelled, or unknown.
3. Preserve non-sensitive context and already approved content.
4. Offer the smallest safe next action: correct, status-check, retry, refresh,
   reauthenticate, Quick Access, human/Contact, or Book.
5. Escalate operationally without inventing a visitor-facing owner or SLA.

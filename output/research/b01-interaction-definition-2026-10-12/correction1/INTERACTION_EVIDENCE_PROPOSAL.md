# Hengshi Design v1 — B01 interaction evidence proposal

Status: DOING. Correction1 prepared 2026-10-12; direction decision and independent review required. No external construction or application feature is released.

## Evidence and controlling scope

The [native-agent census](../../figma-web-agent-2026-10-12/prototype-census/census.json) reports a complete Page1 traversal of7801 descendants,7799 nodes with a reaction property, zero nonempty reactions and an empty flowStartingPoints array. One requested starting-node lookup is unsupported, not null/absent proof. Reports are non-atomic AI assertions. [Native editor inspection](../../figma-web-agent-2026-10-12/prototype-census/native-prototype-panel.png) separately shows the existing390px directory frame with Add action/Add flow starting point controls and no existing interactions displayed; it does not independently certify the entire page or a tested write capability.

D-075 and production-contract WS-P-04 include B01 prototype evidence. EC-05 requires interaction/focus demonstration; EC-07 excludes TEST_CAPTURE. The three templates remain TPL-GLOBAL-NAVIGATION, TPL-DIRECTORY-SEARCH and TPL-SYSTEM-RECOVERY. Full host/state/stream/viewport/mode allocation remains unchanged; this proposal does not reduce it or release B02–B09. Keep existing frames, components, source masters, accepted palette/copy and archive protected. The later runtime implementation must separately establish real DOM, pointer, keyboard, assistive-technology, privacy and timing behavior.

## One unresolved interaction choice

PRIM-004 and the directory template explicitly allow a dialog or nonmodal panel. DF-01 fixes opening on the labeled search input and closing to the invoker but does not select modality. The existing full-page seed is not evidence that this choice was accepted.

Recommend an explicitly opened modal directory: centered responsive sheet on wide screens, full-width sheet on narrow screens, same semantics and visible Close throughout. Page/World context is retained; it is never a homepage gate or automatic popup. Only the open directory is operable until dismissal. Include Book inside it; after choosing a canonical destination, follow the destination heading-focus contract. Where the invoker disappears, document the logical current-shell fallback. Keep the complete semantic static directory available without this overlay or JavaScript. World consumers remain B07, not an implemented B01 camera/movement change.

Alternative: a nonmodal in-page panel with the surrounding page still operable, normal document Tab order and no focus trap. It also preserves close-to-invoker and semantic fallback. Choosing it changes the directory's focus/interaction annotations; do not silently mix modal and nonmodal behavior across widths.

This is a proposed interaction direction, not accepted appearance or a new scope. Founder direction is needed before preparing its exact external-write batch. Independent review and the existing external-write gate still follow.

## Required interaction scenarios

Every row is design evidence, using synthetic fixture text. Its actual Figma frame/control IDs and reviewed source bindings must be resolved before construction; seed IDs alone are not hotspot identities. Planned sequences show the intended focus state without claiming a real browser focus loop. A missing source, destination, profile or bound keeps that row TODO.

| ID | Template / controlling source | Sequence and inspection requirement |
|---|---|---|
| B01-P01 | Navigation; ACT-01, PRIM-002 | Closed → explicit open → destinations → Close/Escape → invoker. Show focus entry/return, expanded state and persistent Book. |
| B01-P02 | Navigation; UXTEST-021/022, design §8 | Keyboard traversal in authored order, visible focus, no unintended trap; Enter/Space activate disclosure. Separate a simulated key trigger from later native Tab behavior. |
| B01-P03 | Navigation; design §10, UXTEST-039 | Pointer-down followed by cancel/exit produces no navigation; completed activation alone opens or navigates. Touch non-drag equivalent is shown. |
| B01-P04 | Navigation; ACT-02 | Clean canonical destination and changed-heading focus. Use a marked boundary fixture; actual B02 route content is not built here. |
| B01-P05 | Navigation; PRIM-014 | Book is reachable with the narrow menu closed and open. End at a marked B06 boundary fixture, without a real booking or publication claim. |
| B01-P06 | Directory; ACT-03, DF-01, PRIM-004 | Explicit open → labeled input → clear/browse/Close → invoker, applying the chosen modality consistently. If modal: show contained focus, inert background, Escape and visible Close; if nonmodal: show normal page order and no trap. |
| B01-P07 | Directory; ACT-04, UXTEST-008 | Preset fixture queries show empty browse, loading, results and no results; Clear restores browse. No real search engine, free text inference or raw-query analytics. |
| B01-P08 | Directory; DF-01, PRIM-004 | Index unavailable/offline → static active-release directory; stale checksum refuses activation. A retry or available source is explicit, with no false success. |
| B01-P09 | Stream control; ACT-09, PRIM-001 | Checked pending selection differs from in-force state → deliberate Apply → new in-force state. Retain route, scroll and open panel; show status/focus annotations. Cover every allowed stream. |
| B01-P10 | Stream control; ACT-09, UXTEST-046 | Focus, arrows, Tab, pointer/touch selection, blur and elapsed time never Apply. Only the explicit submit paths change the in-force stream. Diagram native form Enter separately from Figma key simulation. |
| B01-P11 | Stream control; ACT-09 | Above-ceiling option remains visible with textual refusal; no silent substitution, content loss or automatic fallback. |
| B01-P12 | Stream control; ACT-09 | Apply/change failure retains the prior in-force stream and explains failure; selection remains deliberate. |
| B01-P13 | Stream control; ACT-09/11 | Successful session application with preference-write failure states non-persistence honestly; content and Book continue. |
| B01-P14 | Recovery; shared recovery contract | Loading/pending/unavailable/offline/error remain distinct. Explicit status-check or recovery never converts an unknown outcome to success or fabricates availability. |
| B01-P15 | Recovery; shared recovery contract | Stale/conflict → deliberate refresh/reconcile under current truth, retaining context. No duplicate intent or unreviewed retry policy. |
| B01-P16 | Recovery; shared recovery contract | Asset/checksum failure → explicit canonical/Quick Access recovery with safe context. No mid-session silent stream promotion/demotion. |
| B01-P17 | Recovery; D-076/D-078, EC-13 | Approved visitor inactivity warning at least20s before expiry → deliberate More time → permitted new30-minute inactivity deadline; demonstrate at least ten extension opportunities without inventing an absolute conversation limit. Unknown/stale/refused extension outcomes remain distinct fixture branches. |
| B01-P18 | Recovery; visitor-lifetime controls | End/expiry is terminal for that access generation. Recovery does not revive credentials or restore a private process automatically; any new session is explicit. Parent conversation operations remain B05. |
| B01-P19 | Directory/Navigation; design §8/10 | Close returns to the invoker; if the invoker is gone, show a logical shell/heading fallback. No focus loss to the page body or a hidden control. |
| B01-P20 | All three; design §8 | Reduced-motion transitions use stable states without travel, parallax or opacity waits. Any default transition keeps content/action/focus available. |
| B01-P21 | All three; design §8/10 | Show pointer/touch/keyboard equivalence and 320/400%/landscape focus visibility with existing allocation. No physical-phone or assistive-technology claim from Figma. |
| B01-P22 | Recovery; template focus notes | Ordinary status updates announce without stealing focus; deliberate error-summary/route-change focus differs from background recovery. Show smallest safe recovery action. |

## Construction, inspection and exit

1. Resolve each case against the accepted template/primitive/profile/stream allocation and actual current source frame/control IDs. Record exact source checks and refusal conditions; no placeholder ID is an executable target.
2. Prepare isolated file-local prototype copies and annotations, preserving existing source frames/components; apply the mandatory per-stream evidence-ID grammar and v1 product naming. No new file/project, provider Make flow, public link, plugin or account action is included.
3. Use normal editor Prototype controls or a separately approved reviewed MCP batch after provider quota becomes usable. Visible controls establish exposure only. Do not assume the built-in agent can write prototype reactions or that AI credits enlarge MCP quota.
4. For each case, preserve trigger/action/destination and flow-start metadata, annotation references and native edited-source inventory. Inspect actual Presentation paths, cancellation, return and transition fixtures; screenshot strips alone do not prove interaction.
5. Keep the full contracted allocation. Reuse only under its approved bounding-frame/annotation rules; do not replace required distinct critical states by one generic interaction loop.
6. Export native editable and provider-independent evidence; inspect restore separately. Obtain independent design/accessibility review, bounded revision and founder B01 pilot acceptance before later batches. No application TEST_CAPTURE or Phase1 acceptance follows.

Primary guidance checked2026-10-12: [Figma reactions](https://developers.figma.com/docs/plugins/api/properties/nodes-reactions/) and [PageNode flow points](https://developers.figma.com/docs/plugins/api/PageNode/) describe prototype data. Context7 /websites/developers_figma was queried for read-only reaction traversal; its generic GET/endpoint formatting is not an HTTP contract. [WAI modal guidance](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/) supports contained focus, background inactivity and return; [disclosure guidance](https://www.w3.org/WAI/ARIA/apg/patterns/disclosure/) supports explicit expansion controls. These guide the proposal; they establish no implementation, conformance or founder acceptance.

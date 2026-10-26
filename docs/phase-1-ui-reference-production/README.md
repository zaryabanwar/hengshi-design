# Phase 1 UI reference production — v1

## HSD-001 homepage and shared navigation

The founder's 2026-10-26 execution prompt authorizes additive design in the
existing Figma file, followed by one independent design review, corrections and
visual acceptance before implementation. Reuse accepted Signal Ledger + Framework
Relay assets, D035 tokens and existing components; Inter is a Figma-only fallback.
The reference set must show a complete 1440px desktop and 320px mobile homepage,
shared navigation and its open/focus/search states, the five formal service wings,
Agriculture/Mining context, distinct Work and Demos, direct 30-minute discovery
booking, optional World entry and truthful missing-evidence/asset treatments.
Inspect editable layers, readable wrapping, navigation coverage, mark fidelity and
actual pixels. Annotate semantic order, keyboard/dismissal/focus return and static
reduced-motion behavior; design evidence does not establish runtime accessibility.
Preserve B01 references and the protected app/GLB. The initial design-only task
excluded implementation, publication, paid activation and Git delivery. On
2026-10-26 the founder accepted the complete reference set presented below and
explicitly authorized local implementation of the accepted homepage and shared
navigation. Upgrades, commits, publication and deployment remain excluded.

Interaction contract for this reference: source order is skip link, header/nav,
main (one H1, then section H2s), optional World link, contact and footer. The skip
link appears on keyboard focus and moves focus to main; route changes focus the
new page heading. Menu is a nonmodal disclosure: Enter/Space toggles it, Tab follows
visible destinations, and Escape/Close menu closes it and returns focus to Menu.
Closed destinations leave the tab order. Search/Directory is an ordinary canonical
directory link, not a modal or a claim of live results; its route heading takes
focus. Book links directly to `/book` without chat/World prerequisites. Focus uses
the shown 2px D035 cyan outline on Ink (light-surface cyan uses cyan-light).
Reduced motion is the complete static composition; essential content never waits
for animation. Missing-mark treatment retains the full name, navigation and Book.
These are implementation requirements, not verified browser behavior or WCAG proof.

Saved editable references (2026-10-26, [existing Figma file](https://www.figma.com/design/GOmLP6Cv96l768ueSrZ5Dg)):

| Reference | Node | Inspected size/state |
|---|---|---|
| [Desktop homepage](https://www.figma.com/design/GOmLP6Cv96l768ueSrZ5Dg?node-id=246-7658) | `246:7658` | 1440 × 3783; restored brand headline and complete actual export inspected |
| [Mobile homepage](https://www.figma.com/design/GOmLP6Cv96l768ueSrZ5Dg?node-id=246-7883) | `246:7883` | 320 × 5723; restored brand headline and full export inspected at native width |
| [Shared mobile states](https://www.figma.com/design/GOmLP6Cv96l768ueSrZ5Dg?node-id=243-4391) | `243:4391` | Closed `246:8214`, open `243:4392`, focus `243:4436`, missing mark `247:4052` |
| [Desktop keyboard specimen](https://www.figma.com/design/GOmLP6Cv96l768ueSrZ5Dg?node-id=247-4020) | `247:4020` | Focused skip link; all desktop destinations retained |
| Exact Framework Relay source | `246:3890` | Imported accepted 80-unit SVG; seven editable vector shapes |

One independent static design review inspected the complete homepage exports and
mobile states. Its desktop keyboard and missing-asset gaps were corrected and
their actual exports inspected. On 2026-10-26 the founder rejected the generated
page copy as unfriendly and obnoxious in tone, including "all destinations",
"no AI conversation needed", "five service wings" and "one connected conversation".
The rejection applies to the page copy generally. The founder's subsequent
"continue" authorizes the copy rewrite. Natural, respectful visitor language and
concrete services replace internal architecture and process commentary.

The founder rejected the replacement H1, "Build the products and systems your
business needs.", on 2026-10-26. It was replaced in both saved homepages with the
accepted D-026 brand promise, "From complex ambition to accountable delivery.",
at existing text nodes desktop `246:7694` and mobile `246:7933`. Native browser
editing and actual exported pixels verify this correction. Reusing the accepted
brand line originally left visual acceptance open. The founder subsequently
accepted the presented homepage treatment, supporting copy, layout and navigation
set on 2026-10-26; this does not approve unseen destination pages or publication.
The introduction explains digital products, AI and business systems; section
headings include "How can we help?", "Explore ideas for your industry" and "How
we'll work together". Actions use "Book a call", "View services" and "Contact us";
the 30-minute call remains explicit. Work and Demos retain short, separate honest
empty states. Accepted identity and formal service names remain unchanged; this
is accepted reference messaging, not a change to the D-026 brand-strategy definition.

MCP applied the revised supporting copy to both existing homepages and shared
navigation, including managed button-instance labels. Readback confirmed native
text, components, Auto Layout, Inter/Cascadia Mono and no image-filled nodes in
either homepage. The included Starter MCP limit stopped mobile screenshot
retrieval; no extra allowance or paid activation was used. After the founder's
full app restart, fresh browser inventory exposed the authenticated Figma tab.
The setting/tool mismatch was resolved without settings or credential changes.
Native browser editing restored both headline nodes, and all four current
references were exported and visually inspected on 2026-10-26:

- `artifacts/hsd-001/final-reference/desktop.png` — 1440 × 3783.
- `artifacts/hsd-001/final-reference/mobile.png` — 320 × 5723; the full export
  was also inspected in four contiguous native-width strips in
  `mobile-inspection.png` (cuts are presentation only, not page breaks).
- `artifacts/hsd-001/final-reference/navigation.png` — 740 × 930 source set:
  320px closed/open/focus/missing-mark specimens, all route labels retained.
- `artifacts/hsd-001/final-reference/desktop-keyboard.png` — 1440 × 165,
  focused skip-link specimen with complete desktop navigation.

No text clipping, section overlap or horizontal overflow was observed in these
exports. Full formal service names, Agriculture/Mining, distinct truthful Work
and Demos empty states, 30-minute booking and optional World entry are retained.
The exact imported Framework Relay source and existing token/component bindings
remain in use. Existing B01 references were preserved; Search reuses the existing
canonical Directory reference rather than duplicating it.

One independent review covered the coherent composition and navigation; its
missing desktop keyboard and missing-mark specimens were corrected and inspected.
The later copy and accepted-brand-line corrections received the scoped full-page
and navigation inspections above. Earlier rejected exports remain historical
files in `artifacts/hsd-001/`; only `final-reference/` contains the current set.

### Accepted reference implementation — local only, 2026-10-26

Status: DOING; design acceptance and scoped local implementation are verified,
while commits remain deferred. The founder explicitly answered "Yes—implement the
accepted homepage and navigation locally". The additive `apps/web/site/` entry
preserves the existing application, `/world` prototype, GLB and dependency lockfile.
Only four additive npm scripts change `apps/web/package.json`; no dependency or
provider was selected/upgraded. The existing local React 18.3.1/Vite 5.4.21 graph
was exercised for this local slice, not qualified as the latest production graph.

- `npm run site:build`: TypeScript plus Vite client/server builds; React renders
  the complete approved homepage into initial HTML, then hydrates the same tree.
  [Vite 5 SSR](https://v5.vite.dev/guide/ssr) and [React 18 rendering](https://18.react.dev/reference/react-dom/server/renderToString)
  were checked through Context7 and official docs; installed APIs were inspected.
- `npm run site:preview`: loopback-only `http://127.0.0.1:5174/`; the local entry
  carries noindex/nofollow and unknown destinations return genuine 404s. It is not
  connected to publication, live booking, AI, a content API or the World runtime.
- `npm run site:dev`: semantic dev rendering on the same port (stop preview first).
  Development HTTP readback also confirmed complete initial HTML and noindex.
- `npm run site:test`: nine Chromium browser tests pass against the built site:
  no-JavaScript content/navigation, approved primary-route targets, keyboard
  disclosure/close/Escape/focus-return/resize, skip-link focus, exact SVG bytes and
  32px geometry, early image failure, 320/768/1024/1440 reflow, reduced-motion
  composition, desktop/mobile/open-menu axe scans and truthful unknown-route 404.
  Automated axe results are not WCAG conformance or full assistive-tech proof.
- Existing prototype regression: both smoke tests passed; both axe tests passed on
  a focused single-worker retry after the first run timed out during page loads.
  No prototype source, test expectations or lockfile was changed to obtain this.

Actual built-site screenshots are in `artifacts/hsd-001/local-implementation/`:
`homepage-1440.png`, `homepage-320.png`, `mobile-menu.png`,
`mobile-missing-mark.png`, and the contiguous-strip `mobile-inspection.png`.
The complete exports and live browser menu/Escape behavior were inspected.
Production typography remains the approved system and evidence-monospace stacks;
Inter is not shipped, so platform font metrics differ from the Figma fallback.
The exact accepted SVG is imported unchanged and original brand JSON supplies
colors/font stacks. The missing-artwork handler also checks errors that precede
hydration; its focused browser reproduction passed after the correction.

The initial homepage, responsive navigation and local behaviors are implemented.
Search and accessibility utility URLs (`/directory`, `/accessibility`) are
reversible local route targets for the accepted utility labels; they are not
claims of implemented utility pages. Canonical destination pages, booking,
content/admin/publication and 3D remain future assigned increments. No unseen
screen, fake booking confirmation or fabricated evidence was added. No commit,
push, deployment, account change, Figma overwrite or active-goal change occurred.

## Current authority — reconciled 2026-10-25

D-097 supersedes the universal B01/Phase1 sequencing gate and numeric correction
limits. Reuse existing B01 references/evidence; allocate all required template,
state and profile coverage to the relevant 2D or 3D increment. An assigned 2D
surface does not wait for unrelated B01 trial mechanisms or future World designs.
Scope-specific visual acceptance, required design review and external-write
permission remain. Historical frozen contracts below retain their old wording;
interpret their scheduling/correction restrictions through D-097.

MA-025 was accepted on 2026-09-06. Read the [decisions](../../DECISIONS.md),
[current constitution](../../.specify/memory/constitution.md) and
[reconciliation map](../software-definition/04-reconciliation-map.md) before the
preserved pre-approval contract below. Its old awaiting-approval and provider
availability statements are historical observations, not current instructions.

| Subject | Controlling source |
|---|---|
| Definition authority | D-037/MA-024 and accepted amendments govern the [reference-design package](../phase-1-ui-reference-design/README.md). D-045's stream model, D-061's quality closure and D-063's exact source-bound approval retain their own scope. |
| Production permission and sequence | D-075 permits B01 execution in the existing private [Hengshi v1 file](https://www.figma.com/design/GOmLP6Cv96l768ueSrZ5Dg), with Page 1/file-local components. [Production authority](UI_REFERENCE_PRODUCTION_CONTRACT.md#01-controlling-authority) and the [batch plan](batch-production-plan.csv) preserve pilot acceptance and separate B07/B09/MA-026 prerequisites. |
| Actual references and inspections | The [B01 brief](B01_EXECUTION_BRIEF.md) owns current created-reference coverage, exact receipts and bounded review claims. Its [directory checkpoint](B01_EXECUTION_BRIEF.md#current-directory-checkpoint--2026-10-08) includes the successful full-resolution export and independent static-pixel review. These do not establish interactions, accessibility or complete pilot acceptance. |
| Recovery and refusal references | Twelve stream recovery references and eight capability-refusal host views are created under their separate approvals. The [latest existing-view export](B01_EXECUTION_BRIEF.md#fifteen-existing-view-export-result--2026-10-11) supplies the previously missing fifteen native views with bounded independent static PASS. The [combined grammar result](B01_EXECUTION_BRIEF.md#combined-recovery-grammar-execution-result--2026-10-11) adds all48 shared grammar references/native views with bounded independent static PASS. Full host/profile evidence and annotation/editability census remain separate; construction and pixels do not establish runtime behavior or full B01 acceptance. |
| Connection, calls and cost | D-095 governs [current tool routing](B01_EXECUTION_BRIEF.md#calls-costs-and-authority): batch MCP within actual included20-call availability, then use computer control and available included Design agent/Make features within approved scope. Repeated per-call/method prompts are superseded; extra allowance, new scope, destructive cleanup, paid/account/sharing/publication actions retain separate gates. Use the brief and current provider UI for dated included-call availability; earlier exhausted balances are historical. Do not repeat identity/reconnect requests without an actual authentication failure. The [ledger](validation/mcp-call-ledger.csv) owns attempts, separate from actual provider debit; the B01 brief owns dated AI balances/results and browser interruptions. No separate changing count is maintained here. |
| Native evidence and pilot exit | [Capability evidence](validation/capability-evidence.md) retains the verified PRE and dated construction/font observations. The [D-091 browser cleanup result](B01_EXECUTION_BRIEF.md#authorized-browser-cleanup-result--2026-10-12) links preserved before/after native archives with verified hashes/ZIP integrity and bounded original-source checks. It is not _EXIT or a restore test; the actual-result review is separately commissioned. Restore, complete contracted profiles, independent design/accessibility review, _EXIT and founder pilot acceptance remain separate requirements. |
| Timing definition | D-078 accepts the source-bound nine-document correction, now applied and locally verified. The [timing reconciliation](B01_EXECUTION_BRIEF.md#timing-branch-source-conflict--2026-10-09) preserves the earlier conflict and current accepted successor; no repeat decision is needed. Actual timed references and complete-process accessibility evidence remain separate. |

Keep the full [production contract](UI_REFERENCE_PRODUCTION_CONTRACT.md),
[evidence capture plan](evidence-capture-plan.csv), [write scope](external-write-scope.csv)
and [stop conditions](stop-conditions.csv) under current founder authority.
D-097 and each work-chat prompt determine the increment's scope and sequencing.
A construction receipt alone still grants no visual acceptance or implementation
permission; the relevant approved reference and feature contract are required.

Use latest mutually compatible stable dependencies and preserve semantic/World
parity. D-068 defers provider/region/cost selection. Current World/storyboard
amendments require reconciled visual references; composition acceptance does not
accept detailed appearance, asset rights, production measurements or the full
Phase 1 package. Review receipts apply only to their exact frozen inputs.

The [preceding entry](../../output/research/ui-production-entry-consolidation-2026-10-09/README.before.md)
is preserved with its original links interpreted from this directory. This
navigation consolidation changes no contract, design, review receipt or approval.

## Phase 1 evidence and accepted amendments

D-038 accepted MA-025; D-075 releases the bounded B01 execution, not pilot exit
or unseen design acceptance. D-097 now governs increment sequencing.
The old awaiting-human/no-write wording inside the preserved
contract is historical. D-095 supersedes repeated per-call/method prompts within
already-approved design scope; it does not grant extra MCP allowance, paid
activation or new scope. The [B01 brief](B01_EXECUTION_BRIEF.md) owns actual usage,
dated evidence and remaining work. D-094's approved qualification trial remains
separate from complete B01 and Phase1 acceptance.

D-078 supersedes the old extension-duration wording in production-contract §4.3
item 5: the warning branch provides at least 20 seconds to act and at least ten
extension opportunities. The separate pre-start adjustment branch retains its
range rule. Read the accepted [timing/source successor](B01_EXECUTION_BRIEF.md#timing-branch-source-conflict--2026-10-09)
and current [EC-13 capture rule](evidence-capture-plan.csv), preserving the original
contract and frozen reviews as provenance. D-076 visitor inactivity/End policy and
separate staff clocks remain unchanged. This entry introduces no timing policy.

The remaining B01 design evidence is contracted host/state/stream/viewport/mode
coverage, PRIM mappings, fixture-marked annotations and Figma prototypes for focus
return, disclosure, modal and transition behavior. Native editable archives,
provider-independent PNG/SVG/PDF evidence and inventories, restore/_EXIT, distinct
independent design/accessibility reviews and founder pilot acceptance remain.
These requirements are unchanged; small static crop sets do not discharge them.

[Production-contract §4.1](UI_REFERENCE_PRODUCTION_CONTRACT.md#41-evidence-unit-types-in-scope)
and [EC-07](evidence-capture-plan.csv) explicitly exclude TEST_CAPTURE from MA-025:
actual browser/assistive-technology evidence follows application implementation.
A Figma prototype or accessibility annotation cannot establish runtime or WCAG
conformance. Phase 1 must define and design those behaviors; it does not implement
them to obtain a design-production exit. Keep later runtime testing on its later
implementation/launch gates, while retaining all current design requirements.

The [bounded independent navigation review](../../output/research/ui-production-current-entry-2026-10-11/independent-review-entry-v1.json)
passes the eight frozen inputs for this new entry section and the single
reconciliation coverage row, with no actionable findings. It grants no new policy,
production call, implementation or acceptance. Later result/gallery links remain
outside that frozen scope.

## Preserved 2026-09-06 pre-approval snapshot

The following awaiting-human, no-call and unreachable-host statements describe
that historical preparation snapshot. Later accepted decisions and the dated
capability record above supersede them; they are not a fresh approval request or
current tool-readiness audit. The original snapshot body is retained as provenance.

# Phase 1 External UI Reference-Production Contract (MA-025)

**Project:** Hengshi Design
**Package date:** 2026-09-06
**Status:** `awaiting_human` — prepared for founder decision at MA-025
**External-write status:** Not authorized; no Figma or Stitch account, file,
project, comment, export, or API call has been created, read, written, or
attempted

## Purpose

This package is the bounded contract the founder must approve **before** any
external design-provider write may happen. D-037 accepted the UI reference-design
*documentation* contract and explicitly left external production closed. This
package answers the eleven questions that gate must resolve: provider, scope and
sequence, write scope, deliverables, evidence capture, review sequence, cost
boundary, stop conditions, rollback, credential handling, and acceptance criteria.

It creates no screen, no external file, no application code, and no publication.

## Controlling authority

- **D-025** foundation, claims, SEO, 33 routes; `/industries` retained.
- **D-026** Evidence in Motion; evidence-led innovation delivery partner.
- **D-035** frozen Signal Ledger system + Framework Relay logo hybrid; marks
  unregistered and trademark-not-cleared.
- **D-036** the exact Phase 1 UX architecture package.
- **D-037** the exact 13-file UI reference-design freeze, SHA-256
  `97E79201CC36F01718A027AD800E63BDD5AAFC47E41137D65253BAABA6B2120F`.
- **Constitution 2.0.0** principles IV, VII, and VIII.

The D-037 package is the normative input. Where this package and D-037 appear to
differ, D-037 governs and the difference is a defect here.

## Artifact map

| Artifact | Role |
|---|---|
| [MA-025 production contract](UI_REFERENCE_PRODUCTION_CONTRACT.md) | Normative provider decision, batch scope and sequence, write scope, deliverables, evidence capture, review sequence, cost boundary, stop conditions, rollback, credential boundary, and acceptance criteria |
| [Provider evaluation](provider-evaluation.csv) | Criterion-by-criterion Figma/Stitch assessment traced to the accepted contract requirement that drives each criterion |
| [Batch production plan](batch-production-plan.csv) | The nine batches with their MA-025 disposition, execution order, entry and exit conditions |
| [External write scope](external-write-scope.csv) | Eight permitted and eleven prohibited external operations, plus repository and Git scope |
| [Evidence capture plan](evidence-capture-plan.csv) | Thirty evidence, naming, coverage, export, hashing, credential, and claim rules with verification methods |
| [Stop conditions](stop-conditions.csv) | Twelve enumerated halts with escalation target and resume authority |
| [Traceability](traceability.csv) | Forty rows mapping every contract section to its upstream authority and downstream gate |
| [Validator](validation/validate-ui-reference-production.ps1) | Deterministic parsing, exact-set, reference, scope, claim, and gate checks |
| [Validation report](validation/validation-report.md) | Executed command, timestamp, counts, outcome, and limitations |
| [Producer inspection](producer-inspection.md) | Producer scope, completeness, feasibility, and unresolved-gate inspection |

## The two findings that change the shape of this gate

### 1. Only seven of nine batches are authorizable

`design-batch-plan.csv` makes **B07** depend on an approved 3D storyboard and
asset specification and on **MA-004** for GLB reuse. The storyboard workstream is
`not_started` and MA-004 is `blocked`. **B09** hard-requires B07. Therefore:

- **Authorizable now:** B01, B02, B03, B04, B05, B06, B08.
- **Deferred to MA-026:** B07, B09, `docs/ui/UI_SPEC.md`, and the final
  visual-direction decision.

Because B09 produces the evidence index and `UI_SPEC.md`, the D-037 §15 handoff
**cannot complete under MA-025 alone**. Approving MA-025 is not approval of the
whole reference-screen programme.

### 2. Neither provider is reachable from this host today

`AGENTS.md` names `%APPDATA%\Code\User\mcp.json` as the canonical MCP inventory.
That file does not exist here, and no Figma or Stitch MCP is configured or exposed
in any checked location. `docs/software-definition/02-ai-dev-tooling-and-mcp.md`
line 43 claims a Stitch MCP is "Configured locally"; that claim is not true of this
host and is recorded as a correction obligation.

**Approving MA-025 does not by itself make production possible.** One of two
enablement paths (§3.5) must complete first: a human operator working directly in
Figma, or a configured and capability-tested agent path.

## Boundary and non-claims

This package contains Markdown, CSV, and one PowerShell validator only. It does
not create a screen, prototype, component library, external file, or
`docs/ui/UI_SPEC.md`; perform or attempt any provider operation; approve a visual
direction or any exact public or legal copy; assert any Figma free-tier limit
(five are recorded as unverified); certify WCAG 2.2 conformance; or authorize
spend, paid assets, dependencies, migrations, infrastructure, publication, Git
operations, deployment, complete Phase 1 acceptance, or launch.

WCAG 2.2 Level AA for every applicable full page and complete process remains the
normative production and review **target**, never a conformance claim. Design
references and annotations alone cannot establish conformance.

MA-013 compatibility acceptance remains a separate, unaffected gate.

## Review and approval gates

1. Run the deterministic validator and complete producer inspection.
2. Present **MA-025** to the founder. Approval authorizes bounded external
   production for B01–B06 and B08 only.
3. Complete and record §3.5 capability enablement before the first external write.
4. Run B01 as a gated pilot; halt for founder pilot acceptance before B02.
5. Run B02–B08 serially, each exiting on two clean independent reviews.
6. Present MA-026 for B07, B09, `UI_SPEC.md`, and the final visual direction.

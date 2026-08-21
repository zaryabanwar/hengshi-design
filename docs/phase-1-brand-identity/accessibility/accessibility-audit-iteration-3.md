# Brand Identity Accessibility Audit — Iteration 3

**Audit date:** 2026-07-19 (Asia/Karachi)  
**Reviewed version:** Producer iteration 3 of 3  
**Current producer candidate:** Signal Ledger system + Framework Relay logo  
**Authority:** D-006, D-008, D-026, D-027, CR-001  
**Target:** WCAG 2.2 Level AA-relevant identity-definition evidence and semantic/non-WebGL parity  
**Decision scope:** Readiness for a founder decision on the exact hybrid only  
**Verdict:** REVISE

## Independence, scope, and exclusions

This is the one independent accessibility pass for frozen producer iteration 3.
I did not create, revise, approve, or otherwise edit producer artifacts, CR-001,
durable project state, application code, prior reports, or design-review files.
The only repository write made by this audit is this report.

The audit covered:

- the current Framework Relay primary, light, monochrome, reverse, 80-unit,
  24-unit, and 16-unit logo family;
- the retained Signal Ledger identity system and the current/source/superseded/
  historical semantics required by D-027;
- closure evidence for R-020's direct-labelled data series;
- WCAG 2.2 AA-relevant semantics, names/roles, reading order, non-color meaning,
  contrast, keyboard/focus, target spacing, 320 CSS px reflow, text spacing,
  reduced motion, forced colors, grayscale, print, static/non-WebGL, asset
  failure, and full-name-first SEO/entity behavior; and
- 1440, 900, 390, and 320 CSS px board states plus the DPR1 16/20/24/32 and
  rejected-144/supported-168 scale evidence.

This report does not approve or certify the identity, WCAG conformance,
assistive-technology interoperability, trademark/legal clearance, physical print,
production masters, UI/application/WebGL implementation, publication, Phase 1,
Git/deployment, or launch. No external request, dependency install, download,
purchase, credential operation, Git action, deployment, or public write occurred.

## Required authority and freeze

D-026 remains unchanged: **Evidence in Motion**, category **evidence-led
innovation delivery partner**, and promise **From complex ambition to accountable
delivery**. D-027/CR-001 retains the Signal Ledger system, rejects the iteration-2
H-derived Signal Ledger logo, and authorizes only a reconciled Quiet Framework-
derived logo revision. D-008, FR-001/FR-002, SEO-001/SEO-007, and UX-001 through
UX-005 require complete semantic, Quick Access, keyboard, reduced-motion,
non-WebGL, and failure-state equivalence.

### Entry validation

The required command was executed before substantive review:

```powershell
& 'docs/phase-1-brand-identity/validation/validate-brand-identity.ps1'
```

Entry result: **41 passes, 0 failures, `RESULT: PASS`**.

### Contract freeze anchors

| Artifact | Independently recomputed SHA-256 | Contract match |
|---|---|---|
| `asset-manifest.json` | `B6A3824C6751A69DACC746ABCB160CC92C5C7B0ED78720F3FDEE7166AF4FB3A4` | Exact |
| `BRAND_IDENTITY.md` | `BC60E1B8FCF3E2780B861ACC76487B85FCCF8AF35F43B8C2FF696005ED711671` | Exact |
| `geometry-spec.json` | `0D612364E87CAC04155C72267D6DE4FA7C2BB82D0A5A6E35C9BAC96A64167420` | Exact |
| `semantic-tokens.json` | `9AE5C814DBEA4D23CB07FB1DCC5AE1479D5784DA116B1877A517B4BA02D17DF7` | Exact |
| `visual-boards/index.html` | `2C2A4FC2ACFF5C2F8F33262A150C9840FE46005716D9EF94EE6D43200A6F3EB3` | Exact |

The manifest contains 26 current entries and passed deterministic checksum
validation. The archive inventory identifies the five CR-001 intake anchors and
eight superseded sources. Superseded Signal Ledger logo filenames are absent from
the current asset root and are explicitly non-current under the archive.

### Immutable prior reports

| Report | SHA-256 | Result |
|---|---|---|
| Design review iteration 1 | `12014D5772250EF8B2BA07B911D833B4F53C4CA880961BA55F5B4DCF07CE78DD` | Exact |
| Design review iteration 2 | `490A4391327D476014CC1B758EDFDDF66DE4C8A03628BE116659E5ADA272D895` | Exact |
| Accessibility audit iteration 1 | `532779730294F74716D85115514E3EAA749FF9FAA6EEE48B20CFECF2BEED70D2` | Exact |
| Accessibility audit iteration 2 | `FD06D3500F797A2148B7432C6AB2F7F6CF613D71732710BCBE54E65C8761B519` | Exact |

The two iteration-1 accessibility findings remain mechanically closed: prohibited
luminous-on-light signal pairings have not returned, and the lockup/optical size
authority still rejects 144 CSS px while supporting 168/32/24/16 CSS px.

## Methods, tools, and limitations

The audit used the repository's existing Node v24.14.0, Playwright 1.61.1,
Playwright Chromium runtime, axe-core 4.12.1, PowerShell, source/XML/JSON/CSV
inspection, exact sRGB contrast calculation, SVG arithmetic, accessibility-tree
inspection, keyboard operation, and visual review of all eight supplied captures.
No new tool or dependency was installed.

One bounded main local browser pass covered the board at 1440×900, 900×900,
390×844, and 320×800 CSS px and the scale page at 1200×900. One allowed targeted
fallback identified the source of the text-spacing overflow; no other browser
retry was made. All non-local requests were aborted. Zero external request was
observed, the clean page produced zero console/page errors, and the bounded OS
temporary profile was removed.

Axe WCAG A/AA, 2.1 AA, and 2.2 AA rules returned **zero violations and zero
incomplete results** in all five cases. Axe's injected `file://` analysis emitted
stylesheet XHR/CORS console messages; the separate clean load did not. The axe
result is supporting evidence, not proof of accessibility or conformance.

The eight visually inspected captures were wide, preview, medium, narrow,
forced-colors, grayscale, print, and scale evidence. No human screen-reader audio
session, mobile assistive technology, Firefox/Safari engine, real touch device,
physical print/low-resolution process, color-vision participant study, or actual
application/WebGL journey was available. These limits prevent any product or
assistive-technology certification claim.

## CR-001 accessibility acceptance matrix

| CR-001 concern | Result | Independent evidence |
|---|---|---|
| Current Quiet Framework-derived master is one coherent family | PASS | Primary/light/mono/reverse/standard assets use exact `framework-relay-master-80-v1`; named 24/16 variants preserve open brackets and stepped relay. |
| Rejected Signal Ledger mark is not a current asset | PASS WITH MATERIAL TEXT CONFLICT | Current asset root and board/archive semantics are correct. `01-identity-principles.md` still calls the rejected diagonal/rail construction the “recommended mark”; see `BI-A11Y-I3-001`. |
| Full-name-first entity and SEO behavior | PASS | Board title/H1, visible semantic copy, logo titles/descriptions, lockups, and guidance lead with “Hengshi Design”; mark-only use is explicitly secondary and Organization logo data remains held. |
| Dark/light text and meaningful-graphic contrast | PASS | Every declared pairing recomputed exactly and met its threshold. Current light relay `#006D82` is 5.68:1 on Paper and 5.29:1 on Mist; dark relay `#00D4FF` is 10.86:1 on Ink. Former prohibited `#00D4FF`/Paper and `/Mist` remain 1.68:1 and 1.57:1 and are not authorized light-surface pairings. |
| Monochrome/reverse/grayscale/forced colors | PASS | Geometry and full-name adjacency survive one-ink and reverse assets. Grayscale and forced-colors captures retain current/source/superseded labels, state names, series text, and action meaning. |
| Small optics and supported lockup | PASS | Exact arithmetic and the scale capture support 16/20/24/32 and 168 CSS px; 144 remains visibly rejected. Physical 7/38 mm proof remains pending and unapproved. |
| SVG names/descriptions and semantic identity | PASS | All current SVGs expose `role="img"`, title, description, dimensions, and viewBox. Current logo descriptions name Framework Relay and the full entity; 24/16 descriptions state adjacency/optical limits. |
| R-020 direct-labelled data closure | REVISE | Series names exist in SVG text, image alt, and an accessible semantic list, but endpoint text scales below the package's 12 px floor at 390/320 CSS px and the current data guidance separately reintroduces evidence-state-like combinations; see `BI-A11Y-I3-002`. |
| Reading/DOM order and accessible names | PASS | One header/nav/main/footer, one H1, ordered H2/H3 hierarchy, regions/articles/figures/lists/definition lists, 13 meaningful image alternatives, six state names, and five series names appeared in the accessibility snapshot. |
| Keyboard, bypass, focus, and target spacing | PASS | Tab sequence is skip link, five navigation links, then two main actions. Skip activates `#main`; the next Tab enters main content. Focus uses a visible 3 px outline with 3–4 px offset. Primary actions exceed 24×24 CSS px; 21 px-high nav text links retain the WCAG 2.5.8 spacing exception through configured gaps. |
| Base zoom/reflow and 200%/400% equivalence | PASS | Base 390 and 320 CSS px views had `scrollWidth === clientWidth`, preserved logical order, and lost no image/semantic/action content. The 320 CSS px state provides the required narrow reflow evidence for a 1280 CSS px layout at 400%; 200% is less restrictive. |
| WCAG text spacing | REVISE — LOW | The standard 1.4.12 spacing override caused 329 px document width at a 320 px viewport through the application grid; see `BI-A11Y-I3-003`. |
| Reduced motion | PASS FOR STATIC DEFINITION | The static board has no running animation, autoplay, flash, or camera movement. Under reduced motion, computed scroll behavior is `auto`; complete labels/actions remain. Later implementation must be tested independently. |
| Static/non-WebGL/asset-failure parity | PASS FOR DEFINITION | With all 13 SVG requests deliberately failed, current candidate text, all five series names, both actions, Quick Access, and reading order remained; no horizontal overflow occurred. No canvas or JavaScript is required. |
| Forms/errors/media | NOT APPLICABLE TO BOARD | No form, audio, or video exists. The six-state system includes visible Error text and a required recovery action; actual forms, status announcements, captions/transcripts, and booking errors require later application testing. |

## Logo and size arithmetic

The current 420-unit horizontal lockup uses a 34-unit full name, 5-unit relay,
and 6-unit frame. Independent DPR1 calculations are:

| Output | Name | Relay | Frame | Result |
|---:|---:|---:|---:|---|
| 144 CSS px | 11.66 CSS px | 1.71 device px | 2.06 device px | **Rejected:** name fails the 12 px meaningful-text floor and relay fails the 2-device-pixel floor |
| 168 CSS px | 13.60 CSS px | 2.00 device px | 2.40 device px | **Supported minimum** |

| Mark form | Arithmetic | Result |
|---|---|---|
| Standard mark at 32 CSS px | relay `5×32/80 = 2.00`; frame `6×32/80 = 2.40` device px | PASS |
| Optical small mark at 24 CSS px | retained 2-unit strokes on a 24-unit viewBox = 2.00 device px | PASS |
| Optical favicon at 16 CSS px | retained 2-unit strokes on a 16-unit viewBox = 2.00 device px | PASS |
| Optical favicon at 20 CSS px | `2×20/16 = 2.50` device px | PASS |

The 16-unit favicon's checkpoint removal is explicit and does not remove entity
meaning because the mark never replaces the full text name. Physical 38 mm/7 mm
behavior remains conditional on process proof.

## Findings

### BI-A11Y-I3-001 — MEDIUM — Current text authority identifies the superseded logo as the recommended mark

**Requirement/standard references:** D-008; D-027; CR-001 sections 3, 8, and 9;
FR-002; UX-002; UX-003; UX-005; WCAG 2.2 SC 1.3.1, 1.3.2, and 3.2.4.

**Exact location:** `01-identity-principles.md:21-23` states that “the diagonal
signal path in the recommended mark” represents progression. Lines 64-65 state
that “the recommended mark” is made from “two accountable rails, a joining field,
and one advancing signal.” Those statements describe the archived, founder-
rejected H-derived Signal Ledger logo. Current `02-visual-directions.md`,
`03-logo-system.md`, `geometry-spec.json`, SVGs, and board instead define four open
brackets, a non-diagonal stepped relay, and a square checkpoint as Framework Relay.

**Reproduction:** Read the cited principles with images disabled or as a text-only
identity specification. Compare its “recommended mark” description with
`geometry-spec.json` and the current Framework Relay SVG title/description. The
same current package gives mutually exclusive answers about the recommended mark.

**User impact:** A screen-reader, text-only, non-WebGL, or asset-failure consumer
can be told that the rejected logo is current. A downstream author can copy that
language into alt text, metadata, accessible documentation, design-system names,
or fallback content and reintroduce the founder-rejected symbol. This breaks the
required current/superseded distinction and makes visual and semantic identity
evidence unequal.

**Acceptance test:** Reconcile the current principles to D-027 and the Framework
Relay authority. Text must describe open brackets, a stepped non-diagonal relay,
and checkpoint; identify the H-derived diagonal/rails/bridge mark only as archived
and superseded; and contain no current/recommended reference to the rejected
geometry. A deterministic current-text scan plus independent text-only/asset-
failure review must return one unambiguous current mark.

### BI-A11Y-I3-002 — MEDIUM — R-020 direct-labelling closure is visually undersized at narrow widths and contradicted by current guidance

**Requirement/standard references:** D-008; D-027; CR-001 sections 5 and 8;
R-020; UX-001 through UX-005; WCAG 2.2 SC 1.3.1, 1.4.1, 1.4.4, and 1.4.10;
`semantic-tokens.json:58`; `04-color-and-typography.md:114-115`.

**Exact locations:**

1. `assets/icon-data-specimen.svg` defines endpoint labels at 15 SVG units in a
   960-unit-wide image. On the board the image renders 357.97 CSS px wide at the
   390 viewport and 287.98 CSS px wide at the 320 viewport. The labels therefore
   render at approximately `15×357.97/960 = 5.59 CSS px` and
   `15×287.98/960 = 4.50 CSS px`, below the package's 12 CSS px minimum for
   meaningful content. This contradicts `05-imagery-iconography-and-data.md:122`,
   which says direct labels remain visible at narrow widths.
2. `05-imagery-iconography-and-data.md:113-123` specifies the five distinct
   plus/ring/cross/hexagon/X mappings and says they must not be reused as evidence
   states. The current “Series encoding” table beginning at line 126 then directs
   Circle/Solid, Triangle/Long dash, Square/Short dash, and Diamond/Dash-dot
   combinations that reproduce the separate evidence-state grammar.

**Reproduction:** Open the board at 390 and 320 CSS px and inspect the five labels
attached to the plotted endpoints; compare their effective size with the 12 px
token floor. Then read both current data-encoding tables sequentially and compare
them with the six evidence-state mappings.

**User impact:** Mobile and low-vision users cannot reliably associate a plotted
line with its direct endpoint name at default narrow rendering. The readable
semantic list below prevents total information loss, but it no longer demonstrates
the claimed direct association. Authors following the later conflicting table can
also recreate evidence-status-like series, increasing ambiguity for color-vision,
cognitive, and nonvisual users. R-020 therefore cannot be truthfully closed as a
coherent accessible system.

**Acceptance test:** Establish one current data-series authority using the exact
five distinct mappings, remove or explicitly supersede the conflicting table,
and render endpoint names as responsive semantic text or an alternative chart
whose meaningful labels remain at least 12 CSS px at 390 and 320 CSS px. The
names, marker/pattern mapping, alt/description, and exact-value table/list must
agree. Independently verify color, grayscale, forced colors, 200%/400% zoom,
320 CSS px reflow, and a screen-reader-oriented reading sequence without any
evidence-state combination being reused ambiguously.

### BI-A11Y-I3-003 — LOW — WCAG text-spacing override introduces narrow horizontal overflow

**Requirement/standard references:** UX-001; WCAG 2.2 SC 1.4.10 and 1.4.12;
`07-accessibility-seo-and-applications.md` reflow requirement.

**Exact location:** `visual-boards/identity-board.css:76-81` and its narrow grid
state at lines 92-94. At 320 CSS px, applying line height 1.5, paragraph spacing
2em, letter spacing 0.12em, and word spacing 0.16em changes document width from
320 to 329 CSS px. The application grid is 288 px wide but its content expands to
313 px; both `.hero-sample` and `.evidence-sample` extend to x=328.5.

**Reproduction:** Load the board at 320×800 CSS px, apply the WCAG text-spacing
override, and compare `document.documentElement.scrollWidth` (329) with
`clientWidth` (320). Base 320 reflow passes before the override.

**User impact:** Users who increase spacing encounter a small horizontal pan in
the application section. Content and actions remain present, so this is LOW and
would not by itself block the founder's identity choice, but it must not become a
production pattern.

**Acceptance test:** Constrain grid children (`min-width: 0` or an equivalent
content-safe rule), allow long metadata to wrap, and repeat the specified spacing
override at 320 CSS px. Require `scrollWidth === clientWidth` with no clipping,
overlap, obscured focus, content loss, or action loss.

## Finding summary and gate

| Severity | New findings | Unresolved |
|---|---:|---:|
| Critical | 0 | 0 |
| High | 0 | 0 |
| Medium | 2 | 2 |
| Low | 1 | 1 |

The Framework Relay geometry, contrast, size floors, full-name-first behavior,
SVG accessible descriptions, keyboard/focus order, base reflow, monochrome,
reverse, forced-colors, grayscale, print, reduced-motion, and asset-failure
semantics otherwise pass within this definition scope. Automated scans found no
violation, but manual review identified the barriers above; automated silence
does not override them.

## Verdict, limitations, and human escalation

**REVISE.** PASS requires no unresolved CRITICAL, HIGH, or MEDIUM accessibility
finding. `BI-A11Y-I3-001` breaks the required current/superseded semantic truth,
and `BI-A11Y-I3-002` prevents an accessible, coherent R-020 closure. The exact
hybrid package is therefore **not ready for a clean founder identity-approval
gate** on accessibility evidence.

Producer iteration 3 of 3 is exhausted. This report does not authorize an
iteration 4 or edit the frozen work. The two MEDIUM findings and LOW residual
must be recorded and returned to the founder for a decision under D-027/CR-001.
Only a human may accept a conformance exception, retain an accessibility risk, or
choose among product-level accommodations.

Even after any decision, trademark/legal clearance, physical print and low-
resolution production proof, final production masters, paid fonts/assets,
external design/shared-library writes, actual application/browser/assistive-
technology testing, UI/3D implementation, public use, complete Phase 1 approval,
Git/deployment, and launch remain separate gates. Nothing in this report is a
WCAG conformance statement or production authorization.

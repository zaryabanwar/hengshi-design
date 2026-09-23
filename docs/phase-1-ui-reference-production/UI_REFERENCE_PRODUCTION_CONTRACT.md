# MA-025 External UI Reference-Production Contract

**Project:** Hengshi Design
**Package date:** 2026-09-06
**Status:** `awaiting_human` — prepared for founder decision at MA-025
**External-write status:** Not authorized. No Figma or Stitch account, file,
project, comment, export, or API call has been created, read, written, or
attempted by this package.

## 0. Purpose and standing

This package defines the exact bounded contract under which a later authorized
producer may perform **external design-provider writes** to create the reference
screens contracted by D-037. It is documentation only. It creates no screen, no
external file, no application code, and no publication.

MA-025 is the separate external-write gate that `docs/phase-1-ui-reference-design/`
§16 and `README.md` step 5 require and that D-037 explicitly left closed:

> External Figma/Stitch production, application implementation, publication,
> deployment, and complete Phase 1 acceptance remain unauthorized.

### 0.1 Controlling authority

| Authority | Constrains this contract by |
|---|---|
| **D-025** | The public route foundation, claims, SEO, and conversion model; `/industries` retained. The foundation was 33 routes at D-025; `/credits` was reconciled as the 34th under R-032 in the CR-002 revision window, so the operative count is **34** |
| **D-026** | Evidence in Motion; evidence-led innovation delivery partner; From complex ambition to accountable delivery |
| **D-035** | The frozen Signal Ledger system + Framework Relay logo hybrid; marks unregistered and trademark-not-cleared |
| **D-036** | The exact Phase 1 UX architecture package |
| **D-037** | The exact 13-file UI reference-design freeze, SHA-256 `97E79201CC36F01718A027AD800E63BDD5AAFC47E41137D65253BAABA6B2120F` — **superseded 2026-09-06**, see below |

> **D-037 freeze supersession — 2026-09-06, CR-002 revision window, decision D-039.**
> The hash cited above is the value **as accepted at D-037 on 2026-09-05**. It is
> retained as provenance and must not be deleted, but it no longer describes the
> current package. The founder-approved CR-002 revision window amended the design
> package to the four-peer-stream model and reconciled `/credits` as the 34th
> route per R-032. The amended 13-file aggregate is SHA-256
> `F16093D07D1E2634DB440ED35E4D4648ABF4F6D85C2BCD4E8F9CE5092F9C4AD6`, which is
> the value accepted at MA-028. **Superseded again on 2026-09-06 by D-042**, the
> remediation of the blocking review findings; the current aggregate is
> `4B9EB9AFF439D98A67AE0B75FC83DF06999BDB8178A69C9333F15FD45062289B`.
>
> **Superseded again on 2026-09-06 by D-043.** Independent re-reviews of the D-042
> remediation both returned FAIL, converging on five defects — chiefly that the
> delivery stream axis D-042 introduced was **inert**, asserted by row count and
> selected by no record. The full schema fix added `stream_profile` to the route,
> flow, and template records, added `DS-STREAM-INVARIANT`, moved `ACT-09` into
> authorized `B01`, and withdrew a WCAG conformance claim. **The current design
> aggregate is
> `DB92B4D0B889948D6C272F0DC7397327055B0108E7EEB953924F34E735BD4649`.**
> All earlier values are retained as provenance and are not authorities.
>
> **Superseded again on 2026-09-06 by D-045.** Independent re-reviews of the D-043
> remediation both returned FAIL a second time, converging again on the same shape
> of defect: `stream_profile` was a total function of `state_profile`, so a column
> that had been added to end an inert axis was itself inert, and
> `DS-STREAM-INVARIANT` was a profile with zero members. D-045 accepted the two
> `[PROPOSED]` delivery-stream specifications as the sole authority and directed
> that the producer implements and only implements them. Under that model stream is
> **not assigned on a record at all**: it is declared at the primitive in
> `component-primitives.csv.stream_presence`, computed at the template as the union
> over `primitive_dependencies`, and inherited unstored by routes and flows.
> `stream_profile` and `DS-STREAM-INVARIANT` were deleted rather than amended, and
> assertions `A-01`..`A-11` replace the two count-based checks that preceded them.
> **The current design aggregate is
> `0AA83FD298ABB12A96782205996EB3783BF8E80E11AD1B2BE44473F2E87EB536`,**
> computed after every design-package edit in this slice had settled. It supersedes
> the intra-slice value `D41C10FE…DF7F`, which described the package part-way
> through the same slice and was never a freeze point.
> This contract adds `A-12`..`A-16` and the `stream_disposition` column, and
> `stream_id` becomes a mandatory single-valued manifest column under §5.2.
>
> **B01's disposition changed under D-045 gate G-4.** It is no longer
> `authorized_pilot` held by a review condition; it is `future_not_authorized` in
> both the design batch plan and the production batch plan. Nothing in this
> contract is authorized to execute today. Six batches carry
> `authorized_released_by_pilot`, which is a conditional disposition that the held
> pilot has not triggered and cannot trigger while B01 is not authorized.
>
> **B01 is held** by explicit founder decision until the D-043 remediation has a
> clean independent re-review (**MA-029**, **R-035**). Authorization under MA-025
> does not by itself release B01.
>
> **MA-028 was accepted by the founder on 2026-09-06 (D-041).** The amended
> aggregate above is the operative freeze value. This contract now derives its
> authority from the amended package, and the authorized batches **may** rely on
> changes introduced by the amendment — including `/credits` in **B02** and the
> `S-SEMANTIC` peer stream at P0. The superseded `97E7…120F` value remains cited
> above as provenance only.
>
> **Two limits still apply.** First, B07 remains deferred and not authorizable
> under MA-025 (§2.1, `SC-10`); the four-stream reference evidence is therefore not
> produced under this contract and waits on MA-026. `S-SEMANTIC`'s P0 status is a
> written commitment that the current production path does not yet discharge, and
> that gap is tracked as an open risk rather than treated as satisfied. Second, the
> independent design and accessibility reviews MA-028 also called for ran on
> 2026-09-06 **after** acceptance and returned FAIL. They have since returned FAIL
> twice more: once against the D-042 remediation and once against the D-043
> remediation, converging each time on the same defect shape. Three remediations
> have now been produced (D-042, D-043, D-045) and **none of them has been reviewed
> by anyone other than the producer who wrote it.** A passing validator is a
> determinism check, not a review. **MA-029 remains `awaiting_human` and R-035
> stays open; the producer cannot close it.**
| **Constitution 2.0.0 §IV** | Approved Stitch or Figma reference before production UI; UI revision limit 3 |
| **Constitution 2.0.0 §VII** | The producer must not approve their own material output |
| **Constitution 2.0.0 §VIII** | Only founder approval moves a phase to `accepted` |

The **current accepted design aggregate** is the normative input — that is, the
D-037 package **as amended** through the CR-002 revision window, whose operative
hash is the last value in the supersession note above. This contract does not
restate, extend, reinterpret, or weaken it. Where this contract and the current
aggregate appear to differ, **the current aggregate governs** and the difference
is a defect in this contract.

*Corrected 2026-09-06 under D-043.* This clause previously named the D-037
package as governing. Read literally after the amendment, it directed a producer
to resolve every conflict back to a superseded freeze — which would have meant
dropping `/credits` as an orphan route and leaving a dangling footer link and an
unmet CC BY 4.0 attribution obligation. The superseded hashes remain cited above
as provenance; they are not authorities.

### 0.2 Status vocabulary

- **[ACCEPTED INPUT]** — an accepted upstream definition constrains this package.
- **[PROPOSED PRODUCTION CONTRACT]** — a reversible requirement in this package,
  pending founder decision at MA-025.
- **[UNRESOLVED GATE]** — a fact that must not be inferred, invented, or assumed.
- **[MUST VERIFY AT GATE]** — a provider capability, limit, or price that could
  not be established from a primary source at this package date and must be
  verified and dated before the first external write.

---

## 1. Provider selection and rationale

### 1.1 Decision

**[PROPOSED PRODUCTION CONTRACT]** Use **Figma** as the sole authoritative
production and evidence environment for batches B01–B06 and B08.

**Google Stitch is not used in MA-025.** It is neither prohibited forever nor
disparaged; it is excluded from this scope because the contracted work is a
long-lived, versioned, component-based reference system rather than a one-shot
screen generation.

### 1.2 Rationale, argued against the accepted contract's own requirements

The selection is not a general tool preference. Each reason below cites the
D-037 requirement that drives it.

| # | D-037 requirement | Why Figma satisfies it | Why Stitch does not |
|---|---|---|---|
| 1 | §5 evidence type `VARIANT` — state and option variants must be distinguishable evidence units | Components with named variant properties produce addressable, diffable variant sets | Generative screen output has no persistent variant-property model |
| 2 | §5 evidence type `PROTOTYPE` — focus return, disclosure, modal, and transition behaviour must be demonstrable | Prototype links, interactions, and overlay/return behaviour are first-class | No equivalent interaction-prototyping surface |
| 3 | §2.2 — every reference must map to the 62 `PRIM-*` component primitives | A published component library gives each `PRIM-*` a stable node and property set | No reusable published-library model |
| 4 | §6 naming grammar — `V01→VNN` revisions must increment **without renaming the stable template/instance source IDs** | Frames are named, addressable, and stable across versions | Regeneration produces new artifacts; identity is not stable by construction |
| 5 | §14 — two independent reviews per batch must attach findings to specific evidence | Threaded comments anchor to a frame or region and survive revision | No anchored review surface |
| 6 | §15 handoff — must deliver "the design-file/file-key and page/frame inventory without credentials" | The phrasing already presumes a file-key addressing model | No file-key concept |
| 7 | Rollback (§9 of this contract) — every batch must be restorable to a named pre-write state | Named version history plus file export gives a real restore point | No versioned rollback of a generation |
| 8 | 40 templates × 7 viewports × states × modes across 8 authorized batches | A durable multi-page, multi-library file system | Not designed as a system of record |

### 1.3 Where Stitch may still be proposed later

A **separately approved** ideation slice could use Stitch to explore visual
direction for B02/B03 before Figma production, on three conditions: its output is
explicitly non-authoritative, it is never submitted as contracted evidence, and it
is covered by its own external-write gate. **No such slice is proposed or
authorized here.**

### 1.4 Host capability gap — must be closed before any write

**[UNRESOLVED GATE]** Per `AGENTS.md`, the canonical MCP inventory is
`%APPDATA%\Code\User\mcp.json`. On the current host that file **does not exist**.
No Figma MCP server and no Stitch MCP server is configured or exposed in any of:

- `%APPDATA%\Code\User\mcp.json` (canonical; absent)
- `%APPDATA%\Code - Insiders\User\mcp.json` (absent)
- `.cursor/mcp.json`, `.vscode/mcp.json`, `.mcp.json` (absent)
- `~/.claude.json` (present, no `mcpServers` entries)
- `%APPDATA%/Claude/claude_desktop_config.json` (present, no `mcpServers` entries)

`docs/software-definition/02-ai-dev-tooling-and-mcp.md` line 43 states that a
Stitch MCP is "Configured locally". **That claim is not true of this host** and is
recorded as a correction obligation, not silently relied upon.

**Consequence, stated plainly:** approving MA-025 does **not** by itself make an
agent-performed external write possible. Production cannot begin until one of the
two enablement paths in §3.5 is completed and its capability test recorded.

---

## 2. Exact B01–B09 production scope and sequence

### 2.1 Authorization split — the material finding

Two of the nine contracted batches **cannot** be authorized by MA-025, because
their hard prerequisites are held by gates outside this contract.

| Batch | MA-025 disposition | Reason |
|---|---|---|
| B01–B06, B08 | **Proposed for authorization** (7 batches) | All hard prerequisites reduce to `B01` and to the accepted D-025/D-026/D-035/D-036 inputs and the current amended design aggregate (D-037 as amended) |
| **B07** | **Deferred — not authorizable** | Requires "separate 3D storyboard provenance and asset specification approved" (`phase_1.workstreams.three_d_storyboard_and_asset_specification: not_started`) and "GLB reuse still requires MA-004" (`MA-004: blocked`) |
| **B09** | **Deferred — not authorizable** | `hard_prerequisite_batch_ids = B01;B02;B03;B04;B05;B06;B07;B08` includes B07 |

Because B09 produces the evidence index and `docs/ui/UI_SPEC.md`, **the §15
handoff cannot complete under MA-025 alone.** MA-025 delivers seven batches of
reviewed reference evidence and an interim index; a later gate (MA-026) must
cover B07, B09, and the final visual-direction decision.

This is stated as a limit, not worked around. Approving MA-025 must not be
mistaken for approving the whole reference-screen programme.

### 2.2 Dependency graph (derived from `design-batch-plan.csv`)

```
B01 ──┬── B02 ── B03 ──┬── [B07]* ──┐
      ├── B04          │            │
      ├── B05          │            ├── [B09]*
      ├── B06          │            │
      └── B08 ─────────┴────────────┘

* B07 and B09 are outside MA-025 scope (see §2.1).
```

After B01, five batches (B02, B04, B05, B06, B08) are simultaneously unblocked.
The critical path through the authorized set is **B01 → B02 → B03**.

### 2.3 Execution order

**[PROPOSED PRODUCTION CONTRACT]** Execute **strictly serially** in this order:

| Order | Batch | Name | Entry condition |
|---:|---|---|---|
| 1 | **B01** | Semantic shell and recovery foundation | MA-025 accepted **and** §3.5 capability evidence recorded **and** §7 cost boundary confirmed |
| 2 | **B02** | Core public decision routes | B01 exit passed **and** founder B01 pilot acceptance (§6.4) |
| 3 | **B03** | Services, industries, and wayfinding | B02 exit passed |
| 4 | **B04** | Evidence and publication-facing public routes | B01 exit passed |
| 5 | **B05** | Concierge, handoff, media, and contact | B01 exit passed |
| 6 | **B06** | Qualified booking lineage | B01 exit passed |
| 7 | **B08** | Staff auth, operations, publication, and audit | B01 exit passed |

Serial execution is chosen deliberately over the available parallelism: each batch
consumes two independent reviews, and the global operating rule is to run one main
agent and one bounded specialist rather than broad fan-out. Parallel execution of
B04/B05/B06/B08 after B03 is **possible** under the dependency graph and may be
requested later as a bounded amendment; it is **not** requested here.

### 2.4 B01 is a gated pilot

**[PROPOSED PRODUCTION CONTRACT]** B01 is the pilot. It establishes the file
structure, the `PRIM-*` component library, the naming grammar in practice, the
export pipeline, and the evidence ledger that every later batch consumes.

After B01 exits, work **halts** for an explicit founder pilot acceptance (§6.4)
before B02 begins. This is the cheapest possible point to discover that the
provider, the naming grammar, the evidence volume, or the visual direction is
wrong. Batches B02–B08 are authorized by MA-025 but **released** by that pilot
acceptance.

### 2.5 Per-batch scope is fixed by the accepted contract

Each batch's primary templates, supporting templates, primary source IDs,
supporting evidence IDs, required visual evidence, review obligations, stop
condition, `BP-NFR-006` browser profile, and WCAG 2.2 SC 2.2.1 time-limit branch
are taken **verbatim** from
`docs/phase-1-ui-reference-design/design-batch-plan.csv`. This contract adds
execution, evidence, review, cost, rollback, and credential rules around them and
**changes none of them**. `batch-production-plan.csv` in this package restates the
authorized rows with their MA-025 disposition and adds no scope.

---

## 3. External write scope

### 3.1 Permitted external operations

**[PROPOSED PRODUCTION CONTRACT]** Only these operations, only in the single
approved Figma file, only for an authorized batch:

| ID | Permitted operation |
|---|---|
| `WS-P-01` | Create one Figma project and one design file dedicated to Hengshi Design UI reference production |
| `WS-P-02` | Create, rename, and reorder pages within that file |
| `WS-P-03` | Create, edit, and delete frames, components, component sets, variants, styles, and variables within that file |
| `WS-P-04` | Create prototype links and interactions within that file |
| `WS-P-05` | Add, resolve, and reply to comments within that file |
| `WS-P-06` | Create named version-history checkpoints within that file |
| `WS-P-07` | Export images, PDFs, and the file archive **out** of that file to the local repository evidence directory |
| `WS-P-08` | Read the file's own node/page/frame inventory for evidence indexing |

### 3.2 Prohibited external operations

| ID | Prohibited operation |
|---|---|
| `WS-X-01` | Any write to any file, project, or team other than the single approved one |
| `WS-X-02` | Publishing a library, plugin, widget, or file to the Figma Community |
| `WS-X-03` | Enabling public link sharing, "anyone with the link", or embed sharing |
| `WS-X-04` | Inviting, adding, or removing any collaborator or seat |
| `WS-X-05` | Any billing, plan-change, trial-start, or paid-seat action |
| `WS-X-06` | Uploading the protected exterior GLB, any client-confidential material, any personal data, or any real lead/booking record |
| `WS-X-07` | Uploading or embedding any paid, licensed, or third-party asset not covered by D-035 |
| `WS-X-08` | Any Stitch operation of any kind |
| `WS-X-09` | Any write outside an authorized batch, including "small fixes" to an accepted batch |
| `WS-X-10` | Any use of provider AI/generative features that transmits project material for model processing |
| `WS-X-11` | Connecting the file to any external integration, webhook, or third-party plugin |

### 3.3 Repository write scope

Writes are confined to `docs/phase-1-ui-reference-production/**` plus the durable
root records (`PROJECT_STATE.yaml`, `TASKS.md`, `MANUAL_ACTIONS.md`, `RISKS.md`,
`CHANGELOG.md`, `PROJECT.md`, `DECISIONS.md`, `docs/decisions-log.md`) and the
correction to `docs/software-definition/02-ai-dev-tooling-and-mcp.md` required by
§1.4. **No application, dependency, migration, or infrastructure file is written.**

`docs/ui/UI_SPEC.md` is a **B09 deliverable** and is therefore **not** written
under MA-025.

### 3.4 Git scope

No commit, push, branch switch, tag, or history rewrite occurs without a separate
explicit founder instruction. Evidence accumulates in the working tree.

### 3.5 Capability enablement — required before the first write

**[UNRESOLVED GATE]** Exactly one path must be completed and recorded:

- **Path A — human operator.** An authorized person performs the Figma writes
  directly in the Figma UI, following this contract, and places exports into the
  repository evidence directory. No agent credential or MCP is required. This path
  is available immediately on MA-025 approval.
- **Path B — agent-performed.** A Figma MCP server or equivalent authorized API
  path is configured in the canonical inventory, authenticated by a person through
  an official flow, and **capability-tested read-only first** (list file, read node
  inventory) before any write. The test result and its date are recorded in
  `validation/capability-evidence.md`.

Under either path, the following must be recorded before `WS-P-01`: provider,
account type, plan tier, date, the read-only capability result, and the
`[MUST VERIFY AT GATE]` items in §7.2. **Capability must never be assumed.**

---

## 4. Visual deliverables

### 4.1 Evidence unit types in scope

D-037 §5 defines seven evidence unit types. MA-025 produces six:

| Type | In MA-025 scope | Note |
|---|---|---|
| `FRAME` | Yes | Full reference frame |
| `FOCUSED_FRAME` | Yes | Region-level evidence where a full frame is not required |
| `VARIANT` | Yes | State/option variant of a component or template |
| `ANNOTATION` | Yes | Interaction, focus order, semantics, and accessibility notes |
| `PROTOTYPE` | Yes | Focus return, disclosure, modal, transition demonstration |
| `ROUTE_INSTANCE_SHEET` | Yes | Coverage sheet per route instance |
| **`TEST_CAPTURE`** | **No** | D-037 §5 defines this as later browser/assistive-technology evidence after implementation, "never substituted by a design mockup". Producing it here would be a false conformance artifact. |

**A design reference cannot establish WCAG 2.2 conformance.** WCAG 2.2 Level AA
for every applicable full page and complete process remains the normative
production and review **target**. Nothing in MA-025 is, or may be presented as, a
conformance claim.

### 4.2 Naming

Every evidence unit uses the D-037 §6 grammar unchanged:

```
HSD_UIR_<BATCH>_<TEMPLATE>_<INSTANCE>_<STATE>_<VIEWPORT>_<MODE>_V<NN>
```

Revisions increment `V<NN>` and **must not** rename the stable template or
instance source IDs.

### 4.3 Coverage per authorized batch

For each authorized batch, the producer delivers:

1. Every primary template's minimum reference evidence, per its row in
   `design-batch-plan.csv`.
2. Every route instance assigned to that batch in `foundation-route-coverage.csv`,
   as a `ROUTE_INSTANCE_SHEET`. A route-instance record is coverage evidence, not
   a mandatory duplicate full-page frame.
3. Every applicable profile from `responsive-state-mode-matrix.csv`, honouring
   each profile's `minimum_evidence` and `critical_distinct_frame_values`.
4. The `BP-NFR-006` viewport set where the profile requires it: `VP-320`,
   `VP-NARROW`, `VP-LANDSCAPE`, `VP-TABLET`, `VP-DESKTOP`, `VP-WIDE`,
   `VP-ZOOM-400`.
5. The batch's declared time-limit branch, visibly annotated: `TL-WARN-EXTEND`
   evidence must show a warning at least 20 seconds before expiry and an extension
   of at least 10× the default; `TL-REMOVABLE-ADJUSTABLE` must show the off or
   adjust-before-start control. **No record may select `TL-EXCEPTION`.**
6. The `PRIM-*` mapping for every component used.
7. The semantic Quick Access equivalent for any client below the `BP-NFR-006`
   floor, without WebGL.

### 4.4 Content rule

All copy in every frame is a **reference fixture**, visibly marked
`REFERENCE FIXTURE — NOT PUBLIC COPY` per D-037 §11. Exact public, legal, privacy,
claim, person, office, credential, client-outcome, and provider-behaviour content
remains gated by MA-002, MA-003, and MA-011 and **must not be invented to fill a
frame**. A frame that cannot be completed without inventing a gated fact triggers
that batch's stop condition (§8).

### 4.5 Asset rule

The only approved visual assets are the D-035 brand-identity files under
`docs/phase-1-brand-identity/assets/` and the tokens in `semantic-tokens.json`.
No stock photography, icon set, typeface, or illustration outside that set is
introduced. Typeface licensing for any non-D-035 face is `[UNRESOLVED GATE]`.

---

## 5. Evidence and screenshot capture

### 5.1 Local evidence tree

```
docs/phase-1-ui-reference-production/evidence/
  <BATCH>/
    frames/        PNG @2x and SVG per evidence unit
    prototypes/    PDF flow sheets and interaction annotations
    sheets/        ROUTE_INSTANCE_SHEET exports
    inventory/     node/page/frame inventory JSON (no credentials)
    archive/       file archive export for the batch checkpoint
    manifest.csv   one row per evidence unit
    manifest.sha256
```

### 5.2 Manifest columns

`evidence_id, batch_id, evidence_type, template_id, instance_id, state_id,
viewport_id, mode_id, stream_id, profile_ids, prim_ids, time_limit_branch,
file_relpath, sha256, export_scale, exported_on, figma_node_id, revision`

**`stream_id` is mandatory and single-valued** (D-045). Its value is exactly one of
`S-HIGH`, `S-MEDIUM`, `S-LOW`, `S-SEMANTIC`. There is no aggregate value, no empty
value, and no "applies to all streams" form: a frame is drawn in one stream or it is
a different frame. `A-12` resolves `stream_id` against the `_STREAM_<X>_` segment of
the row's own `evidence_id` and fails if the two disagree, so the column cannot be
filled in independently of the artefact it describes. `A-14` resolves the set of
`(batch_id, template_id, stream_id)` triples in the manifest against the obligation
set computed from the accepted design package's primitive-to-template presence fold;
a stream that is owed and not captured must be recorded as a deferral under `EC-33`
and is never silently absent.

### 5.3 Capture rules

- Exports are **deterministic**: fixed scale (`@2x` PNG, `1x` SVG), fixed
  background, no ad-hoc cropping.
- Every exported file is hashed **SHA-256, uppercase**, and recorded in the batch
  manifest.
- The batch manifest is itself hashed using the D-037 freeze algorithm:
  ordinal-sorted relative forward-slash paths, `UPPERCASE_SHA256` + two spaces +
  path, joined with LF, no terminal newline, hashed as UTF-8 without BOM.
- **No credential, token, cookie, session URL, or account email** appears in any
  export, filename, manifest field, inventory JSON, or annotation. The Figma file
  key **is** recorded, per D-037 §15, which requires the file key without
  credentials.
- Screenshots of the Figma editor chrome are **not** evidence. Evidence is
  exported artwork plus the inventory, so review does not depend on a live session.
- Exports are re-generated, never hand-edited. A hand-edited export is void.

### 5.4 What the evidence must not imply

No export may be captioned, filed, or described as a rendered product, a live
page, a test result, an accessibility audit, a conformance statement, or approved
public content.

---

## 6. Design and accessibility review sequence

### 6.1 Per-batch loop

For each authorized batch, in order:

1. **Produce** the batch's evidence.
2. **Validate** deterministically — run `validation/validate-ui-reference-production.ps1`
   for coverage, naming-grammar conformance, manifest/hash integrity, profile
   coverage, `PRIM-*` mapping, fixture marking, claim scanning, and scope.
3. **Producer inspection** — the producer records completeness, feasibility, and
   unresolved gates. Per Constitution §VII the producer **must not** approve their
   own output.
4. **Independent design review** — a reviewer who did not produce the batch.
5. **Independent accessibility review** — a reviewer who did not produce the batch
   and did not perform the design review.
6. **Revise** — at most **3** producer revisions (the UI limit). Findings are
   closed by revision, not by argument.
7. **Re-validate** and re-run both reviews until both return zero CRITICAL, HIGH,
   and MEDIUM findings.
8. **Batch exit** — both reviews PASS, validator `RESULT=PASS FAIL_COUNT=0`,
   manifest hash recorded, named Figma version checkpoint created.

### 6.2 Revision-limit exhaustion

If a batch reaches 3/3 producer revisions with an unresolved CRITICAL, HIGH, or
MEDIUM finding, work on that batch **stops**. It is escalated as a change request
under `hengshi-change-request-management`, not continued into a fourth revision.
Revision budgets are **per batch** and are not transferable between batches.

### 6.3 Reviewer independence

The producer of a batch may not review it. The design reviewer and accessibility
reviewer are distinct. Neither reviewer can grant founder approval.

### 6.4 Founder gates inside MA-025

| Gate | When | What it decides |
|---|---|---|
| **MA-025** | Now | Whether external production may begin at all |
| **B01 pilot acceptance** | After B01 exit | Whether the pilot's structure, grammar, evidence volume, and emerging visual direction are right, and whether B02–B08 are released |
| **MA-026** (later) | After B08 exit | B07, B09, `docs/ui/UI_SPEC.md`, and the final visual-direction decision |

Batches B02–B08 do **not** each require a separate founder gate; their exit is
governed by the two independent reviews. This keeps the founder's attention on the
two decisions that are genuinely theirs.

---

## 7. Provider and cost boundary

### 7.1 Hard boundary

**[PROPOSED PRODUCTION CONTRACT]**

- **Zero spend.** MA-025 authorizes **no** payment, plan change, trial start,
  paid seat, add-on, or credit purchase. `WS-X-05` prohibits all billing actions.
- Work proceeds on Figma's **free tier only**, with a **single editor**.
- Any move to a paid tier is a **separate MA-010 paid-envelope decision** and
  cannot be taken inside MA-025 — not even to unblock a batch.
- If a free-tier limit blocks contracted evidence, that is a **stop condition**
  (`SC-05`), not a purchase trigger.

### 7.2 Pricing evidence and its limits

**[MUST VERIFY AT GATE]** A read-only fetch of the Figma pricing page on
2026-09-06 established the tier structure and that the free tier is styled
"Starter" with unlimited drafts and a daily/monthly AI-credit allowance. It did
**not** reliably establish, because the page rendered its comparison grid without
attributable plan columns:

- Starter design-file count and pages-per-file limit
- Starter version-history retention period
- Starter editor/collaborator caps
- Dev Mode availability on Starter
- Any provider MCP tool-call allowance

**These five items are not asserted.** They must be verified against the provider's
own current documentation, recorded with the observation date in
`validation/capability-evidence.md`, and re-checked before the first write. If any
verified limit makes the contracted evidence volume infeasible on the free tier,
`SC-05` fires and the founder decides — this contract does not pre-authorize a
workaround.

### 7.3 Data boundary

The Figma file receives **only**: reference fixtures, D-035 brand assets,
D-037-contracted structure, and annotations. It receives no personal data, no
client-confidential material, no real lead or booking record, no credential, and
no protected GLB (`WS-X-06`). Provider AI/generative features that transmit
project material are prohibited (`WS-X-10`).

---

## 8. Stop conditions

Work halts immediately and returns to the founder when any of these fire. A stop
is a normal, expected outcome — not a failure to route around.

| ID | Trigger | Action on trigger |
|---|---|---|
| `SC-01` | A frame cannot be completed without inventing a gated fact — legal entity, privacy copy, a claim, a person, an office, a credential, a client outcome, provider behaviour, or exact public copy | Halt the batch; record the exact missing fact; escalate to MA-002 / MA-003 / MA-011 |
| `SC-02` | The batch's own stop condition in `design-batch-plan.csv` fires | Halt the batch; quote the row verbatim; request a founder decision |
| `SC-03` | A material change to the D-035 identity, the 62 `PRIM-*` primitives, the route set, or the accepted UX architecture would be needed | Halt all production; raise a change request; do not amend an accepted package in place |
| `SC-04` | A batch reaches 3/3 producer revisions with an unresolved CRITICAL, HIGH, or MEDIUM finding | Halt the batch; escalate as a change request (§6.2) |
| `SC-05` | A verified free-tier limit blocks contracted evidence | Halt; report the limit and the exact shortfall; **do not purchase**; route to MA-010 |
| `SC-06` | Any operation would require a prohibited write (`WS-X-01`…`WS-X-11`) | Refuse the operation; halt; report |
| `SC-07` | §3.5 capability enablement fails, or a capability test would require an unofficial credential path | Halt before any write; report the gap |
| `SC-08` | The evidence would need to assert or imply WCAG conformance, a test result, or a live rendered page | Halt; the artifact is void; re-scope the annotation |
| `SC-09` | An accepted upstream package would have to be edited to make production work | Halt; accepted packages are immutable outside a change request |
| `SC-10` | B07 or B09 work is requested or begun under MA-025 | Refuse; both are outside scope per §2.1 and require MA-026 |
| `SC-11` | A paid, licensed, or non-D-035 asset would be needed | Halt; route to MA-010 and the asset-rights gate |
| `SC-12` | Any external write would touch a file, project, or team other than the single approved one | Refuse; halt; report |

---

## 9. Rollback and export strategy

### 9.1 Principle

Every batch must be restorable to its exact pre-write state without depending on
the provider remaining available, and the repository must retain a
provider-independent copy of all accepted evidence.

### 9.2 Per-batch checkpoints

1. **Pre-write checkpoint.** Before the first write of a batch: create a named
   Figma version `HSD_UIR_<BATCH>_PRE`, export the file archive, and record its
   SHA-256 in the batch manifest.
2. **Post-exit checkpoint.** After batch exit: create a named Figma version
   `HSD_UIR_<BATCH>_EXIT`, export the archive, export all evidence, hash
   everything, and freeze the manifest.
3. **Provider-independent copy.** The exported archive plus PNG/SVG/PDF exports
   and the inventory JSON live in the repository. If the Figma file were lost, the
   accepted evidence survives.

### 9.3 Rollback procedures

| Scenario | Procedure |
|---|---|
| Bad edit inside an in-progress batch | Restore the `_PRE` named version; re-export; re-hash |
| A rejected batch | Restore `_PRE`; the batch's evidence directory is marked `void` and retained, never deleted |
| Provider loss or account loss | Rebuild from the last `_EXIT` archive; the repository evidence remains the record |
| Bad repository documentation change | Revert the working-tree change; accepted evidence directories are append-only |
| Contract itself is wrong | Halt production; raise a change request; accepted batches are unaffected |

### 9.4 Retention

**[MUST VERIFY AT GATE]** Figma free-tier version-history retention is one of the
five unverified items in §7.2. Because retention may be time-limited, the exported
archive in the repository — **not** provider version history — is the authoritative
rollback artifact. This is why §9.2 requires an export at every checkpoint rather
than relying on the provider.

### 9.5 Immutability

An accepted batch's evidence is **immutable**. A later correction produces a new
`V<NN>` in a new revision cycle; it never overwrites accepted evidence in place.

---

## 10. Credential-handling boundary

**[PROPOSED PRODUCTION CONTRACT]**

| Rule | Statement |
|---|---|
| `CR-01` | Authentication happens only through the provider's official OAuth or browser sign-in flow, performed by a person |
| `CR-02` | No token, personal access token, API key, cookie, session URL, password, or recovery code is ever written into any repository file, evidence artifact, manifest, log, filename, commit message, or chat message |
| `CR-03` | Any token required by Path B lives only in the OS credential store or an environment variable, and is referenced **by name only** in documentation |
| `CR-04` | The Figma **file key is not a secret** and **is** recorded, per D-037 §15, which requires the file key and page/frame inventory without credentials |
| `CR-05` | Account email addresses and seat identities are not recorded in the repository |
| `CR-06` | Exported evidence and inventory JSON are scanned for credential-shaped strings by the validator before a batch can exit |
| `CR-07` | If a credential is ever exposed, production halts, the credential is rotated by a person, and the exposure is recorded in `RISKS.md` |
| `CR-08` | MA-025 authorizes **no** credential creation, rotation, storage change, or sharing |

---

## 11. Acceptance criteria

### 11.1 Acceptance of MA-025 itself

MA-025 is accepted when the founder explicitly approves this contract. Approval
means:

1. Figma is the approved provider for B01–B06 and B08; Stitch is not used.
2. The permitted external write scope in §3.1 is authorized; §3.2 remains
   prohibited.
3. Zero spend is confirmed; free tier only; any paid step returns to MA-010.
4. B01 runs as a gated pilot; B02–B08 are released only by B01 pilot acceptance.
5. B07 and B09 remain unauthorized and are deferred to MA-026.
6. No write occurs until §3.5 capability enablement is completed and recorded.

### 11.2 Acceptance of an individual batch

A batch exits when **all** hold:

- Deterministic validator returns `RESULT=PASS` with `FAIL_COUNT=0`.
- Every contracted template, route instance, profile, viewport, mode, state, and
  time-limit annotation for that batch has evidence in the manifest.
- Every evidence unit conforms to the §6 naming grammar and maps to its `PRIM-*`.
- Every frame's copy is marked `REFERENCE FIXTURE — NOT PUBLIC COPY`.
- The manifest hash is recorded and reproducible.
- `_PRE` and `_EXIT` checkpoints exist with exported archives.
- Independent design review: zero CRITICAL, HIGH, MEDIUM.
- Independent accessibility review: zero CRITICAL, HIGH, MEDIUM.
- Producer inspection recorded; producer did not self-approve.
- No credential-shaped string appears anywhere in the evidence.
- No unsupported conformance, test-result, or live-page claim appears.

### 11.3 Acceptance of the MA-025 programme

The MA-025 programme completes when B01–B06 and B08 have all exited, an interim
evidence index exists, and the founder is presented with the seven-batch result
plus a scoped MA-026 proposal for B07, B09, `docs/ui/UI_SPEC.md`, and the final
visual direction.

**MA-025 completion does not**: approve a final visual direction, complete the
D-037 §15 handoff, accept Phase 1, authorize implementation, authorize
publication, or authorize deployment.

---

## 12. Boundary and non-claims

This package contains Markdown, CSV, and one PowerShell validator only. It does
not:

- create a screen, prototype, component library, external file, or `docs/ui/UI_SPEC.md`;
- perform, schedule, or attempt any Figma or Stitch operation;
- approve a visual direction or any exact public, legal, or claim copy;
- assert that a Figma or Stitch MCP is available on this host — §1.4 records that
  none is;
- assert any Figma free-tier limit, retention period, or entitlement — §7.2
  records five unverified items;
- certify WCAG 2.2 conformance or convert a design reference into a test result;
- authorize spend, paid assets, dependencies, migrations, infrastructure,
  publication, Git operations, deployment, complete Phase 1 acceptance, or launch.

MA-013 compatibility acceptance remains a separate, unaffected gate.

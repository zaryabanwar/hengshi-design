# Producer Inspection — MA-025 External UI Reference-Production Contract

**Inspected package:** `docs/phase-1-ui-reference-production/`
**Inspection date:** 2026-09-06
**Producer role:** Hengshi project manager (contract author)
**Inspection type:** Producer self-inspection only
**Revision:** D-045 delivery-stream evidence model; supersedes the 2026-09-06 pre-D-045 inspection

**This is not a review and not an approval.** Constitution 2.0.0 principle VII
states that the producer must not approve their own material output. This document
records scope, completeness, feasibility, and unresolved gates so that an
independent reviewer and the founder can act on accurate information.

---

## 1. Scope inspection

### 1.1 What was produced

Nine documentation files: one README, one normative contract, five CSVs, one
PowerShell validator, and this inspection. No screen, no external file, no
application code, no publication.

### 1.2 What was deliberately not produced

| Not produced | Why |
|---|---|
| Any Figma or Stitch operation | MA-025 is not approved; no external write is authorized |
| `docs/ui/UI_SPEC.md` | It is a B09 deliverable and B09 is deferred |
| A D-038 decision entry | The founder has not decided MA-025; a decision must not precede its approval |
| `validation/capability-evidence.md` | It records a post-approval capability test that has not happened |
| Any evidence directory | It would imply production began |
| A visual direction | That is a later founder gate after B09 |

### 1.3 Producer-verified external actions taken

Two **read-only, unauthenticated** web fetches of public pricing and product pages
were performed to source the cost boundary. No account was created, no credential
was supplied, no project data was transmitted, and no provider state changed. The
outcome, including what could **not** be established, is recorded in contract §7.2.

---

## 2. Completeness inspection

The founder enumerated eleven required areas. Each maps to a contract section:

| # | Required area | Contract section | Complete |
|---:|---|---|---|
| 1 | Figma or Stitch provider and rationale | §1 | Yes — Figma selected, argued against eight D-037 requirements |
| 2 | Exact B01–B09 production scope and sequence | §2 | Yes, with a material limit: only seven batches are authorizable |
| 3 | External write scope | §3 | Yes — 8 permitted, 11 prohibited, plus repository and Git scope |
| 4 | Visual deliverables | §4 | Yes — six evidence types; `TEST_CAPTURE` excluded with reason |
| 5 | Evidence and screenshot capture | §5 | Yes — tree, manifest schema, determinism, hashing, exclusions |
| 6 | Design and accessibility review sequence | §6 | Yes — eight-step loop, independence, revision limit, founder gates |
| 7 | Provider/cost boundary | §7 | Yes — zero spend, with five limits recorded as unverified |
| 8 | Stop conditions | §8 | Yes — twelve enumerated halts |
| 9 | Rollback/export strategy | §9 | Yes — `_PRE`/`_EXIT` checkpoints, provider-independent copies |
| 10 | Credential-handling boundary | §10 | Yes — eight rules; file key recorded, secrets never |
| 11 | Acceptance criteria | §11 | Yes — for MA-025, for a batch, and for the programme |

---

## 3. Feasibility inspection

### 3.1 The contract is feasible for seven batches, not nine

Reading `design-batch-plan.csv` against `PROJECT_STATE.yaml` shows that B07's
prerequisites — "separate 3D storyboard provenance and asset specification
approved" and "GLB reuse still requires MA-004" — are held by a `not_started`
workstream and a `blocked` manual action. B09 hard-requires B07.

A contract promising B01–B09 would have been **unbuildable on day one**. The
package therefore authorizes seven batches and defers two, and says so in the
README, the contract, the batch CSV, and the traceability matrix rather than
burying it.

### 3.2 The contract is not executable today even for B01

Approval of MA-025 is necessary but **not sufficient**. No Figma or Stitch MCP is
configured or exposed on this host, and the canonical inventory file named by
`AGENTS.md` does not exist. Contract §3.5 therefore requires one of two enablement
paths to complete and be recorded before the first write. Path A (a human operator
working directly in Figma) is available immediately; Path B (agent-performed)
requires configuration this package does not perform and does not authorize.

The producer flags this as the single most likely source of a false expectation:
**approving MA-025 does not start production.**

### 3.3 Evidence volume is significant and not yet quantified

Seven batches spanning 40 templates, 34 route instances, 36 profiles, four delivery
streams, up to seven
viewports, and multiple states and modes will produce a large evidence set. The
exact count is deliberately **not** asserted here, because the per-profile
`minimum_evidence` and `critical_distinct_frame_values` rules make the true total
a function of the accepted matrix rather than a simple product. B01 is a gated
pilot precisely so the real volume is measured on a small batch before six more
are committed, and so `SC-05` can fire against a measured number rather than a
guess.

### 3.4 Serial execution is a deliberate cost

The dependency graph permits B02, B04, B05, B06, and B08 to run concurrently after
B01. The contract chooses serial execution because each batch consumes two
independent reviews and the operating rule is one main agent plus one bounded
specialist. This trades wall-clock time for review quality and reviewer
availability. If the founder prefers speed, parallelising the four independent
batches is a bounded amendment — it is **not** requested here.

---

## 4. Unresolved gates carried by this package

| Gate | Statement | Where recorded |
|---|---|---|
| Host capability | No Figma or Stitch MCP is configured or exposed; the canonical inventory file is absent | §1.4, §3.5, TR-004, TR-015 |
| Stale tooling claim | `docs/software-definition/02-ai-dev-tooling-and-mcp.md` line 43 claims a locally configured Stitch MCP; untrue on this host | §1.4, TR-004 |
| Provider limits | Five Figma free-tier facts could not be attributed from the pricing page and are not asserted | §7.2, TR-030 |
| B07 | Blocked by MA-004 and the `not_started` 3D storyboard workstream | §2.1, TR-005 |
| B09 and handoff | Blocked by B07; the D-037 §15 handoff cannot complete under MA-025 | §2.1, TR-006, TR-007 |
| Gated content | Legal entity, privacy copy, claims, people, offices, credentials, client outcomes, and provider behaviour remain held by MA-002, MA-003, MA-011 | §4.4, `SC-01`, TR-020 |
| Non-D-035 typefaces | Licensing for any face outside the accepted identity is ungranted | §4.5, `SC-11` |
| Final visual direction | Remains a later founder gate after B09 | §6.4, §11.3, TR-039 |
| B01 authorization | Set to `future_not_authorized` in **both** plan files under founder gate G-4; approving MA-025 still does not start B01 | §0.1, `batch-production-plan.csv` |
| Inert `stream_disposition` | Constant across all nine batches; reported by `A-13`, not failed; owed a founder decision alongside the design package's twenty-two inert columns | validation report, §"What the D-045 assertions added" |
| Design-system stream axis | The design system declares no stream axis, no stream-control component, no four stream tokens, and no 3D focus-ring token; gate G-6 records the gap and commissions the amendment later as its own bounded contract | design `validation-report.md` known limits |
| Independent review | Three producer remediations (D-042, D-043, D-045) have landed since the last independent reviews; MA-029 is `awaiting_human` and R-035 is open | §7 |

---

## 5. Consistency inspection against accepted authority

- The 13-file D-037 freeze hash is cited verbatim and no accepted file was edited.
- Per-batch prerequisites, time-limit branches, and browser profiles are carried
  **verbatim** from `design-batch-plan.csv`; the validator asserts equality field
  by field rather than trusting the transcription.
- The validator also asserts that every accepted batch row still reads
  `status = future_not_authorized`, so this package cannot silently flip the
  accepted plan's own authorization state.
- The `TEST_CAPTURE` exclusion follows D-037 §5 directly: a design mockup may
  never substitute for browser or assistive-technology evidence.
- WCAG 2.2 Level AA is stated as a target throughout and never as a claim.

---

## 6. Known limitation in the inherited validator pattern

The D-037 validator asserts that **all** worktree changes begin with
`docs/phase-1-ui-reference-design/`. That assertion cannot hold once durable root
records are updated as part of the same slice, which is why the accepted package's
183/183 is a valid point-in-time record that is not reproducible in place.

This package's validator deliberately widens the scope check to the package
directory **plus** the enumerated durable root records, and separately asserts that
no application, dependency-lock, or migration file changed. The intent of the
original check — documentation-only work — is preserved; the self-defeating part
is not repeated.

---

## 6a. What the D-045 slice changed in this package

Decision **D-045** states that the producer now implements, and only implements. Two
`[PROPOSED]` specifications — `DELIVERY_STREAM_EVIDENCE_MODEL.md` and
`DELIVERY_STREAM_ACCESSIBILITY_OBLIGATIONS.md` — are the authority, and this package
was changed to match them and to nothing else.

Three edits to `UI_REFERENCE_PRODUCTION_CONTRACT.md`: a D-045 supersession block in
§0.1, a replacement of the stale "not re-reviewed since" paragraph with a record of
the three unreviewed producer remediations, and a `stream_id` column plus its
normative paragraph in §5.2. Five assertions added to the validator, `A-12`-`A-16`.
One column added to `batch-production-plan.csv`, `stream_disposition`. The freeze
hash moved accordingly.

**Three results are recorded as observations rather than repaired**, because
repairing them would be the producer authoring the model again — the exact pattern
D-045 was decided to end:

1. `stream_disposition` is constant across all nine batches, and therefore inert.
2. `A-14`'s obligation set is entirely unmet, and passes only because every unmet
   obligation is explained by held authorization.
3. `A-15` and `A-16` scan three packages and nothing else, so `docs/active/` — which
   this slice also amended — is unswept.

A fourth result was a defect in the producer's own work and **is** recorded in full in
the design package's validation report rather than quietly fixed: a PowerShell
operator-precedence collapse made the peer-framing guard silently inert while it
reported zero hits across 56 files. Both validators now assert the alternative count.

## 7. Producer statement

The producer believes this package is complete against the eleven requested areas,
internally consistent, and faithful to D-037 — and that its two material findings
(seven-of-nine authorizable batches; no provider reachable from this host today)
are stated plainly rather than minimised. Under D-045 the producer additionally
asserts that **no model content was authored beyond the two accepted specifications**,
and that every place where literal implementation produced a result the producer
believes is wrong has been recorded as an observation for the reviewers instead of
being corrected.

The producer **does not approve** this package. It requires independent review and
an explicit founder decision at MA-025.

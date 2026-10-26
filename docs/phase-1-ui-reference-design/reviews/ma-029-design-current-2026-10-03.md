# MA-029 independent design and evidence-model review

Date: 2026-10-03. Verdict: **FAIL** for the current definition/evidence-verifier
package. Independent nonauthor review; no application, visual production,
accessibility conformance, publication or founder approval is implied.

Authority: D-045 and its accepted reviewer-authored model, the 2026-09-23 mapping
amendment, D-047, and D-051 through D-057. Historical D-043 schemas and unresolved
entries subsequently superseded by these decisions are not current requirements.
Only this review file was authored; all inspection and synthetic probes were
read-only and in memory. Existing evidence manifests were not created or altered.

## Findings

1. **HIGH — Evidence identity resolution is incomplete.**
   `../phase-1-ui-reference-production/validation/validate-ui-reference-production.ps1:637`
   checks shape and stream, but not accepted batch/template/state/viewport/mode
   sets. Lines 751–764 then combine manifest batch/template columns with the state
   parsed from its ID without resolving the encoded identity to that ownership.
   Accepted model `DELIVERY_STREAM_EVIDENCE_MODEL.md:599` requires every segment
   to resolve; line 620 requires evidence resolving to the obliged template.
   Reproduction: synthetic row batch B01, template TPL-GLOBAL-NAVIGATION, stream
   S-SEMANTIC, ID
   `HSD_UIR_B99_TPL_UNKNOWN_REF_STATE_REST_VP_BOGUS_MODE_BOGUS_STREAM_SEMANTIC_V01`
   yields `Test-EvidenceId=True`, invalid-scope=False, and satisfied coordinate
   `B01|TPL-GLOBAL-NAVIGATION|STATE-REST|S-SEMANTIC`.
   Exit: resolve all tokens and row identity against accepted records and owning
   batch/profile sets; negative probes must reject unknown and disagreeing tokens.

2. **HIGH — Coverage uses global authorization instead of the owning batch.**
   The production validator at lines 735–746 computes obligations across every
   batch, while lines 767–769 permit missing coverage only when no pilot exists.
   It never applies the owning batch's execution state or stream deferral to each
   missing coordinate. Model `DELIVERY_STREAM_EVIDENCE_MODEL.md:620` limits A-14
   to authorized batches and explicitly recognizes resolving named deferrals;
   `../phase-1-ui-reference-production/evidence-capture-plan.csv:32` requires this.
   Read-only probe: completing all 56 B01 primary-owned coordinates and making
   B01 executable still fails the current guard because at least 384 coordinates
   belonging to other primary owners remain unmet, including held B07.
   Exit: resolve execution eligibility and permitted deferral per obligation owner;
   independently test complete B01 with held B07 and incomplete executable B01.

3. **MEDIUM — Staff evidence vocabulary contradicts its scope exception.**
   `../phase-1-ui-reference-production/evidence-capture-plan.csv:33` (EC-32,
   all_batches) permits only four public stream IDs. EC-08 at line 9 instead
   requires staff `SCOPE_EXCLUDED` and `STREAM-SCOPE-EXCLUDED`, which the shared
   resolver and production validator correctly preserve as nonpublic evidence.
   Exit: make EC-32 explicitly distinguish public streams from resolved excluded
   staff scope; retain exactly one scope per row and prohibit a fifth public stream.

All three findings preexist D-051–D-057: production validator code is identical
to HEAD, and EC-32 is unchanged. The current decisions did not introduce them.
They nevertheless prevent MA-029 acceptance of the current evidence package.

## Verified definition strengths and remaining gates

- Independently ran `scripts/validation/test-ui-stream-mapping.ps1`: PASS,
  1000 checks, 440 frame obligations. Mutation checks resolve actual primitives
  and dependencies, not row counts: content can restrict a consumer; shared
  content cannot expand a World host; semantic World-HUD claims are rejected.
- Public routes resolve four streams; four World templates resolve three; six
  staff templates retain excluded baseline evidence. The discriminator is
  load-bearing and the deletion of per-record stream_profile remains intact.
- B01 remains future_not_authorized; B07 remains deferred_not_authorizable.
  B01 owns shell recovery, B07 World/reset evidence, and B02 privacy instances.
  `/privacy` remains inactive; equivalent destinations and non-World initial
  home framing persist (style guide line 483). D-057 resolves copy/order only.
- Gated visual values are expected, not defects in a definition. D-055 leaves
  backing thickness, geometry/layering and bounded-scene method verification open;
  UG-2 focus values and UG-6 action/state pairings still need reviewed approval.
  U-03 thresholds, final legal facts/copy and actual browser/AT evidence remain
  deferred. Native radio rendering is preserved by D-054. No measured result exists.
- A-11's classifier restriction and unresolved G-5/time_limit_branch remain
  declared governance/model gaps; this review does not silently approve exemptions.
  Historical proposed headers and superseded UG entries do not supersede decisions.

MA-029 remains undischarged pending the findings' scoped correction and independent
recheck, the companion accessibility review, and the applicable founder decision.

## Current independent recheck — 2026-10-03

**Verdict: PASS for the current definition/evidence-verifier package.**
Open findings in this reviewed scope: **CRITICAL 0; HIGH 0; MEDIUM 0**.
Independent reviewer: `reset_definition`. Producers: `root` and `verify_r044`.
The reviewer did not author `ui-exit-coverage.ps1`; this recheck independently
inspects producer implementation, including that helper, rather than accepting
the producer's own certification. Original FAIL findings above remain preserved
as historical evidence; the current verdict closes their identified defects.

Reviewed input snapshot: **74 files**, SHA-256
`027E4DFCEB674AFF84B39B82B93096CB8EADB178E090CDD489509BC30FB29D2B`.
Snapshot algorithm: ordinal-sort repository-relative paths for recursively
included md/csv/ps1 files in the design, production and UX packages, excluding
`/reviews/`; include all `scripts/validation/*.ps1`, AGENTS.md, constitution,
PROJECT.md, DECISIONS.md, TASKS.md, active SRS/style guide and foundation route
inventory JSON. Each digest line is uppercase file SHA-256, two spaces, path;
join with LF and no final newline; hash UTF-8 without BOM. Review reports are
excluded so appending this verdict does not alter its input snapshot.

### Previous design findings closed

- Evidence IDs and manifest columns resolve against accepted batch, template,
  instance and profile ownership; unknown or disagreeing values are rejected.
- Target batch eligibility and coverage follow the owning batch, explicit pilot
  authorization/acceptance and pinned prerequisite exits. A pilot does not
  authorize unrelated exits or waive a target's own evidence.
- EC-32 preserves the excluded staff scope consistently with EC-08; it does
  not create a fifth public stream.

### Current implementation inspection

`scripts/validation/ui-exit-coverage.ps1` enforces the same necessary coverage
for target, accepted-pilot and prerequisite manifests: ordinary axes, critical
visual frames, complete viewport minima, profile/primitive ownership and route
instance sheets. Privacy requires its own notice frame in every stream; generic
or credits evidence cannot substitute. Qualitative evidence still requires the
independent pinned reports rather than a mechanical conformance claim.

D-060 registry/resolution isolates boundary identities from ordinary profiles;
eight destination triples and twelve directed cases retain B07 ownership,
visible destination focus, ordered annotation and ancestor substitution.
B01 same-shell proof remains separate. The active contract grammar/mapping,
D-057 copy reconciliation and D-058 dismissal/test requirements agree with the
accepted decisions. No new application behavior is selected by these validators.

Independent verification: stream regression **1026 checks / 440 ordinary frame
obligations PASS**; pilot/release **43 checks PASS**; exit coverage **21 checks
PASS**; boundary evidence **44 checks / 8 triples / 12 cases PASS**.
Design validator: **210 PASS / 1 FAIL**, solely cumulative uncommitted
write-scope guard. Production validator: **172 PASS / 1 FAIL**, solely its
cumulative uncommitted write-scope guard. Definition mode reports outstanding
evidence without certifying an exit. Deferred commits explain these known guard
failures; this review does not waive or relabel them as validator PASS.

UG-2/UG-6 visual values, UG-4 measurement, approved scene geometry/envelopes,
legal content and actual browser/assistive-technology evidence remain future
gates. Gated values are not fabricated conformance results. This definition
review is not a B01 or other batch-exit review, application acceptance, complete
Phase 1 approval, accessibility conformance or founder approval. It authorizes
no Figma operation, visual production, publication, commit, push or deployment.
MA-029 closure and any B01 authorization still require their founder decision.

# A-02 — Distinct boundary evidence allocation

**Accepted definition under D-060 — independent specification author under D-044; corrected nonauthor review PASS. Implementation and verification authorized; visual production remains held.**
Date: 2026-10-03. Original proposal below is provenance adopted by D-060. No actual frames, provider calls or conformance are claimed.

## Authority and minimum outcome

Accepted OBL-BND-01–04 and NFR-A11Y-010 require destination-visible focus, stream/location/substitution announcement and ordered shell replacement in both directions. Same-shell STATE-STREAM-CHANGED retains focus and cannot satisfy those obligations. MA-029 accessibility A-02 identifies missing allocation, not an undecided focus behavior. Preserve D-057 approved copy and refusal of a change unable to preserve booking state; no destructive crossing is introduced.

Recommend B07 as the existing primary owner of **all boundary and nearest-ancestor frames**, using its existing supporting TPL-GLOBAL-NAVIGATION and primary TPL-WORLD-HUD. This avoids increasing B01's shell-only pilot or pretending deferred B07 evidence is already produced. B01 keeps same-shell evidence and explicitly names these B07 deferrals; its acceptance cannot discharge full boundary evidence.

## Proposed explicit obligation rows

| Proposed state identity | Destination template | Destination stream scope | Origin scope | Owner |
|---|---|---|---|---|
| STATE-BOUNDARY-TO-SEMANTIC | TPL-GLOBAL-NAVIGATION | S-SEMANTIC only | S-HIGH, S-MEDIUM, S-LOW separately | B07 |
| STATE-ANCESTOR-TO-SEMANTIC | TPL-GLOBAL-NAVIGATION | S-SEMANTIC only | S-HIGH, S-MEDIUM, S-LOW separately | B07 |
| STATE-BOUNDARY-TO-WORLD | TPL-WORLD-HUD | S-HIGH, S-MEDIUM, S-LOW separately | S-SEMANTIC | B07 |
| STATE-ANCESTOR-TO-WORLD | TPL-WORLD-HUD | S-HIGH, S-MEDIUM, S-LOW separately | S-SEMANTIC | B07 |

These yield eight destination template/state/stream triples, while review must cover twelve directed cases (six mapped crossings and six nearest-ancestor crossings). A semantic destination frame may share visual geometry across its three origins, but its annotated evidence must separately resolve all three source cases; a destination-only picture does not prove every origin. Per-stream World results never inherit another stream's rendering. Exact frames, locations and source-case evidence identifiers await the authorized producer; do not invent scene/UI references.

Each boundary frame shows the incoming shell's named mapped location, stream control visibly focused, and polite stream-and-location announcement. Each ancestor frame is **distinct** from mapped arrival, shows the nearest surviving mapped ancestor and D-057 substitution wording in the actual incoming status surface, and records requested location, mapping failure and chosen ancestor. It must not be an unrelated generic error/recovery frame.

Annotate **both frame classes**, in every directed case, with these ordered steps:

1. Remove outgoing shell from the accessibility tree.
2. Add incoming shell with its status region present and empty; restore preserved process state before announcement under NFR-A11Y-010.
3. Set visible focus on its delivery-stream control; never body or a destroyed node.
4. Write the polite announcement naming new stream and arrival location; ancestor entry also names the substitution and reason.
5. Only for a 3D destination, add canvas after announcement; for S-SEMANTIC annotate “no canvas”.

No simultaneous exposed shells; no message inserted together with a new region. Later keyboard/screen-reader execution evidence verifies ordering, focus visibility and process preservation; a screenshot alone cannot certify timing or assistive announcements. Refused process-state-preservation changes remain refusals, not successful-boundary frames.

## Smallest safe executable-model amendment

Do **not** insert direction-specific identities into DS-S-* stream-critical sets: Get-UiFrameObligations currently unions those identities and multiplies them across every present stream, producing impossible semantic/World obligations. Do not attach these states indiscriminately to every template sharing SP-NAVIGATION.

Recommend one explicit, validated boundary-allocation table carrying the four rows above (template, state, destination scopes, origin scopes, batch), then append its exact scoped obligations to the ordinary calculation. Register the four identities in an **allocation-only state registry**, not in shared profiles' ordinary required_values or critical_distinct_frame_values and not in the generic stream-critical union. Both ordinary state-axis coverage and per-stream generation must exclude allocation-only identities; registry membership must never expand obligations to other profile consumers, batches, templates or streams. The dedicated allocation validator and evidence resolver accept only the exact batch/template/state/destination-stream combinations declared above, with their required origin cases. Validate exact membership, actual destination presence, permitted origin/destination directions, B07 ownership and complete directed-case annotation; retain existing baseline and same-shell generation unchanged.

Reconcile B07 batch wording (qualify “focus not moved” as same-shell only), B01 named deferrals, allocation-only registry, ACT-09/flow trace and production EC-31/manifest coverage against this explicit allocation. Guard tests must reject deleting any row/direction, a wrong batch/destination stream/template, leakage into ordinary state-axis or stream generation, same-shell substitution, absent ancestor wording/ordered annotation, and removal of destination-visible-focus evidence. Do not treat prose-only allocation as completed executable coverage.

## Decision and remaining gates

No fresh product choice is needed for focus destination, mapping, canvas ordering or process preservation: those are approved requirements. The proposed B07 ownership and explicit scope-table mechanism amend the evidence model and need founder acceptance after nonauthor review; they do not authorize B07 visual production or lift MA-026. If the founder needs boundary evidence in the B01 pilot instead, that is a separate scope/production-budget decision, not a silent reassignment.

Missing inputs for actual production remain approved destination references, mapping/ancestor cases and authorized batch evidence. This proposal claims allocation only, not existing visual or runtime proof. Sources: accepted accessibility obligations OBL-BND-01–04; SRS NFR-A11Y-010; A-02 review; current Get-UiFrameObligations behavior.

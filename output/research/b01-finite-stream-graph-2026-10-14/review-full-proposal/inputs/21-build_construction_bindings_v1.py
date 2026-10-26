"""Prepare explicit local design allocation, not evidence of constructed UI."""
import csv
import hashlib
import json
from pathlib import Path

ROOT = Path.cwd()
OUT = ROOT / "output/research/b01-finite-stream-graph-2026-10-14"
BASE = ROOT / "output/research/b01-prototype-workflow-2026-10-13"
SOURCE = json.loads((BASE / "source-bindings-and-cases-v1.json").read_text(encoding="utf-8-sig"))
GRAPH = json.loads((OUT / "full-case-graph-proposal-v1.json").read_text())
RECORDS = SOURCE["complete_recorded_source_catalogue"]["records"]
PROFILES = SOURCE["complete_recorded_source_catalogue"]["profile_requirements"]
STREAMS = ["S-HIGH", "S-MEDIUM", "S-LOW", "S-SEMANTIC"]


def rows(path, key):
    with (ROOT / path).open(encoding="utf-8-sig", newline="") as f:
        return {r[key]: r for r in csv.DictReader(f)}


TEMPLATES = rows("docs/phase-1-ui-reference-design/reference-template-inventory.csv", "template_id")
PRIMITIVES = rows("docs/phase-1-ui-reference-design/component-primitives.csv", "primitive_id")
FLOWS = rows("docs/phase-1-ui-reference-design/foundation-flow-coverage.csv", "source_id")
OWNER = {"TPL-GLOBAL-NAVIGATION": "FLOW-NAVIGATION-SEARCH", "TPL-DIRECTORY-SEARCH": "FLOW-NAVIGATION-SEARCH", "TPL-SYSTEM-RECOVERY": "FLOW-ERROR-OFFLINE-RECOVERY"}
BASE_STATE = {t: "STATE-ERROR" if t == "TPL-SYSTEM-RECOVERY" else "STATE-OPEN" for t in OWNER}
UNITS = {}
OBLIGATIONS = []


def evidence_id(t, instance, state, viewport, mode, stream):
    parts = [t, instance, state, viewport, mode]
    return "HSD_UIR_B01_" + "_".join(x.replace("-", "_") for x in parts) + "_STREAM_" + stream[2:] + "_V01"


def unit(t, state, viewport, mode, stream, kind="FRAME", instance="REF"):
    eid = evidence_id(t, instance, state, viewport, mode, stream)
    if eid in UNITS:
        assert UNITS[eid]["evidence_type"] == kind, "Evidence ID/type collision"
        return eid
    axes = {"template_id": t, "state_id": state, "viewport_id": viewport, "mode_id": mode, "stream_id": stream}
    exact = [r for r in RECORDS if all(r["declared_axes"].get(k) == v for k, v in axes.items())]
    # No arbitrary source from another stream/host earns the coordinate.
    baseline = [r for r in RECORDS if all(r["declared_axes"].get(k) == v for k, v in {**axes, "state_id": BASE_STATE[t], "viewport_id": "VP-320", "mode_id": "MODE-KEYBOARD"}.items())]
    selected = exact[0] if exact else baseline[0] if baseline else None
    UNITS[eid] = {
        "evidence_id": eid, "evidence_type": kind, **axes, "instance_id": instance.replace("-", "_"),
        "owner_id": t if instance == "REF" else OWNER[t],
        "export_role": "Template coordinate" if instance == "REF" else "Flow-owned interaction/semantic evidence",
        "actual_owned_node_id": None, "actual_export_path": None, "observed_or_accepted": False,
        "source_candidate_id": selected["expected_node_id"] if selected else None,
        "source_candidate_axes": selected["declared_axes"] if selected else None,
        "source_is_exact_coordinate": bool(exact),
        "operation": "Inspect exact source and reuse only after qualitative admission" if exact and kind == "FRAME" else "Construct isolated owned evidence from admitted baseline; no protected-source edits",
        "lineage": {"recorded_source_name": selected["recorded_name"] if selected else None, "reported_size": selected["reported_size"] if selected else None},
        "qualitative_admission": "Check complete context, truthful state, labels, anatomy, text spacing/reflow, active/pending distinction, focus and failure paths. Name or exact axis match alone earns no coverage.",
        "primitives": TEMPLATES[t]["primitive_dependencies"].split(";"),
        "profile_ids": [TEMPLATES[t][k] for k in ["state_profile", "viewport_profile", "mode_profile", "browser_profile", "time_limit_branch"]] + ["DS-" + stream],
        "time_limit_branch": TEMPLATES[t]["time_limit_branch"] if instance == "REF" else FLOWS[OWNER[t]]["time_limit_branch"],
    }
    return eid


# Full frames are chosen for viewport values instead of claiming unmeasured
# intermediate-width annotation equivalence. This is linear profile coverage,
# not a state x viewport x mode Cartesian product.
for p in PROFILES:
    t = p["template_id"]
    dimension = "state" if p["profile_id"].startswith("SP-") else "viewport" if p["profile_id"].startswith("VP-") else "mode"
    for value in p["required_values"]:
        for stream in STREAMS:
            state, viewport, mode = BASE_STATE[t], "VP-320", "MODE-KEYBOARD"
            if dimension == "state": state = value
            if dimension == "viewport": viewport = value
            if dimension == "mode": mode = value
            eid = unit(t, state, viewport, mode, stream)
            OBLIGATIONS.append({"template_id": t, "profile_id": p["profile_id"], "value": value, "stream_id": stream,
                "critical": value in p["critical_distinct_frame_values"], "unit_id": eid,
                "minimum_evidence": p["minimum_evidence"], "annotation_requirements": p["annotation_requirements"],
                "exception_rule": p["exception_rule"], "qualitatively_discharged": False})


# Public flow units compose private case branches. No pending-stream field is
# invented in the evidence grammar. Effective tuples remain case associations,
# never used to count the entry coordinate as every observed destination.
PROTOTYPES, ANNOTATIONS = [], []
OUTGOING = {}
for e in GRAPH["edges"]:
    OUTGOING.setdefault(e["from"], []).append(e["to"])
for t, owner in OWNER.items():
    assert t in FLOWS[owner]["template_ids"].split(";")
    for stream in STREAMS:
        proto = unit(t, "STATE-FOCUS", "VP-320", "MODE-KEYBOARD", stream, "PROTOTYPE", owner)
        annotation = unit(t, BASE_STATE[t], "VP-320", "MODE-KEYBOARD", stream, "ANNOTATION", owner)
        entries = [e for e in GRAPH["entries"] if e["entry_active"] == stream and any(n["symbol"] == e["node"] and n["template"] == t for n in GRAPH["nodes"])]
        reachable, queue = set(), [e["node"] for e in entries]
        while queue:
            symbol = queue.pop()
            if symbol in reachable: continue
            reachable.add(symbol)
            queue.extend(OUTGOING.get(symbol, []))
        associated = [n for n in GRAPH["nodes"] if n["symbol"] in reachable]
        PROTOTYPES.append({"unit_id": proto, "public_entry_state": "Visibly simulated focus on initial Menu/Directory action or appropriate recovery control",
            "private_nodes": [n["symbol"] for n in associated], "case_ids": sorted({c for n in associated for c in n["case_ids"]}),
            "entry_to_case_policy": "Labelled private inspection index reaches exact graph entry; entering a fixture grants no product permission. Actual entry and component default must be checked.",
            "ownership_policy": "Each public prototype owns independent copies of its reachable private sets and boundary frames. Symbolic recipes may repeat across prototypes; actual IDs never shared between public compositions. Explicit inspection restart must qualify initial defaults and cannot be mistaken for granted access.",
            "anchor_coordinate_only": True, "result_coordinates_earned_by_entry": False})
        ANNOTATIONS.append({"unit_id": annotation, "prototype_unit_id": proto,
            "case_entries": entries,
            "case_observation_fields": ["private_node_symbol", "actual_owned_id", "active", "pending", "route_query_panel", "control_action_target", "nonzero_scroll_anchor", "visible_focus_annotation", "what_is_observed", "what_is_only_authored", "capture_locator"],
            "semantics": "Design/reference annotations only. In-force stream is single-valued. No FRAME/PROTOTYPE/ANNOTATION duplicate ID and no added INSTANCE or public state token."})


STAGE_TO_STATE = {
    "CLOSED": "STATE-CLOSED", "OPEN": "STATE-OPEN", "BASE": "STATE-CLOSED", "FOCUS": "STATE-FOCUS",
    "EMPTY-QUERY": "STATE-EMPTY-QUERY", "QUERY-DESIGN": "STATE-RESULTS", "QUERY-UNMATCHED": "STATE-NO-RESULTS",
    "RESULTS": "STATE-RESULTS", "NO-RESULTS": "STATE-NO-RESULTS", "LOADING": "STATE-LOADING",
    "DERIVED-INDEX-UNAVAILABLE": "STATE-DERIVED-INDEX-UNAVAILABLE", "OFFLINE": "STATE-OFFLINE", "ERROR": "STATE-ERROR",
    "STALE": "STATE-STALE", "CONFLICT": "STATE-CONFLICT", "ASSET-FAILURE": "STATE-ASSET-FAILURE",
    "CHECKSUM-MISMATCH": "STATE-CHECKSUM-MISMATCH", "REFUSED": "STATE-STREAM-CEILING-REFUSED",
    "PREFERENCE-WRITE-FAILED": "STATE-PREFERENCE-WRITE-FAILED", "PENDING": "STATE-PENDING", "TERMINAL": "STATE-SESSION-EXPIRED",
}
NODE_ALLOCATION = []
for n in GRAPH["nodes"]:
    t, stream = n["template"], n["active"]
    state = STAGE_TO_STATE.get(n["stage"], BASE_STATE[t])
    allowed = next(p["required_values"] for p in PROFILES if p["template_id"] == t and p["profile_id"].startswith("SP-"))
    public_state = state if state in allowed else BASE_STATE[t]
    host_id = unit(t, public_state, "VP-320", "MODE-KEYBOARD", stream)
    NODE_ALLOCATION.append({"private_node_symbol": n["symbol"], "template_id": t, "active_stream": stream,
        "host_unit_id": host_id, "host_is_construction_source_not_branch_proof": True,
        "owned_instantiations": [{"public_prototype_id": p["unit_id"], "logical_component_set": n["private_component_set_symbol"], "actual_owned_id": None, "actual_component_set_id": None} for p in PROTOTYPES if n["symbol"] in p["private_nodes"]],
        "branch_recipe": "Complete owned parent variant with exact graph tuple and correct controls. Adapt an admitted source; a generic ERROR or OPEN label does not represent a distinct Apply/timing/cancellation outcome.",
        "actual_owned_id": None, "actual_component_set_id": None})


ROLE_MAP = {
    "menu": "PRIM-002", "close_navigation": "PRIM-002", "destination": "PRIM-002",
    "open_directory": "PRIM-004", "close_directory": "PRIM-004", "search": "PRIM-004", "clear": "PRIM-004", "browse": "PRIM-004",
    "book": "PRIM-014", "pending_choice": "PRIM-001", "apply": "PRIM-001", "advisement": "PRIM-001",
    "directory_shell_book": "PRIM-001", "recovery_book": "PRIM-015",
    "more_time": "PRIM-015", "ordinary_end": "PRIM-015", "check_current_status": "PRIM-015", "error_summary": "PRIM-023",
}
FUNCTIONAL = []
for role, primitive in ROLE_MAP.items():
    assigned = [t for t in OWNER if primitive in TEMPLATES[t]["primitive_dependencies"].split(";")]
    if role == "directory_shell_book": assigned = ["TPL-DIRECTORY-SEARCH"]
    if role == "recovery_book": assigned = ["TPL-SYSTEM-RECOVERY"]
    FUNCTIONAL.append({"role": role, "intended_functional_primitive": primitive, "assigned_templates": assigned,
        "mechanical_source": "14:18 PRIM-015 visual proxy only; preserve master" if role not in ["pending_choice", "advisement", "error_summary"] else "Admitted host/control anatomy; no whole-fieldset or semantic claim from static text",
        "required_approved_definition": PRIMITIVES[primitive],
        "owned_topology": "Dedicated labelled owned control in the owning host; exact property/descendant and reaction recorded after copying. Selector is parent-owned A/P state, never shared mutable nested selector.",
        "guard": "A copied PRIM-015 appearance does not add PRIM-015 to navigation/directory dependencies. Inspect each assigned functional primitive's complete anatomy/states, not just Label."})

GRAMMAR = [{"state_id": r["declared_axes"]["state_id"], "surface": r["declared_axes"]["surface_id"],
    "source_id": r["expected_node_id"], "source_annotation_id": r["expected_annotation_id"], "fixture": r["fixture"],
    "role": "Shared focused visual specimen only, supplement correctly contextualised per-stream host. No standalone host/profile coverage or automatic action mapping.", "qualitatively_discharged": False}
    for r in RECORDS if r["source_family"] == "shared_recovery_grammar"]

GUARDS = [
    {"stage": "Source admission", "operation": "Read-only normal editor", "checks": ["Exact file/page, source ID/type/parent chain/name/dimensions", "Visible text, properties, approved tokens/fonts and required descendants", "Reaction triggers/actions/destinations/no duplicate or inherited writes", "Source axes and contextual fixture match allocation; source cannot be selected by generic name only"], "on_missing": "Hold affected source; no hidden API, capped MCP, AI retry or silent substitute"},
    {"stage": "Pre-copy", "operation": "Editable archive plus recorded selected-source baseline", "checks": ["Existing private/team-restricted sharing and active account", "Protected source/control baseline and admitted source inventory", "Exact owner-labelled isolated section and composition manifest; no master target", "Applicable explicit external-write release and remaining revision allowance"], "on_missing": "No copy"},
    {"stage": "Owned discovery", "operation": "Bounded native copy after release", "checks": ["Discover actual new root/set/component/instance/control/annotation IDs through visible layers", "Compare actual tuple/type/parent/geometry/property/reaction against symbolic manifest", "Component sets isolated; no guessed aliases or outside-parent writes", "Capture native archive/checkpoint before wiring"], "on_missing": "Stop affected operation; no unapproved detach/delete/undo of originals"},
    {"stage": "Wire and inspect", "operation": "One independently reviewed edge at a time within admitted owned set", "checks": ["Actual source/control/target ID associations, same owned set for Change-to", "One expected action/trigger only and exact target tuple", "Private scroll-body name/dimensions match; inspect nonzero scroll on Apply and return", "Navigate-to fixed boundary defaults and key simulations qualified first", "All four streams/case branches and qualitative profiles inspected"], "on_missing": "Do not credit unqualified edge/profile"},
    {"stage": "Exit", "operation": "Provider-independent exports and immutable review packet", "checks": ["Unique allowed evidence identity and exact export association", "Actual case observations and separately labelled authored semantics", "Protected source equivalence demonstrated at required scope", "Tested native restore and _EXIT checkpoint under applicable release", "Independent design/accessibility review then founder B01 acceptance"], "on_missing": "No pilot/later-batch/Phase1 acceptance"},
]

result = {"product": "Hengshi Design v1", "status": "DOING", "date": "2026-10-14",
    "scope": "Full case/profile allocation proposal and staged safeguards; not a complete executable release or constructed evidence",
    "units": list(UNITS.values()), "profile_obligations": OBLIGATIONS, "prototypes": PROTOTYPES, "annotations": ANNOTATIONS,
    "node_allocation": NODE_ALLOCATION, "functional_roles": FUNCTIONAL, "shared_recovery_specimens": GRAMMAR, "staged_guards": GUARDS,
    "complete_assigned_primitive_definitions": [{"template_id": t, "primitive_id": p, "approved_definition": PRIMITIVES[p], "qualitative_anatomy_states_and_evidence_mapping": "TODO; row attachment is a requirement, not coverage", "actual_owned_ids": None} for t in OWNER for p in TEMPLATES[t]["primitive_dependencies"].split(";")],
    "private_composition_policy": "Public prototype is one correctly owned inspection composition per family/stream, visibly focused at entry. Private case/pending branches and inspection navigation have internal symbols only; no pending axis or fabricated public state/INSTANCE. Observed effective tuples never earn unexported frame coordinates.",
    "remaining": ["Independent review of identities, graph semantics and profile/source interpretation", "Qualitative visual/source admission and complete functional primitive coverage", "Exact new intermediate viewport measurements and stress layouts", "Fresh native action/scroll/default qualifications", "Complete owned component-set/source manifest after guarded discovery", "Explicit external release, actual complete case/profile execution, preservation/restore/_EXIT and founder acceptance"],
    "external_write_released": False, "runtime_proof": False, "pilot_accepted": False, "independent_review": None}
assert len(UNITS) == len(set(UNITS))
assert len(NODE_ALLOCATION) == len(GRAPH["nodes"])
assert all(o["unit_id"] in UNITS for o in OBLIGATIONS)
assert len(PROTOTYPES) == len(ANNOTATIONS) == 12
assert len(GRAMMAR) == 48
(OUT / "construction-bindings-proposal-v1.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf8")
print(json.dumps({"proposed_units": len(UNITS), "profile_obligations": len(OBLIGATIONS), "private_node_bindings": len(NODE_ALLOCATION), "interpretation": "Artifact allocation only; actual IDs, source admission and qualitative coverage remain unproven"}))

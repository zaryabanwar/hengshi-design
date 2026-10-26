"""Local per-use construction blueprint; never application or Figma mutation."""
import csv
import hashlib
import json
import re
from pathlib import Path

ROOT = Path.cwd()
PRIOR = ROOT / "output/research/b01-finite-stream-graph-2026-10-14"
OUT = ROOT / "output/research/b01-control-anatomy-2026-10-14"
GRAPH = json.loads((PRIOR / "full-case-graph-proposal-v1.json").read_text())
ALLOC = json.loads((PRIOR / "construction-bindings-proposal-v1.json").read_text())
PREP = json.loads((ROOT / "output/research/b01-prototype-workflow-2026-10-13/source-bindings-and-cases-v1.json").read_text(encoding="utf-8-sig"))


def csv_rows(path, key):
    with (ROOT / path).open(encoding="utf-8-sig", newline="") as f:
        return {r[key]: r for r in csv.DictReader(f)}


PRIMS = csv_rows("docs/phase-1-ui-reference-design/component-primitives.csv", "primitive_id")
TPLS = csv_rows("docs/phase-1-ui-reference-design/reference-template-inventory.csv", "template_id")
COPY_PATH = "docs/phase-1-ui-reference-design/accessibility/UG-3_CONTROL_COPY_PROPOSAL.md"
COPY_TEXT = (ROOT / COPY_PATH).read_text(encoding="utf-8-sig")
# Read the accepted phrases from their source rather than inventing wording.
COPY_ROWS = {}
for line in COPY_TEXT.splitlines():
    if line.startswith("| ") and line.count("|") == 3:
        context, wording = [x.strip() for x in line.strip("|").split("|")]
        if wording.startswith("“"):
            COPY_ROWS[context] = wording.split("”", 1)[0][1:]
STREAM_LABELS = {"S-HIGH": "Detailed 3D", "S-MEDIUM": "Balanced 3D", "S-LOW": "Simplified 3D", "S-SEMANTIC": "Quick Access"}
NODES = {n["symbol"]: n for n in GRAPH["nodes"]}
NODE_ALLOC = {n["private_node_symbol"]: n for n in ALLOC["node_allocation"]}


def slug(value):
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def semantic_slot(primitive, text):
    if primitive == "PRIM-001" and "radio" in text:
        return "Four authored native-radio semantics annotations; parent A/P variant renders checked state. Not Figma text pretending to be actual DOM radio inputs."
    if "legend" in text or "fieldset" in text:
        return "Authored group/legend association; resulting semantic HTML after implementation must supply the native element."
    if "status" in text:
        return "Persistent authored status text with scope/announcement/focus annotation; no live-region runtime claim."
    if "focus" in text or "invoker" in text:
        return "Visible focus/reference relationship annotation, backed by a separately inspected prototype path where available."
    if "link" in text or "destination" in text:
        return "Separate labelled canonical-link/action slot with exact target; no combined-text hotspot or invented publication."
    if "control" in text or "action" in text or "close" in text or "trigger" in text:
        return "Dedicated labelled owned control, exact target area and expected single reaction bound after discovery."
    return "Dedicated named owned text/shape/content slot; preserve approved meaning, approved assets and non-colour redundancy."


BLUEPRINTS = []
for assigned in ALLOC["complete_assigned_primitive_definitions"]:
    t, primitive = assigned["template_id"], assigned["primitive_id"]
    row = PRIMS[primitive]
    allowed_streams = row["stream_presence"].split(";")
    anatomy = []
    for i, text in enumerate(row["required_anatomy"].split(";")):
        anatomy.append({"slot": f"{t}/{primitive}/anatomy/{i:02}-{slug(text)}", "source_requirement": text,
            "owned_private_layer_name": f"HSD private {primitive} / {i:02} / {text}", "construction_instruction": semantic_slot(primitive, text),
            "conditional_guard": "Retain qualification stated in the approved anatomy; no optional counter/icon/dismissal/reauthentication introduced without the named applicability",
            "actual_owned_id": None, "observed": False})
    BLUEPRINTS.append({"template_id": t, "primitive_id": primitive, "blueprint_symbol": f"{t}/{primitive}",
        "allowed_streams": allowed_streams, "required_anatomy_slots": anatomy,
        "variant_slots": [{"variant": v, "private_symbol": f"{t}/{primitive}/variant/{v}", "required_definition": "Preserve the accepted variant meaning; not a new product state/INSTANCE", "scope_guard": "Absolute expiry is a staff/session reference only; D076 gives visitors no absolute conversation limit" if v == "absolute_expired" else "Staff-separate/auth/role fixtures are supplemental references, not public visitor routes or operational grants" if v in ["staff", "staff_separate", "active_role", "CSRF_failure", "ambiguous_role"] else "Apply named availability/approval qualifiers from the canonical row; this reference cannot enlarge graph/product scope", "constructed_or_accepted": False} for v in row["required_variants"].split(";")],
        "pseudo_state_slots": [{"state": s, "private_symbol": f"{t}/{primitive}/pseudo/{s}", "rendering": "Approved focus/text/shape/border redundancy; no colour-only state. Inherit admitted tokens/fonts, no new asset or typeface.", "constructed_or_accepted": False} for s in row["pseudo_states"].split(";")],
        "transaction_slots": [{"state": s, "private_symbol": f"{t}/{primitive}/transaction/{s}", "required_truth": row["state_redundancy"], "constructed_or_accepted": False} for s in row["transactional_or_content_states"].split(";")],
        "responsive_and_mode_requirement": row["responsive_and_mode_obligations"], "source_requirements": row["source_requirements"].split(";"),
        "source_actions": row["source_actions"].split(";"), "source_ux_tests": row["source_ux_tests"].split(";"),
        "evidence_destination": "Attach exact slot/state/variant observations to the admitted allocated host/owned component reference and its permitted stream; no coverage from this blueprint alone",
        "host_guard": "Alternative World component reference only in S-HIGH/S-MEDIUM/S-LOW. No HUD in Quick Access, and no live World inferred from a prior 3D preference on a semantic host." if primitive in ["PRIM-043", "PRIM-044"] else "Use only within the assigned approved template and stream support",
        "physical_source_admission": None, "actual_owned_root_id": None, "qualitative_evidence_complete": False})


def classify(n, control):
    t = n["template"]
    if control.startswith("inspection_") or control == "next_simulated_focus":
        return None, "private-inspection", "Inspection-only fixture control; visually separate from the visitor interface and labelled as simulation"
    if control in ["apply", "apply_control", "apply_current"] or control.startswith("pending_choice/") or control == "choose_quick_access":
        return "PRIM-001", "stream-control", "Parent-owned four-radio/Apply anatomy; no shared mutable nested selector"
    if control == "book":
        return {"TPL-GLOBAL-NAVIGATION": "PRIM-014", "TPL-DIRECTORY-SEARCH": "PRIM-001", "TPL-SYSTEM-RECOVERY": "PRIM-015"}[t], "booking-boundary", "Direct visible Book; fixed B06 /book boundary only, no availability or confirmed booking"
    if control in ["menu", "menu_activation", "close_activation"] or control.startswith("destination/"):
        return "PRIM-002", "navigation", "Dedicated menu or labelled destination control, not one combined text layer"
    if control == "host":
        return "PRIM-002" if t == "TPL-GLOBAL-NAVIGATION" else "PRIM-004", "container-key-simulation", "Escape belongs to the disclosure/modal host, never the delivery-stream control or a navigation/back action"
    if control == "close":
        return "PRIM-002" if t == "TPL-GLOBAL-NAVIGATION" else "PRIM-004", "close", "Visible named Close with same invoker/fallback-focus lineage"
    if control in ["open_directory", "search", "clear", "browse", "browse_static_directory"]:
        return "PRIM-004", "directory", "Modal heading/labelled input/Clear/group browse/status/Close; query fixtures only"
    if control.startswith("result/"):
        return "PRIM-005", "canonical-result", "Separate canonical link inside a typed/context-labelled result row; no whole-card ambiguity or raw query URL"
    if control in ["more_time", "ordinary_end", "check_current_status", "try_again", "continue_browsing"]:
        return "PRIM-015" if t == "TPL-SYSTEM-RECOVERY" else "PRIM-058", "safe-recovery", "Explicit scope/result/preservation and smallest safe recovery; no unknown operation becomes a new dispatch or success"
    if control in ["canonical_page", "public_recovery", "public_website", "services", "start_new_session_boundary"]:
        return "PRIM-016" if "PRIM-016" in TPLS[t]["primitive_dependencies"].split(";") else "PRIM-058", "canonical-boundary", "Dedicated foreground public recovery link or explicit B05 boundary; no modal-background wiring, private-access revival or automatically restored transcript"
    raise ValueError(f"Unclassified real control {t}: {control}")


CONTROL_USES = []
BUTTON_CONTROLS = {"apply", "apply_control", "apply_current", "book", "menu", "menu_activation", "close", "close_activation", "open_directory", "search", "clear", "browse", "more_time", "ordinary_end", "check_current_status", "try_again", "continue_browsing"}
BLUEPRINT_BY_PAIR = {(b["template_id"], b["primitive_id"]): b for b in BLUEPRINTS}


def anatomy_patterns(primitive, control):
    if primitive == "PRIM-001":
        if control.startswith("pending_choice/") or control == "choose_quick_access": return ["four native stream radio", "stream fieldset", "stream legend"]
        if control.startswith("apply"): return ["Apply submit", "advisement", "status region"]
        return ["direct Book access"]
    if primitive == "PRIM-002":
        if control.startswith("destination/"): return ["destination list", "current item"]
        if control.startswith("menu"): return ["menu trigger", "navigation label"]
        return ["close action", "menu trigger"]
    if primitive == "PRIM-004":
        return {"open_directory":["open control"],"clear":["clear"],"search":["search label/input","status"],"browse":["group navigation"],"browse_static_directory":["group navigation","status"],"close":["close"],"host":["close"]}[control]
    if primitive == "PRIM-005": return ["type label", "formal title", "context", "canonical link"]
    if primitive in ["PRIM-014", "PRIM-015"]: return ["visible", "state text", "focus indicator"]
    if primitive == "PRIM-016": return ["visible link text", "destination context"]
    if primitive == "PRIM-058": return ["alternate route"] if control in ["services","public_recovery","public_website","canonical_page","start_new_session_boundary"] else ["smallest safe recovery", "status region", "what remains valid"]
    raise ValueError(f"Missing anatomy mapping {primitive}:{control}")


for i, e in enumerate(GRAPH["edges"]):
    n, target = NODES[e["from"]], NODES[e["to"]]
    primitive, classification, anatomy = classify(n, e["control_symbol"])
    if primitive:
        assert primitive in TPLS[n["template"]]["primitive_dependencies"].split(";"), "New primitive dependency refused"
        assert n["active"] in PRIMS[primitive]["stream_presence"].split(";"), "Unsupported primitive/stream refused"
    public_owners = [x["public_prototype_id"] for x in NODE_ALLOC[n["symbol"]]["owned_instantiations"]]
    anatomy_refs = [] if primitive is None else [slot["slot"] for slot in BLUEPRINT_BY_PAIR[(n["template"], primitive)]["required_anatomy_slots"] if any(p.lower() in slot["source_requirement"].lower() for p in anatomy_patterns(primitive, e["control_symbol"]))]
    assert primitive is None or anatomy_refs, "Functional control lacks exact anatomy slot"
    CONTROL_USES.append({"edge_index": i, "source_symbol": n["symbol"], "control_symbol": e["control_symbol"], "destination_symbol": target["symbol"],
        "classification": classification, "functional_primitive": primitive, "required_control_topology": anatomy,
        "owned_control_slot": n["symbol"] + "/control/" + slug(e["control_symbol"]),
        "anatomy_slot_refs": anatomy_refs,
        "independent_physical_copy_slots": [{"owner": owner,"private_control_slot":owner+"/private/"+n["symbol"]+"/control/"+slug(e["control_symbol"]),"actual_owned_id":None} for owner in public_owners],
        "trigger": e["trigger"], "one_action": e["action"], "public_composition_owners": public_owners,
        "actual_owned_source_control_destination_ids": None,
        "source_mechanical_proxy": (
            "Owned inspection-only fixture, no public primitive/evidence credit" if primitive is None else
            "14:18 permitted as button appearance starting point only; inherit admitted Label/style/font/token; no source/master write" if e["control_symbol"] in BUTTON_CONTROLS else
            "21:25 stream master radio anatomy is an appearance candidate only; construct an owned checked/unchecked native-radio reference, never substitute a General action button" if e["control_symbol"].startswith("pending_choice/") or e["control_symbol"] == "choose_quick_access" else
            "No visual control copy for host-scoped key trigger; retain qualified host/context and separate focus annotation" if e["control_symbol"] == "host" else
            "Admitted matching host/result canonical text/link anatomy; separate label/target/context and non-colour link affordance, never assume a combined text layer supplies independent destinations"
        ),
        "copy_guard": "Accepted D057 stream copy overrides illustrative graph.copy strings; preserve graph outcome meaning and do not change its reviewed bytes",
        "geometry_guard": "Measure each admitted target and visible label at least24x24 CSS-px reference intent; wrap/expand without clipping; actual device/CSS evidence later",
        "focus_annotation": e.get("focus_annotation", n.get("focus_annotation", "Retain focus for ordinary status; explicit action/route focus follows its approved case")),
        "observation": "TODO; exact discovered ID/property/reaction and actual Presentation behavior required before evidence credit"})

STREAM_CONTROL = {
    "functional_owner": "PRIM-001", "alternative_world_owners": ["PRIM-043", "PRIM-044"],
    "proposed_private_anatomy_order": ["legend_active_stream", "peer_explanation", "four_native_radio_reference_options", "persistent_advance_advisement", "separate_apply", "privacy_link"],
    "order_scope": "Advisement must precede Apply in visual/DOM order. Other placement is a construction proposal within accepted constraints, not implementation.",
    "radio_order": [{"stream_id": s, "exact_label": v, "role_specification": "native radio", "shared_name_specification": "One fieldset-local radio group", "checked_is": "pending only", "active_is_reported_by": "legend"} for s,v in STREAM_LABELS.items()],
    "accepted_copy_source": COPY_PATH, "accepted_phrase_templates": COPY_ROWS,
    "accepted_peer_explanation": re.search(r'Proposed persistent peer explanation: \*\*“([^”]+)”\*\*', COPY_TEXT).group(1),
    "control_trigger_guard": "Selection/focus/Tab/arrows/blur/time cannot Apply; Escape has no stream-control reaction. Explicit Apply or scoped native form submit only. Native Enter and real radio-arrow semantics are annotated, not Figma global-key bindings.",
    "disabled_above_ceiling": "Keep the peer option visible, textually explain the verified capability fact, and disable choice under current ceiling. Refusal chronology fixture retains a choice made before established unavailability.",
    "status_guard": "Empty page status exists before changes; same-shell polite status retains focus/scroll/context. Radio changes never announce successful application. Above-ceiling/failure/newer/unknown branches retain authority truth.",
    "annotation_guard": "Figma native component/shape/text is not the resulting semantic DOM. Include names, shared group, associations, reading/focus order and native interaction notes; real DOM/browser/AT checks remain later.",
    "actual_controls_or_runtime": False,
}

bindings=[]
for p in ["docs/phase-1-ui-reference-design/component-primitives.csv", "docs/phase-1-ui-reference-design/reference-template-inventory.csv", "docs/phase-1-ui-reference-design/DESIGN_SYSTEM_IMPLICATIONS.md", COPY_PATH,
    "output/research/b01-finite-stream-graph-2026-10-14/full-case-graph-proposal-v1.json", "output/research/b01-finite-stream-graph-2026-10-14/construction-bindings-proposal-v1.json", "output/research/b01-finite-stream-graph-2026-10-14/review-full-proposal/correction1/independent-review-full-proposal-v1.json"]:
    raw=(ROOT/p).read_bytes();bindings.append({"path":p,"bytes":len(raw),"sha256":hashlib.sha256(raw).hexdigest()})
result={"product":"Hengshi Design v1","status":"DOING","date":"2026-10-14","scope":"Proposed exact per-use control/component construction anatomy; not source admission, actual semantic UI, external release or coverage", "authority_bindings":bindings,
    "component_blueprints":BLUEPRINTS,"control_uses":CONTROL_USES,"delivery_stream_control":STREAM_CONTROL,
    "remaining":["Independent control/anatomy proposal review", "Fresh exact source/property/style/font/token/reaction admission", "Actual owned source/control IDs and guarded per-composition copy manifest", "Qualified native action/default/scroll and complete case/profile/variant inspection", "Native source preservation/tested restore/EXIT, design/accessibility review and founder B01/Phase1 acceptance"],
    "external_write_released":False,"application_changed":False,"runtime_proof":False,"independent_review":None}
OUT.mkdir(exist_ok=True)
(OUT/"control-anatomy-bindings-v1.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf8")
print(json.dumps({"component_blueprints":len(BLUEPRINTS),"edge_control_use_bindings":len(CONTROL_USES),"private_inspection_uses":sum(x['functional_primitive'] is None for x in CONTROL_USES),"accepted_copy_templates":len(COPY_ROWS),"scope":"Construction definition only; no observed or accepted coverage"}))

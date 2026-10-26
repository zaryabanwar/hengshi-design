"""Build a local proposed Figma fixture graph, never application/runtime evidence."""
import csv
import hashlib
import json
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path.cwd()
BASE = ROOT / "output/research/b01-prototype-workflow-2026-10-13"
OUT = ROOT / "output/research/b01-finite-stream-graph-2026-10-14"
SOURCE = json.loads((BASE / "source-bindings-and-cases-v1.json").read_text(encoding="utf-8-sig"))
CORE = json.loads((OUT / "finite-stream-subgraph-v1.json").read_text(encoding="utf8"))
REFUSALS = json.loads((ROOT / "output/research/b01-ceiling-refusal-bindings-2026-10-09/execution-preparation/input.json").read_text(encoding="utf-8-sig"))
STREAMS = ["S-HIGH", "S-MEDIUM", "S-LOW", "S-SEMANTIC"]
TEMPLATES = {"navigation": "TPL-GLOBAL-NAVIGATION", "directory": "TPL-DIRECTORY-SEARCH", "recovery_host": "TPL-SYSTEM-RECOVERY"}
NODES, EDGES, ENTRIES = [], [], []


def node(symbol, case, family, active, stage, pending=None, **fields):
    value = {
        "symbol": symbol, "case_ids": case if isinstance(case, list) else [case],
        "template": TEMPLATES[family], "family": family, "active": active,
        "pending": pending or active, "stage": stage, "owned_actual_id": None,
        "context": {"route_fixture": "ROUTE-SERVICES", "path": "/services", "query_fixture": fields.get("query", "design" if family == "directory" else None), "world_entered": False},
        "reference_fixture": True, "public_copy": False,
    }
    value.update(fields)
    value["semantic_evidence_limit"] = "Authored design-reference state only; no DOM, provider or permission enforcement"
    NODES.append(value)
    return symbol


def edge(source, target, control, trigger="On click", action="Change to", **fields):
    value = {"from": source, "to": target, "control_symbol": control,
             "trigger": trigger, "action": action, "animation": "Instant",
             "owned_control_id": None, "actual_destination_id": None,
             "trigger_scope": "Only this owned case composition; key triggers are simulations, never DOM-focus proof"}
    value.update(fields)
    EDGES.append(value)


def prefix(case, family, stream):
    return f"{case}/{family}/{stream}"


def entry(case, family, stream, target):
    ENTRIES.append({"case_id": case, "family": family, "entry_active": stream, "node": target,
                    "kind": "Explicit private inspection entry, not a product action", "actual_flow_id": None})


# The qualified parent-variant mechanism is proposed across all four streams.
# Separate case compositions prevent one case's synthetic outcomes from silently
# changing another case's capability/recovery fixtures.
for case in ["B01-P09", "B01-P10"]:
    for item in CORE["nodes"]:
        symbol = case + "/" + item["symbol"]
        node(symbol, case, item["symbol"].split("/")[0], item["active"], "OPEN", item["pending"],
             source_candidate_ids=item["source_candidate_ids"],
             outcome_fixture="apply_success_only", panel="OPEN",
             preserved_context=["route", "query", "open panel", "recovery message independent of mode"],
             form_submit="Annotated native form Enter contract only; no global Enter trigger")
    for item in CORE["edges"]:
        edge(case + "/" + item["from"], case + "/" + item["to"], item["control"], action=item["action"],
             expected_active=item.get("expected_active"), expected_pending=item.get("expected_pending"),
             scroll_policy="Matching private scroll-body names and dimensions; observe actual nonzero anchor retention before credit")
    for family in TEMPLATES:
        for stream in STREAMS:
            entry(case, family, stream, f"{case}/{family}/{stream}/{stream}/OPEN")
    if case == "B01-P10":
        for item in CORE["nodes"]:
            symbol = case + "/" + item["symbol"]
            for control in ["inspection_focus_only", "inspection_tab_only", "inspection_blur_only", "inspection_elapsed_time"]:
                edge(symbol, symbol, control, action="No transition", expected_active=item["active"], expected_pending=item["pending"], annotation="Negative authored fixture: no Apply. Real focus/blur/time enforcement remains runtime evidence")


# Per-case navigation fixtures. No uncommitted pending-choice lifetime across a
# new route is invented: P04 starts at the declared diagonal pair A/A.
for stream in STREAMS:
    for case in ["B01-P01", "B01-P04", "B01-P05", "B01-P19"]:
        p = prefix(case, "navigation", stream)
        closed = node(p + "/CLOSED", case, "navigation", stream, "CLOSED", menu_visible=False, book_visible=True)
        opened = node(p + "/OPEN", case, "navigation", stream, "OPEN", menu_visible=True, book_visible=True)
        edge(closed, opened, "menu", focus_annotation="Enter declared disclosure sequence")
        edge(opened, closed, "close", focus_annotation="Return to original menu invoker")
        edge(opened, closed, "host", trigger="Key/Gamepad Esc", focus_annotation="Simulated return to invoker")
        entry(case, "navigation", stream, closed)
        if case == "B01-P04":
            for label, route, path in [("Services", "ROUTE-SERVICES", "/services"), ("Evidence", "ROUTE-WORK", "/work"), ("About", "ROUTE-ABOUT", "/about"), ("Contact", "ROUTE-CONTACT", "/contact")]:
                boundary = node(p + "/B02-" + route, case, "navigation", stream, "BOUNDARY", boundary_batch="B02", route_id=route, canonical_path=path, production_route_active=False)
                edge(opened, boundary, "destination/" + label, action="Navigate to", focus_annotation="Destination heading; boundary fixture only")
        if case == "B01-P05":
            book = node(p + "/B06-BOOK", case, "navigation", stream, "BOUNDARY", boundary_batch="B06", route_id="ROUTE-BOOK", canonical_path="/book", real_booking=False)
            for origin in [closed, opened]:
                edge(origin, book, "book", action="Navigate to")
        if case == "B01-P19":
            absent = node(p + "/OPEN-ABSENT-INVOKER", case, "navigation", stream, "OPEN", invoker_present=False)
            fallback = node(p + "/CLOSED-FALLBACK-FOCUS", case, "navigation", stream, "CLOSED", focus_annotation="Current shell heading or first appropriate visible control; not body/hidden content")
            edge(absent, fallback, "close")
            edge(absent, fallback, "host", trigger="Key/Gamepad Esc")
            entry(case, "navigation", stream, absent)
    p = prefix("B01-P02", "navigation", stream)
    order = ["Menu", "Services", "Evidence", "About", "Contact", "Book", "Close", "Next visible shell control"]
    chain = [node(p + "/FOCUS-" + str(i), "B01-P02", "navigation", stream, "FOCUS", focus_target=label, menu_visible=i not in [0, 7], focus_kind="Visibly simulated, not actual native Tab/AT") for i, label in enumerate(order)]
    closed_book = node(p + "/CLOSED-BOOK-FOCUS", "B01-P02", "navigation", stream, "FOCUS", focus_target="Book", menu_visible=False)
    edge(chain[0], closed_book, "next_simulated_focus", trigger="Key/Gamepad Tab", annotation="Tab alone does not open the menu")
    edge(closed_book, chain[-1], "next_simulated_focus", trigger="Key/Gamepad Tab")
    for left, right in zip(chain, chain[1:]):
        if left == chain[0]:
            continue
        edge(left, right, "next_simulated_focus", trigger="Key/Gamepad Tab")
        edge(left, right, "inspection_next_focus")
    edge(chain[0], chain[1], "menu_activation", trigger="Key/Gamepad Enter")
    edge(chain[0], chain[1], "menu_activation", trigger="Key/Gamepad Space")
    edge(chain[6], chain[0], "close_activation", trigger="Key/Gamepad Enter")
    edge(chain[6], chain[0], "close_activation", trigger="Key/Gamepad Space")
    for focused in chain[1:7]:
        edge(focused, chain[0], "host", trigger="Key/Gamepad Esc", focus_annotation="Menu invoker, simulated")
    entry("B01-P02", "navigation", stream, chain[0])
    p = prefix("B01-P03", "navigation", stream)
    idle = node(p + "/BASE", "B01-P03", "navigation", stream, "BASE", press_completed=False)
    cancelled = node(p + "/CANCELLED-PRESS", "B01-P03", "navigation", stream, "BASE", press_completed=False, navigated=False)
    completed = node(p + "/OPEN-AFTER-COMPLETED-ACTIVATION", "B01-P03", "navigation", stream, "OPEN", press_completed=True, menu_visible=True)
    edge(idle, cancelled, "inspection_cancelled_press", action="Change to", annotation="Authored cancel-before-pointer-up fixture, not proof of real pointer cancellation")
    edge(idle, completed, "menu", annotation="Click/tap completion contrast; cancellation enforcement remains runtime evidence")
    edge(cancelled, completed, "menu")
    edge(completed, idle, "close")
    entry("B01-P03", "navigation", stream, idle)


# Explicit modal reference, deterministic query fixtures and static recovery.
for stream in STREAMS:
    for case in ["B01-P06", "B01-P07", "B01-P08", "B01-P19"]:
        p = prefix(case, "directory", stream)
        closed = node(p + "/CLOSED", case, "directory", stream, "CLOSED", modal_open=False, query="")
        opened = node(p + "/OPEN", case, "directory", stream, "OPEN", modal_open=True, background_actions_wired=False, query="")
        edge(closed, opened, "open_directory")
        edge(opened, closed, "close", focus_annotation="Original directory invoker")
        edge(opened, closed, "host", trigger="Key/Gamepad Esc")
        entry(case, "directory", stream, closed)
        if case == "B01-P06":
            filled = node(p + "/PRESET-QUERY", case, "directory", stream, "OPEN", modal_open=True, query="design", background_actions_wired=False, input_label="Search directory", search_backend=False)
            browse = node(p + "/BROWSE", case, "directory", stream, "EMPTY-QUERY", modal_open=True, query="", background_actions_wired=False, static_directory_available=True)
            edge(opened, filled, "inspection_preset/design")
            edge(filled, browse, "clear")
            edge(opened, browse, "browse")
            for source in [filled, browse]:
                edge(source, closed, "close", focus_annotation="Original directory invoker")
                edge(source, closed, "host", trigger="Key/Gamepad Esc")
        if case == "B01-P07":
            stages = {}
            for stage, query in [("EMPTY-QUERY", ""), ("QUERY-DESIGN", "design"), ("LOADING", "design"), ("RESULTS", "design"), ("QUERY-UNMATCHED", "unmatched example"), ("NO-RESULTS", "unmatched example")]:
                stages[stage] = node(p + "/" + stage, case, "directory", stream, stage, modal_open=True, query=query, background_actions_wired=False, search_backend=False)
                edge(stages[stage], closed, "close")
                edge(stages[stage], closed, "host", trigger="Key/Gamepad Esc")
            edge(opened, stages["QUERY-DESIGN"], "inspection_preset/design", annotation="Preset supplied by source; no free-text query processing")
            edge(stages["QUERY-DESIGN"], stages["LOADING"], "search")
            edge(stages["LOADING"], stages["RESULTS"], "inspection_complete_query_fixture", annotation="Explicit synthetic outcome control outside product action area")
            edge(stages["RESULTS"], stages["EMPTY-QUERY"], "clear")
            edge(opened, stages["QUERY-UNMATCHED"], "inspection_preset/unmatched_example")
            edge(stages["QUERY-UNMATCHED"], stages["NO-RESULTS"], "search")
            edge(stages["NO-RESULTS"], stages["EMPTY-QUERY"], "clear")
            for source in [stages["EMPTY-QUERY"], stages["RESULTS"], stages["NO-RESULTS"]]:
                edge(source, stages["QUERY-DESIGN"], "inspection_preset/design")
                edge(source, stages["QUERY-UNMATCHED"], "inspection_preset/unmatched_example")
            result = node(p + "/B02-CLEAN-SERVICES", case, "directory", stream, "BOUNDARY", canonical_path="/services", query_in_url=False, boundary_batch="B02")
            edge(stages["RESULTS"], result, "result/Services", action="Navigate to")
        if case == "B01-P08":
            static = node(p + "/STATIC-DIRECTORY", case, "directory", stream, "STATIC-DIRECTORY", source_release="Explicit synthetic eligible active-release example, not live publication", derived_index=False)
            for stage in ["DERIVED-INDEX-UNAVAILABLE", "OFFLINE", "STALE", "ERROR"]:
                failure = node(p + "/" + stage, case, "directory", stream, stage, query="design", result_currentness_confirmed=False, stale_candidate_activated=False, modal_open=True, background_actions_wired=False)
                edge(failure, static, "browse_static_directory")
                edge(failure, closed, "close")
                edge(failure, closed, "host", trigger="Key/Gamepad Esc")
                entry(case, "directory", stream, failure)
            edge(static, closed, "close")
            edge(static, closed, "host", trigger="Key/Gamepad Esc")
        if case == "B01-P19":
            absent = node(p + "/OPEN-ABSENT-INVOKER", case, "directory", stream, "OPEN", modal_open=True, invoker_present=False, background_actions_wired=False)
            fallback = node(p + "/CLOSED-FALLBACK-FOCUS", case, "directory", stream, "CLOSED", focus_annotation="Current shell heading or first appropriate visible control")
            edge(absent, fallback, "close")
            edge(absent, fallback, "host", trigger="Key/Gamepad Esc")
            entry(case, "directory", stream, absent)


# The reviewed refusal chronology is outside the World. A previously applied
# preference is not a claim that an unavailable WebGL renderer is running.
for item in REFUSALS["frames"]:
    c = item["case"]
    family = "navigation" if c["template_id"] == TEMPLATES["navigation"] else "directory"
    active, pending = c["stream_id"], c["pending_stream_id"]
    p = prefix("B01-P11", family, active)
    before = node(p + "/GATE-ESTABLISHED", "B01-P11", family, active, "GATE-ESTABLISHED", pending, eligibility="3D currently unavailable; pending choice predates gate", chronology=c["chronology"], source_candidate_ids=[item["source_id"]], live_renderer_claim=False)
    refused = node(p + "/REFUSED", "B01-P11", family, active, "REFUSED", pending, refusal_notice=c["notice"], chronology=c["chronology"], source_candidate_ids=SOURCE["expected_host_state_bindings"]["ceiling_refusal"][c["template_id"]][active], silent_substitution=False, live_renderer_claim=False)
    semantic_pending = node(p + "/SEMANTIC-PENDING", "B01-P11", family, active, "REFUSED", "S-SEMANTIC", eligibility="Only Quick Access admitted in this fixture", live_renderer_claim=False)
    semantic = node(p + "/SEMANTIC-APPLIED", "B01-P11", family, "S-SEMANTIC", "OPEN", "S-SEMANTIC", eligibility="3D remains unavailable", live_renderer_claim=False)
    edge(before, refused, "apply")
    edge(refused, semantic_pending, "pending_choice/S-SEMANTIC")
    edge(semantic_pending, semantic, "apply")
    edge(semantic, semantic, "apply_current", action="No transition")
    entry("B01-P11", family, active, before)


# Off-diagonal Apply failure is separate from current-choice no-op. Preference
# failure follows a confirmed mode application, never an unconfirmed Apply.
for case in ["B01-P12", "B01-P13"]:
    for family in TEMPLATES:
        for active in STREAMS:
            for pending in STREAMS:
                if active == pending:
                    continue
                p = prefix(case, family, active) + "/" + pending
                ready = node(p + "/READY", case, family, active, "OPEN", pending, outcome_fixture="apply_failure" if case == "B01-P12" else "applied_but_preference_unsaved")
                if case == "B01-P12":
                    result = node(p + "/APPLY-FAILED", case, family, active, "APPLY-FAILED", pending, copy="The selected view was not applied. Your current view and context are unchanged.", renderer_outcome="Explicit synthetic failure; no generic search-error substitute")
                    edge(ready, result, "apply")
                    edge(result, ready, "try_again", annotation="Explicit same mode-change fixture; no automatic successful outcome")
                else:
                    result = node(p + "/APPLIED-NOT-SAVED", case, family, pending, "PREFERENCE-WRITE-FAILED", pending, preference_saved=False, copy="This view is active for this visit. Saving your preference is not confirmed.")
                    edge(ready, result, "apply")
                    continued = node(p + "/CONTINUE-NOT-SAVED", case, family, pending, "OPEN", pending, preference_saved=False, book_and_content_available=True)
                    edge(result, continued, "continue_browsing")
                    book = node(p + "/B06-BOOK", case, family, pending, "BOUNDARY", route_id="ROUTE-BOOK", canonical_path="/book", boundary_batch="B06", real_booking=False, preference_saved=False)
                    content = node(p + "/B02-SERVICES", case, family, pending, "BOUNDARY", route_id="ROUTE-SERVICES", canonical_path="/services", boundary_batch="B02", production_route_active=False, preference_saved=False)
                    for origin in [result, continued]:
                        edge(origin, book, "book", action="Navigate to")
                        edge(origin, content, "services", action="Navigate to")
                entry(case, family, active, ready)


# Recovery fixtures preserve truth. Checking pending/unknown never creates a new
# request, and an explicitly terminal generation has no edge back to active.
recovery_classes = {"B01-P14": ["LOADING", "PENDING", "UNAVAILABLE", "OFFLINE", "ERROR"], "B01-P15": ["STALE", "CONFLICT"], "B01-P16": ["ASSET-FAILURE", "CHECKSUM-MISMATCH"], "B01-P22": ["STATUS-UPDATE", "DELIBERATE-ERROR-SUMMARY"]}
for case, classes in recovery_classes.items():
    for active in STREAMS:
        p = prefix(case, "recovery_host", active)
        public = node(p + "/PUBLIC-RECOVERY", case, "recovery_host", active, "BOUNDARY", public_only=True, real_request=False)
        for stage in classes:
            source = node(p + "/" + stage, case, "recovery_host", active, stage, confirmed_success=False, secret_or_provider_details=False,
                          focus_annotation="Retain existing focus" if stage == "STATUS-UPDATE" else "Deliberate error summary only when appropriate; never infer focus from a status change")
            entry(case, "recovery_host", active, source)
            if stage in ["PENDING", "STALE", "CONFLICT"]:
                checked = node(p + "/" + stage + "-CHECKED", case, "recovery_host", active, stage, check_same_intent=True, dispatched_new_intent=False, confirmed_success=False)
                edge(source, checked, "check_current_status")
                edge(checked, checked, "check_current_status", action="No transition", annotation="Same unresolved fixture, not a fresh dispatch")
                edge(checked, public, "public_recovery", action="Navigate to")
                if stage in ["STALE", "CONFLICT"]:
                    reconciled = node(p + "/" + stage + "-CURRENT-SNAPSHOT", case, "recovery_host", active, stage, fresh_synthetic_snapshot=True, check_same_intent=True, dispatched_new_intent=False, confirmed_success=False, context_retained=True)
                    edge(checked, reconciled, "inspection_current_snapshot", annotation="Explicit current-authority fixture; never manufacture a successful operation")
                    edge(reconciled, public, "public_recovery", action="Navigate to")
            elif stage in ["ASSET-FAILURE", "CHECKSUM-MISMATCH"]:
                semantic = node(p + "/" + stage + "-SEMANTIC-PENDING", case, "recovery_host", active, stage, "S-SEMANTIC", eligible_canonical_content_preserved=True)
                applied = node(p + "/" + stage + "-SEMANTIC-APPLIED", case, "recovery_host", "S-SEMANTIC", stage, "S-SEMANTIC", eligible_canonical_content_preserved=True, failed_candidate_active=False)
                edge(source, semantic, "choose_quick_access")
                edge(semantic, applied, "apply")
                edge(source, public, "canonical_page", action="Navigate to", annotation="Approved eligible canonical boundary only; no silent stream substitution")
            else:
                edge(source, public, "public_recovery", action="Navigate to")


# Timing is a reference-stage model, not a real clock or an absolute session cap.
for active in STREAMS:
    p = prefix("B01-P17", "recovery_host", active)
    admitted = datetime(2026, 1, 1, 12, 0, tzinfo=timezone.utc)
    deadline = admitted + timedelta(minutes=30)
    previous_applied = None
    for opportunity in range(1, 11):
        q = p + f"/OPPORTUNITY-{opportunity:02d}"
        common = {"clock_kind": "Labelled synthetic server-authority example; no real clock", "confirmed_deadline_fixture": deadline.isoformat(), "opportunity": opportunity, "more_time_available": True, "ordinary_end_available": True, "book_available": True, "notice_from_start": True}
        current = node(q + "/ACTIVE", "B01-P17", "recovery_host", active, "ACTIVE", **common)
        warning = node(q + "/WARNING", "B01-P17", "recovery_host", active, "WARNING", **common, warning_time_fixture=(deadline - timedelta(seconds=20)).isoformat(), usable_warning_requirement_seconds=20, measured_usable_interval=False)
        pending = node(q + "/PENDING", "B01-P17", "recovery_host", active, "PENDING", **common, immutable_intent_fixture="renewal-example-" + str(opportunity), new_deadline_confirmed=False, duplicate_dispatch_enabled=False)
        request_admission = deadline - timedelta(seconds=15)
        next_deadline = request_admission + timedelta(minutes=30)
        applied = node(q + "/APPLIED", "B01-P17", "recovery_host", active, "APPLIED", original_admission_fixture=request_admission.isoformat(), original_granted_deadline_fixture=next_deadline.isoformat(), current_permitted_snapshot_fixture=next_deadline.isoformat(), immutable_intent_fixture="renewal-example-" + str(opportunity), ordinary_end_available=True, more_time_available=True, notice_from_start=True, book_available=True, no_real_permission=True)
        edge(current, warning, "inspection_show_warning", annotation="Synthetic stage control, not timeout authority")
        edge(current, pending, "more_time")
        edge(warning, pending, "more_time")
        edge(pending, applied, "inspection_acknowledged_result", annotation="Synthetic outcome only, not real polling/renewal")
        edge(pending, pending, "check_current_status", action="No transition", same_immutable_intent=True, new_dispatch=False)
        if previous_applied:
            edge(previous_applied, current, "inspection_next_opportunity", annotation="Next finite demonstration stage, no runtime maximum")
        else:
            entry("B01-P17", "recovery_host", active, current)
        previous_applied, deadline = applied, next_deadline
    further = node(p + "/FURTHER-REQUEST-PENDING", "B01-P17", "recovery_host", active, "PENDING", confirmed_deadline_fixture=deadline.isoformat(), new_deadline_confirmed=False, more_time_policy_capped=False, ordinary_end_available=True, no_real_permission=True)
    edge(previous_applied, further, "more_time", annotation="Request still available beyond ten demonstrated grants; outcome remains pending, no absolute limit")
    edge(further, further, "check_current_status", action="No transition", same_immutable_intent=True, new_dispatch=False)
    for stage in ["STALE-TICKET", "REFUSED", "UNKNOWN-DEADLINE", "BACKGROUND-RETURN", "NEWER-ACTIVITY-SNAPSHOT"]:
        example = node(p + "/BRANCH-" + stage, ["B01-P17", "B01-P22"], "recovery_host", active, stage, guessed_deadline=False, background_return_is_activity=False, current_snapshot_required=True, ordinary_end_available=True,
                       notice="Known prior expiry is historical, not a current grant" if stage == "UNKNOWN-DEADLINE" else "Reference fixture; use only currently permitted authority",
                       original_receipt_deadline_fixture=deadline.isoformat() if stage == "NEWER-ACTIVITY-SNAPSHOT" else None,
                       newer_current_snapshot_fixture=(deadline + timedelta(seconds=5)).isoformat() if stage == "NEWER-ACTIVITY-SNAPSHOT" else None)
        entry("B01-P17", "recovery_host", active, example)
        checked = node(p + "/BRANCH-" + stage + "-CHECKED", ["B01-P17", "B01-P22"], "recovery_host", active, stage, current_snapshot_required=True, guessed_deadline=False, new_deadline_confirmed=False, new_dispatch=False, background_return_is_activity=False, ordinary_end_available=True)
        edge(example, checked, "check_current_status", annotation="Same renewal intent/current permitted status, not a new grant")
        edge(checked, checked, "check_current_status", action="No transition", new_dispatch=False)
    terminal = node(prefix("B01-P18", "recovery_host", active) + "/TERMINAL", "B01-P18", "recovery_host", active, "TERMINAL", generation="retired-example", private_access=False, send_available=False, extend_available=False)
    public = node(prefix("B01-P18", "recovery_host", active) + "/PUBLIC", "B01-P18", "recovery_host", active, "BOUNDARY", public_only=True)
    new_session = node(prefix("B01-P18", "recovery_host", active) + "/B05-NEW-SESSION-BOUNDARY", "B01-P18", "recovery_host", active, "BOUNDARY", boundary_batch="B05", new_permission_granted=False, restored_transcript=False)
    late = node(prefix("B01-P18", "recovery_host", active) + "/LATE-REPLY-AFTER-TERMINAL", "B01-P18", "recovery_host", active, "TERMINAL", generation="retired-example", private_access=False, revived=False)
    book = node(prefix("B01-P18", "recovery_host", active) + "/B06-BOOK", "B01-P18", "recovery_host", active, "BOUNDARY", route_id="ROUTE-BOOK", canonical_path="/book", boundary_batch="B06", real_booking=False)
    for source in [n["symbol"] for n in NODES if n["symbol"].startswith(p + "/")]:
        edge(source, terminal, "ordinary_end", annotation="End while pending is allowed; visitor End does not end staff authentication")
        edge(source, book, "book", action="Navigate to")
        edge(source, terminal, "inspection_authoritative_expiry", annotation="Explicit synthetic expiry observation; no client clock or real timeout")
    edge(terminal, public, "public_website", action="Navigate to")
    edge(terminal, new_session, "start_new_session_boundary", action="Navigate to")
    edge(terminal, book, "book", action="Navigate to")
    edge(terminal, late, "inspection_late_reply", annotation="Late provider result cannot revive retired generation")
    edge(late, public, "public_website", action="Navigate to")
    edge(late, book, "book", action="Navigate to")
    entry("B01-P18", "recovery_host", active, terminal)
    entry("B01-P18", "recovery_host", active, late)


# These cases retain all three templates and streams. Modes/profile values are
# bound by the separate allocation draft, never discharged by a generic example.
for case in ["B01-P20", "B01-P21"]:
    for family in TEMPLATES:
        for stream in STREAMS:
            p = prefix(case, family, stream)
            initial = node(p + "/ENTRY", case, family, stream, "OPEN", motion="Instant, stable" if case == "B01-P20" else "Inherited candidate profile", profiles_required=True, input_modes="Pointer/touch activation and separately simulated keyboard/AT annotations")
            result = node(p + "/RESULT", case, family, stream, "OPEN", motion="Instant", content_and_action_parity=True, measured_device_or_AT=False)
            action_control = {"navigation": "menu", "directory": "open_directory", "recovery_host": "check_current_status"}[family]
            next(x for x in NODES if x["symbol"] == initial)["panel_open"] = False if family != "recovery_host" else None
            next(x for x in NODES if x["symbol"] == result)["panel_open"] = True if family != "recovery_host" else None
            edge(initial, result, action_control, annotation="Concrete disclosure or same-intent status action; no generic success/focus claim")
            if family != "recovery_host":
                edge(result, initial, "close")
                edge(result, initial, "host", trigger="Key/Gamepad Esc")
            entry(case, family, stream, initial)


by_symbol = {n["symbol"]: n for n in NODES}
for n in NODES:
    parts = n["symbol"].split("/")
    n["private_component_set_symbol"] = (
        "TIMING/" + "/".join(parts[1:3]) if parts[0] in ["B01-P17", "B01-P18"] else
        "/".join(parts[:2]) if parts[0] in ["B01-P09", "B01-P10"] else
        "/".join(parts[:4]) if parts[0] in ["B01-P12", "B01-P13"] else
        "/".join(parts[:3])
    )
    n["native_node_role"] = "Standalone fixed boundary frame" if n["stage"] == "BOUNDARY" else "Owned parent variant"
for transition in EDGES:
    source, target = by_symbol[transition["from"]], by_symbol[transition["to"]]
    transition["source_tuple"] = {k: source[k] for k in ["template", "active", "pending", "stage", "context"]}
    transition["destination_tuple"] = {k: target[k] for k in ["template", "active", "pending", "stage", "context"]}
    if transition["action"] == "Change to":
        assert source["private_component_set_symbol"] == target["private_component_set_symbol"], "Change-to crosses component sets"
    transition["state_reset_policy"] = (
        "Boundary frame has no surviving interactive instance and fixed authored defaults; fresh Navigate-to qualification required before wiring"
        if transition["action"] == "Navigate to" else
        "No transition; retain the exact current parent variant and nonzero scroll anchor"
        if transition["action"] == "No transition" else
        "One explicit target parent variant in the same owned component set; no reused nested selector state or automatic reset. Match private scroll-body names/dimensions and qualify retention."
    )


graph = {
    "product": "Hengshi Design v1", "status": "DOING", "date": "2026-10-14",
    "scope": "Complete proposed case-level mechanical fixture graph for B01-P01-P22; not an accepted executable plan or external-write release",
    "case_policy": "Each case has an isolated synthetic composition and exact entry. Cross-case private fixture controls are not production UI; untested combinations are not claimed.",
    "nodes": NODES, "edges": EDGES, "entries": ENTRIES,
    "source_case_requirements": SOURCE["cases"],
    "mechanism_evidence": "native-qualification/execution/review-native-successor/independent-review-native-successor-v1.json under the prior research base; six-case bounded parent-variant PASS only",
    "native_action_limits": {"observed": ["On click -> Change to -> Instant", "Key/Gamepad Esc -> Change to -> Instant", "current-choice no-op"], "requires_fresh_qualification": ["Navigate to boundary/entry frames and reset options", "Tab/Enter/Space key simulation", "state/scroll retention on the enlarged LOW/SEMANTIC/three-host graph"], "not_used": ["Back", "paid variables", "conditionals", "multiple-action chains", "native overlay swap history", "After delay as a server clock"]},
    "overlay_model": "Owned complete-host variants depict the D092 modal. Private background actions remain unwired while modal is open. No real DOM inertness, focus trap or AT semantics claim.",
    "source_preservation": "Original references, masters, protected app/Atlanta asset and the successful isolated trial remain unchanged. Actual new IDs are discovered only after authorized guarded copying.",
    "temporal_limits": "Ten authored grant examples plus a further-request-pending stage are a finite demonstration, not an absolute visitor access limit. Real20-second operability, ten opportunities and deadline/race/privacy enforcement remain runtime evidence.",
    "external_write_released": False, "runtime_proof": False, "independent_review": None,
    "remaining": ["Independent whole proposed graph review", "BNP01 public evidence composition and effective-coordinate associations", "BNP02 exact functional primitive anatomy/proxy mapping", "BNP04 nine-profile exact qualitative allocation", "BNP05 staged fresh source/owned-copy/discovery safeguards", "Fresh native action qualifications before wiring", "Reviewed complete executable plan and explicit applicable external-write release", "Actual complete cases/profiles, source preservation/restore/_EXIT and founder B01/Phase1 acceptance"]}
OUT.mkdir(exist_ok=True)
(OUT / "full-case-graph-proposal-v1.json").write_text(json.dumps(graph, indent=2) + "\n", encoding="utf8")

keys = {n["symbol"] for n in NODES}
assert len(keys) == len(NODES), "Duplicate private node symbol"
assert all(e["from"] in keys and e["to"] in keys for e in EDGES), "Unbound endpoint"
assert {f"B01-P{i:02}" for i in range(1, 23)} == {c for n in NODES for c in n["case_ids"]}, "Case coverage mismatch"
assert all(e["action"] in {"Change to", "Navigate to", "No transition"} for e in EDGES)
assert all(e["owned_control_id"] is None and e["actual_destination_id"] is None for e in EDGES)
for n in NODES:
    if n["stage"] == "TERMINAL":
        assert all(next(x for x in NODES if x["symbol"] == e["to"])["stage"] in {"BOUNDARY", "TERMINAL"} for e in EDGES if e["from"] == n["symbol"]), "Retired-generation resurrection edge"
print(json.dumps({"nodes": len(NODES), "edges": len(EDGES), "entries": len(ENTRIES), "cases": 22, "checks": "Referential/case/terminal artifact integrity only; no runtime or release proof"}))

"""Read-only D-062 source/record verification; never creates approval evidence."""
import csv
import hashlib
import json
import re
from pathlib import Path

DESIGN = "docs/phase-1-ui-reference-design/"
TARGETS = {
    "foundation-route-coverage.csv": ("route_id", "template_id state_profile viewport_profile mode_profile semantic_quick_access immersive_stream_representation content_or_policy_gate activation_status time_limit_branch".split()),
    "foundation-flow-coverage.csv": ("coverage_id", "state_profile viewport_profile mode_profile gate time_limit_branch".split()),
    "reference-template-inventory.csv": ("template_id", "surface_kind state_profile viewport_profile mode_profile time_limit_branch".split()),
    "component-primitives.csv": ("primitive_id", "primitive_category interaction_class stream_presence".split()),
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def closed(obj, keys):
    require(isinstance(obj, dict) and set(obj) == set(keys), "Closed schema mismatch")


def text(value):
    require(isinstance(value, str) and bool(value.strip()), "Nonempty text required")
    return value


def unique_pairs(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, "Duplicate JSON property")
        result[key] = value
    return result


def load_json(raw):
    return json.loads(raw, object_pairs_hook=unique_pairs)


def source_path(root, relative):
    text(relative)
    require(not re.search(r"[:\\]", relative) and not relative.startswith("/")
            and all(p not in ("", ".", "..") for p in relative.split("/")), "Unsafe source path")
    root = Path(root).resolve()
    candidate = root
    for part in relative.split("/"):
        candidate = candidate / part
        require(not candidate.is_symlink() and not candidate.is_junction(), "Linked source path")
    require(candidate.is_file() and candidate.resolve().is_relative_to(root), "Missing or escaped source")
    return candidate


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def normalize(value):
    return value.replace("\r\n", "\n").replace("\r", "\n")


def csv_rows(path):
    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        require(reader.fieldnames and len(set(reader.fieldnames)) == len(reader.fieldnames), "Duplicate CSV fields")
        rows = list(reader)
        require(all(None not in row and all(v is not None for v in row.values()) for row in rows), "Malformed CSV row")
        return rows


def selected_fact(root, source, cache=None):
    closed(source, ("path", "selector", "quoted_fact", "supports"))
    text(source["supports"])
    quote = normalize(text(source["quoted_fact"]))
    path = source_path(root, source["path"])
    selector = source["selector"]
    require(isinstance(selector, dict), "Missing source selector")
    kind = selector.get("kind")
    resolved_row = None
    cache = {} if cache is None else cache

    def read_text():
        key = (str(path), "text")
        if key not in cache:
            cache[key] = path.read_text(encoding="utf-8-sig")
        return cache[key]

    if kind == "csv_record":
        closed(selector, ("kind", "key_field", "key_value", "field"))
        csv_key = (str(path), "csv")
        if csv_key not in cache:
            cache[csv_key] = csv_rows(path)
        matches = [row for row in cache[csv_key] if row.get(selector["key_field"]) == selector["key_value"]]
        require(len(matches) == 1 and selector["field"] in matches[0], "Ambiguous CSV source")
        resolved_row = matches[0]
        content = matches[0][selector["field"]]
    elif kind == "json_pointer":
        closed(selector, ("kind", "pointer"))
        pointer = selector["pointer"]
        require(isinstance(pointer, str) and (pointer == "" or pointer.startswith("/")), "Invalid JSON pointer")
        json_key = (str(path), "json")
        if json_key not in cache:
            cache[json_key] = load_json(read_text())
        value = cache[json_key]
        for token in pointer.split("/")[1:] if pointer else []:
            require(not re.search(r"~(?![01])", token), "Invalid pointer escape")
            token = token.replace("~1", "/").replace("~0", "~")
            if isinstance(value, list):
                require(re.fullmatch(r"0|[1-9][0-9]*", token) and int(token) < len(value), "Invalid pointer index")
                value = value[int(token)]
            else:
                require(isinstance(value, dict) and token in value, "Missing pointer member")
                value = value[token]
        content = value if isinstance(value, str) else json.dumps(value, ensure_ascii=False, separators=(",", ":"))
    elif kind == "markdown_table_id":
        closed(selector, ("kind", "id"))
        matches = []
        for line in read_text().splitlines():
            if line.lstrip().startswith("|"):
                first = line.strip().split("|")[1].strip()
                if first == selector["id"]:
                    matches.append(line)
        require(len(matches) == 1, "Ambiguous Markdown table source")
        content = matches[0]
    elif kind == "markdown_section":
        closed(selector, ("kind", "heading_path"))
        require(isinstance(selector["heading_path"], list) and selector["heading_path"], "Missing heading path")
        stack, matches, current, active = [], [], [], False
        fenced = False
        for line in read_text().splitlines():
            if re.match(r"^\s{0,3}(```|~~~)", line):
                fenced = not fenced
            heading = None if fenced else re.match(r"^(#{1,6})\s+(.+?)(?:\s+#+)?\s*$", line)
            if heading:
                if active:
                    matches.append("\n".join(current)); current = []; active = False
                level = len(heading[1])
                stack = [(n, h) for n, h in stack if n < level] + [(level, heading[2])]
                active = [h for _, h in stack] == selector["heading_path"]
                if active:
                    current.append(line)
            elif active:
                current.append(line)
        if active:
            matches.append("\n".join(current))
        require(len(matches) == 1, "Ambiguous Markdown heading source")
        content = matches[0]
    else:
        raise ValueError("Unknown source selector")
    require(quote in normalize(content), "Quoted fact not in selected source")
    return resolved_row


def timing(record):
    criterion = record["timing_criterion"]
    closed(criterion, ("process_source", "applicability", "selected_branch", "obligations", "implementation_truth"))
    require(criterion["process_source"] in record["sources"], "Process source must resolve a recorded source")
    require(criterion["implementation_truth"] == "future_qa_required", "Definition cannot certify runtime")
    branch = record["declared_value"]
    require(criterion["selected_branch"] == branch, "Branch criterion disagrees with cell")
    applicability = criterion["applicability"]
    obligations = criterion["obligations"]
    if applicability == "no_user_limit_declared":
        require(branch == "TL-NOT-APPLICABLE" and obligations == {}, "No-limit criterion mismatch")
        return
    require(applicability in ("defined_user_limit", "protection_required_if_user_limit_introduced"), "Invalid timing applicability")
    common = {"preserve_permitted_data": True, "preserve_authoritative_state": True,
              "accessible_reauthentication": "required_if_protected_session"}
    if branch == "TL-WARN-EXTEND":
        expected = dict(common, warning_seconds_min=20, extension_factor_min=10)
    elif branch == "TL-REMOVABLE-ADJUSTABLE":
        expected = dict(common, before_start="turn_off_or_adjust", adjustment_range="criterion_supported")
    else:
        raise ValueError("Unsupported protected branch")
    require(obligations == expected and all(type(obligations[k]) is type(v) for k, v in expected.items()), "Timing protection mismatch")


def validate_registry(root, registry):
    closed(registry, ("schema_version", "columns", "source_snapshots", "records"))
    require(type(registry["schema_version"]) is int and registry["schema_version"] == 1, "Unsupported schema")
    expected_columns = {(file, column) for file, (_, columns) in TARGETS.items() for column in columns}
    columns = {}
    for column in registry["columns"]:
        closed(column, ("file", "column", "authority_kind", "criterion_id", "decision_meaning", "guard"))
        key = (column["file"], column["column"])
        require(key not in columns and key in expected_columns, "Unknown or duplicate column authority")
        require(column["authority_kind"] == "DECLARED", "Forbidden derived authority")
        for field in ("criterion_id", "decision_meaning", "guard"):
            text(column[field])
        columns[key] = column
    require(set(columns) == expected_columns, "Missing column authority")
    snapshots = {}
    snapshot_files = []
    for snapshot in registry["source_snapshots"]:
        closed(snapshot, ("path", "raw_sha256"))
        relative, sha = snapshot["path"], snapshot["raw_sha256"]
        require(relative not in snapshots and isinstance(sha, str) and re.fullmatch("[A-F0-9]{64}", sha), "Duplicate or invalid source pin")
        pinned_file = source_path(root, relative)
        require(not any(pinned_file.samefile(prior) for prior in snapshot_files), "Duplicate physical source snapshot")
        require(digest(pinned_file) == sha, "Stale source snapshot")
        snapshot_files.append(pinned_file)
        snapshots[relative] = sha
    expected = {}
    for file, (row_key, fields) in TARGETS.items():
        relative = DESIGN + file
        require(relative in snapshots, "Missing target snapshot")
        for row in csv_rows(source_path(root, relative)):
            identity = text(row[row_key])
            for field in fields:
                key = (file, identity, field)
                require(key not in expected, "Duplicate live row key")
                expected[key] = row[field]
    records = {}
    source_cache = {}
    for record in registry["records"]:
        base = ("file", "row_id", "column", "declared_value", "criterion_id", "sources", "rationale")
        closed(record, base + (("timing_criterion",) if record.get("column") == "time_limit_branch" else ()))
        key = (record["file"], record["row_id"], record["column"])
        require(key not in records and key in expected, "Duplicate or unknown target cell")
        require(record["declared_value"] == expected[key], "Declared cell mismatch")
        require(record["criterion_id"] == columns[(key[0], key[2])]["criterion_id"], "Unresolved criterion")
        text(record["rationale"])
        require(isinstance(record["sources"], list) and record["sources"], "Missing source witnesses")
        independent = False
        for witness in record["sources"]:
            require(witness.get("path") in snapshots, "Unpinned criterion source")
            resolved_row = selected_fact(root, witness, source_cache)
            selector = witness["selector"]
            witness_file = source_path(root, witness["path"])
            target_file = source_path(root, DESIGN + key[0])
            own_cell = witness_file.samefile(target_file) and resolved_row is not None and resolved_row.get(TARGETS[key[0]][0]) == key[1] and selector.get("field") == key[2]
            require(not witness["path"].endswith("column-authority.json"), "Registry cannot witness itself")
            registry_file = Path(root) / DESIGN / "column-authority.json"
            require(not registry_file.exists() or not witness_file.samefile(registry_file), "Registry alias cannot witness itself")
            independent |= not own_cell
        require(independent, "Target cell cannot be sole authority")
        if key[2] == "time_limit_branch":
            timing(record)
        records[key] = record
    require(set(records) == set(expected), "Missing target cell authority")
    for relative, sha in snapshots.items():
        require(digest(source_path(root, relative)) == sha, "Source changed during verification")
    return records


def validate_approval(root, registry_path, decision_id):
    """Require actual-cell acceptance separately from model acceptance D-062."""
    require(re.fullmatch(r"D-[0-9]{3}", decision_id), "Invalid decision ID")
    decisions = source_path(root, "DECISIONS.md").read_text(encoding="utf-8-sig")
    sections = re.findall(r"(?ms)^## " + re.escape(decision_id) + r"(?=[ \t\r\n])[^\n]*\n(.*?)(?=^## D-|\Z)", decisions)
    require(len(sections) == 1, "Missing or duplicate authority decision")
    section = sections[0]
    statuses = re.findall(r"(?m)^\*\*Status:\*\* (\w+)\s*$", section)
    require(len(statuses) == 1 and statuses[0].lower() in ("approved", "accepted"), "Decision not accepted")

    def metadata(name):
        matches = re.findall(r"(?m)^" + re.escape(name) + r":[ \t]+([^\r\n]+)\r?$", section)
        require(len(matches) == 1, "Missing or duplicate approval binding: " + name)
        return matches[0].strip()

    require(metadata("column_authority_registry_path") == registry_path, "Wrong registry approval path")
    registry_file = source_path(root, registry_path)
    registry_hash = digest(registry_file)
    require(metadata("column_authority_registry_sha256") == registry_hash, "Stale registry approval")
    registry = load_json(registry_file.read_text(encoding="utf-8-sig"))
    records = validate_registry(root, registry)
    review_path = metadata("column_authority_review_path")
    require(review_path != registry_path, "Review must be separate evidence")
    review_file = source_path(root, review_path)
    require(metadata("column_authority_review_sha256") == digest(review_file), "Stale review approval")
    review = load_json(review_file.read_text(encoding="utf-8-sig"))
    closed(review, ("schema_version", "registry_path", "registry_sha256", "reviewer_id", "producer_id", "result", "open_critical", "open_high", "open_medium", "source_snapshots", "examined_records"))
    require(type(review["schema_version"]) is int and review["schema_version"] == 1, "Invalid review schema")
    require(review["registry_path"] == registry_path and review["registry_sha256"] == registry_hash, "Review registry binding mismatch")
    require(text(review["reviewer_id"]) != text(review["producer_id"]), "Author cannot review own registry")
    require(review["result"] == "PASS" and all(type(review[k]) is int and review[k] == 0 for k in ("open_critical", "open_high", "open_medium")), "Review findings block acceptance")
    require(review["source_snapshots"] == registry["source_snapshots"], "Review source snapshot mismatch")
    examined = {}
    for record in review["examined_records"]:
        closed(record, ("file", "row_id", "column", "source_criterion_conclusion"))
        key = (record["file"], record["row_id"], record["column"])
        require(key not in examined and key in records, "Invalid or duplicate reviewed key")
        text(record["source_criterion_conclusion"])
        examined[key] = record
    require(set(examined) == set(records), "Review did not examine exact record set")
    return records


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--registry", default=DESIGN + "column-authority.json")
    parser.add_argument("--decision", required=True)
    args = parser.parse_args()
    try:
        verified = validate_approval(args.root, args.registry, args.decision)
    except (ValueError, KeyError, TypeError, OSError) as error:
        parser.exit(1, "FAIL column authority: " + str(error) + "\n")
    print("PASS column authority: " + str(len(verified)) + " source-bound declarations")

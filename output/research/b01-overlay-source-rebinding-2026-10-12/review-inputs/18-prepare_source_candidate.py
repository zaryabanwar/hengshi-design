"""Research-only D-092 witness candidate; never modifies current authority."""
import copy
import csv
import hashlib
import importlib.util
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[3]
folder = Path(__file__).resolve().parent
source = root / "docs/phase-1-ui-reference-design/column-authority.json"
original = json.loads(source.read_text(encoding="utf-8-sig"))
registry = copy.deepcopy(original)
spec = importlib.util.spec_from_file_location("authority", root / "scripts/validation/ui_column_authority.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
changes, process_changes, pins, cache, tables = [], [], [], {}, {}

for index, record in enumerate(registry["records"]):
    for position, witness in enumerate(record["sources"]):
        try:
            module.selected_fact(root, witness, cache)
            continue
        except ValueError as error:
            if str(error) != "Quoted fact not in selected source":
                raise
        selector = witness["selector"]
        if selector["kind"] == "csv_record":
            assert selector["key_value"] in ("PRIM-004", "TPL-DIRECTORY-SEARCH")
            if witness["path"] not in tables:
                with (root / witness["path"]).open(encoding="utf-8-sig", newline="") as handle:
                    tables[witness["path"]] = list(csv.DictReader(handle))
            matches = [r for r in tables[witness["path"]] if r[selector["key_field"]] == selector["key_value"]]
            assert len(matches) == 1
            actual = matches[0][selector["field"]]
        else:
            assert witness["path"] == "docs/phase-1-ux-architecture/FLOWS.md"
            assert selector["heading_path"] == ["Detailed Task Flows", "DF-01 — Search, directory, and immersive HUD"]
            actual = re.search(r"^## DF-01 — Search, directory, and immersive HUD\n.*?(?=^#{1,6} |\Z)",
                               (root / witness["path"]).read_text(encoding="utf-8-sig"), re.M | re.S).group(0).rstrip()
        before = copy.deepcopy(witness)
        witness["quoted_fact"] = actual
        changes.append({"record_index": index, "source_index": position, "before": before, "after": copy.deepcopy(witness)})
        timing = record.get("timing_criterion")
        if timing and timing["process_source"] == before:
            process_changes.append({"record_index": index, "before": copy.deepcopy(timing["process_source"]), "after": copy.deepcopy(witness)})
            timing["process_source"] = copy.deepcopy(witness)

for pin in registry["source_snapshots"]:
    actual = hashlib.sha256((root / pin["path"]).read_bytes()).hexdigest().upper()
    if actual != pin["raw_sha256"]:
        pins.append({"path": pin["path"], "before": pin["raw_sha256"], "after": actual})
        pin["raw_sha256"] = actual

assert len(changes) == 41 and len({c["record_index"] for c in changes}) == 33 and len(pins) == 3
for before, after in zip(original["records"], registry["records"]):
    assert before["declared_value"] == after["declared_value"]
    if "timing_criterion" in before:
        assert {k: v for k, v in before["timing_criterion"].items() if k != "process_source"} == {k: v for k, v in after["timing_criterion"].items() if k != "process_source"}

candidate = folder / "column-authority-candidate-v1.json"
candidate.write_text(json.dumps(registry, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
report = {"product": "Hengshi Design v1", "status": "DOING", "scope": "D-092 quote/snapshot candidate only; canonical registry unchanged; independent review and acceptance held",
          "prior_failures": ["CSV-only candidate failed on ten DF-01 section quotes", "DF-01 repair also requires matching copied timing process_source witnesses"],
          "quote_changes": changes, "copied_process_source_changes": process_changes, "snapshot_changes": pins, "declared_value_changes": 0, "timing_policy_changes": 0,
          "canonical_registry_sha256": hashlib.sha256(source.read_bytes()).hexdigest(), "candidate_sha256": hashlib.sha256(candidate.read_bytes()).hexdigest(), "runtime_proof": False}
print(json.dumps({"quotes": len(changes), "records": 33, "copied_process_sources": len(process_changes), "pins": 3}), flush=True)
try:
    verified = module.validate_registry(root, registry)
    report["artifact_validation"] = {"result": "PASS", "source_bound_records": len(verified)}
except Exception as error:
    report["artifact_validation"] = {"result": "FAIL", "error": str(error)}
    raise
finally:
    (folder / "source-rebinding-diff-v1.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
print(json.dumps(report["artifact_validation"]), flush=True)

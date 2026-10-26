"""Synthetic source/approval tests; no repository authority is generated."""
import copy
import csv
import json
import os
import tempfile
import unittest
from pathlib import Path

from ui_column_authority import DESIGN, TARGETS, digest, load_json, selected_fact, validate_approval, validate_registry


class ColumnAuthorityTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="hsd-column-test-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / DESIGN).mkdir(parents=True)
        self.registry_path = DESIGN + "column-authority.json"
        self.registry = {"schema_version": 1, "columns": [], "source_snapshots": [], "records": []}
        self.put("sources.md", "# Processes\n\n## R001\nR001 approved process, with no user time limit declared.\n")
        witness = {"path": "sources.md", "selector": {"kind": "markdown_section", "heading_path": ["Processes", "R001"]},
                   "quoted_fact": "R001 approved process, with no user time limit declared.", "supports": "R001 process definition"}
        for file, (row_id, columns) in TARGETS.items():
            row = {row_id: "R001"}
            for column in columns:
                row[column] = "TL-NOT-APPLICABLE" if column == "time_limit_branch" else "fixture-" + column
                criterion = file + ":" + column
                self.registry["columns"].append({"file": file, "column": column, "authority_kind": "DECLARED",
                                                  "criterion_id": criterion, "decision_meaning": "Synthetic fixture decision", "guard": "Synthetic source binding"})
                record = {"file": file, "row_id": "R001", "column": column, "declared_value": row[column],
                          "criterion_id": criterion, "sources": [copy.deepcopy(witness)], "rationale": "Synthetic process witness only"}
                if column == "time_limit_branch":
                    record["timing_criterion"] = {"process_source": copy.deepcopy(witness), "applicability": "no_user_limit_declared",
                                                  "selected_branch": row[column], "obligations": {}, "implementation_truth": "future_qa_required"}
                self.registry["records"].append(record)
            with (self.root / DESIGN / file).open("w", encoding="utf-8", newline="") as handle:
                writer = csv.DictWriter(handle, fieldnames=list(row)); writer.writeheader(); writer.writerow(row)
        self.registry["source_snapshots"] = [{"path": path, "raw_sha256": digest(self.root / path)}
                                              for path in [DESIGN + file for file in TARGETS] + ["sources.md"]]
        self.save_approval()

    def put(self, path, value):
        (self.root / path).write_text(value, encoding="utf-8")

    def save_approval(self):
        self.put(self.registry_path, json.dumps(self.registry))
        self.review_path = "review.json"
        self.review = {"schema_version": 1, "registry_path": self.registry_path, "registry_sha256": digest(self.root / self.registry_path),
                       "reviewer_id": "synthetic-reviewer", "producer_id": "synthetic-author", "result": "PASS", "open_critical": 0,
                       "open_high": 0, "open_medium": 0, "source_snapshots": self.registry["source_snapshots"],
                       "examined_records": [{"file": r["file"], "row_id": r["row_id"], "column": r["column"],
                                             "source_criterion_conclusion": "Synthetic record/source examined"} for r in self.registry["records"]]}
        self.save_review()

    def save_review(self):
        self.put(self.review_path, json.dumps(self.review))
        self.put("DECISIONS.md", "## D-999 — Synthetic approval\n\n**Status:** Approved\n"
                 + "column_authority_registry_path: " + self.registry_path + "\n"
                 + "column_authority_registry_sha256: " + digest(self.root / self.registry_path) + "\n"
                 + "column_authority_review_path: " + self.review_path + "\n"
                 + "column_authority_review_sha256: " + digest(self.root / self.review_path) + "\n")

    def test_valid_complete_binding(self):
        self.assertEqual(22, len(validate_approval(self.root, self.registry_path, "D-999")))

    def test_registry_rejections(self):
        mutations = {
            "missing record": lambda r: r["records"].pop(),
            "duplicate record": lambda r: r["records"].append(r["records"][0]),
            "changed cell": lambda r: r["records"][0].update(declared_value="different"),
            "missing column": lambda r: r["columns"].pop(),
            "derived classifier": lambda r: r["columns"][0].update(authority_kind="DERIVED"),
            "missing criterion": lambda r: r["records"][0].update(criterion_id="unknown"),
            "quote wrong section": lambda r: r["records"][0]["sources"][0].update(quoted_fact="unrelated process"),
            "ambiguous heading": lambda r: r["records"][0]["sources"][0]["selector"].update(heading_path=["absent"]),
            "wildcard selector": lambda r: r["records"][0]["sources"][0]["selector"].update(kind="range"),
            "unsafe path": lambda r: r["source_snapshots"][0].update(path="../sources.md"),
            "runtime claim": lambda r: next(x for x in r["records"] if x["column"] == "time_limit_branch")["timing_criterion"].update(implementation_truth="PASS"),
            "unsupported user limit": lambda r: next(x for x in r["records"] if x["column"] == "time_limit_branch")["timing_criterion"].update(applicability="defined_user_limit"),
            "extra duration": lambda r: next(x for x in r["records"] if x["column"] == "time_limit_branch")["timing_criterion"].update(duration=30),
        }
        for name, mutate in mutations.items():
            with self.subTest(name=name):
                registry = copy.deepcopy(self.registry); mutate(registry)
                with self.assertRaises(ValueError):
                    validate_registry(self.root, registry)

    def test_stale_source(self):
        self.put("sources.md", (self.root / "sources.md").read_text() + "\n")
        with self.assertRaisesRegex(ValueError, "Stale source"):
            validate_registry(self.root, self.registry)

    def test_target_cell_alias_cannot_witness_itself(self):
        record = self.registry["records"][0]
        record["sources"] = [{"path": DESIGN + record["file"],
                              "selector": {"kind": "csv_record", "key_field": "state_profile", "key_value": "fixture-state_profile", "field": record["column"]},
                              "quoted_fact": record["declared_value"], "supports": "Alias of target cell"}]
        with self.assertRaisesRegex(ValueError, "sole authority"):
            validate_registry(self.root, self.registry)

    def test_physical_snapshot_alias_rejected(self):
        relative = DESIGN + next(iter(TARGETS))
        if os.name == "nt":
            alias = relative.upper()
        else:
            alias = "alias.csv"
            os.link(self.root / relative, self.root / alias)
        self.registry["source_snapshots"].append({"path": alias, "raw_sha256": digest(self.root / alias)})
        record = self.registry["records"][0]
        record["sources"] = [{"path": alias, "selector": {"kind": "csv_record", "key_field": "route_id", "key_value": "R001", "field": record["column"]},
                              "quoted_fact": record["declared_value"], "supports": "Physical alias of target cell"}]
        with self.assertRaisesRegex(ValueError, "Duplicate physical"):
            validate_registry(self.root, self.registry)

    def test_approval_rejections(self):
        original = (self.root / "DECISIONS.md").read_text()
        for name, changed in [("generic", "## D-999\n**Status:** Approved\n"), ("duplicate", original + original),
                              ("prefix collision", original.replace("## D-999 ", "## D-9999 ")),
                              ("unapproved", original.replace("Approved", "Proposed")),
                              ("stale registry", original.replace(digest(self.root / self.registry_path), "A" * 64))]:
            with self.subTest(name=name):
                self.put("DECISIONS.md", changed)
                with self.assertRaises(ValueError):
                    validate_approval(self.root, self.registry_path, "D-999")

    def test_review_rejections(self):
        original = copy.deepcopy(self.review)
        for name, mutate in [("author review", lambda r: r.update(reviewer_id=r["producer_id"])),
                             ("findings", lambda r: r.update(open_medium=1)),
                             ("mismatched snapshot", lambda r: r["source_snapshots"].pop()),
                             ("missing examined key", lambda r: r["examined_records"].pop()),
                             ("duplicate examined key", lambda r: r["examined_records"].append(r["examined_records"][0])),
                             ("receipt without conclusion", lambda r: r["examined_records"][0].update(source_criterion_conclusion="")),
                             ("wrong registry hash", lambda r: r.update(registry_sha256="A" * 64))]:
            with self.subTest(name=name):
                self.review = copy.deepcopy(original); mutate(self.review); self.save_review()
                with self.assertRaises(ValueError):
                    validate_approval(self.root, self.registry_path, "D-999")

    def test_duplicate_json_rejected(self):
        with self.assertRaises(ValueError):
            load_json('{"schema_version":1,"schema_version":1}')

    def test_selector_resolution(self):
        self.put("data.json", '{"a/b":{"~key":["specific process"]}}')
        witness = {"path": "data.json", "selector": {"kind": "json_pointer", "pointer": "/a~1b/~0key/0"},
                   "quoted_fact": "specific process", "supports": "Synthetic process"}
        selected_fact(self.root, witness)
        witness["selector"]["pointer"] = "/a~1b/~0key/00"
        with self.assertRaises(ValueError):
            selected_fact(self.root, witness)
        self.put("table.md", "| ACT-001 | source fact |\n")
        witness.update(path="table.md", selector={"kind": "markdown_table_id", "id": "ACT-001"}, quoted_fact="source fact")
        selected_fact(self.root, witness)
        self.put("table.md", "| ACT-001 | source fact |\n| ACT-001 | duplicate |\n")
        with self.assertRaises(ValueError):
            selected_fact(self.root, witness)


if __name__ == "__main__":
    unittest.main(verbosity=2)

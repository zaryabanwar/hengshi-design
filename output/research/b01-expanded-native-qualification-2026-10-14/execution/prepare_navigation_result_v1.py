"""Freeze the bounded native navigation construction evidence; no Figma access."""
import hashlib
import json
import shutil
import zipfile
from pathlib import Path

from PIL import Image

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
REVIEW = HERE / "review-navigation-construction"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path):
    return path.relative_to(ROOT).as_posix()


def write_new(path, value):
    data = (json.dumps(value, indent=2, ensure_ascii=False) + "\n").encode()
    if path.exists() and path.read_bytes() != data:
        raise RuntimeError(f"Refusing to replace frozen evidence: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)


census = json.loads((HERE / "navigation-32-native-census-v1.json").read_text(encoding="utf-8"))
modes = ["HIGH", "MEDIUM", "LOW", "SEMANTIC"]
expected = {(a, p, d) for a in modes for p in modes for d in ["OPEN", "CLOSED"]}
tuples = [tuple(row["name"].split(", ")) for row in census["rows"]]
assert len(tuples) == len(set(tuples)) == 32 and set(tuples) == expected
assert len({row["id"] for row in census["rows"]}) == 32
assert all(row["type"] == "Variant" and row["level"] == 2 for row in census["rows"])
early = json.loads((HERE / "navigation-early-state-reinspection-v1.json").read_text(encoding="utf-8"))
assert len(early) == 5 and not any(row.get("mismatch") for row in early)
archives = []
for name in ["navigation-two-seeds-v1.fig", "navigation-32-states-v1.fig",
             "navigation-32-final-v1.fig", "navigation-32-native-export.zip"]:
    path = HERE / name
    with zipfile.ZipFile(path) as archive:
        bad_member = archive.testzip()
        assert bad_member is None
        archives.append({"path": relative(path), "bytes": path.stat().st_size,
                         "sha256": digest(path), "members": len(archive.infolist()),
                         "crc_failure": bad_member})
with Image.open(HERE / "navigation-32-native-resolution.png") as image:
    assert image.size == (3020, 4880)

checkpoint = {
    "product": "Hengshi Design v1", "status": "DOING", "date": "2026-10-15",
    "authority": "D-094; guarded owned-seed refinement's bounded review retained",
    "file_key": "GOmLP6Cv96l768ueSrZ5Dg", "page_id": "0:1",
    "section_id": "144:3197", "navigation_set_id": "144:3287",
    "conversion_chains": {
        "open": ["144:3198 INSTANCE", "144:3220 FRAME", "144:3241 COMPONENT"],
        "closed": ["144:3242 INSTANCE", "144:3265 FRAME", "144:3286 COMPONENT"],
    },
    "construction_observed": {"new_sections": 1, "family_sets": 1,
        "navigation_variants": 32, "directory_variants": 0, "recovery_variants": 0,
        "preview_comparison_frames": 0, "new_edges_wired": 0},
    "qualification": {"native_scenarios_exercised": 0, "status": "TODO",
        "complete_trial": False, "B01_accepted": False, "phase_1_accepted": False},
    "inspection": {"native_badge": "32 Variants", "unique_tuples": 32,
        "expected_navigation_tuples_match": True, "five_early_states_reinspected": True,
        "image": relative(HERE / "navigation-32-native-resolution.png"),
        "image_dimensions": [3020, 4880], "image_sha256": digest(HERE / "navigation-32-native-resolution.png"),
        "method": "Native editor construction and visible DOM/field observations. The normal 1x export contains one full-resolution matrix image, not32 separate exports."},
    "preservation_limits": [
        "The original trial's owner, set, preview and eight variant names/properties were re-observed read-only; no exhaustive whole-file comparison.",
        "CRC verifies archive integrity only; native restore and _EXIT remain untested.",
        "Inherited-reaction inspection covers the saved root/functional-owner observations. Exhaustive descendant reaction census and new wiring remain open.",
        "The early CLOSED conversion name comparison observed16 rows with folded radio children; it is not a full subtree-equivalence proof.",
        "This is a private control qualification fixture, not a complete production navigation screen or semantic HTML/accessibility implementation.",
    ],
    "recovery_accounting": [
        "Browser binding changed; continued in the existing saved file/section without recreating the section.",
        "Producer anatomy-count guard corrected from22 descendants to21 (22 including the root); the stopped copy was reused.",
        "Hidden panel visibility is exposed as Show checked; observed native control used without inventing Hide semantics.",
        "Specific locator interactions/reads became stale or timed out. Normal screen actions and fresh evaluateAll DOM field inventories were used; initial three pending states and both seeds were subsequently reinspected.",
        "Layer virtualization hid ancestor rows. Native selected-variant inspector/set name plus owned tree levels replaced positional ancestor assumptions; stopped operations were reused or retried only after no-copy checks.",
        "A local attempt to generate an automation function from strings was refused by the tool before execution. Explicit normal-editor functions were used instead; no page-code injection or private Figma API.",
        "The new set was fitted to3020x4880 after observing its old1190 height clipped lower rows. Original sources were outside that resize.",
    ],
    "archives": archives,
    "unchanged_boundaries": ["No MCP/AI/paid/sharing/account/provider action", "No application/Git/deployment work", "Original reference/source writes not authorized or used"],
    "remaining": ["Directory32 and Recovery16 variants/two family sets", "36 preview/comparison frames", "324 reviewed single-action edges and60 no-ops", "Full native ENQ01-08 observations and result review", "Complete source preservation/restore/_EXIT and B01/Phase1 acceptance"],
    "review_status": "TODO; this producer checkpoint inherits no prior result verdict",
}
write_new(HERE / "navigation-construction-checkpoint-v1.json", checkpoint)

sources = [
    ROOT / "AGENTS.md", ROOT / ".specify/memory/constitution.md", ROOT / "DECISIONS.md",
    ROOT / "docs/software-definition/03-autonomous-ai-development-workflow.md",
    HERE.parent / "qualification-plan-v1.json",
    HERE.parent / "review/correction1/independent-review-expanded-qualification-v1.json",
    HERE / "owned-seed-conversion-proposal-v1.json",
    HERE / "review-seed-conversion/independent-review-seed-conversion-v1.json",
    HERE / "seed-detach-name-geometry-accounting-v1.json",
    HERE / "closed-seed-detach-accounting-v1.json",
    HERE / "detached-functional-owner-reaction-inspections-v1.json",
    HERE / "closed-functional-owner-reaction-inspections-v1.json",
    HERE / "seed-detached-root-prototype-current.txt",
    HERE / "seed-detached-close-prototype-current.txt",
    HERE / "independent-open-seed-named-current.txt",
    HERE / "independent-closed-seed-named-current.txt",
    HERE / "navigation-set-created-rows-current.json",
    HERE / "navigation-set-named-current.txt",
    HERE / "navigation-set-32-states-current.txt",
    HERE / "navigation-native-actions-20261015-v1.json",
    HERE / "navigation-32-native-census-v1.json",
    HERE / "navigation-early-state-reinspection-v1.json",
    HERE / "original-trial-post-navigation-observation-v1.json",
    HERE / "navigation-32-states-overview.png",
    HERE / "navigation-32-native-resolution.png",
    HERE / "navigation-export-settings-current.txt",
    HERE / "navigation-construction-checkpoint-v1.json",
    HERE / "before-expanded-trial-v1.fig",
    HERE / "owned-instance-before-conversion-v1.fig",
    HERE / "navigation-two-seeds-v1.fig",
    HERE / "navigation-32-final-v1.fig",
    HERE / "navigation-32-native-export.zip",
]
sources.extend(HERE / f"144-{suffix}-prototype-current.txt" for suffix in
               [3221, 3223, 3225, 3227, 3229, 3233, 3236])
sources.extend(HERE / f"144-{suffix}-closed-prototype-current.txt" for suffix in
               [3265, 3266, 3268, 3270, 3272, 3274, 3278, 3280, 3281])
bindings = []
for number, source in enumerate(sources):
    assert source.is_file(), source
    frozen = REVIEW / "inputs" / f"{number:02d}-{source.name}"
    frozen.parent.mkdir(parents=True, exist_ok=True)
    if frozen.exists() and digest(frozen) != digest(source):
        raise RuntimeError(f"Frozen source changed: {source}")
    shutil.copyfile(source, frozen)
    bindings.append({"source": relative(source), "frozen": relative(frozen),
                     "sha256": digest(source), "bytes": source.stat().st_size})
write_new(REVIEW / "review-inputs-v1.json", {
    "product": "Hengshi Design v1", "status": "DOING", "date": "2026-10-15",
    "scope": "Bounded owned-seed conversion and32-state navigation construction/accounting. No interaction/native scenario, full80-state trial, restore, source-preservation, B01 or Phase1 acceptance verdict.",
    "bindings": bindings,
    "requested_checks": ["Exact input binding integrity", "D094 and refinement alignment", "Observed owner/seed chains/current32-tuple inventory", "Native image and early-state observations", "Honest scope/preservation/recovery limits and remaining work"],
})
print(json.dumps({"native_tuples": len(tuples), "frozen_inputs": len(bindings),
                  "packet": relative(REVIEW / "review-inputs-v1.json"),
                  "checkpoint": relative(HERE / "navigation-construction-checkpoint-v1.json")}, indent=2))

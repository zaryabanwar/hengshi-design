"""Apply only the independently identified distribution-size wording repair."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
REVIEW = HERE / "review"
initial = REVIEW / "independent-review-identity-graph-v1.json"
if not initial.is_file():
    raise SystemExit("Initial independent receipt must exist before the repair")
initial_raw = initial.read_bytes()
packet = REVIEW / "correction-1"
if packet.exists():
    raise SystemExit("Correction packet already exists; do not overwrite it")
doc = ROOT / "docs/phase-1-compatibility/backend-evidence-2026-10-04.md"
before = doc.read_bytes()
old = b"compressed registry archive size is18,439,402bytes, not installed footprint."
new = b"registry-declared compressed wheel download size is18,439,402bytes, not installed footprint."
if before.count(old) != 1:
    raise SystemExit("Expected exactly one original wording occurrence")
packet.mkdir()
(packet / "before-backend-evidence.md").write_bytes(before)
doc.write_bytes(before.replace(old, new, 1))
manifest = json.loads((REVIEW / "review-inputs.json").read_bytes())
paths = [
    "docs/phase-1-compatibility/backend-evidence-2026-10-04.md",
    "docs/software-definition/04-reconciliation-map.md",
    initial.relative_to(ROOT).as_posix(),
    (REVIEW / "review-inputs.json").relative_to(ROOT).as_posix(),
    (packet / "before-backend-evidence.md").relative_to(ROOT).as_posix(),
    (HERE / "closure-observations.json").relative_to(ROOT).as_posix(),
    (HERE / "pip-report.json").relative_to(ROOT).as_posix(),
    Path(__file__).relative_to(ROOT).as_posix(),
]
inputs = []
for rel in paths:
    raw = (ROOT / rel).read_bytes()
    snap = packet / "inputs" / rel
    snap.parent.mkdir(parents=True, exist_ok=True)
    snap.write_bytes(raw)
    inputs.append({"path": rel, "snapshot": snap.relative_to(ROOT).as_posix(),
                   "sha256": hashlib.sha256(raw).hexdigest(), "bytes": len(raw)})
receipt = {"status": "DOING", "revision_cycle": 1,
           "scope": "Distribution wheel size terminology only; prior closure scope retained",
           "initial_review_sha256": hashlib.sha256(initial_raw).hexdigest(),
           "original_manifest_inputs": len(manifest["inputs"]),
           "inputs": inputs}
output = packet / "review-inputs.json"
output.write_bytes((json.dumps(receipt, indent=2) + "\n").encode())
print(json.dumps({"inputs": len(inputs), "manifest_sha256": hashlib.sha256(output.read_bytes()).hexdigest()}))

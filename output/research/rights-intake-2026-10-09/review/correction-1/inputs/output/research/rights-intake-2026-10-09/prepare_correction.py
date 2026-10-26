"""Repair RIGHTS01 only; preserve the original review and prior canonical bytes."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
REVIEW = HERE / "review"
initial = REVIEW / "independent-review-rights-intake-v1.json"
if not initial.exists():
    raise SystemExit("Initial independent receipt must exist")
packet = REVIEW / "correction-1"
if packet.exists():
    raise SystemExit("Correction already prepared")
doc = ROOT / "docs/phase-1-architecture/contracts/SECURITY_PRIVACY_CONTRACT.md"
before = doc.read_bytes()
old = b"""An authorized handler scopes the requested right against actual record/copy and
recipient inventories. Access output excludes other people's data and secrets;
review justified redactions without refusing all information automatically.
Correction, restriction, objection, erasure and applicable portability receive
"""
new = b"""An authorized handler scopes the requested right against actual record/copy and
recipient inventories. For mixed personal data, assess concrete impact on others'
rights and freedoms, balance the affected interests and reconcile them with
proportionate measures. Do not categorically remove another participant's data;
apply necessary scoped redactions and provide the useful remaining access. Where
reconciliation is impossible, record the assessed grounds for the specific limit.
Credentials and unrelated records remain protected; no broader access grant is
created by this assessment. Correction, restriction, objection, erasure and applicable portability receive
"""
if before.count(old) != 1:
    raise SystemExit("Expected exact unique rights-response paragraph")
packet.mkdir()
(packet / "before-security.md").write_bytes(before)
doc.write_bytes(before.replace(old, new, 1))
paths = [doc.relative_to(ROOT).as_posix(),
         "docs/phase-1-architecture/contracts/INTERFACE_CATALOG.md",
         initial.relative_to(ROOT).as_posix(),
         (REVIEW / "review-inputs.json").relative_to(ROOT).as_posix(),
         (packet / "before-security.md").relative_to(ROOT).as_posix(),
         (HERE / "edpb-access.raw.gz").relative_to(ROOT).as_posix(),
         (HERE / "primary-sources.json").relative_to(ROOT).as_posix(),
         Path(__file__).relative_to(ROOT).as_posix()]
inputs = []
for rel in paths:
    raw = (ROOT / rel).read_bytes()
    snap = packet / "inputs" / rel
    snap.parent.mkdir(parents=True, exist_ok=True)
    snap.write_bytes(raw)
    inputs.append({"path": rel, "snapshot": snap.relative_to(ROOT).as_posix(),
                   "sha256": hashlib.sha256(raw).hexdigest(), "bytes": len(raw)})
manifest = packet / "review-inputs.json"
manifest.write_bytes((json.dumps({"status": "DOING", "revision_cycle": 1,
    "scope": "RIGHTS01 concrete mixed-data impact/balancing repair only",
    "initial_review_sha256": hashlib.sha256(initial.read_bytes()).hexdigest(),
    "inputs": inputs}, indent=2) + "\n").encode())
print(json.dumps({"inputs": len(inputs), "manifest_sha256": hashlib.sha256(manifest.read_bytes()).hexdigest()}))

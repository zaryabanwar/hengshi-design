"""Apply only the reviewed prospective footprint-plan correction."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
STUDY = HERE.parent
ROOT = STUDY.parents[2]
OUT = HERE / "correction-1"
OUT.mkdir(exist_ok=True)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def write(path, obj):
    path.write_bytes((json.dumps(obj, indent=2) + "\n").encode())


plan_path = STUDY / "qualification-plan.json"
backend = ROOT / "docs/phase-1-compatibility/backend-evidence-2026-10-04.md"
for path in (plan_path, backend):
    target = OUT / "before" / path.name
    target.parent.mkdir(exist_ok=True)
    target.write_bytes(path.read_bytes())
plan = json.loads(plan_path.read_bytes())
plan["limits"]["budget_kind"] = "Conservative admission and command-boundary stop budget, not an OS-enforced hard quota during installation/native execution"
plan["limits"]["expanded_wheel_copy_reservation_factor"] = 2
plan["limits"]["additional_installer_output_reservation_bytes"] = 67108864
plan["steps"][1] = "Recheck frozen inputs, current native Python/pip identity and exact candidate hashes; refuse an existing target or incompatible host. Before any download or venv creation, require free disk greater than the full 256 MiB admission budget plus the retained 1 GiB floor. Check measured output/free space before and after each command, including failure; stop on over-budget or reserve loss."
plan["steps"][3] = "Download only the 43 exact hashed binary wheels with --require-hashes --only-binary=:all: --no-deps --no-cache-dir into the dedicated wheelhouse. Before installation, check every actual wheel size/hash against its frozen record and inspect zipfile.infolist without execution or extraction; reject malformed archives and sum declared expanded file sizes. Reserve measured retained download/venv/output bytes + twice total expanded wheel bytes + 64 MiB additional installer/output allowance. Require that total at or below 256 MiB and available disk at least 1 GiB plus all remaining reserved allocations; otherwise refuse installation without cleanup. No compressed-size-to-installed-footprint inference."
plan["steps"][4] += " Preserve the pre-install expanded-size/reservation calculation and post-command footprint/free-space observations. This conservative reservation is not an OS hard quota; installer/native code can consume unexpected space, which command-boundary checks detect rather than guarantee prevention."
plan["remaining"].append("No installed-footprint or hard disk-cap assurance from metadata or this unexecuted admission plan")
write(plan_path, plan)
raw = backend.read_bytes()
old = b'''18,107,329 archive bytes; the proposed new-output budget is256MiB with at least1GiB
free disk retained. Preflight and measured footprint checks precede installation;
refuse an existing target, source builds or changed protected inputs. Existing
'''
new = b'''18,107,329 compressed archive bytes, not installed footprint. The proposed256MiB
admission/stop budget retains1GiB free disk. Before downloads/venv creation, reserve
that full allowance. Before installation, match actual wheel sizes/hashes, inspect
ZIP entry sizes without extraction and require measured retained output plus twice
the expanded contents plus64MiB installer/output allowance to fit the budget and
free-disk reserve. Refuse when it does not fit. Measure before/after each command
and stop on over-budget/reserve loss, preserving failures. This is a conservative
admission calculation, not an OS-enforced hard quota during installer/native
execution. Refuse an existing target, source builds or changed protected inputs. Existing
'''
assert raw.count(old) == 1
backend.write_bytes(raw.replace(old, new, 1))
paths = [
    "AGENTS.md", ".specify/memory/constitution.md", "TASKS.md",
    "docs/phase-1-compatibility/backend-evidence-2026-10-04.md",
    "docs/phase-1-compatibility/README.md",
    "output/research/backend-crypto-graph-2026-10-08/qualification-plan.json",
    "output/research/backend-crypto-graph-2026-10-08/review/review-inputs.json",
    "output/research/backend-crypto-graph-2026-10-08/review/independent-review-crypto-graph-v1.json",
    "output/research/backend-crypto-graph-2026-10-08/review/correction-1/before/qualification-plan.json",
    "output/research/backend-crypto-graph-2026-10-08/review/correction-1/before/backend-evidence-2026-10-04.md"
]
inputs = []
for rel in paths:
    source = ROOT / rel
    data = source.read_bytes()
    target = OUT / "inputs" / rel
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(data)
    inputs.append({"path": rel, "snapshot": target.relative_to(ROOT).as_posix(),
                   "bytes": len(data), "sha256": sha(data)})
write(OUT / "review-inputs.json", {"status": "DOING", "revision_cycle": 1,
      "scope": "CRYPTO01 prospective admission/reservation correction only; original metadata review retains exact scope",
      "inputs": inputs})
print(json.dumps({"inputs": len(inputs), "manifest_sha256": sha((OUT / "review-inputs.json").read_bytes()),
                  "native_trial_exists": (STUDY / "native-trial").exists()}))

"""Read-only Authlib/backend resolver experiment. Never install or import it."""
import hashlib
import json
import os
import subprocess
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
BASIS = ROOT / "output/research/backend-crypto-graph-2026-10-08"
proposal = json.loads((BASIS / "proposal.json").read_bytes())
protected = {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest()
             for p in proposal["protected_inputs_before"]}
assert protected == proposal["protected_inputs_before"]
roots = (BASIS / "candidate-roots.txt").read_bytes() + b"authlib==1.8.0\n"
(HERE / "candidate-roots.txt").write_bytes(roots)
command = [str(ROOT / "apps/api/.venv/Scripts/python.exe"), "-B", "-m", "pip",
           "--isolated", "install", "--dry-run", "--ignore-installed", "--only-binary=:all:",
           "--no-cache-dir", "--disable-pip-version-check", "--progress-bar", "off",
           "--index-url", "https://pypi.org/simple", "--report", str(HERE / "pip-report.json"),
           "-r", str(HERE / "candidate-roots.txt")]
env = os.environ.copy()
env["PIP_CONFIG_FILE"] = os.devnull
started = time.monotonic()
with (HERE / "stdout.txt").open("wb") as stdout, (HERE / "stderr.txt").open("wb") as stderr:
    try:
        result = subprocess.run(command, env=env, cwd=ROOT, stdout=stdout, stderr=stderr, timeout=180)
        exit_code = result.returncode
    except subprocess.TimeoutExpired:
        exit_code = None
after = {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in protected}
report = HERE / "pip-report.json"
receipt = {"status": "DOING", "scope": "Unselected Authlib/backend Windows wheel-only metadata experiment",
           "command": command, "deadline_seconds": 180, "elapsed_seconds": round(time.monotonic()-started, 2),
           "exit_code": exit_code, "installation_performed": False,
           "basis_report_sha256": hashlib.sha256((BASIS / "pip-report.json").read_bytes()).hexdigest(),
           "roots_sha256": hashlib.sha256(roots).hexdigest(),
           "report_sha256": hashlib.sha256(report.read_bytes()).hexdigest() if report.exists() else None,
           "protected_inputs_before": protected, "protected_inputs_after": after,
           "protected_inputs_unchanged": protected == after,
           "limits": "Not runtime, OIDC/JWKS/provider/claim/expiry/atomic-consumption conformance, selection or permission for native installation"}
(HERE / "receipt.json").write_bytes((json.dumps(receipt, indent=2)+"\n").encode())
print(json.dumps({k: v for k, v in receipt.items() if k not in ("command", "protected_inputs_before", "protected_inputs_after")}, indent=2))

"""Isolated actual CLI probes; no application edits or package installation."""
import hashlib
import json
from pathlib import Path
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
TOOL = ROOT / "output/research/compatibility-resolution-2026-10-04/native-lint-probe/tool/node_modules/oxlint/bin/oxlint"
NODE = shutil.which("node")
PROTECTED = ["package.json", "package-lock.json", "apps/web/package.json", "apps/web/package-lock.json", "apps/api/requirements.txt", "apps/web/src/world/WorldHUD.tsx", "apps/web/src/world/ExteriorScene.tsx", "apps/web/src/world/WorldCanvas.tsx", "output/research/compatibility-resolution-2026-10-04/native-lint-probe/package.json", "output/research/compatibility-resolution-2026-10-04/native-lint-probe/package-lock.json"]

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

before = {p: digest(ROOT / p) for p in PROTECTED}
config = OUT / "probe-config.json"
config.write_text(json.dumps({"plugins": ["react"], "rules": {"react/rules-of-hooks": "error", "react/exhaustive-deps": "error"}}, indent=2) + "\n", encoding="utf-8")
fixtures = OUT / "base-fixtures"
fixtures.mkdir(exist_ok=True)
# Required semantics come from React's Rules of Hooks/dependency documentation.
# Renaming the callable does not make a conditional Hook semantically safe.
# These capability probes do not claim upstream plugin alias parity.
cases = [
    ("namespace-valid", True, "import * as React from 'react';\nexport function View({value}: {value: number}) {\n React.useEffect(() => { console.log(value); }, [value]);\n return <p>{value}</p>;\n}\n"),
    ("namespace-conditional", False, "import * as React from 'react';\nexport function View({ready}: {ready: boolean}) {\n if (!ready) return null;\n const [value] = React.useState(0);\n return <p>{value}</p>;\n}\n"),
    ("namespace-missing-dependency", False, "import * as React from 'react';\nexport function View({value}: {value: number}) {\n React.useEffect(() => { console.log(value); }, []);\n return <p>{value}</p>;\n}\n"),
    ("custom-hook-conditional", False, "import {useState} from 'react';\nfunction useSession() { return useState(0); }\nexport function View({ready}: {ready: boolean}) {\n if (!ready) return null;\n const [value] = useSession();\n return <p>{value}</p>;\n}\n"),
    ("named-hook-alias-conditional", False, "import {useState as useCounter} from 'react';\nexport function View({ready}: {ready: boolean}) {\n if (!ready) return null;\n const [value] = useCounter(0);\n return <p>{value}</p>;\n}\n"),
    ("renamed-hook-conditional", False, "import {useState as state} from 'react';\nexport function View({ready}: {ready: boolean}) {\n if (!ready) return null;\n const [value] = state(0);\n return <p>{value}</p>;\n}\n"),
    ("renamed-effect-missing-dependency", False, "import {useEffect as effect} from 'react';\nexport function View({value}: {value: number}) {\n effect(() => { console.log(value); }, []);\n return <p>{value}</p>;\n}\n"),
]
base = [NODE, str(TOOL), "--config", str(config), "--allow", "all", "--deny", "react/rules-of-hooks", "--deny", "react/exhaustive-deps", "--no-ignore", "--disable-nested-config", "--format", "json"]
results = []
for name, expected_accept, source in cases:
    path = fixtures / (name + ".tsx")
    path.write_text(source, encoding="utf-8")
    command = base + [str(path)]
    run = subprocess.run(command, cwd=OUT, capture_output=True, text=True, timeout=30)
    (OUT / (name + "-stdout.json")).write_text(run.stdout, encoding="utf-8")
    (OUT / (name + "-stderr.txt")).write_text(run.stderr, encoding="utf-8")
    parsed = json.loads(run.stdout)
    observed_accept = run.returncode == 0 and not parsed.get("diagnostics")
    results.append({"case": name, "source_sha256": digest(path), "expected_accept_from_react_semantics": expected_accept, "exit_code": run.returncode, "observed_accept": observed_accept, "required_semantics_detected": observed_accept == expected_accept, "codes": [d["code"] for d in parsed.get("diagnostics", [])], "number_of_files": parsed.get("number_of_files"), "number_of_rules": parsed.get("number_of_rules"), "command": command, "stdout_sha256": digest(OUT / (name + "-stdout.json")), "stderr_sha256": digest(OUT / (name + "-stderr.txt"))})

# A CI-like caller must treat input/config failures as failures, independently
# of source diagnostics. Invalid JSON and no files are deliberately isolated.
bad = OUT / "invalid-config.json"
bad.write_text("{invalid json", encoding="utf-8")
controls = [("invalid-config", [NODE, str(TOOL), "--config", str(bad), "--format", "json", str(fixtures / "namespace-valid.tsx")]), ("unmatched-file", base + [str(OUT / "absent-source.tsx")]), ("directory-scope", base + [str(fixtures)])]
for name, command in controls:
    run = subprocess.run(command, cwd=OUT, capture_output=True, text=True, timeout=30)
    (OUT / (name + "-stdout.txt")).write_text(run.stdout, encoding="utf-8")
    (OUT / (name + "-stderr.txt")).write_text(run.stderr, encoding="utf-8")
    try:
        parsed = json.loads(run.stdout)
    except json.JSONDecodeError:
        parsed = {}
    results.append({"case": name, "command": command, "exit_code": run.returncode, "expected_nonzero": True, "nonzero_observed": run.returncode != 0, "number_of_files": parsed.get("number_of_files"), "number_of_rules": parsed.get("number_of_rules"), "codes": [d["code"] for d in parsed.get("diagnostics", [])], "stdout_sha256": digest(OUT / (name + "-stdout.txt")), "stderr_sha256": digest(OUT / (name + "-stderr.txt"))})

# React documents both a shared setting and a rule-level option for custom
# Effect hooks. Test the actual candidate; do not assume config API parity.
custom_fixtures = OUT / "custom-fixtures"
custom_fixtures.mkdir(exist_ok=True)
for name, shared, valid in [("custom-effect-shared-invalid", True, False), ("custom-effect-rule-invalid", False, False), ("custom-effect-rule-valid", False, True), ("custom-effect-rule-invalid-cli-override", False, False)]:
    configured = {"plugins": ["react"], "categories": {"correctness": "off"}, "rules": {"react/rules-of-hooks": "error", "react/exhaustive-deps": "error"}}
    if shared:
        configured["settings"] = {"react-hooks": {"additionalEffectHooks": "useSpecialEffect"}}
    else:
        configured["rules"]["react/exhaustive-deps"] = ["error", {"additionalHooks": "useSpecialEffect"}]
    cfg = OUT / (name + "-config.json")
    cfg.write_text(json.dumps(configured, indent=2) + "\n", encoding="utf-8")
    path = custom_fixtures / (name + ".tsx")
    deps = "[value]" if valid else "[]"
    path.write_text("import {useSpecialEffect} from './custom-effects';\nexport function View({value}: {value: number}) {\n useSpecialEffect(() => { console.log(value); }, " + deps + ");\n return <p>{value}</p>;\n}\n", encoding="utf-8")
    command = [NODE, str(TOOL), "--config", str(cfg), "--no-ignore", "--disable-nested-config", "--format", "json", str(path)]
    if name.endswith("cli-override"):
        command = list(base)
        command[3] = str(cfg)
        command.append(str(path))
    run = subprocess.run(command, cwd=OUT, capture_output=True, text=True, timeout=30)
    (OUT / (name + "-stdout.json")).write_text(run.stdout, encoding="utf-8")
    (OUT / (name + "-stderr.txt")).write_text(run.stderr, encoding="utf-8")
    parsed = json.loads(run.stdout)
    observed_accept = run.returncode == 0 and not parsed.get("diagnostics")
    results.append({"case": name, "source_sha256": digest(path), "config_sha256": digest(cfg), "expected_accept_from_react_semantics": valid, "exit_code": run.returncode, "observed_accept": observed_accept, "required_semantics_detected": observed_accept == valid, "codes": [d["code"] for d in parsed.get("diagnostics", [])], "number_of_files": parsed.get("number_of_files"), "number_of_rules": parsed.get("number_of_rules"), "command": command, "stdout_sha256": digest(OUT / (name + "-stdout.json")), "stderr_sha256": digest(OUT / (name + "-stderr.txt"))})

after = {p: digest(ROOT / p) for p in PROTECTED}
receipt = {"schema_version": 1, "date": "2026-10-05", "status": "DOING", "candidate": "Oxlint 1.86.0", "node_version": subprocess.check_output([NODE, "--version"], text=True).strip(), "tool_version": subprocess.check_output([NODE, str(TOOL), "--version"], text=True).strip(), "oracle_sources": ["https://react.dev/reference/rules/rules-of-hooks", "https://react.dev/reference/eslint-plugin-react-hooks/lints/exhaustive-deps"], "only_two_stable_native_rules": True, "experimental_rules_enabled": False, "production_selection": False, "upstream_alias_parity_claimed": False, "application_runtime_tests": False, "protected_before": before, "protected_after": after, "protected_unchanged": before == after, "cases": results}
(OUT / "receipt.json").write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"version": receipt["tool_version"], "protected_unchanged": receipt["protected_unchanged"], "observations": [{k: c.get(k) for k in ("case", "exit_code", "required_semantics_detected", "nonzero_observed", "number_of_files", "codes")} for c in results]}, indent=2))

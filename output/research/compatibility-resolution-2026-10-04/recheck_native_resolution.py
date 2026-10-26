"""Record a separate strict lock-only observation; never install app packages.

The original native study and protected application inputs stay unchanged.
This is resolver evidence, not stable graph selection or runtime compatibility.
"""
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import subprocess


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    root = Path(__file__).resolve().parents[3]
    evidence = root / "output/research/compatibility-resolution-2026-10-04"
    original = evidence / "native-lint-probe"
    study = evidence / "native-lint-strict-resolution-recheck"
    protected = [root / name for name in (
        "package.json", "package-lock.json", "apps/web/package.json",
        "apps/web/package-lock.json", "apps/api/requirements.txt",
        "apps/web/src/world/WorldCanvas.tsx", "apps/web/src/world/ExteriorScene.tsx",
        "apps/web/src/world/WorldHUD.tsx",
    )] + [original / "package.json", original / "package-lock.json"]
    before = {str(p.relative_to(root)): digest(p) for p in protected}
    if study.exists():
        raise SystemExit("Study already exists; preserve evidence rather than overwrite it")
    assert study.resolve().is_relative_to(evidence.resolve())
    study.mkdir()
    manifest = study / "package.json"
    manifest.write_bytes((original / "package.json").read_bytes())
    user_config = study / "empty-user.npmrc"
    global_config = study / "empty-global.npmrc"
    user_config.write_text("", encoding="utf-8")
    global_config.write_text("", encoding="utf-8")
    node = Path("C:/nvm4w/nodejs/node.exe")
    npm_cli = Path("C:/nvm4w/nodejs/node_modules/npm/bin/npm-cli.js")
    definitions = npm_cli.parent.parent / "node_modules/@npmcli/config/lib/definitions/definitions.js"
    env = {k: v for k, v in os.environ.items()
           if not k.lower().startswith("npm_config_") and k.upper() != "NODE_OPTIONS"}
    command = [str(node), str(npm_cli), "install", "--package-lock-only",
               "--ignore-scripts", "--strict-peer-deps=true", "--legacy-peer-deps=false",
               "--engine-strict=true", "--force=false", "--no-audit", "--no-fund",
               "--workspaces=false", "--include=dev", "--include=optional", "--include=peer",
               "--registry=https://registry.npmjs.org/", "--loglevel=error",
               "--userconfig=" + str(user_config), "--globalconfig=" + str(global_config),
               "--cache=" + str(study / "metadata-cache")]
    receipt = {
        "schema_version": 1, "status": "DOING", "production_selection": False,
        "started_at": datetime.now(timezone.utc).isoformat(), "cwd": str(study),
        "command": command, "input_manifest_sha256": digest(manifest),
        "initial_lock_present": False, "initial_node_modules_present": False,
        "node_version": subprocess.check_output([str(node), "--version"], text=True, env=env).strip(),
        "npm_version": subprocess.check_output([str(node), str(npm_cli), "--version"], text=True, env=env).strip(),
        "npm_cli_sha256": digest(npm_cli), "installed_npm_definitions_sha256": digest(definitions),
        "configuration_boundary": "Empty explicit user/global config; npm_config_* and NODE_OPTIONS removed only from child environment; no environment values copied to evidence",
        "protected_before_sha256": before,
        "limits": ["Fresh manifest-only resolution, not reproduction of the original lock",
                   "Lock/peer/engine observation only; no install, lifecycle, compiler, build or browser proof",
                   "No production selection, licence clearance or application change"],
    }
    receipt_path = study / "receipt.json"
    receipt_path.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    stdout, stderr = study / "stdout.txt", study / "stderr.txt"
    with stdout.open("w", encoding="utf-8") as out, stderr.open("w", encoding="utf-8") as err:
        process = subprocess.run(command, cwd=study, env=env, stdout=out, stderr=err,
                                 creationflags=subprocess.CREATE_NO_WINDOW)
    after = {str(p.relative_to(root)): digest(p) for p in protected}
    lock = study / "package-lock.json"
    receipt.update({"completed_at": datetime.now(timezone.utc).isoformat(),
                    "exit_code": process.returncode,
                    "stdout_sha256": digest(stdout), "stderr_sha256": digest(stderr),
                    "protected_after_sha256": after, "protected_inputs_unchanged": before == after,
                    "manifest_unchanged": digest(manifest) == receipt["input_manifest_sha256"],
                    "node_modules_present_after": (study / "node_modules").exists(),
                    "lock_sha256": digest(lock) if lock.exists() else None})
    if lock.exists():
        packages = json.loads(lock.read_text(encoding="utf-8"))["packages"]
        original_packages = json.loads((original / "package-lock.json").read_text(encoding="utf-8"))["packages"]
        receipt["package_records"] = len(packages)
        receipt["original_package_records"] = len(original_packages)
        receipt["lock_bytes_match_original"] = digest(lock) == digest(original / "package-lock.json")
        receipt["package_identity_changes"] = [
            {"path": p, "original": original_packages.get(p), "observed": packages.get(p)}
            for p in sorted(set(packages) | set(original_packages))
            if original_packages.get(p) != packages.get(p)]
        receipt["prerelease_records"] = [
            {"path": p, "version": row["version"]} for p, row in packages.items()
            if p and "version" in row and "-" in row["version"].split("+")[0]]
    receipt_path.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print("STRICT_RESOLUTION_RECHECK", process.returncode, "records", receipt.get("package_records"),
          "unchanged inputs", before == after, "node_modules", receipt["node_modules_present_after"])
    if process.returncode or before != after or not receipt["manifest_unchanged"] or receipt["node_modules_present_after"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

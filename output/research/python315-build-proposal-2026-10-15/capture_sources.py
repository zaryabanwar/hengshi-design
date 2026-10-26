"""Read-only current stable roots and exact upstream build source; no resolver/build."""
import concurrent.futures
import gzip
import hashlib
import json
import shutil
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

from packaging.requirements import Requirement
from packaging.specifiers import SpecifierSet
from packaging.utils import canonicalize_name, parse_wheel_filename
from packaging.version import Version
from packaging.tags import compatible_tags, cpython_tags

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
BASIS = ROOT / "output/research/test-client-graph-2026-10-09"
PROTECTED = ["package.json", "package-lock.json", "apps/web/package.json",
             "apps/web/package-lock.json", "apps/api/requirements.txt", "apps/api/.venv/pyvenv.cfg"]
TOOLS = ["pip", "setuptools", "cython", "wheel", "build", "packaging"]
DOCS = {
    "pyyaml-setup": "https://raw.githubusercontent.com/yaml/pyyaml/6.0.3/setup.py",
    "pyyaml-pyproject": "https://raw.githubusercontent.com/yaml/pyyaml/6.0.3/pyproject.toml",
    "pyyaml-build-backend": "https://raw.githubusercontent.com/yaml/pyyaml/6.0.3/packaging/_pyyaml_pep517.py",
    "pip-build-interface": "https://pip.pypa.io/en/stable/reference/build-system/",
    "pip-install": "https://pip.pypa.io/en/stable/cli/pip_install/",
    "python-windows": "https://docs.python.org/3.15/using/windows.html",
}
sha = lambda value: hashlib.sha256(value).hexdigest()


def capture(key, url, is_json):
    request = urllib.request.Request(url, headers={"Accept-Encoding": "identity",
        "User-Agent": "Hengshi-Phase1-read-only-build-planning/1"})
    with urllib.request.urlopen(request, timeout=40) as response:
        raw = response.read(8 * 1024 * 1024 + 1)
        if len(raw) > 8 * 1024 * 1024:
            raise RuntimeError("Per-response metadata budget exceeded")
        content = gzip.decompress(raw) if raw.startswith(b"\x1f\x8b") else raw
        rel = f"captures/{key}.{'json' if is_json else 'txt'}.gz"
        compressed = gzip.compress(raw, mtime=0)
        with (OUT / rel).open("xb") as stream:
            stream.write(compressed)
        record = {"key": key, "url": url, "final_url": response.geturl(),
            "captured_at_utc": datetime.now(timezone.utc).isoformat(), "status": response.status,
            "content_type": response.headers.get("Content-Type"),
            "content_encoding": response.headers.get("Content-Encoding"),
            "etag": response.headers.get("ETag"), "last_serial": response.headers.get("X-PyPI-Last-Serial"),
            "response_bytes": len(raw), "response_sha256": sha(raw),
            "decoded_bytes": len(content), "decoded_sha256": sha(content),
            "saved": rel, "saved_sha256": sha(compressed)}
        return record, json.loads(content) if is_json else content.decode("utf-8")


def main():
    (OUT / "captures").mkdir(exist_ok=True)
    if list((OUT / "captures").iterdir()):
        raise RuntimeError("Existing capture; do not retry or overwrite")
    if shutil.disk_usage(OUT).free < 1024**3 + 64 * 1024 * 1024:
        raise RuntimeError("Metadata disk reservation/floor failed")
    before = {name: sha((ROOT / name).read_bytes()) for name in PROTECTED}
    roots = [Requirement(line.strip()) for line in (BASIS / "candidate-roots.txt").read_text(encoding="utf-8").splitlines()
             if line.strip() and not line.startswith("#")]
    names = sorted({canonicalize_name(r.name) for r in roots} | set(TOOLS))
    captures, data, errors = [], {}, []
    jobs = [(name, f"https://pypi.org/pypi/{name}/json", True) for name in names]
    jobs += [(key, url, False) for key, url in DOCS.items()]
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
        futures = {pool.submit(capture, *job): job[0] for job in jobs}
        for future in concurrent.futures.as_completed(futures):
            key = futures[future]
            try:
                record, value = future.result()
                captures.append(record)
                data[key] = value
            except Exception as exc:
                errors.append({"key": key, "error": f"{type(exc).__name__}: {exc}"})
    target = set(cpython_tags((3, 15), abis=["cp315"], platforms=["win_amd64"]))
    target.update(compatible_tags((3, 15), interpreter="cp315", platforms=["win_amd64"]))
    observations = []
    for name in names:
        if name not in data:
            continue
        release = data[name]
        info = release["info"]
        version = Version(info["version"])
        eligible = []
        for file in release["urls"]:
            if file["packagetype"] != "bdist_wheel" or file.get("yanked"):
                continue
            if not SpecifierSet(file.get("requires_python") or "").contains("3.15.0", prereleases=False):
                continue
            if parse_wheel_filename(file["filename"])[-1] & target:
                eligible.append({key: file[key] for key in ["filename", "size", "url", "digests", "requires_python"]})
        observations.append({"name": name, "observed_version": info["version"],
            "stable_version_identifier": not version.is_prerelease and not version.is_devrelease,
            "requires_python": info.get("requires_python"),
            "declared_python315_allowed": SpecifierSet(info.get("requires_python") or "").contains("3.15.0", prereleases=False),
            "requires_dist": info.get("requires_dist", []), "matching_windows315_wheels": eligible,
            "role": "existing qualification root" if name in {canonicalize_name(r.name) for r in roots} else "prospective build/installer tool",
            "old_root_pin": next((str(r) for r in roots if canonicalize_name(r.name) == name), None)})
    after = {name: sha((ROOT / name).read_bytes()) for name in PROTECTED}
    result = {"product": "Hengshi Design v1", "status": "DOING", "date": "2026-10-15",
        "capture_failures": errors, "captures": sorted(captures, key=lambda r: r["key"]),
        "current_observations": observations, "protected_before": before, "protected_after": after,
        "protected_unchanged": before == after,
        "raw_network_bytes": sum(r["response_bytes"] for r in captures),
        "scope": "Dated independently-current registry root/tool observations and exact6.0.3 source only. No coupled selection, resolver, package/runtime download, build, installation or application/environment changes.",
        "context7_limit": "Context7 main branch contains7.0.0.dev0; only exact stable6.0.3 sources can define this build proposal."}
    with (OUT / "source-observations.json").open("x", encoding="utf-8") as stream:
        json.dump(result, stream, indent=2); stream.write("\n")
    print(json.dumps({"captures": len(captures), "errors": errors, "protected_unchanged": before == after,
        "versions": [{"name": r["name"], "old": r["old_root_pin"], "observed": r["observed_version"],
                      "windows315_wheel_count": len(r["matching_windows315_wheels"])} for r in observations]}, indent=2))
    if errors or before != after:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

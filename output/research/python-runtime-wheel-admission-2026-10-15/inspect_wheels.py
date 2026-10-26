"""Read-only PyPI admission for the frozen trial; never installs or resolves."""
from __future__ import annotations

import concurrent.futures
import gzip
import hashlib
import json
import shutil
import sys
import threading
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

import packaging
from packaging.specifiers import SpecifierSet
from packaging.tags import compatible_tags, cpython_tags
from packaging.utils import canonicalize_name, parse_wheel_filename
from packaging.version import Version

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
SOURCE = ROOT / "output/research/test-client-graph-2026-10-09/pip-report.json"
PROTECTED = ["package.json", "package-lock.json", "apps/web/package.json",
             "apps/web/package-lock.json", "apps/api/requirements.txt",
             "apps/api/.venv/pyvenv.cfg"]
TARGETS = {"3.14.8": (3, 14), "3.15.0": (3, 15)}
DOCS = {
    "python-3150": "https://www.python.org/downloads/release/python-3150/",
    "python-3148": "https://www.python.org/downloads/release/python-3148/",
    "stable-abi-315": "https://docs.python.org/3.15/c-api/stable.html",
    "packaging-tags": "https://packaging.pypa.io/en/stable/tags.html",
    "pypi-json-api": "https://docs.pypi.org/api/json/",
}
LOCK = threading.Lock()
RAW_BYTES = 0
MAX_RESPONSE = 8 * 1024 * 1024
MAX_TOTAL = 64 * 1024 * 1024
FREE_FLOOR = 1024**3


def sha(data):
    return hashlib.sha256(data).hexdigest()


def save(name, value):
    path = OUT / name
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x", encoding="utf-8", newline="\n") as stream:
        json.dump(value, stream, ensure_ascii=False, indent=2)
        stream.write("\n")


def protected():
    return {name: sha((ROOT / name).read_bytes()) for name in PROTECTED}


def fetch(key, url, kind):
    global RAW_BYTES
    if shutil.disk_usage(OUT).free < FREE_FLOOR:
        raise RuntimeError("Free-space admission failed")
    request = urllib.request.Request(url, headers={
        "User-Agent": "Hengshi-Phase1-read-only-compatibility-research/1",
        "Accept": "application/json" if kind == "json" else "text/html",
        "Accept-Encoding": "identity",
    })
    with urllib.request.urlopen(request, timeout=40) as response:
        final_url = response.geturl()
        if urllib.parse.urlsplit(final_url).hostname != urllib.parse.urlsplit(url).hostname:
            raise RuntimeError("Cross-host redirect refused")
        raw = response.read(MAX_RESPONSE + 1)
        if len(raw) > MAX_RESPONSE:
            raise RuntimeError("Response exceeds metadata budget")
        with LOCK:
            RAW_BYTES += len(raw)
            if RAW_BYTES > MAX_TOTAL:
                raise RuntimeError("Aggregate metadata budget exceeded")
        rel = f"captures/{key}.{'json' if kind == 'json' else 'html'}.gz"
        compressed = gzip.compress(raw, mtime=0)
        with (OUT / rel).open("xb") as stream:
            stream.write(compressed)
        capture = {
            "key": key, "url": url, "final_url": final_url,
            "captured_at_utc": datetime.now(timezone.utc).isoformat(),
            "http_status": response.status, "content_type": response.headers.get("Content-Type"),
            "etag": response.headers.get("ETag"), "last_serial": response.headers.get("X-PyPI-Last-Serial"),
            "raw_bytes": len(raw), "sha256": sha(raw), "saved": rel,
            "compressed_bytes": len(compressed), "compressed_sha256": sha(compressed),
        }
    return capture, json.loads(raw) if kind == "json" else raw.decode("utf-8")


def target_tags(pair):
    interpreter = "cp" + "".join(map(str, pair))
    ordered = list(cpython_tags(pair, abis=[interpreter], platforms=["win_amd64"]))
    ordered += list(compatible_tags(pair, interpreter=interpreter, platforms=["win_amd64"]))
    return ordered


def inspect_release(item, data, tags_by_target):
    old = item["metadata"]
    name, version = canonicalize_name(old["name"]), old["version"]
    info = data["info"]
    if canonicalize_name(info["name"]) != name or Version(info["version"]) != Version(version):
        raise RuntimeError(f"PyPI identity mismatch: {name}")
    old_filename = urllib.parse.unquote(urllib.parse.urlsplit(item["download_info"]["url"]).path.split("/")[-1])
    old_hash = item["download_info"]["archive_info"]["hashes"]["sha256"]
    original = [f for f in data["urls"] if f["filename"] == old_filename]
    original_matches = len(original) == 1 and original[0]["digests"]["sha256"] == old_hash
    rows = {}
    for runtime, ordered_tags in tags_by_target.items():
        ranks = {tag: i for i, tag in enumerate(ordered_tags)}
        applicable = []
        rejected = {"yanked": 0, "requires_python": 0, "tags": 0, "not_wheel": 0}
        release_allows = SpecifierSet(info.get("requires_python") or "").contains(runtime, prereleases=False)
        for file in data["urls"]:
            if file["packagetype"] != "bdist_wheel":
                rejected["not_wheel"] += 1
                continue
            wheel_name, wheel_version, _, wheel_tags = parse_wheel_filename(file["filename"])
            if wheel_name != name or wheel_version != Version(version):
                raise RuntimeError(f"Wheel identity mismatch: {file['filename']}")
            if file.get("yanked", False):
                rejected["yanked"] += 1
                continue
            if not SpecifierSet(file.get("requires_python") or "").contains(runtime, prereleases=False):
                rejected["requires_python"] += 1
                continue
            matching = wheel_tags.intersection(ranks)
            if not matching:
                rejected["tags"] += 1
                continue
            applicable.append({
                "filename": file["filename"], "url": file["url"],
                "sha256": file["digests"]["sha256"], "size": file["size"],
                "requires_python": file.get("requires_python"),
                "upload_time_iso_8601": file.get("upload_time_iso_8601"),
                "matching_tags": sorted(map(str, matching)),
                "preference_rank": min(ranks[tag] for tag in matching),
            })
        applicable.sort(key=lambda f: (f["preference_rank"], f["filename"]))
        rows[runtime] = {"release_requires_python_allows": release_allows,
                         "admitted": release_allows and bool(applicable),
                         "applicable_wheels": applicable, "rejected_file_counts": rejected}
    return {"name": name, "version": version, "release_requires_python": info.get("requires_python"),
            "original_trial_filename": old_filename, "original_trial_sha256": old_hash,
            "original_file_registry_hash_matches": original_matches, "targets": rows}


def main():
    (OUT / "captures").mkdir(exist_ok=True)
    if (OUT / "observations.json").exists() or list((OUT / "captures").iterdir()):
        raise RuntimeError("Capture already started; replay saved bytes instead of overwriting/retrying")
    before = protected()
    report = json.loads(SOURCE.read_text(encoding="utf-8-sig"))
    items = report["install"]
    identities = [(canonicalize_name(i["metadata"]["name"]), i["metadata"]["version"]) for i in items]
    if len(identities) != 48 or len(set(n for n, _ in identities)) != 48:
        raise RuntimeError("Frozen candidate must contain 48 unique package identities")
    save("admission.json", {"status": "DOING", "started_at_utc": datetime.now(timezone.utc).isoformat(),
         "source": str(SOURCE.relative_to(ROOT)), "source_sha256": sha(SOURCE.read_bytes()),
         "source_environment": report["environment"], "analysis_python": sys.version,
         "analysis_interpreter": sys.executable, "packaging_version": packaging.__version__,
         "protected_before": before, "free_before": shutil.disk_usage(OUT).free,
         "max_response_bytes": MAX_RESPONSE, "max_raw_total_bytes": MAX_TOTAL,
         "free_floor_bytes": FREE_FLOOR, "target_scope": "normal GIL-enabled CPython, Windows AMD64, frozen exact versions only",
         "network": "53 read-only metadata/document GETs; no retry, wheels, resolution or installation"})
    tags = {runtime: target_tags(pair) for runtime, pair in TARGETS.items()}
    save("target-tags.json", {runtime: list(map(str, values)) for runtime, values in tags.items()})
    jobs = [(f"{n}-{v}", f"https://pypi.org/pypi/{n}/{v}/json", "json", item)
            for (n, v), item in zip(identities, items)]
    jobs += [(key, url, "html", None) for key, url in DOCS.items()]
    captures, observations, failures = [], [], []
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
        futures = {pool.submit(fetch, key, url, kind): (key, item) for key, url, kind, item in jobs}
        for future in concurrent.futures.as_completed(futures):
            key, item = futures[future]
            try:
                capture, data = future.result()
                captures.append(capture)
                if item:
                    observations.append(inspect_release(item, data, tags))
            except Exception as exc:
                failures.append({"key": key, "error": f"{type(exc).__name__}: {exc}"})
    after = protected()
    summary = {runtime: {"admitted_count": sum(p["targets"][runtime]["admitted"] for p in observations),
                        "not_admitted": [{"name": p["name"], "version": p["version"],
                                          "release_requires_python": p["release_requires_python"],
                                          **p["targets"][runtime]} for p in observations if not p["targets"][runtime]["admitted"]]}
               for runtime in TARGETS}
    save("captures.json", sorted(captures, key=lambda x: x["key"]))
    save("observations.json", {"status": "DOING", "captured_at_utc": datetime.now(timezone.utc).isoformat(),
         "packages": sorted(observations, key=lambda x: x["name"]), "summary": summary,
         "failures": failures, "raw_bytes": RAW_BYTES,
         "original_registry_hash_matches": sum(x["original_file_registry_hash_matches"] for x in observations),
         "protected_after": after, "protected_unchanged": before == after,
         "free_after": shutil.disk_usage(OUT).free,
         "limits": ["Registry tags and Requires-Python admit files only; not runtime compatibility or complete resolver closure.",
                    "Changing Python markers can change the closure. No new dependency resolution was attempted.",
                    "No wheel or runtime was downloaded, installed or executed; no version or exception was selected.",
                    "No free-threaded, debug, ARM, Linux, provider, provenance, licence or security qualification.",
                    "Existing 18 library cases remain evidence only for their original CPython 3.14.5 environment."]})
    print(json.dumps({"summary": summary, "captures": len(captures), "failures": failures,
                      "raw_bytes": RAW_BYTES, "protected_unchanged": before == after}, indent=2))
    if failures or before != after:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

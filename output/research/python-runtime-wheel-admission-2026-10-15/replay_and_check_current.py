"""Preserve the capture failure; decode saved docs and inspect two latest releases."""
import gzip
import json
import re
from datetime import datetime, timezone

import inspect_wheels as study


def main():
    before = study.protected()
    initial = json.loads((study.OUT / "observations.json").read_text(encoding="utf-8"))
    captures = json.loads((study.OUT / "captures.json").read_text(encoding="utf-8"))
    recovery = []
    for key in ("python-3150", "python-3148"):
        path = study.OUT / "captures" / f"{key}.html.gz"
        saved = path.read_bytes()
        response_bytes = gzip.decompress(saved)
        if not response_bytes.startswith(b"\x1f\x8b"):
            raise RuntimeError("Expected saved gzip response bytes")
        html = gzip.decompress(response_bytes)
        text = html.decode("utf-8")
        expected = "Python 3.15.0" if key == "python-3150" else "Python 3.14.8"
        if expected not in text:
            raise RuntimeError("Unexpected release document")
        rel = f"captures/{key}.decoded.html.gz"
        with (study.OUT / rel).open("xb") as stream:
            stream.write(gzip.compress(html, mtime=0))
        recovery.append({"key": key, "source_url": study.DOCS[key],
            "saved_response": str(path.relative_to(study.OUT)), "saved_sha256": study.sha(saved),
            "response_bytes_sha256": study.sha(response_bytes), "decoded": rel,
            "decoded_bytes": len(html), "decoded_sha256": study.sha(html),
            "release_heading": re.findall(r'<h1 class="page-title">(.*?)</h1>', text),
            "date_strings": re.findall(r'Release Date:</strong>\s*(.*?)</p>', text),
            "recovery": "Offline decode of compressed response; no second request.",
            "limitation": "Original fetch wrote response before its text decode failed; response headers/status/timestamp were not retained for these two records."})
    report = json.loads(study.SOURCE.read_text(encoding="utf-8-sig"))
    tags = {runtime: study.target_tags(pair) for runtime, pair in study.TARGETS.items()}
    replay = []
    for item in report["install"]:
        metadata = item["metadata"]
        key = f'{study.canonicalize_name(metadata["name"])}-{metadata["version"]}'
        capture = next(c for c in captures if c["key"] == key)
        raw = gzip.decompress((study.OUT / capture["saved"]).read_bytes())
        if study.sha(raw) != capture["sha256"]:
            raise RuntimeError("Saved package capture hash mismatch")
        replay.append(study.inspect_release(item, json.loads(raw), tags))
    replay.sort(key=lambda p: p["name"])
    if replay != initial["packages"]:
        raise RuntimeError("Offline replay disagrees with first package observations")
    current = []
    for name in ("httptools", "pyyaml"):
        capture, data = study.fetch(f"{name}-current", f"https://pypi.org/pypi/{name}/json", "json")
        original = next(i for i in report["install"] if study.canonicalize_name(i["metadata"]["name"]) == name)
        candidate = {**original, "metadata": data["info"]}
        row = study.inspect_release(candidate, data, tags)
        row.pop("original_trial_filename")
        row.pop("original_trial_sha256")
        row.pop("original_file_registry_hash_matches")
        if study.Version(row["version"]).is_prerelease or study.Version(row["version"]).is_devrelease:
            raise RuntimeError("Current observation unexpectedly prerelease")
        current.append({"capture": capture, "observation": row})
    # Exercise the actual packaging APIs with independent binary-tag boundaries.
    boundaries = [
        ("demo-1.0-cp314-cp314-win_amd64.whl", False),
        ("demo-1.0-cp314-abi3-win_amd64.whl", True),
        ("demo-1.0-cp315-cp315-win_amd64.whl", True),
        ("demo-1.0-cp315-cp315t-win_amd64.whl", False),
        ("demo-1.0-py3-none-any.whl", True),
        ("demo-1.0-cp315-cp315-manylinux_2_17_x86_64.whl", False),
    ]
    boundary_results = []
    target = set(tags["3.15.0"])
    for filename, expected in boundaries:
        actual = bool(study.parse_wheel_filename(filename)[-1] & target)
        boundary_results.append({"filename": filename, "expected_admission": expected,
                                 "actual_admission": actual})
        if actual != expected:
            raise RuntimeError("Public wheel tag boundary disagrees")
    after = study.protected()
    if before != after or before != initial["protected_after"]:
        raise RuntimeError("Protected inputs changed")
    result = {"status": "DOING", "completed_at_utc": datetime.now(timezone.utc).isoformat(),
        "original_failures_preserved": initial["failures"], "offline_document_recovery": recovery,
        "package_replay_equal": True, "package_count": len(replay),
        "original_trial_files_still_match_registry": initial["original_registry_hash_matches"],
        "frozen_summary": initial["summary"], "latest_blocker_observations": current,
        "public_tag_boundary_observations": boundary_results,
        "abi3t_limit": "Packaging26.3 GIL-enabled cp315 tags omit abi3t despite CPython3.15 documenting a fallback. The frozen cryptography release has abi3t files and also matching abi3 Windows files; neither missing-wheel package has abi3t files. Thus this omission does not change the two observed blockers. Free-threaded builds remain unqualified.",
        "protected_before": before, "protected_after": after, "protected_unchanged": True,
        "claim_scope": "Metadata admission for frozen48 and two current package observations only; not new resolver closure, runtime execution, latest compatible selection, full notices/provenance or adoption.",
        "next_action": "Check current stable package alternatives and changed-marker closure before proposing any separately authorized isolated runtime qualification. Do not bypass latest-compatible policy by assuming old runtime selection or silently removing Uvicorn standard extras."}
    study.save("replay-and-current-observations.json", result)
    print(json.dumps({"package_replay_equal": True, "original_hash_matches": initial["original_registry_hash_matches"],
        "latest": [{"name": c["observation"]["name"], "version": c["observation"]["version"],
                    "cp315_admitted": c["observation"]["targets"]["3.15.0"]["admitted"]} for c in current],
        "protected_unchanged": True}, indent=2))


if __name__ == "__main__":
    main()

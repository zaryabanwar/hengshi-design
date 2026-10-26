"""Capture bounded public primary sources; no accounts or application effects."""
import gzip
import hashlib
import json
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

import fitz

HERE = Path(__file__).resolve().parent
sources = [
    ("edpb-access", "https://www.edpb.europa.eu/system/files/documents/2023-04/edpb_guidelines_202201_data_subject_rights_access_v2_en.pdf"),
    ("gdpr", "https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng"),
    ("commission-rights", "https://commission.europa.eu/law/law-topic/data-protection/information-business-and-organisations/dealing-requests-individuals_en"),
]
observations = []
for name, url in sources:
    target = HERE / (name + ".raw.gz")
    if target.exists():
        raise SystemExit(f"Existing source snapshot: {target.name}")
    request = urllib.request.Request(url, headers={"User-Agent": "Hengshi-Phase1-public-source-research"})
    with urllib.request.urlopen(request, timeout=35) as response:
        raw = response.read(4 * 1024 * 1024 + 1)
        if len(raw) > 4 * 1024 * 1024:
            raise SystemExit("Public source exceeded 4 MiB cap")
        record = {"url": url, "final_url": response.url, "status": response.status,
                  "observed_utc": datetime.now(timezone.utc).isoformat(),
                  "content_type": response.headers.get("Content-Type"), "bytes": len(raw),
                  "raw_sha256": hashlib.sha256(raw).hexdigest(), "snapshot": target.name}
    target.write_bytes(gzip.compress(raw, mtime=0))
    record["snapshot_sha256"] = hashlib.sha256(target.read_bytes()).hexdigest()
    if name == "edpb-access":
        document = fitz.open(stream=raw, filetype="pdf")
        # Human-visible source page numbers = indices + 1.
        indices = [22, 23, 24, 25, 26, 27, 28, 49, 50, 51]
        excerpts = "\n".join(f"\n--- PDF page {i+1} ---\n" + document[i].get_text() for i in indices)
        (HERE / "edpb-selected-pages.txt").write_bytes(excerpts.encode("utf-8"))
        record["pdf_pages"] = len(document)
        record["extracted_pdf_pages"] = [i + 1 for i in indices]
        document.close()
    observations.append(record)
    print(json.dumps({"source": name, "http_status": record["status"], "bytes": len(raw)}), flush=True)
(HERE / "primary-sources.json").write_bytes((json.dumps(observations, indent=2) + "\n").encode())

from pathlib import Path
from urllib.request import Request, urlopen
from datetime import datetime, timezone
import gzip, hashlib, json
import fitz

base = Path(__file__).resolve().parent
assert not (base / 'primary-sources.json').exists(), 'Preserve the existing capture.'
sources = [
    ('edpb-breach', 'https://www.edpb.europa.eu/system/files/2023-04/edpb_guidelines_202209_personal_data_breach_notification_v2.0_en.pdf', list(range(9, 27))),
    ('nist-incident', 'https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-61r3.pdf', None),
]
records = []
for name, url, pages in sources:
    with urlopen(Request(url, headers={'User-Agent': 'Hengshi-public-source-research/1.0'}), timeout=40) as response:
        raw = response.read(5 * 1024 * 1024 + 1)
        assert response.status == 200 and raw.startswith(b'%PDF') and len(raw) <= 5 * 1024 * 1024
        record = {'url': url, 'final_url': response.url, 'status': response.status,
                  'observed_utc': datetime.now(timezone.utc).isoformat(), 'bytes': len(raw),
                  'raw_sha256': hashlib.sha256(raw).hexdigest(), 'snapshot': name + '.raw.gz'}
    compressed = gzip.compress(raw, mtime=0)
    (base / record['snapshot']).write_bytes(compressed)
    record['snapshot_sha256'] = hashlib.sha256(compressed).hexdigest()
    doc = fitz.open(stream=raw, filetype='pdf')
    selected = pages if pages is not None else [i for i in range(len(doc)) if any(term in doc[i].get_text() for term in ('RS.MA', 'RS.AN', 'RS.CO', 'RS.MI', 'RC.RP', 'RC.CO'))]
    record['pdf_pages'] = len(doc)
    record['extracted_zero_based_pages'] = selected
    text = '\n'.join(f'=== PDF page {i + 1} ===\n' + doc[i].get_text() for i in selected)
    (base / (name + '-selected-pages.txt')).write_text(text, encoding='utf-8')
    records.append(record)
(base / 'primary-sources.json').write_text(json.dumps(records, indent=2) + '\n', encoding='utf-8')
print(json.dumps([{k: v for k, v in row.items() if k not in ('final_url', 'extracted_zero_based_pages')} for row in records]))

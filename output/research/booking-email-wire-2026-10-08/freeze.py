from pathlib import Path
import hashlib
import importlib.metadata
import json
import re
import sys
from urllib.parse import urlsplit

root=Path.cwd(); out=root/'output/research/booking-email-wire-2026-10-08'
cat=root/'docs/phase-1-architecture/contracts/INTERFACE_CATALOG.md'; raw=cat.read_bytes()
pre=(out/'INTERFACE_CATALOG.before.md').read_bytes()
assert hashlib.sha256(pre).hexdigest()=='39404b9cc2e25d2fc31b3a226078d001a8084e4f204c239c873bf054d4204ea5'
assert raw.startswith(pre)
for target in re.findall(r'\]\(([^)]+)\)',raw[len(pre):].decode('utf-8')):
    if not target.startswith('https://'):
        assert (cat.parent/target.split('#')[0]).resolve().is_file(),target
checks=dict(scope='Schema/validator boundary only; no application or deployed dependency selection',
    command='C:/Python314/python.exe -B -m unittest scripts.validation.test_booking_email_schema scripts.validation.test_booking_qualification_schema scripts.validation.test_process_value_schema scripts.validation.test_booking_creation_request_schema scripts.validation.test_chat_creation_request_schema',
    observation='Producer command output chunk f14243',result='PASS',methods=52,new_email_methods=15,
    initial_pre_freeze_defect='Wrong local $defs/revision reference corrected to existing $defs/positive_revision; uppercase-negative fixture now contains alphabetic hex.',
    python=sys.version,packages={n:importlib.metadata.version(n) for n in ['jsonschema','referencing','rfc3339-validator']},
    format_assertions=['uuid','date-time'],registry_retrieval='Unregistered schemas refused; local closure only',
    source='https://json-schema.org/draft/2020-12/json-schema-validation#section-7',checked='2026-10-08',
    limits=['No raw-parser/HTTP/auth/clocks/counters/secret-store/mail/current-projection runtime proof','No integrated acceptance or full production graph selection'])
check=out/'schema-checks.json'; assert not check.exists();check.write_text(json.dumps(checks,indent=2)+'\n',encoding='utf-8')
old=json.loads((root/'output/research/booking-email-ownership-2026-10-08/review-inputs.json').read_bytes())
paths=[r['path'] for r in old['inputs']]
paths += ['output/research/booking-email-ownership-2026-10-08/final-independent-review.json',
          'scripts/validation/test_booking_email_schema.py',
          'scripts/validation/test_booking_qualification_schema.py',
          'scripts/validation/test_process_value_schema.py',
          'scripts/validation/test_booking_creation_request_schema.py',
          'scripts/validation/test_chat_creation_request_schema.py',
          str(check.relative_to(root)).replace('\\','/')]
seen=set()
def refs(value):
    if isinstance(value,dict):
        for k,v in value.items():
            if k=='$ref': yield v
            else: yield from refs(v)
    elif isinstance(value,list):
        for v in value: yield from refs(v)
def schema_closure(path):
    if path in seen: return
    seen.add(path); paths.append(str(path.relative_to(root)).replace('\\','/'))
    for ref in refs(json.loads(path.read_text(encoding='utf-8'))):
        parsed=urlsplit(ref)
        assert not parsed.scheme and not parsed.netloc,ref
        if parsed.path:
            target=(path.parent/parsed.path).resolve()
            assert target.is_relative_to(cat.parent.resolve()) and target.is_file(),ref
            schema_closure(target)
schema_closure((cat.parent/'booking-email.schema.json').resolve())
paths=list(dict.fromkeys(paths));snaps=out/'snapshots';snaps.mkdir(exist_ok=False);rows=[]
for i,name in enumerate(paths):
    p=root/name;data=p.read_bytes();s=snaps/f'{i:02d}-{p.name}';s.write_bytes(data)
    rows.append(dict(path=name,snapshot=str(s.relative_to(root)).replace('\\','/'),bytes=len(data),sha256=hashlib.sha256(data).hexdigest()))
m=dict(scope='Proposed IF-BOOK-03/04 directional wire/current-controls/HTTP and shared work profile; no runtime or integrated acceptance',inputs=rows,
       prefix=dict(path=str((out/'INTERFACE_CATALOG.before.md').relative_to(root)).replace('\\','/'),bytes=len(pre),sha256=hashlib.sha256(pre).hexdigest()))
data=(json.dumps(m,indent=2)+'\n').encode();dest=out/'review-inputs.json';assert not dest.exists();dest.write_bytes(data)
print(json.dumps(dict(inputs=len(rows),schema_modules=len(seen),manifest_sha256=hashlib.sha256(data).hexdigest(),catalogue_sha256=hashlib.sha256(raw).hexdigest(),schema_sha256=hashlib.sha256((cat.parent/'booking-email.schema.json').read_bytes()).hexdigest(),prefix_bytes=len(pre))))

"""Definition-only shared admission profile; preserve all predecessor bytes."""
from pathlib import Path
import hashlib,json,urllib.request,subprocess
ROOT=Path(__file__).resolve().parents[3]
OUT=Path(__file__).resolve().parent
if (OUT/'DATA_CONTRACT.md.before').exists():raise SystemExit('Already produced; inspect rather than rerun.')
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
oldguards=json.loads((ROOT/'output/playwright/world-walking-walkthrough-2026-10-06/protected-before.json').read_text(encoding='utf-8'))
guards=[{'path':x['path'],'sha256':digest(ROOT/x['path'])} for x in oldguards]
(OUT/'protected-before.json').write_text(json.dumps(guards,indent=2)+'\n',encoding='utf-8')
sources=[]
for name,url in [('python-json.html','https://docs.python.org/3.14/library/json.html'),('python-decimal.html','https://docs.python.org/3.14/library/decimal.html'),('rfc8259.html','https://www.rfc-editor.org/rfc/rfc8259.html'),('fastapi-request.html','https://fastapi.tiangolo.com/reference/request/'),('fastapi-errors.html','https://fastapi.tiangolo.com/tutorial/handling-errors/')]:
    request=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 (compatible; HengshiDefinitionResearch/1.0)'})
    with urllib.request.urlopen(request,timeout=20) as r:
        data=r.read();status=r.status; final=r.url
    (OUT/name).write_bytes(data)
    sources.append({'requested_url':url,'final_url':final,'http_status':status,'path':name,'sha256':digest(OUT/name)})
(OUT/'source-observations.json').write_text(json.dumps(sources,indent=2)+'\n',encoding='utf-8')
data_add='''
## Private browser JSON admission profile proposal — 2026-10-06

Status: DOING. This refines the existing raw-representation boundary, not its
schemas or any endpoint. Apply the proposed common decoder to anonymous visitor
JSON HTTP mutations in IF-CHAT-01/02 and IF-BOOK-01–09 where a JSON body is defined,
and IF-STAFF-09 availability commands. Existing route-specific stricter limits
win. This is not a global replacement for publication/compiler messages, content
authoring, public release reads, WebSocket frames or provider callbacks; those
need their own bound profiles. No new parser dependency or production selection.

### Finite starting limits

All new numbers are unmeasured engineering proposals requiring integrated
acceptance and actual ingress/resource qualification. They are not RFC limits.

| Item | Proposed ceiling / meaning |
|---|---|
| Raw JSON body | 16,384 received bytes across all chunks; use the smaller route cap, including IF-BOOK-01's 1,024 bytes. No accepted compression or alternate encoding bypass. |
| Decoded container nesting | 16 object/array levels; root container is level 1. Scalars do not add a container level. |
| Object / array breadth | 64 members per object; 256 elements per array. A member name and its value are distinct counted nodes. |
| Total decoded nodes | 4,096, including root, every container, member name and scalar; count each once. |
| Decoded string / member name | 8,192 / 96 Unicode scalar values, respectively; field schemas may be stricter. These do not replace the received-byte cap. |
| Numeric spelling | At most 128 ASCII characters including sign, decimal point and exponent; explicit exponent at most four digits excluding sign and absolute value at most 1,024. Field value/range/type rules still apply. |

A route must bind its method/media/origin/proof, receive deadline, admitted work
and response/error profile before implementation. Unbound routes stay unavailable;
the common body limit supplies neither an auth policy nor a queue/concurrency
budget. IF-BOOK-01 retains its existing five-second receive/finite-work proposal,
JSON media and response/status rules unchanged. This profile does not authorize
a larger route body or add a JSON body to a bodyless action.

### Standard-library-first decoding recommendation

1. Do the applicable cheap transport/origin and work-admission checks first.
   Count actual chunks through the framework's request stream before copying or
   concatenating an over-limit body; reject an oversized declared length early
   but never trust that length instead of actual bytes. Empty/disconnected or
   incomplete framing is not an empty successful command. Keep the work permit
   until known cleanup. Upstream ASGI/proxy buffering can already allocate an
   oversized chunk; received-byte counting alone does not bound that allocation.
2. Decode accepted bytes explicitly as strict UTF-8 with no BOM. Do not pass raw
   bytes to a decoder that auto-detects UTF-16/32, silently replace invalid bytes,
   trim a BOM or normalize Unicode. Accept exactly one complete RFC 8259 value
   plus its permitted whitespace, never a parsed prefix or concatenated values.
   The route's closed schema decides its allowed root type.
3. Prefer Python `json.loads` with `strict=True`, an `object_pairs_hook` that
   rejects repeated **decoded** member names at every depth before dict collapse,
   and a rejecting `parse_constant`. Escaped spelling cannot evade duplicate
   detection; compare decoded names exactly, without case folding or Unicode
   normalization. Case/normalization variants remain separate names subject to
   the closed field schema. `strict=True` alone is not this contract.
4. Bound numeric token length/exponent before numeric construction. Recommend
   bounded `parse_int` and `parse_float` hooks, with exact finite `Decimal` for
   decimal/exponent spellings rather than immediate binary floating conversion.
   This preserves values such as 1e400 and 1e-400 long enough for field admission;
   it does not authorize them as a particular field value. Reject NaN/Infinity
   extensions, unbounded tokens and conversion failures. Keep native integer and
   recursion protections; do not change process-global limits to accept input.
5. Before schema/model dispatch, walk the parsed tree with bounded work, enforcing
   container/breadth/node/string ceilings and Unicode scalar validity in keys
   and values. A valid escaped surrogate pair may decode to its scalar; reject
   isolated surrogates. Escaped control characters permitted by JSON still need
   each text field's rule; do not invent global trimming or silently repair them.
   Stop counting on first excess rather than building another full tree copy.
6. Bind exact field representations before model coercion. A mathematically
   integral decimal can become an integer only when that field permits JSON
   integer semantics and its exact admitted range; `true` is never integer 1.
   A contract requiring a string stays a string. Reject a required conversion
   that overflows, underflows or changes the admitted value; do not round it to
   another revision, identifier, amount or operation meaning. No arbitrary
   `default=str`, float round-trip or serializer normalization defines identity.

The tree ceilings are **accepted-document bounds**, not claims that the native
decoder allocates only that many nodes or descends only sixteen levels. Hooks
may run after sub-values have been built. Account bounded raw bytes, decoding,
temporary containers and rejection cleanup in the route's admission envelope;
native recursion failures deny input. Prove actual peak allocation/CPU/cleanup
under malformed near-cap bodies before acceptance. If this candidate cannot fit
the qualified envelope, do not approve it; assess a bounded supported parser
through the complete stable compatibility graph rather than removing safeguards.

### Framework integration, effects and errors

Use framework streaming and typed validation, with the raw gate before any
automatic body parser, Body-dependent dependency or handler capable of effects.
An explicit Request boundary followed by validation of the admitted representation
is a candidate integration pattern; exact route/dependency/model wiring remains
to be verified against installed source. Calling the normal handler first and
catching its validation error cannot restore duplicate keys or undo effects.
OpenAPI declarations likewise do not enforce this admission boundary.

Only an accepted representation reaches closed field, current proof/CSRF,
source/consent/revision and immutable-operation checks. Parsing is neither
authorization nor permission to persist, call AI/provider code or return private
existence. Raw bodies and derived parser/model exception input are not recorded
in logs, traces, queues or response detail. The body has its original privacy
class during ephemeral handling; safe counters never include submitted values.

Use the applicable route's fixed safe denial, not raw framework exceptions or
new guessed universal status codes. Malformed current input cannot undo or
definitively describe an earlier uncertain operation. Capacity/internal failures
remain distinct from confirmed input rejection. Never claim another session or
lineage does not exist, or say an earlier effect failed because parsing now fails.

For output, project only the route's closed permitted response, enforce its
finite size and use JSON serialization with nonfinite output disabled. Decimal
or another unsupported internal value must reach only an explicit validated
field representation, never a generic string fallback. Serialization failure
cannot turn an admitted operation into an asserted no-effect result. JWT, cookie,
CSRF, staff identity, consent, data retention and idempotency policies are unchanged.

### Primary support and remaining proof

Checked 2026-10-06: [RFC 8259](https://www.rfc-editor.org/rfc/rfc8259.html)
defines JSON grammar, Unicode/interoperability and permitted parser limits.
[Python JSON](https://docs.python.org/3.14/library/json.html) documents duplicate
collapse, numeric extensions, hooks, encoding detection and untrusted-input risk;
[Decimal](https://docs.python.org/3.14/library/decimal.html) preserves numeric text
without immediate binary rounding. The current rolling 3.14 docs identify a later
minor than the existing 3.14.5 research runtime: they do not select an upgrade.
Context7 `/websites/fastapi_tiangolo`, [Request](https://fastapi.tiangolo.com/reference/request/)
and [error handling](https://fastapi.tiangolo.com/tutorial/handling-errors/)
support streaming/model integration and show access to raw invalid input; copying
that tutorial body/error echo would violate this private contract.

This proposal adds no compliant decoder or route. Prior installed-framework
observations remain narrow evidence of defaults, not enforcement. After approved
planning, actual HTTP-boundary tests must cover nested/escaped duplicate keys,
valid international text and surrogate pairs, isolated surrogates, BOM/UTF-16/32,
trailing values, numeric overflow/underflow/integral equivalence and boolean
denial, every cap boundary, slow/oversized chunks and permit cleanup, redacted
errors and no business dispatch on rejection. Qualified ingress limits, actual
model/number binding, compatibility, privacy and integrated/founder approval remain.
'''
catalog_add='''
### Shared private browser decoding profile proposal — 2026-10-06

The [private browser JSON profile](DATA_CONTRACT.md#private-browser-json-admission-profile-proposal--2026-10-06)
refines raw admission for the explicitly listed existing visitor HTTP mutations
and availability commands. It proposes finite accepted-document/body/token
ceilings, strict UTF-8, recursive decoded-name duplicate rejection, exact numeric
admission, a standard-library-first candidate and redacted errors before effects.
It preserves stricter route limits and does not apply to public/worker payloads,
authoring, WebSocket events or callback ingress. No route, field, proof, grant,
consent, retention or response variant changes; independent review, exact ingress/
model wiring and resource/actual HTTP evidence remain required before implementation.
'''
for name,addition in [('DATA_CONTRACT.md',data_add),('INTERFACE_CATALOG.md',catalog_add)]:
    p=ROOT/'docs/phase-1-architecture/contracts'/name
    before=p.read_bytes()
    (OUT/(name+'.before')).write_bytes(before)
    p.write_bytes(before+addition.replace('\n','\r\n').encode('utf-8'))
    (OUT/(name+'.reviewed')).write_bytes(p.read_bytes())
    assert p.read_bytes().startswith(before)
assert all(digest(ROOT/x['path'])==x['sha256'] for x in guards)
result=subprocess.run(['git','-c','core.autocrlf=false','-c','core.whitespace=blank-at-eol,blank-at-eof,space-before-tab,cr-at-eol','diff','--check','--','docs/phase-1-architecture/contracts/DATA_CONTRACT.md','docs/phase-1-architecture/contracts/INTERFACE_CATALOG.md'],cwd=ROOT,capture_output=True)
assert result.returncode==0,result.stdout+result.stderr
files=[p for p in OUT.iterdir() if p.is_file() and p.name!='review-inputs.json']
context=['AGENTS.md','.specify/memory/constitution.md','PROJECT.md','PROJECT_STATE.yaml','TASKS.md','DECISIONS.md','docs/software-definition/README.md','docs/phase-1-architecture/contracts/DATA_CONTRACT.md','docs/phase-1-architecture/contracts/INTERFACE_CATALOG.md','docs/phase-1-architecture/contracts/PRIVATE_PROCESS_PROOF.md','docs/phase-1-architecture/contracts/AVAILABILITY_WRITE_HTTP.md','output/research/raw-json-admission-2026-10-06/observations.json']
inputs=[{'path':p.relative_to(ROOT).as_posix(),'sha256':digest(p)} for p in files]+[{'path':p,'sha256':digest(ROOT/p)} for p in context]
packet={'scope':'Only additive private-browser decoder profile and catalogue reference. No new implementation or parser tests; earlier requirements/probes are context, not reviewed anew.','inputs':inputs,'protected_guards':78,'guard_match':True,'whitespace_pass':True}
(OUT/'review-inputs.json').write_text(json.dumps(packet,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'inputs':len(inputs),'packet_sha256':digest(OUT/'review-inputs.json'),'guard_match':True,'whitespace_pass':True}))

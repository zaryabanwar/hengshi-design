"""Record closed request proposal and exercise actual local validator boundary."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import os
import subprocess

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
PROOF = ROOT / 'docs/phase-1-architecture/contracts/PRIVATE_PROCESS_PROOF.md'

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def save(name, value):
    with (OUT / name).open('x', encoding='utf-8') as file:
        json.dump(value, file, indent=2)
        file.write('\n')

def main():
    if (OUT / 'PRIVATE_PROCESS_PROOF.md.before').exists():
        raise RuntimeError('Refusing overwrite')
    prior_guards = json.loads((ROOT / 'output/research/frontend-supply-chain-2026-10-06/protected-before.json').read_text(encoding='utf-8'))
    if any(sha(ROOT / row['path']) != row['sha256'] for row in prior_guards):
        raise RuntimeError('Unexpected protected change')
    (OUT / 'PRIVATE_PROCESS_PROOF.md.before').write_bytes(PROOF.read_bytes())
    text = '''
## Booking creation request encoding proposal — 2026-10-06

PROPOSED encoding refinement for existing IF-BOOK-01, POST
`/api/v1/bookings/lineages`, under the directional creation/admission obligations
above. The [closed request schema](booking-creation-request.schema.json) defines
only the client body. It adds no endpoint, form, account, issued proof, storage,
calendar call or operational grant. Earlier reviewed proposal bytes remain
preserved; this refinement requires its own independent and founder acceptance.

| Phase | Exact body | Continuing authority checks |
|---|---|---|
| Bootstrap | `{ "phase": "bootstrap" }` | Explicit user initiation; exact trusted browser Origin and approved raw media/work profile. May allocate only the bounded empty ephemeral provisional context and its independently issued proof. No operation, personal/context/consent/qualification data or effects in this body. |
| Create | `{ "phase": "create", "provisional_id": "<UUID>", "operation_id": "<UUIDv4>" }` | Current selected provisional cookie and separate CSRF transport; server-allocated booking-family context, permitted empty-lineage purpose and atomic single promotion/immutable-operation reconciliation. No qualification, email, chat context, consent, slot or provider action. |

Every body is a closed object. Missing fields, unknown phases/properties, wrong
types and noncanonical UUID text reject before promotion. Do not normalize case,
trim or coerce references. Strict raw decoding still rejects duplicate members
and malformed input before schema validation; validation of a parsed object
cannot recover discarded duplicates or prove Origin/proof/CSRF authority. Keep
the existing raw JSON admission and validation-error confidentiality boundaries.
This body is not the credential transport: bearer and CSRF values are forbidden
in JSON and remain under their separately reviewed cookie/header mechanisms.

`provisional_id` adopts the common UUID representation for this one direction;
the server must resolve an allocated, current booking-family provisional context
under the exact selected proof. UUID shape, including syntactically valid Nil/Max
or a reference whose text matches the operation, proves none of those facts.
Do not rewrite other schemas or replace public release/wing identifiers.

Recommend a fresh caller-generated UUIDv4 `operation_id` from a CSPRNG for each
deliberate promotion intent, generated once and retained for authorized retry/
reconciliation. The schema narrows the common UUID shape to version 4 and its
standard variant; it cannot prove the generator's entropy or uniqueness. In a
supported secure browser, the standard `crypto.randomUUID()` is a candidate
generator. Do not substitute Math.random, timestamps, email or a device fingerprint
if unavailable; preserve truthful recovery until the authorized generator works.
This recommendation selects no package, browser matrix or database primary key.

Operation identity remains scoped to the selected provisional context and process
family. The same text in another context provides no result access; collision or
changed meaning conflicts under current authority. Proof/CSRF rotation is not new
intent, a new operation cannot evade pending promotion, and retries cannot mint
a second lineage or repeat effects. Reuse does not renew proof or retention.
Bounded operation retention/expiry, physical uniqueness/fencing, current-response
disclosure and lost-cookie recovery remain the governing lifecycle obligations.

The corresponding server bootstrap/admitted/pending/denied response encodings,
cookie/CSRF profile, expiry/work limits and HTTP error/status mappings remain
explicit inputs before implementation. Chat creation keeps its distinct release/
wing and versioned consent obligations; this booking schema cannot validate it.
Qualification and purpose-specific consent remain at IF-BOOK-02. Neither bootstrap
nor create body grants durable personal storage or verifies email/booking success.

Primary guidance checked 2026-10-06: [RFC9562 UUIDv4](https://www.rfc-editor.org/rfc/rfc9562.html#section-5.4)
defines its random layout; [MDN randomUUID](https://developer.mozilla.org/en-US/docs/Web/API/Crypto/randomUUID)
documents the cryptographically secure browser generator and secure-context
requirement. Context7 `/websites/fastapi_tiangolo` was checked for request/error
handling; body-echo tutorial examples are not adopted. No framework version or
tutorial substitutes for strict decoding, confidential errors or current admission.

Focused synthetic tests exercise the actual schema/registered reference/format
validator boundary only. They prove no cryptography, browser, HTTP status/header,
cookie/CSRF, permission, transaction/concurrency, retention or operational behavior.
No documentation wording assertions or duplicate reference state machine are added.
Full wire/lifecycle definition, stable graph, independent review and integrated
Phase 1 founder approval remain required before application implementation.
'''
    with PROOF.open('ab') as file:
        file.write(text.replace('\n', '\r\n').encode('utf-8'))
    (OUT / 'PRIVATE_PROCESS_PROOF.md.reviewed').write_bytes(PROOF.read_bytes())
    env = {key: os.environ[key] for key in ('SystemRoot', 'WINDIR', 'COMSPEC', 'TEMP', 'TMP') if key in os.environ}
    env['PATH'] = 'C:/Python314' + os.pathsep + str(Path(env['SystemRoot']) / 'System32')
    env['PYTHONUTF8'] = '1'
    env['PYTHONDONTWRITEBYTECODE'] = '1'
    command = ['C:/Python314/python.exe', '-B', '-m', 'unittest',
       'scripts.validation.test_booking_creation_request_schema',
       'scripts.validation.test_process_value_schema', '-v']
    started = datetime.now(timezone.utc).isoformat()
    process = subprocess.run(command, cwd=ROOT, env=env, capture_output=True)
    (OUT / 'validator.stdout.txt').write_bytes(process.stdout)
    (OUT / 'validator.stderr.txt').write_bytes(process.stderr)
    changed = [row['path'] for row in prior_guards if sha(ROOT / row['path']) != row['sha256']]
    save('validator-receipt.json', {'started_at_utc': started,
       'ended_at_utc': datetime.now(timezone.utc).isoformat(), 'command': command,
       'exit_code': process.returncode, 'protected_inputs': len(prior_guards),
       'changed_protected_inputs': changed,
       'scope': 'Closed proposed client-request and common-value validator boundary only; no application admission/security proof.'})
    if process.returncode or changed:
        raise RuntimeError('Validator or guard failed; preserve initial evidence')
    paths = [PROOF, ROOT / 'docs/phase-1-architecture/contracts/booking-creation-request.schema.json',
       ROOT / 'docs/phase-1-architecture/contracts/process-value.schema.json',
       ROOT / 'docs/phase-1-architecture/contracts/publication-preparation.schema.json',
       ROOT / 'docs/phase-1-architecture/contracts/publication-manifest.schema.json',
       ROOT / 'docs/phase-1-architecture/contracts/DATA_CONTRACT.md',
       ROOT / 'docs/phase-1-architecture/contracts/INTERFACE_CATALOG.md',
       ROOT / 'docs/phase-1-architecture/contracts/interface-catalog.csv',
       ROOT / 'docs/phase-1-architecture/contracts/process-fields.csv',
       ROOT / 'docs/phase-1-architecture/contracts/SECURITY_PRIVACY_CONTRACT.md',
       ROOT / 'specs/001-platform-security-hardening/spec.md',
       ROOT / 'specs/004-design-services-content/spec.md',
       ROOT / 'scripts/validation/test_booking_creation_request_schema.py',
       ROOT / 'scripts/validation/test_process_value_schema.py',
       ROOT / 'AGENTS.md', ROOT / '.specify/memory/constitution.md', ROOT / 'DECISIONS.md', ROOT / 'TASKS.md']
    paths.extend(OUT.iterdir())
    paths.extend(ROOT / row['path'] for row in prior_guards)
    packet = [{'path': path.relative_to(ROOT).as_posix(), 'sha256': sha(path)}
              for path in sorted(set(paths), key=lambda path: path.as_posix()) if path.is_file()]
    save('review-inputs.json', packet)
    print(f'15 focused validator tests pass; {len(packet)} review inputs SHA256 {sha(OUT / "review-inputs.json")}')

if __name__ == '__main__':
    main()

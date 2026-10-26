"""Add an unselected, researched client recommendation to its controlling source."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
backend = ROOT / "docs/phase-1-compatibility/backend-evidence-2026-10-04.md"
mapping = ROOT / "docs/software-definition/04-reconciliation-map.md"
before = HERE / "before"
before.mkdir(exist_ok=True)
for path in (backend, mapping):
    (before / path.name).write_bytes(path.read_bytes())

appendix = '''
## Maintained staff identity client comparison — 2026-10-08

Status: DOING. Recommend evaluating Authlib's async Starlette/HTTPX OIDC integration
as the leading staff sign-in candidate; MSAL plus a separately qualified verifier
is an alternative. This selects neither package nor adapter and changes no accepted
identity, session, API, provider or role boundary. The existing
[staff mediation proposal](../phase-1-architecture/contracts/SECURITY_PRIVACY_CONTRACT.md#staff-sign-in-mediation-proposal)
requires a maintained client, server-held state/nonce/PKCE credentials, token
verification and current Hengshi eligibility; the library does not own grants.
The [dated registry observations](../../output/research/staff-identity-client-options-2026-10-08/registry-observations.json)
and [immutable source associations](../../output/research/staff-identity-client-options-2026-10-08/primary-sources.json)
preserve exact inputs. Tags resolve to recorded commits, not proven wheel builds.
Both release objects are non-draft/non-prerelease; both registry classifiers say
Production/Stable. This is not full support, licence, advisory or runtime evidence.

| Candidate observation | Fit and extra work |
|---|---|
| MSAL1.39.0; Python>=3.9; requests<3, PyJWT[crypto]<3 and cryptography<51 | Microsoft's confidential client supports code-flow state, PKCE and nonce protection. Its current token acquisition decodes ID-token claims without signature/issuer/audience/expiry validation; the legacy decoder is deprecated and is no substitute. Hengshi would need a separately qualified maintained verifier. The default added offline-access scope needs explicit exclusion; no Graph/broker or durable provider-token cache is implied. Its default Requests path also needs bounded blocking-work isolation in FastAPI. |
| Authlib1.8.0; Python>=3.10; cryptography>=45.0.1 and joserfc>=1.6.1 | Native async framework integration uses the retained HTTPX family, with documented S256 configuration and an ID-token signature/claims validation path. An async server cache can hold temporary flow data while the browser session retains a correlation marker. This avoids copying provider secrets into the signed browser session, but does not establish atomic consumption, policy compliance or runtime compatibility. |

These ranges are registry declarations, not complete lower bounds or resolved
graphs; the frozen registry contains every exact Requires-Dist clause. Neither
candidate is installed, resolved together with the complete graph or included in
the separately prepared43-package native trial. Adding an adapter later requires
its own full coupled evaluation, qualification and integrated acceptance.

The recommendation follows the existing requirement to use a maintained client
and verifier, rather than hand-building OAuth. Research used Context7 MSAL and
Authlib identifiers, [Microsoft's acquisition guidance](https://learn.microsoft.com/en-us/entra/msal/python/getting-started/acquiring-tokens),
[Authlib's async framework guidance](https://docs.authlib.org/en/stable/oauth2/client/web/starlette.html)
and its [S256 configuration](https://docs.authlib.org/en/stable/oauth2/client/web/index.html#oauth-2-0-code-challenge).
The version-pinned source exposes defaults that illustrative examples omit:

- Authlib's cache path requires a browser-session marker. Its cache get/delete
  are separate calls; they do not prove the required one-time, expiring transaction
  claim under concurrent callbacks. The adapter must provide that guarantee.
- Without a server cache, the framework stores temporary flow data in the session.
  A signed cookie is readable; do not use that path to carry nonce/verifier or
  provider tokens. Do not copy the example's browser-session ID-token storage.
- Automatic ID-token parsing is conditional on both ID-token and stored nonce
  presence. Require the expected token/nonce explicitly before any staff grant.
  The generic parser permits `nonce_supported=false` to disable its nonce check;
  Hengshi must retain its mandatory nonce requirement and reject that bypass.
- Algorithms are taken from discovery metadata (default RS256), expiry leeway
  defaults to120seconds, and custom claim options can replace the default issuer
  options. None is an approved Hengshi policy. Configure and qualify explicit
  permitted issuer/tenant, audience, algorithms, time bounds and nonce checks
  without losing any guard when options change.
- Discovery/JWKS refresh needs the existing origin, bounded fetch/work and
  key-rotation controls. Local session issuance/current role checks and Hengshi
  logout remain owned by the backend, independently of provider logout.

Required later synthetic qualification covers wrong issuer/audience/key/algorithm,
missing or bypassed nonce, expiry, swapped token kind, browser mismatch, concurrent
or expired transaction use, missing/rotated keys, bounded network failure and
unchanged local logout/eligibility. These are retained requirement oracles, not
executed tests. Exact graph, storage/transaction/transport bindings, account
registration, legal/security qualification and integrated/founder acceptance
remain held. Earlier receipts do not review this new comparison; independent
review is required before treating its source claims as settled.
'''
backend.write_bytes(backend.read_bytes() + appendix.encode())
raw = mapping.read_bytes()
old = b"Complete approved compatibility; D-068 defers deployment/cost/region planning. Dated prototype observations do not prove continuing service health."
new = b"DOING. The compatibility package remains unselected. Its controlling entry now distinguishes the reviewed43-package crypto study from the unselected maintained staff sign-in client comparison; native execution, full graph qualification and integrated acceptance remain held. D-068 defers deployment/cost/region planning. Dated prototype observations do not prove continuing service health."
assert raw.count(old) == 1
raw = raw.replace(old, new, 1)
lines = raw.splitlines(keepends=True)
indices = [i for i, line in enumerate(lines) if line.startswith(b"| 12. Compatibility graph |")]
assert len(indices) == 1
i = indices[0]
line = lines[i]
suffix = b" |\r\n" if line.endswith(b" |\r\n") else b" |\n"
assert line.endswith(suffix)
addition = b" The [43-package asymmetric JWT study](../phase-1-compatibility/backend-evidence-2026-10-04.md#asymmetric-jwt-dependency-closure-and-proposed-native-qualification--2026-10-08) now has independently replayed metadata and correction1 prospective disk-plan review; the native trial is unapproved/unexecuted. The [maintained identity-client comparison](../phase-1-compatibility/backend-evidence-2026-10-04.md#maintained-staff-identity-client-comparison--2026-10-08) recommends evaluating Authlib's async path, retaining MSAL with a separate verifier as an alternative. This new source comparison is unreviewed; neither client nor its graph is selected or included in the43-package trial."
lines[i] = line[:-len(suffix)] + addition + suffix
mapping.write_bytes(b"".join(lines))

packet = HERE / "review"
packet.mkdir(exist_ok=True)
paths = ["AGENTS.md", ".specify/memory/constitution.md", "PROJECT.md", "DECISIONS.md",
         "PROJECT_STATE.yaml", "TASKS.md", "docs/software-definition/README.md",
         "docs/phase-1-architecture/contracts/SECURITY_PRIVACY_CONTRACT.md",
         "specs/001-platform-security-hardening/spec.md",
         "docs/phase-1-compatibility/backend-evidence-2026-10-04.md",
         "docs/software-definition/04-reconciliation-map.md"]
paths += [p.relative_to(ROOT).as_posix() for p in HERE.rglob("*")
          if p.is_file() and "review" not in p.relative_to(HERE).parts]
inputs = []
for rel in dict.fromkeys(paths):
    source = ROOT / rel
    data = source.read_bytes()
    dest = packet / "inputs" / rel
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(data)
    inputs.append({"path": rel, "snapshot": dest.relative_to(ROOT).as_posix(),
                   "sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data)})
(packet / "review-inputs.json").write_bytes((json.dumps({
    "status": "DOING", "revision_cycle": 0,
    "scope": "Unselected identity client source comparison and scoped navigation additions only; no graph resolution or runtime qualification",
    "inputs": inputs
}, indent=2) + "\n").encode())
print(json.dumps({"inputs": len(inputs), "manifest_sha256": hashlib.sha256((packet / "review-inputs.json").read_bytes()).hexdigest()}))

# Staff sign-in mediation — independent v1 review

Date: 2026-10-06. Reviewer: `review_staff_signin_boundary_v1`, independent of
the producer. Verdict: **REVISE** — one P2 transport-definition ambiguity.
Task status: DOING; commits remain deferred. This is a bounded proposal-consistency
review, not application/security certification, founder acceptance, integrated
Phase 1 acceptance or implementation authorization.

## Assessed scope and frozen identities

Reviewed the additive `Staff sign-in mediation proposal` in
`SECURITY_PRIVACY_CONTRACT.md:119–212` and the eight nonblank reference lines in
`INTERFACE_CATALOG.md:19–26`. Independently removing only those insertions from
the current text reproduces each preserved predecessor exactly, including line
endings. Existing staff roles, action/object authorization, emergency accounts,
data/provider/privacy and browser-resource boundaries are unchanged.

The [21-input manifest](../../../../output/research/staff-signin-boundary-2026-10-06/review-inputs.json)
has SHA-256 `ee7954d8570242dcf3bcd5c6e0f57c7b651f9781ec748413e2dc8dc557151a94`.
All 21 entries were independently recomputed before assessment and again after
writing this receipt. The two preserved reviewed copies equal the canonical
producer files at the hashes below. The manifest is a byte-identity receipt,
not evidence of behavior or complete Phase 1 coverage.

| Frozen input | Independently verified SHA-256 |
|---|---|
| `SECURITY_PRIVACY_CONTRACT.md` and preserved reviewed copy | `8dfa5c2f10ecde0693eb1e15d4b598f168d20447ee383be58a1b4555ff151055` |
| `INTERFACE_CATALOG.md` and preserved reviewed copy | `05e0b5c850a6bd90cd9512deae3f05d40e99278790b2fa39265dc699bcc8a89a` |
| `SECURITY_PRIVACY_CONTRACT.before.md` | `74ab420b5bec9f0aad72f59178f4ea7c626bd14edfa9d4ba02f3aa1dd0a1a254` |
| `INTERFACE_CATALOG.before.md` | `10476ccaa776ea3903b341e97ec2c12aab519062431afcc1e04ec6216d69fcfb` |
| `source-receipt.json` | `d40190ccc3239af3095cad1ed5c78deb5aed65cef51dab3e5140ff1c3d87ee2b` |
| `unchanged-inputs.json` | `6d640499f07bcf7d3ecf8068735ce67409602c35c6aef7228ebf2f9add782aad` |
| `AGENTS.md` | `55405cb02a96d05f7f6d68e56a588d743f83877fb2691a5a9f2c736126adbcc5` |
| `.specify/memory/constitution.md` | `33ec0bb02b0d0d9a55d0971589bd19f7242f5d56da130f8f496bc1d31a8b5d23` |
| `PROJECT.md` | `a483bd2713fe420322772ab7fb07c848aaf103088697c05ab91f35d2e5ea1461` |
| `DECISIONS.md` | `1d53a14ac3347ebeefeeb728e03862b09de111b748cef4e48d5f4ca19141b6d8` |
| `PROJECT_STATE.yaml` | `f3708ae4a68b1d1bd79be16fdd56ca223a5273c4b654516c652dbc189fe491b3` |
| `TASKS.md` | `158e06c0d8cd67859c8b459b96dce3449cb4d16788d3c520e99d8823f72edcd3` |
| `specs/001-platform-security-hardening/spec.md` | `47704c411b72195a2a4f8b832b07b30d90b00673647afe50d8ac98b917939d99` |
| `DATA_CONTRACT.md` | `46acfea99e0d4db91fb84603699e577100fffa79ca34f242d658a41deab8fb33` |
| `data-classification.csv` | `4b163eec086cb46ca98fabf692632d1778ee116cb014cda179e5b4a2a5fd44c6` |
| Root `package.json` | `a07f9f12c83736625d621781a1b30c8430452ef7e698fa626902cf16cef7946b` |
| Root `package-lock.json` | `d2da4d7206344ba45645d7bafe4ec692bb738ea0c1c98c2680522688b5733908` |
| `apps/web/package.json` | `83e4178348ec081922dd3d53d00c51446b655091d056ec09dde52a2496b04e2a` |
| `apps/web/package-lock.json` | `35486fb012489de4c3b363198304a25f44a0396707db328190d7e056c06d416d` |
| `apps/api/requirements.txt` | `b99f98e119cb6653f38b19d1ee83cc7f33d92a699083645ca19369a8912e89bd` |
| Protected `nature-campus-layout.glb` | `e2161710dc0576ec62e3d096c60e32927e827aa59198a33361e729ec8a7b43c0` |

The fifteen unchanged guards match their supplied receipt. Package and model
hashes establish protected input identity only; no dependency, asset or runtime
conformance verdict follows. The software-definition README and accepted
SEC-001–SEC-005 at `01-product-requirements.md:260–264` were also read for context;
they are not additional producer change targets or frozen reviewed amendments.

## Actionable finding

**P2 — distinguish the required protected cookie from prohibited client storage.**
At `SECURITY_PRIVACY_CONTRACT.md:158–159`, the proposal includes the session JWT
in material that must remain out of browser storage. Yet `:150–151`, the unchanged
session boundary at `:110–117`, and accepted SEC-004 require a browser staff JWT
cookie. A browser stores that cookie and returns it in HTTP requests; HttpOnly
restricts script access rather than removing browser storage. This leaves the
later implementer with conflicting credential-transport instructions.
[RFC 6265 §§4.1.2, 4.1.2.6 and 4.2.2](https://www.rfc-editor.org/rfc/rfc6265.html)
supports this distinction.

Required correction: explicitly keep provider tokens, code/verifier and signing
material server-side; permit the Hengshi session JWT only in its required
Secure/HttpOnly/SameSite cookie transport, and prohibit its JavaScript-readable
storage, response-body/React disclosure, generated HTML and general logs. Retain
the existing unselected cookie names/mode/algorithm and exact CSRF gates. A
scoped textual correction and independent reinspection are sufficient for this
proposal finding; no application change or runtime test is required to resolve it.

## Independently verified evidence and otherwise coherent boundaries

On 2026-10-06 the reviewer independently queried Context7 at
`/websites/learn_microsoft_en-us_entra_identity-platform` for server-mediated
authorization code, PKCE, OIDC validation, identity claims, token kinds and
revocation. Context7 returned primary Microsoft guidance. The multi-page web-tool
request failed with a connection error; read-only direct HTTPS requests then
successfully inspected the official Microsoft and RFC pages below (HTTP 200).
Illustrative scopes, credentials, packages and defaults were not adopted.

- **Backend admission and browser binding (`:127–145`):** Microsoft's
  [authorization-code guidance](https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-auth-code-flow)
  covers server-based applications, recommends PKCE for confidential clients,
  specifies registered redirect matching and verifier redemption, and recommends
  supported authentication libraries. [RFC 9700 §2.1.1](https://www.rfc-editor.org/rfc/rfc9700.html#section-2.1.1)
  requires transaction/user-agent binding and supports S256. The proposal's
  separate unpredictable state/nonce/verifier, bound single-use transaction,
  fixed issuer and allowlisted local return are coherent. No client registration
  or callback method is selected. The protected correlation mechanism is held.
- **Identity and least privilege (`:146–168`):** the Microsoft
  [ID-token claim reference](https://learn.microsoft.com/en-us/entra/identity-platform/id-token-claims-reference)
  confirms immutable object/tenant semantics, the profile scope requirement for
  oid, mutable display/email fields and group-overage handling. Its guest guidance
  preserves tenant-specific identity. The
  [claims-validation guidance](https://learn.microsoft.com/en-us/entra/identity-platform/claims-validation)
  shows that a tenant/object pair alone is insufficient authorization. Explicit
  permitted principal mapping, held guest/membership policy and unchanged
  action/object/purpose/current-state grants are coherent. OIDC-only initial
  scopes create no mail/calendar/presence/directory/offline permission or MA-006
  entitlement; D-068 remains unchanged.
- **Token kinds and validation (`:140–161`):** Microsoft
  [ID-token validation](https://learn.microsoft.com/en-us/entra/identity-platform/id-tokens)
  separates sign-in identity from API authorization and requires confidential-client
  validation of signature, issuer, audience, time and nonce. Graph access tokens
  belong to their resource; they are not locally issued Hengshi credentials.
  [RFC 8725 §§3.1, 3.8–3.12](https://www.rfc-editor.org/rfc/rfc8725.html)
  supports algorithm/issuer/audience checks and mutually exclusive token-kind
  validation. No inferred admin/publication/private-operation or visitor-to-staff
  authority is introduced. The storage ambiguity above is the sole finding.
- **Callbacks and exposure (`:172–180`):**
  [RFC 9700 §§4.2–4.3 and 4.7](https://www.rfc-editor.org/rfc/rfc9700.html)
  covers referrer/history leakage and callback CSRF. The proposal distinguishes
  protocol transaction correlation from subsequent API CSRF, retains cookie/CSRF
  requirements, couples callback method with correlation-cookie behavior, and
  requires parameter removal plus cache/referrer/ingress-log/error redaction.
  Exact methods, header policy and proxy enforcement remain held.
- **Lifetime, revocation and recovery (`:182–205`):** unchanged SEC-004/005 still
  controls 30-minute idle/eight-hour absolute bounds, rotating cookies and
  idempotent authoritative local logout. Microsoft's
  [revoke-user-access guidance](https://learn.microsoft.com/en-us/entra/identity/users/users-revoke-access)
  explains that application-issued sessions need the application's revocation
  policy; Entra cannot directly revoke them. The proposal correctly rejects an
  immediate-provider-revocation inference from an old ID token, preserves current
  local eligibility checks, and holds exact freshness/revalidation/outage policy.
  Uncertain exchange, replay and lost acknowledgements require authoritative
  reconciliation or explicit fresh sign-in, with concurrent callback and late
  logout cases retained as future oracles. No automatic emergency activation or
  self-inferred grant follows. Physical single-use, reconciliation, race and
  revocation enforcement remains unproven and explicitly held.

## Held gates and limits

Exactly two dormant monitored bcrypt/local-MFA emergency accounts, role separation,
no visitor accounts, two deployables, protected prototype and immutable publication
boundaries remain intact. Exact tenant/client/account registration, guest/group
mapping, grants, MFA/activation/custody/recipients, callback/cookie/CSRF formats,
JWT keys/algorithms, transaction/rotation/replay/cache/time/work bounds, freshness
and outage/recovery controls need their applicable review and founder acceptance.
Staff/session/secret retention and legal mappings remain class-specific inputs;
no blanket 90-day staff policy or alias owner is invented.

A maintained client/verifier and complete latest-mutually-compatible stable graph,
approved staff UI/accessibility references, account/API entitlement and actual
synthetic-identity/browser/API/proxy/concurrency evidence remain held before
implementation. No library, package, version, account, permission, provider,
credential, route or external write is selected here. No prose tests or runtime
tests were run for this review. Source receipts and hashes prove input identity
and research scope, not application correctness, security, accessibility, release
readiness or complete Phase 1 acceptance. Founder/integrated acceptance and all
later implementation, Git, activation and deployment gates remain separate.

Only this independent review receipt was written by the reviewer. Resolve the
single P2 ambiguity, retain the prior exact-input verdict, and submit the bounded
correction for reinspection within the existing revision limit.

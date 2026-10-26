
## Preferred HTTPX2 client graph and prospective qualification — 2026-10-09

Status: DOING. Evaluate the supported preferred HTTPX2 path before accepting the
deprecated fallback observed in the isolated 43-package trial. The [metadata-only
resolver](../../output/research/test-client-graph-2026-10-09/receipt.json) adds
HTTPX2 2.13.1, HTTPcore2 2.13.1 and Truststore 0.10.4 to the earlier 45-package
identity candidate. All previous package metadata and wheel identities remain
unchanged. The [48-package/57-active-edge closure](../../output/research/test-client-graph-2026-10-09/closure-observations.json)
checks target Python, wheel tags, markers/extras, exact constraints and non-yanked
stable-looking versions. The three added exact/latest registry observations agree;
their classifications are Production/Stable. HTTPX2's exact release is non-draft/
non-prerelease. These are metadata/source observations, not whole-graph selection,
publisher verification, native execution or installed-footprint proof.

Starlette's preserved TestClient source prefers HTTPX2. The [exact Authlib wheel
source](../../output/research/test-client-graph-2026-10-09/authlib-import-source.json)
also prefers HTTPX2 through its compatibility shim and deprecates HTTPX fallback.
Its AsyncOAuth2Client uses the selected shim's AsyncClient; it must not be assumed
to retain HTTPX classes when HTTPX2 is present. No Authlib client was imported or
instantiated during this inspection. The [tagged migration guidance](https://github.com/pydantic/httpx2/blob/d91c9f4236523eb5978ca800944fa0078f17409f/docs/migration.md)
allows coexistence but keeps client/request/response/exception families distinct.
Recommend qualifying each actual consumer's type ownership; do not replace
imports process-wide or mix exception families. The [tagged TLS guidance](https://github.com/pydantic/httpx2/blob/d91c9f4236523eb5978ca800944fa0078f17409f/docs/advanced/ssl.md)
uses system trust stores by default and still respects explicit SSL contexts and
certificate environment settings. This changes no selected production TLS policy;
never disable verification to make a probe pass. No global alias/injection ran.

The [prospective isolated plan](../../output/research/test-client-graph-2026-10-09/qualification-plan.json)
retains the reviewed 256 MiB admission/1 GiB free-floor/180-second command pattern
with measured expanded-wheel reservation, no existing-environment changes and no
automatic cleanup. It proposes the original 14 offline library cases plus four
new namespace/client-lifecycle cases, with both fallback warnings treated as
errors. None of these 18 cases has run against the enlarged candidate. Authlib/
joserfc coverage is limited to import/type/client lifecycle, not OIDC verification,
callbacks, PKCE/nonce, grants, TLS, database or actual Hengshi behavior. The old
43-package environment and its PASS remain separate protected evidence. Independent
proposal review and fresh explicit execution approval are required; the earlier
43-package permission does not expand. Complete candidate rights/provenance/
advisories, stable graph/locks, runtime platform qualification and integrated/
founder adoption remain held. The evaluation pins are not a production lock.

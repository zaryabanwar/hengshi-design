# Browser resource admission and serialization — independent v1 review

Date: 2026-10-05. Reviewer: `review_semantic_preparation_v1`, independent of
the producer. Verdict: **PASS for the bounded engineering proposal**.
Task status: DOING; commits remain deferred. This is not security certification,
founder acceptance, integrated Phase 1 acceptance or implementation authorization.

## Scope and frozen identities

Inspected only the new `Browser-resource and serialized-content proposal`
(`SECURITY_PRIVACY_CONTRACT.md:185–317`) and its review-coverage notice
(`:7–17`). Publication/loading contracts and earlier receipts provide context;
this does not re-review their entire scope or extend earlier identity/privacy
verdicts to a new hash. The current canonical security contract equals its
preserved review copy byte for byte.

| Frozen input | Independently verified SHA-256 |
|---|---|
| [Security contract, preserved bytes](../../../../output/research/browser-security-definition-2026-10-05/SECURITY_PRIVACY_CONTRACT.reviewed.md) and canonical `SECURITY_PRIVACY_CONTRACT.md` | `956bc25845071a1078ee886415e23965df830b11bf9a5a00ef6792d3b3789a98` |
| [Source receipt](../../../../output/research/browser-security-definition-2026-10-05/source-receipt.json) | `ca3b2725490af2d748f7836e4b09e0a3bcb97ef63b5428dcba7df079822b82bf` |
| [DRACOLoader source](../../../../output/research/browser-security-definition-2026-10-05/DRACOLoader.js) | `fdafdf4aa11bbc65d89adb338efd844bedf94073702f9049240ff1f1ea48ad5f` |
| [KTX2Loader source](../../../../output/research/browser-security-definition-2026-10-05/KTX2Loader.js) | `3a3233ce3409443076d3414b78832e1405fcfac5ecb34d367365fd0781127d6c` |
| [Three registry observation](../../../../output/research/browser-security-definition-2026-10-05/three-registry.json) | `0305c00b56fcf7ded1d9fa5f166b98f070111273663b616b39e75f1f7bccde65` |
| [Publication contract](../PUBLICATION_CONTRACT.md) | `2386bec046387527a50dd8e6b4847ac11133932e2267afb96cb20ac4996f111c` |
| [Campus loading/build definition](../../../phase-1-3d/CAMPUS_ASSET_BUILD_SPEC.md) | `6bd0c2e95df6d227a34c0611e4c957501b1c368cd4f6d460f42b530559d0b228` |

The seven-file [input manifest](../../../../output/research/browser-security-definition-2026-10-05/review-inputs.json)
has SHA-256 `0be70250b5d45542ac7d75dec8f6da85bea3792ae5b68d2f1c9507de30d6f88a`.
All listed byte lengths and hashes were recomputed before review and after writing
this receipt. Canonical and preserved security bytes remained identical.

Applied AGENTS/constitution authority, current Phase 1 gates, D-065/D-068/D-069,
FSC-08/09 and accepted SEC-007/008 obligations. Inspected relevant publication
determinism, public/private projection, eligibility and worker acceptance clauses,
and loading identities, bounded ownership, disposal and semantic recovery clauses.
The security-best-practices skill's React/browser guidance informed this bounded
review; unrelated authentication, backend and application-code audits were not run.

## Findings

No actionable material finding in the commissioned scope.

- **Immutable publication and hashes:** `:196–231` preserves unchanged HTML,
  binds serving policy to the eligible artifact/build, distinguishes CSP hashes
  from artifact digests, and refuses a fixed cached nonce or silent response-time
  rewrite. [Vite's CSP guidance](https://vite.dev/guide/features.html#content-security-policy-csp)
  requires per-request nonce replacement and identifies asset inlining.
  [React's renderer reference](https://react.dev/reference/react-dom/server/renderToPipeableStream)
  documents inline bootstrap content and Suspense reveal scripts even when a
  bootstrap URL is supplied. Inventorying actual candidate output is therefore
  necessary; current/main documentation is not candidate-build proof.
- **Symbolic policy:** `:206–223` is explicitly nondeployable and denies broadly
  sourced scripts, event-handler attributes and JavaScript eval. Same-origin
  endpoints must contain controlled code; `'self'` is not integrity, eligibility
  or authorization. [CSP3 frame-ancestors](https://www.w3.org/TR/CSP3/#directive-frame-ancestors)
  cannot enforce embedding restrictions through a meta element. Required HTTP
  enforcement and the report-only distinction are correct. CSP3 is currently a
  Working Draft; the proposal does not equate that status with universal browser
  support or select draft-only features.
- **Typed data and parser safety:** `:235–248` keeps author/AI output as data,
  constrains URL purposes and excludes private process/provider fields. A hash
  cannot make unsafe serialized content safe. [HTML script-content restrictions](https://html.spec.whatwg.org/multipage/scripting.html#restrictions-for-contents-of-script-elements)
  cover closing-script, opening-script and comment-related parser transitions;
  this applies even when JavaScript string or JSON syntax alone is valid.
  Requiring a reviewed context serializer and actual parser/round-trip/hydration
  checks is coherent with the publication boundary. No sanitizer or serializer
  package is selected by the proposal.
- **Style compatibility:** `:250–256` correctly withholds a compatibility claim.
  [Browser style-src-attr guidance](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy/style-src-attr)
  distinguishes style attributes/setAttribute/cssText from direct style-property
  writes. Thus neither “all React styling works” nor “all runtime style writes
  fail” follows from the symbolic baseline. SSR styles, hydration, canvas sizing
  and overlay/motion APIs require candidate-specific browser evidence.
- **World workers and WASM:** preserved DRACOLoader `:384–440, 504–518` fetches
  wrapper/binary inputs, builds a Blob worker URL and terminates/revokes on disposal;
  KTX2Loader `:295–337, 512–515` shows analogous transcoder/worker construction and
  disposal. Independent read-only retrieval of all three source-receipt URLs
  reproduced their exact retained bytes. Registry `three@0.186.1` and source tag
  `r186` remain distinct observations: no exact patch archive, binary provenance,
  dependency resolution or runtime compatibility was demonstrated.
  `:263–274` proposes controlled release-associated resources and separate bounded
  worker permission review, without admitting document Blob scripts or JS eval.
  [Worker CSP guidance](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Using_web_workers#content_security_policy)
  supports separate response policies for ordinary worker URLs and inherited
  policies for local-scheme workers. The narrower [WASM permission](https://www.w3.org/TR/CSP3/#directive-script-src)
  must be checked in the effective worker environment; it is not selected here.
- **Navigation, recovery and privacy:** `:276–290` does not pretend a React route
  can replace an existing document HTTP policy. [Multiple-policy behavior](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy#multiple_content_security_policies)
  cannot relax an already enforced restriction. Same-document World permissions
  need advance review while entry, resources and sound remain independently gated.
  Denial preserves semantic recovery and does not admit unready terrain. Reports
  remain potentially identifying and require mapped minimization, retention and
  access; no reporting endpoint, raw collection, provider or hosting plan is chosen.

## Unproven implementation obligations

Context7 React/Vite/Three queries and official primary pages corroborate the
general guidance, not a locked package set or an executed production build.
Earlier identity/privacy review retains its exact scope; comparison with the
preserved preceding security body found review-reference/status reconciliation
and this added browser section, without changed identity/privacy obligations.

At implementation, CSP inline hashes must cover the browser's UTF-8 encoded
script/style element content, excluding surrounding tags and preserving relevant
whitespace; [CSP's hashing algorithm](https://www.w3.org/TR/CSP3/#match-element-to-source-list)
is distinct from hashing raw artifact bytes. Verify parser/encoding/line-ending
handling, final generated inline blocks, policy/artifact association, caches,
wrong-release and mismatch denial against real responses. The phrase “final-byte
hash” does not constitute such proof.

Exact origins, style mechanisms, worker/WASM grants and serializers remain held.
Actual build/hydration, HTML-parser injection cases, private-field exclusion,
blocked/effective worker policy, decoder integrity, module/preload behavior,
bounded cleanup, failure recovery and privacy-preserving report handling require
tests at the actual authorized implementation boundaries. Stable feature support
needs the approved exact browser matrix and named-device evidence. No browser,
parser, application or security tests were executed in this review; no dependencies,
settings, headers, application source, assets or external configuration were changed.

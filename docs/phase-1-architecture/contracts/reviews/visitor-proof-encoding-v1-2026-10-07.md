# Independent visitor proof encoding review — v1

Date: 2026-10-07. Status: DOING; uncommitted, commits remain deferred.
Independent reviewer: `/root/review_visitor_lifetime_controls_current`.
Verdict: **bounded proposal/evidence PASS**. No consequential finding established.
This preserves the returned disposition; it does not adopt a production mechanism.

## Exact inspected inputs

The [twenty-nine-input manifest](../../../../output/research/visitor-proof-encoding-2026-10-07/review-inputs.json) has SHA-256 `d166d76dc628fbc1b09c5a39507fbbeaf0a7203b804fd09ac3ea7fa49690fa41`.
The manifest and all twenty-nine snapshot hash/byte identities matched initially and finally. Snapshot paths are relative to the manifest directory. Both predecessor contracts remain exact byte prefixes; additions are 8,139 and 686 bytes. Later receipt/reference/state edits are outside these frozen inputs.

## Returned bounded disposition

- Frozen `PRIVATE_PROCESS_PROOF.md:1460–1475,1502–1513`: exact ASCII length/alphabet, strict 32-byte decoding and re-encode equality reject alternate representations, including nonzero pad bits. Canonicality remains separate from issued credentials and current authority. This agrees with [RFC 4648](https://www.rfc-editor.org/rfc/rfc4648).
- The same snapshot:1477–1495,1514–1519 applies full SHA-256 digest verification to independent random bearer bytes and the exact process/generation record. Missing records, wrong generations and mismatches deny; unrelated-record searches cannot grant access. Raw bearer/verifier secrecy, staff JWT/bcrypt and volatile synchronizer-CSRF handling remain separate. [OWASP's storage guidance](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html#server-side-session-token-storage) supports these bounded distinctions.
- The same snapshot:1521–1543 excludes Context7's CPython `main` decoder options from the recommendation. Observed local 3.14.5 and maintained [3.14 documentation](https://docs.python.org/3.14/library/base64.html) retain the three-argument API. Fixed-size comparison does not establish whole-request constant time; lookup/error/transport side channels remain held, consistent with [compare_digest guidance](https://docs.python.org/3.14/library/hmac.html#hmac.compare_digest).
- The same snapshot:1547–1568 preserves D-076: hashing neither renews authority nor creates an absolute visitor cutoff. Stolen valid-proof exposure remains explicit; the policy is not described as OWASP-endorsed. Issuance, actual ingress, storage, races and enforcement require later evidence.
- Frozen `SECURITY_PRIVACY_CONTRACT.md:879–887` preserves those limits without adopting an algorithm or runtime.

## Independently replayed observation and limits

The reviewer copied the public-synthetic probe to reviewer-owned output and ran:

```text
C:/Python314/python.exe -B output/research/visitor-proof-encoding-independent-2026-10-07/probe_stdlib.py
```

Exit 0 at `2026-10-07T08:39:02Z`; all eleven comparable observation fields and three installed-source snapshots matched. No random credential was generated. [Reviewer observations](../../../../output/research/visitor-proof-encoding-independent-2026-10-07/observations.json) prove library behavior only—not entropy, timing resistance or application admission. These are not documentation phrase tests or a functioning Hengshi authentication test.

Only reviewer-owned probe output was created during review. Canonicals, producer evidence, snapshots, code, accounts, Git and goal were unchanged. No adoption, runtime security, accessibility, legal clearance, full-graph selection or integrated/founder acceptance follows. Concrete parser/storage/transport bindings, actual public-ingress enforcement and separately authorized implementation remain held. This later receipt preserves the completed review without modifying its inputs.

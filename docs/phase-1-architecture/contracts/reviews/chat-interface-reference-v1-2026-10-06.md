# Chat interface reference — independent bounded review

Date: 2026-10-06. Verdict: **PASS**, correction cycle 1 of 2; no actionable findings.

Scope: only the reference clause in PRIVATE_PROCESS_PROOF.md:137. Current appended profiles and previous review bytes are context, not renewed review/acceptance.

Cause and correction: the row assigned messages to IF-CHAT-02. The canonical interface-catalog.csv:6–8 assigns IF-CHAT-02 PATCH to consent, IF-CHAT-03 WebSocket to typed events, and IF-CHAT-04 POST to handoff. The field dictionary independently binds consent-change fields to IF-CHAT-02, event/message fields to IF-CHAT-03 and handoff fields to IF-CHAT-04. The revised clause matches those existing responsibilities without inventing an event protocol or accepting its remaining detailed encoding.

Independent inspection confirms exactly one clause replacement. Reversing that clause in memory restores the entire predecessor bytes; no endpoint, method, phase, payload/schema, grant, proof/CSRF, admission, retention or runtime behavior changed. The frozen reviewed copy matches current producer bytes. The producer reconcile script was read, not executed.

All 17 packet inputs and 78 protected guard hashes match before and after. These are artifact preservation checks only. No prose, schema or application tests were required/run, and no new tool/protocol research was needed. Only this receipt was written; producer, packet, settings and other review records remain unchanged.

The earlier private-creation review retains its original exact-input scope; it is neither altered nor interpreted as covering this corrected clause or later profiles. PASS resolves this source-reference contradiction only. Detailed chat protocol, raw/HTTP/proof enforcement, independent/founder and integrated Phase 1 gates remain held; no application or broad acceptance follows.

Frozen packet output/research/chat-interface-reference-2026-10-06/review-inputs.json SHA-256: `1722bdfa353dc2abeddf4aaf719412baffa64f79384f946c9c1ba29a9ab44cc4`.

| Exact input | SHA-256 |
|---|---|
| `output/research/chat-interface-reference-2026-10-06/PRIVATE_PROCESS_PROOF.md.before` | `b4ff840a32570997fa7abc809ebe4a82a63be9d3cb887965bb8ce78389cd842d` |
| `output/research/chat-interface-reference-2026-10-06/PRIVATE_PROCESS_PROOF.md.reviewed` | `327bc1407cfb1ce20f99a12e706592bd72d1a0bcec348c0a4cb0e54794896a7c` |
| `output/research/chat-interface-reference-2026-10-06/protected-before.json` | `8dd4e0b293a517c9d00c45d2ebcb4b3ec2a7b226593c583a91db1e48c1003554` |
| `output/research/chat-interface-reference-2026-10-06/reconcile.py` | `7116765c01d9694f747f985e9048448f9238ea90afd4840b49e06d0322d9a57c` |
| `output/research/chat-interface-reference-2026-10-06/scope-observations.json` | `bed6faf845bb49407e36394b5a3951527d5fdc339d9a813dd8c38bb2781815d4` |
| `AGENTS.md` | `55405cb02a96d05f7f6d68e56a588d743f83877fb2691a5a9f2c736126adbcc5` |
| `.specify/memory/constitution.md` | `33ec0bb02b0d0d9a55d0971589bd19f7242f5d56da130f8f496bc1d31a8b5d23` |
| `PROJECT.md` | `a483bd2713fe420322772ab7fb07c848aaf103088697c05ab91f35d2e5ea1461` |
| `PROJECT_STATE.yaml` | `ea998af973302020a06f849c0e237bdbd21376ddba062b45c9128a082d7ac2a0` |
| `DECISIONS.md` | `0290e6bed5d983fa1f2162db72f1a9d3167695ff98c867c88987ee1e2c4bcc99` |
| `TASKS.md` | `158e06c0d8cd67859c8b459b96dce3449cb4d16788d3c520e99d8823f72edcd3` |
| `docs/software-definition/README.md` | `72e1528a925808c9dc3067842dafac1bb914b39eabc92c169127ef6e7402d3f3` |
| `docs/phase-1-architecture/contracts/PRIVATE_PROCESS_PROOF.md` | `327bc1407cfb1ce20f99a12e706592bd72d1a0bcec348c0a4cb0e54794896a7c` |
| `docs/phase-1-architecture/contracts/INTERFACE_CATALOG.md` | `0105fba4c418d8c8fc2c72bf09fd1e554c39241eac557432a6f9fb616705e86d` |
| `docs/phase-1-architecture/contracts/interface-catalog.csv` | `42018a3e5cc6c1edf488c392b0349688a92b2cab5a8f50e717f1bca84a70a49c` |
| `docs/phase-1-architecture/contracts/process-fields.csv` | `5737b8f4bd47b90a5020ae8943cb2c7786582c605e14d97212b4334ffb26522a` |
| `docs/phase-1-architecture/contracts/reviews/private-creation-boundary-v1-2026-10-05.md` | `54d1bbb08e1875d2b5be7e73d0eb75b9d03e58018c8651ec81a2dcf46a9066bd` |

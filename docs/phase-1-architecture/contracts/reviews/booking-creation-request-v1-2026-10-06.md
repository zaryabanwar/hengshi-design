# Booking creation request encoding — independent bounded review

Date: 2026-10-06. Verdict: **PASS**, initial candidate. No actionable findings or producer revision requested. This review establishes definition/schema-validator coherence only, not implementation, operational approval or integrated/founder acceptance.

## Contract disposition

The appended PRIVATE_PROCESS_PROOF booking request proposal refines only the existing IF-BOOK-01 client direction. Its entire predecessor byte prefix is preserved. Bootstrap is exactly the closed object with phase bootstrap; create is exactly phase create plus provisional_id and operation_id. The schema's disjoint oneOf branches, required members and additionalProperties:false agree with the prose and existing two-phase logical request definition. Personal information, qualification, consent, chat context, proof/CSRF values, client clocks and server-owned results are excluded from both bodies. Qualification and its separate purpose-specific consent remain at IF-BOOK-02; chat creation retains distinct release/wing and consent obligations. Existing logical routes are not activated or replaced.

The provisional reference uses the unchanged common lowercase UUID definition. Its shape, including Nil/Max or text equal to the operation reference, does not establish an allocated booking-family context, ownership, issuer, uniqueness or current proof. The caller operation reference further constrains the version nibble to 4 and variant nibble to 8/9/a/b. Generation once per deliberate intent, permitted reuse and the CSPRNG recommendation are consistent with that narrower representation, but the schema proves neither entropy nor collision avoidance. UUID references remain nonsecret scoped selectors, not credentials or globally authorized deduplication keys.

Existing selected-context plus process-family operation scope, Origin/current cookie/separate CSRF checks, strict raw decoding, early work admission, confidential denial, current disclosure authority, single guarded promotion and immutable admitted-meaning reconciliation stay intact. Rotating proof/CSRF is not new intent; a new operation reference cannot bypass pending admission or produce a second lineage. Shape acceptance cannot authorize durable personal storage, extend proof/retention, verify email, reserve a slot or establish provider success. Exact response encodings, transport/error profiles, expiry and work limits, legal mappings, physical uniqueness/fencing and lost-cookie recovery remain held. No secret transport or retention decision is silently selected.

## Independent validation

Independently executed:

```text
C:/Python314/python.exe -B -m unittest scripts.validation.test_booking_creation_request_schema scripts.validation.test_process_value_schema -v
```

**8 booking request tests and 7 common helper tests pass**, exit 0. The child environment was cleared and populated only with existing SystemRoot/WINDIR/COMSPEC/TEMP/TMP, a minimal Windows/Python PATH, PYTHONDONTWRITEBYTECODE=1 and PYTHONUTF8=1. No inherited provider/auth variables, install, dependency update, application/service/database change or generator implementation was used. Independent logs are retained separately under ignored test-results/booking-creation-review-2026-10-06/; producer logs and snapshots are unchanged. The producer record-and-check script was inspected, not executed, because it appends and writes producer evidence.

The fixtures exercise the real Draft202012Validator with explicit UUID FormatChecker and four registered local resources. They cover both permitted phases, missing/extra fields, forbidden credential/private/server fields, unknown/noncanonical phases and root types, coercion/normalization rejection, wrong operation version/variant, Nil/Max operation denial, shape-only equal-reference/Nil-provisional controls, and unregistered retrieval denial. The schema's common definition also permits Max provisional syntax without proving allocation; common tests cover that syntax. Registered reference resolution and the throwing retrieval callback prevent an unregistered schema fetch in this tested validator boundary. No prose test, copied runtime state machine or broad product suite is added.

Independently consulted [RFC 9562 section 5.4](https://www.rfc-editor.org/rfc/rfc9562.html#section-5.4): UUIDv4 has the version-4 and standard variant bits, leaving 122 random bits. This supports the pattern, not a guaranteed issuer or secret. [MDN randomUUID](https://developer.mozilla.org/en-US/docs/Web/API/Crypto/randomUUID) confirms the standard cryptographically secure v4 generator and secure-context requirement. The proposed browser candidate selects no package or supported browser matrix; no browser generator capability was executed or accepted here. The producer's Context7 statement is retained as provenance; this reviewer did not infer framework admission or error confidentiality from tutorials.

## Preservation and remaining gates

All **98** frozen packet identities and **78** protected-input guard identities match before and after review. The predecessor prefix and frozen reviewed snapshot match current producer bytes. Common helper and publication manifest identities remain unchanged. Those checks establish preservation, not whole-system correctness or compatibility. Protected files were not substantively reviewed merely because their hashes were checked.

This PASS does not establish raw HTTP/parser enforcement, credential/Origin/CSRF controls, browser behavior, generator entropy, authorization, concurrency/transaction/idempotency, expiry/retention, response/status/header enforcement, cryptography, supply-chain/full-graph selection, whole wire/lifecycle freeze or production readiness. Actual boundary tests and the existing design, security/legal, operational, full Phase 1 and founder gates remain. No application, model, source lock, service, account, provider, Git history or producer file was changed; only this receipt and reviewer-owned ignored test logs were created.

## Exact input identities

Frozen 98-input packet: output/research/booking-creation-request-2026-10-06/review-inputs.json, SHA-256 `9db94ea3470a071eb568ff1f370a172faf9742165eee2cc9e631b6260f4e5bbb`.
The table binds the complete packet, not a broadened substantive review. Additional rows bind the separately checked protected guard manifest and independent logs.

| Input | SHA-256 |
|---|---|
| `.specify/memory/constitution.md` | `33ec0bb02b0d0d9a55d0971589bd19f7242f5d56da130f8f496bc1d31a8b5d23` |
| `AGENTS.md` | `55405cb02a96d05f7f6d68e56a588d743f83877fb2691a5a9f2c736126adbcc5` |
| `DECISIONS.md` | `0290e6bed5d983fa1f2162db72f1a9d3167695ff98c867c88987ee1e2c4bcc99` |
| `PROJECT.md` | `a483bd2713fe420322772ab7fb07c848aaf103088697c05ab91f35d2e5ea1461` |
| `PROJECT_STATE.yaml` | `ea030336814b0fe4cb810ab4097f0ee22b24a8d14712f6ce6cc2f8bedc02fc5a` |
| `TASKS.md` | `158e06c0d8cd67859c8b459b96dce3449cb4d16788d3c520e99d8823f72edcd3` |
| `apps/api/app/__init__.py` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `apps/api/app/admin/__init__.py` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `apps/api/app/admin/routes.py` | `c95dd1a7eacfeb9f5aea82eec38581e56c4e32e389789b21ef2d4cd446e2b33f` |
| `apps/api/app/auth/__init__.py` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `apps/api/app/auth/deps.py` | `6990c8ce351698e75ada326ad546bf8fa95e187678f7f25ad6c778b7bc3d9312` |
| `apps/api/app/auth/jwt.py` | `7807d67dd3cad02543c16d17b77fb156abd484bd9c794ed455f38e71a5aaf316` |
| `apps/api/app/auth/password.py` | `52e5918e298549a6f0138bfb9e3b4c6c0a827d1418af166ef5586884c6901907` |
| `apps/api/app/auth/routes.py` | `9ab927ae71fee54afcd96afb1bb648b53dc4aa4469d6bec884a2f0717ec1af97` |
| `apps/api/app/auth/schemas.py` | `784b1577f82721e1196f13db0c6fc3b8c8eddc21a96342daaa2bd9b9793f4d2d` |
| `apps/api/app/db/__init__.py` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `apps/api/app/db/base.py` | `2e54675f603d29c8751fc2634bb96c1f9b05419c565d0d35300f66bc450e1eed` |
| `apps/api/app/db/session.py` | `c05031b579efd1555a372fdfce5feb7ac289c3e97f013c79d8f6aa19801cf52e` |
| `apps/api/app/leads/__init__.py` | `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` |
| `apps/api/app/leads/routes.py` | `7c8b4b6a014f657f9278664ca569e28687a43263c195ce78f96b264436706111` |
| `apps/api/app/leads/schemas.py` | `f6bfcd46c2ed6620afd46392f12b163abfc612188281d6796dca974f70c63942` |
| `apps/api/app/main.py` | `f6dc16de91ffd3fca40017d9024c156ed3383d2564f08f09389b6be942520ff9` |
| `apps/api/app/models/__init__.py` | `7cf68e30e0e64f4272ecde9ff45c467d6ed7bb3438ca08fc51c5bfe488c20f85` |
| `apps/api/app/models/lead.py` | `070cbf96610340672532f0430bfd0748c063d5dc3e60d7b3eeff0ba720369dab` |
| `apps/api/app/models/project.py` | `4d9ed6aa59749b09195bf1875c97a0d2d47d536af65b5db8b391999bf9b10037` |
| `apps/api/app/models/service.py` | `da12bf5ddfa4a22cbde36c4fef7c6f98332b5e0b027e34a2bfe2f34f05d28216` |
| `apps/api/app/models/user.py` | `b44a19b3ffd2a490abd16aad1ba96929a76d4a488309eb7346c5d9b0ad789086` |
| `apps/api/app/models/world.py` | `1e3f3073cf06ea3e297c7e6934b6e74f6e3e1a536280395c014a7c2aeb133c78` |
| `apps/api/app/projects/__init__.py` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `apps/api/app/projects/routes.py` | `d74cc38ea6e911f0d006cb392f4101cc58598395e1073a71e6ea3fa22894a704` |
| `apps/api/app/projects/schemas.py` | `4c4b6bedcf6a1056e8423916faad0880fae32025c3498c8118d8d67d44d29aab` |
| `apps/api/app/scripts/__init__.py` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `apps/api/app/scripts/create_admin.py` | `6661b18af543d9af44a919aa8016347ff5c37939bf6d005dd16633b889f10529` |
| `apps/api/app/scripts/seed_projects.py` | `e07b31063c914d9ddbf811dfdc69186290df2343413b28b5bf99803f98eeedc0` |
| `apps/api/app/scripts/seed_services.py` | `00d92d9e843b5c9844bfbc5c3818e30d450b3f1e597d511707bda7a18f5da750` |
| `apps/api/app/scripts/seed_world.py` | `8fa6b46c3e539584fbf757ff0c90e2f53cc3c63765e11ca77241d770d12d79a6` |
| `apps/api/app/services/__init__.py` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `apps/api/app/services/routes.py` | `9bfa76519d8c2f4a6d0d7c5f8e3d0fcb63a7188762770e300873cf3762101d7c` |
| `apps/api/app/services/schemas.py` | `0120e3aa01697091489b12bd4e338edf5d19d42f9fc018cffb5561ec69f5c140` |
| `apps/api/app/world/__init__.py` | `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` |
| `apps/api/app/world/routes.py` | `2ea394080bab1a6fec4cdc4dac7a79408b42964da3b404b436d511b4ab1d975e` |
| `apps/api/app/world/schemas.py` | `7364da12889f37e3d65c803cbb17a86f1913f16be73130eeb2b1b8c5de6926fb` |
| `apps/api/requirements.txt` | `b99f98e119cb6653f38b19d1ee83cc7f33d92a699083645ca19369a8912e89bd` |
| `apps/web/package-lock.json` | `35486fb012489de4c3b363198304a25f44a0396707db328190d7e056c06d416d` |
| `apps/web/package.json` | `83e4178348ec081922dd3d53d00c51446b655091d056ec09dde52a2496b04e2a` |
| `apps/web/public/models/hengshi-hq-atlanta-exterior-web.glb` | `4767cab4d346207a2109ffc1584e256e82ae1cecc110780b99c4406a9586aafe` |
| `apps/web/src/App.tsx` | `71cd24168d09a509abe919ffddce0085c46b4fab5e3f69f5198dd92a4b0b7563` |
| `apps/web/src/admin/AdminLayout.tsx` | `3662397b5225b064655c905ee4e2cd054fd6e75a92b2bb9bbeeda905cd1b035f` |
| `apps/web/src/admin/AdminLoginPage.tsx` | `b73cc311a28f2ff853eaa957f4c05f59af79ed572bf8ec95df226ba125cd3791` |
| `apps/web/src/admin/ProjectsAdminPage.tsx` | `d318e078377354f3a25674a5a9870634a10fe469b7a541cd119d794157478266` |
| `apps/web/src/admin/RequireAdmin.tsx` | `722efb7b8bd32831351eb9306da03fb2922e306dbd698ae251ebc20d5c0894d6` |
| `apps/web/src/admin/ServicesAdminPage.tsx` | `00335603d24e8a6c4b333aa879b50986b435de67e9ef476731de5ff52af89cc9` |
| `apps/web/src/admin/WorldAdminPage.tsx` | `02ed75c4fed0dee1689f33f09409bacb3474d36109f6a013d44e8d1694edb804` |
| `apps/web/src/counter.ts` | `7580ce935ad5fd8f5598ee53533fbddbd5d34e5aaf6cfbb7f81f3ef1969bf4e3` |
| `apps/web/src/env.d.ts` | `e551d50cf8c4882827096c5e8e7f9e47d886387cb25a9be381b775587d43d138` |
| `apps/web/src/index.css` | `52a25f99b26417d56be0f5d82bcd92a3225b43dfa375e02de3acc23ed83304a8` |
| `apps/web/src/lib/api.ts` | `b15f2091f084196034917e878485eb70b689162fca422818cf6adba2498bdc58` |
| `apps/web/src/lib/constants.ts` | `6fe20489a0d14adbcc18b3c391bc713694a4c33faf4d052340012d52a510a3a7` |
| `apps/web/src/lib/types.ts` | `d30254f55d8ade0d616dde9be194e4e67e6a28854166137939034b43b346b6ae` |
| `apps/web/src/main.ts` | `9592a6269d9e9c1426595eec9f1b6d2b58d8399f4cdce6546d403d96f613ecdc` |
| `apps/web/src/main.tsx` | `db7dc6ae38613fd712de584d4e595f7f1a653014fe7c57250367745dd0a9a2e3` |
| `apps/web/src/pages/Home.tsx` | `76436a8828bd736b2026d71c07a5e9e355cf54cb80865f8a448f2aea7094552f` |
| `apps/web/src/pages/NotFound.tsx` | `06b1a96c97a105230199b9bb98ceb65c5a5712ae2eb49078bba9ca1d0cfb29f2` |
| `apps/web/src/pages/Studio.tsx` | `3e2e4d90078169e3c7c588129fbf3b956829d4236698fe188a01ba6f476e9104` |
| `apps/web/src/pages/WorldPage.tsx` | `37cdb7cff3be418dcc973125f6a440113adb6eadc36f980e449255acf176f5dd` |
| `apps/web/src/store/useAppStore.ts` | `f90c9924b8acc4e6694a8d92d9911f0e04e34134ebbadfccc273f95b38120311` |
| `apps/web/src/stores/worldStore.ts` | `a93e17bd5b641752ec714b0596c1644f7976656a9e418a3002953c244f35bfe2` |
| `apps/web/src/style.css` | `81b5564e0527ba1f2b7ada78a611777d5dbf7211da9e460dc4d07474fea971f6` |
| `apps/web/src/typescript.svg` | `f6ead1af17acc3f55ad857f3bc936df8754281e2932c1b472dbb9b36ab873f1c` |
| `apps/web/src/world/ExteriorScene.tsx` | `cca5f46a456dcb29362bf2fb89ab4052727f0af37501abef16ba50e9bc74cbc0` |
| `apps/web/src/world/WorldCanvas.tsx` | `8a13414d7cf091584841f278c6fbb9b19a65adf06073dccf49f071cb42d66847` |
| `apps/web/src/world/WorldHUD.tsx` | `a95c352fb7bdd4b9cf4351e98bbeb730ce8200745f62c3a835f69d67f12ebb24` |
| `apps/web/src/world/WorldPanel.tsx` | `02056454cad62bef3a72a0328df907972f7f60dc95cd7efb7cba3de8d183b99f` |
| `artifacts/nature-campus-layout-study/nature-campus-layout.glb` | `e2161710dc0576ec62e3d096c60e32927e827aa59198a33361e729ec8a7b43c0` |
| `docs/phase-1-architecture/contracts/DATA_CONTRACT.md` | `238dcf31e7dfa967a2c93359af145bece5139e6efd224876428342666ab2bc9b` |
| `docs/phase-1-architecture/contracts/INTERFACE_CATALOG.md` | `83daa2246669cbe6292df3f867bf7a796a09d69b7fedc183cf8b67a5ba0aa7c5` |
| `docs/phase-1-architecture/contracts/PRIVATE_PROCESS_PROOF.md` | `6fe23174bd29019b0928a94c9e9096293cb2dce023af82051253b5eec783e0b5` |
| `docs/phase-1-architecture/contracts/SECURITY_PRIVACY_CONTRACT.md` | `50f3c00d5e6aed36bb4fa99e864ba337cc3dc3f76c0665ff30e0f765782ad00a` |
| `docs/phase-1-architecture/contracts/booking-creation-request.schema.json` | `6848784172c0b39951978fb6a93158655b444e1c9400091c0a90c8d0fd509e37` |
| `docs/phase-1-architecture/contracts/interface-catalog.csv` | `42018a3e5cc6c1edf488c392b0349688a92b2cab5a8f50e717f1bca84a70a49c` |
| `docs/phase-1-architecture/contracts/process-fields.csv` | `5737b8f4bd47b90a5020ae8943cb2c7786582c605e14d97212b4334ffb26522a` |
| `docs/phase-1-architecture/contracts/process-value.schema.json` | `b4fd9fc84f322ecb6743c00244f3731ccd612861de53056aaddb20a377a67a95` |
| `docs/phase-1-architecture/contracts/publication-manifest.schema.json` | `d3620c8326246bc34040188de610c5823f1013936572d3ffb63a5eb350bc3852` |
| `docs/phase-1-architecture/contracts/publication-preparation.schema.json` | `23c3569baa844a542dd8f7a283af87f50b93dfa1fdf3ccef2c401136c8acc2ac` |
| `output/research/booking-creation-request-2026-10-06/PRIVATE_PROCESS_PROOF.md.before` | `7c094d5b4c4506caf5a2179a5520f687926d3a77459d9b73925c0d75b297c914` |
| `output/research/booking-creation-request-2026-10-06/PRIVATE_PROCESS_PROOF.md.reviewed` | `6fe23174bd29019b0928a94c9e9096293cb2dce023af82051253b5eec783e0b5` |
| `output/research/booking-creation-request-2026-10-06/record-and-check.py` | `bcde55d8132f4cb0ecb6846aef5514c47e736e22224837a4d97a4442e61b0edc` |
| `output/research/booking-creation-request-2026-10-06/validator-receipt.json` | `078cc270776fc203e127662cecfbbb49930a147f9a1b4c34c7719cfb0e6adb49` |
| `output/research/booking-creation-request-2026-10-06/validator.stderr.txt` | `7e94d108602141c3f6666a42ea5cde07e5d8bb28b36958764dc5d1534c12006a` |
| `output/research/booking-creation-request-2026-10-06/validator.stdout.txt` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `output/research/react-lint-approved-evaluation-2026-10-06/candidate/package-lock.json` | `86dd64aae77da6ab9a0d0f7a88338494c15f68620838ffd40140f254b1e9ca2d` |
| `output/research/react-lint-approved-evaluation-2026-10-06/candidate/package.json` | `29bd6baedb79106c1bd5a3c9050867cb2a7478dd33b35fa9b4326856c8fadf72` |
| `package-lock.json` | `d2da4d7206344ba45645d7bafe4ec692bb738ea0c1c98c2680522688b5733908` |
| `package.json` | `a07f9f12c83736625d621781a1b30c8430452ef7e698fa626902cf16cef7946b` |
| `scripts/validation/test_booking_creation_request_schema.py` | `773fd0f9ea930676c57da53ae9998187bf1a0b8bc8501b7e5753124e04cb98e0` |
| `scripts/validation/test_process_value_schema.py` | `fc9f73eff47cc944122ba019c1c11bfe034fdd113584deeee93f35da88b96d9a` |
| `specs/001-platform-security-hardening/spec.md` | `47704c411b72195a2a4f8b832b07b30d90b00673647afe50d8ac98b917939d99` |
| `specs/004-design-services-content/spec.md` | `a34008a87d29232c1ae8505d905049ea29f95581958e4bfe5a0a97675af6a029` |
| `output/research/frontend-supply-chain-2026-10-06/protected-before.json` | `9bb8f003769b335983ea004bb8caeb085669baee1a7a8cbc816db07367c1c63f` |
| `test-results/booking-creation-review-2026-10-06/stdout.txt` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `test-results/booking-creation-review-2026-10-06/stderr.txt` | `cfde6df9c18b1730b18b81269c11cf4b7956e8f7fa92b6cfba06fe73415cd49f` |

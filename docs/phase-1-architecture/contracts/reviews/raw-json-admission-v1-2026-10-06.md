# Raw JSON admission — independent bounded review

Date: 2026-10-06. Verdict: **PASS**, initial candidate. No actionable findings or producer revision requested. Review covers the two additive proposal sections and native parser observations; it is not decoder conformance, application implementation or founder acceptance.

## Contract coherence

The DATA_CONTRACT raw-admission appendix and INTERFACE_CATALOG shared-boundary appendix preserve existing interface, field, authorization, error and caching authority. Their predecessor byte prefixes are unchanged. The proposal separates transport/resource admission, raw decoding, directional shape, field semantics and current process authority; valid JSON alone cannot complete or authorize a business operation. No middleware, decoder, endpoint, denial code, production dependency, numerical work limit or default policy is selected.

The required strict UTF-8/no-BOM path, decoded-name duplicate rejection at every depth, escape-equivalent key handling, scalar validation and prohibition of non-JSON number tokens agree with the existing availability and private-proof obligations. Valid supplementary-character pairs remain permitted; legitimate text is not silently normalized. Root/array/null policy remains directional. Availability's canonical decimal revision strings retain their exact range and are not converted into the new common numeric helper. Mathematical integer versus lexical spelling, precision/exponent rules, resource limits and actual parser integration remain field/profile inputs.

Finite receive/work limits must apply before unbounded collection/decoding; trusted Content-Length or a hook after allocation cannot prove that. Response shape/Unicode/numeric checks and safe private denials retain their separate responsibilities. Existing proof/Origin/CSRF/object/purpose and atomic/reconciled outcome checks are preserved, including PRIVATE_PROCESS_PROOF's early checks before costly private-data work. No new grant, account, persistence or public/private disclosure follows.

## Independent native observation reproduction

Executed the frozen runner with `apps/api/.venv/Scripts/python.exe -B` in a cleared child environment containing only existing SystemRoot/WINDIR/COMSPEC/TEMP/TMP, Windows system PATH, PYTHONDONTWRITEBYTECODE=1 and PYTHONUTF8=1. No inherited provider/auth variables or candidate installs were used. Exit 0; all **20** case records and source/runtime fields match the producer JSON exactly. The 18 accepted and two rejected cases are observations, not application test passes.

The three valid syntax/Unicode controls parse. Additional independent inspection of five control values confirms literal supplementary text preservation, escaped-pair decoding to the same scalar, last-value retention for duplicate/escape-equivalent keys and nested duplicate collapse. Duplicate information is lost before ordinary schema validation. The runner distinguishes forbidden NaN/Infinity tokens from legal exponent syntax that becomes nonfinite or rounds to zero, and Python-preserved large integers from browser exactness. Isolated surrogates, UTF-16/32 and UTF-8 BOM parse in the observed byte path; trailing data and malformed UTF-8 fail. An array root parses without proving that any directional envelope permits it.

The installed Starlette source is exactly the recorded requests.py identity and Request.json starts at line 262: it collects body bytes and calls ordinary json.loads. Installed Python JSON source independently confirms encoding detection, the byte-input surrogatepass path and its distinction from BOM rejection for already-decoded string input. The probe invokes Request directly with a synthetic single-chunk receive function and no route/application, media headers, authentication, streaming-bound or resource-profile enforcement. Neither the runner nor the control inspection implements an alternative admission decoder.

## Primary sources and limits

Independently consulted [Python 3.14 JSON documentation](https://docs.python.org/3.14/library/json.html), which labels the current page 3.14.8; it is guidance, not exact 3.14.5 runtime evidence. Documented hooks preserve object pairs or intercept non-JSON constants, but default parsing accepts repeated names/nonfinite constants and interpreter limits do not supply the proposed finite profile. The source-verified byte BOM behavior must not be inferred from the documentation's string-input BOM warning.

[RFC 8259](https://www.rfc-editor.org/rfc/rfc8259.html), sections 4, 6 and 8–10, supports the distinction between JSON syntax, interoperability and implementation limits. Object-name uniqueness is SHOULD, parsers may ignore an initial BOM, and syntactically valid exponent magnitude can exceed common numeric capabilities. Duplicate/BOM rejection here is an explicit stronger project profile.

[RFC 7493](https://www.rfc-editor.org/rfc/rfc7493.html), sections 2.1–2.3, supports decoded-name uniqueness, scalar/pair handling and numerical interoperability. This proposal is not blanket I-JSON certification; that profile has additional constraints, including noncharacters. The retained Context7 main-index query does not select an observed runtime capability: future array_hook remains explicitly excluded. No Context7 call, dependency selection or additional decoder capability was inferred by this reviewer.

All 21 packet inputs, both predecessor prefixes and all 12 unchanged-input guards match before and after review. Those hash/prefix checks establish artifact preservation only. No producer/application/dependency/model/service/database file was changed. Only this review and separate ignored reviewer evidence under test-results/raw-json-independent-review-2026-10-06/ were created. No schema/prose test or broad suite was added. Actual raw HTTP/browser denial-before-dispatch, bounded streaming, concurrency, authorization, parser/response conformance, full stable graph, wire freeze and integrated/founder/Phase 1 acceptance remain held. B01, legal, QA exception, provider and operational gates are unchanged.

## Exact identities

Frozen packet: `output/research/raw-json-admission-2026-10-06/review-inputs.json`, SHA-256 `c847a96212feafbc000ef402944b854b8b909064b4c5743b5932a729474c2e48`.
The table binds packet inputs, additional preservation guards, inspected installed source and separate reviewer evidence. Preservation-only inputs are not runtime acceptance evidence.

| Input | SHA-256 |
|---|---|
| `.specify/memory/constitution.md` | `33ec0bb02b0d0d9a55d0971589bd19f7242f5d56da130f8f496bc1d31a8b5d23` |
| `AGENTS.md` | `55405cb02a96d05f7f6d68e56a588d743f83877fb2691a5a9f2c736126adbcc5` |
| `DECISIONS.md` | `0290e6bed5d983fa1f2162db72f1a9d3167695ff98c867c88987ee1e2c4bcc99` |
| `PROJECT_STATE.yaml` | `f5a33ef7b607e467630c463c1ae942ca4fdf85f3569890f2e1f0081fcbaa6926` |
| `TASKS.md` | `158e06c0d8cd67859c8b459b96dce3449cb4d16788d3c520e99d8823f72edcd3` |
| `docs/phase-1-architecture/contracts/AVAILABILITY_READ_HTTP.md` | `d85d2b581980aee36f3132f7de1ee2ae3633ae65bc4bbaf8e6dd49e3c98b4f0f` |
| `docs/phase-1-architecture/contracts/AVAILABILITY_WRITE_HTTP.md` | `16dde36c817d4cb8534292fce3a70032821bb5e3d32ac97e56c114eeca2d747e` |
| `docs/phase-1-architecture/contracts/DATA_CONTRACT.md` | `8d4b9944c1a201a42a451827d5e28c93357b4b84602499200a2bbe6529ca9c22` |
| `docs/phase-1-architecture/contracts/INTERFACE_CATALOG.md` | `83daa2246669cbe6292df3f867bf7a796a09d69b7fedc183cf8b67a5ba0aa7c5` |
| `docs/phase-1-architecture/contracts/PRIVATE_PROCESS_PROOF.md` | `7c094d5b4c4506caf5a2179a5520f687926d3a77459d9b73925c0d75b297c914` |
| `docs/phase-1-architecture/contracts/process-value.schema.json` | `b4fd9fc84f322ecb6743c00244f3731ccd612861de53056aaddb20a377a67a95` |
| `output/research/raw-json-admission-2026-10-06/DATA_CONTRACT.md.before` | `f67a7047338c6d24f8de3474cc6cc250db8289c577e62297832fc83b217e4ace` |
| `output/research/raw-json-admission-2026-10-06/DATA_CONTRACT.md.reviewed` | `8d4b9944c1a201a42a451827d5e28c93357b4b84602499200a2bbe6529ca9c22` |
| `output/research/raw-json-admission-2026-10-06/INTERFACE_CATALOG.md.before` | `fef055645c44bf9e9e7d95eff995c0dc5ec3437a4c85c28b2220bdd5c46f56fc` |
| `output/research/raw-json-admission-2026-10-06/INTERFACE_CATALOG.md.reviewed` | `83daa2246669cbe6292df3f867bf7a796a09d69b7fedc183cf8b67a5ba0aa7c5` |
| `output/research/raw-json-admission-2026-10-06/observations.json` | `4c6282280bed937193b68cb5c13af556538ea20d45aa38a25b3865c94094e400` |
| `output/research/raw-json-admission-2026-10-06/probe.stderr.txt` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `output/research/raw-json-admission-2026-10-06/probe_framework_json.py` | `992c5435a62bb103c7a9e36249835e52e1976b1c50987ab09122c40c0d8f965d` |
| `output/research/raw-json-admission-2026-10-06/source-receipt.json` | `2fb166e49489d96b2e4e10f4af7802f910cc6cdb71a63a774540dce0b9934607` |
| `output/research/raw-json-admission-2026-10-06/unchanged-inputs.json` | `b47d3978352c658106d475b8601fd911a87155a9117295eab8c636756671079f` |
| `specs/001-platform-security-hardening/spec.md` | `47704c411b72195a2a4f8b832b07b30d90b00673647afe50d8ac98b917939d99` |
| `PROJECT.md` | `a483bd2713fe420322772ab7fb07c848aaf103088697c05ab91f35d2e5ea1461` |
| `apps/web/package.json` | `83e4178348ec081922dd3d53d00c51446b655091d056ec09dde52a2496b04e2a` |
| `apps/web/package-lock.json` | `35486fb012489de4c3b363198304a25f44a0396707db328190d7e056c06d416d` |
| `apps/api/requirements.txt` | `b99f98e119cb6653f38b19d1ee83cc7f33d92a699083645ca19369a8912e89bd` |
| `package.json` | `a07f9f12c83736625d621781a1b30c8430452ef7e698fa626902cf16cef7946b` |
| `package-lock.json` | `d2da4d7206344ba45645d7bafe4ec692bb738ea0c1c98c2680522688b5733908` |
| `apps/web/public/models/hengshi-hq-atlanta-exterior-web.glb` | `4767cab4d346207a2109ffc1584e256e82ae1cecc110780b99c4406a9586aafe` |
| `artifacts/nature-campus-layout-study/nature-campus-layout.glb` | `e2161710dc0576ec62e3d096c60e32927e827aa59198a33361e729ec8a7b43c0` |
| `apps/api/.venv/Lib/site-packages/starlette/requests.py` | `8691b01ae49ecfa085fe6419343678f73b77c92fc63a411106a77d8e9bf0ac44` |
| `C:/Python314/Lib/json/__init__.py` | `0439e6546415d4147396afac324beadb7a8dc2c1e2391dcb541fb34c83986d8f` |
| `test-results/raw-json-independent-review-2026-10-06/observations.json` | `4c6282280bed937193b68cb5c13af556538ea20d45aa38a25b3865c94094e400` |
| `test-results/raw-json-independent-review-2026-10-06/stderr.txt` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `test-results/raw-json-independent-review-2026-10-06/inspect_controls.py` | `800a9ff72c89bb7ab081f23933a07f742eb905630d8ec3789cae44d94d48fbcb` |
| `test-results/raw-json-independent-review-2026-10-06/controls.json` | `14a0743e9a3ff1e6bd5df4fddb3408fef10a390777c363549bc41aa1ebd18634` |

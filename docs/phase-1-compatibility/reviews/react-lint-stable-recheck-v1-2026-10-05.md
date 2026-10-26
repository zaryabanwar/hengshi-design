# Fresh React-lint recheck — independent review v1

Reviewed 2026-10-05. **PASS for the bounded evidence recheck; no actionable findings.** This accepts accuracy of the new dated observations, not required lint conformance, a selected dependency graph or full Phase 1 acceptance.

## Exact scope and identities

Only the “Fresh stable React-lint recheck — 2026-10-05” section in `refresh-evidence-2026-10-04.md` is new producer material. Earlier studies/receipts remain context at their own scopes. Removing this single inserted section exactly reproduces `refresh-evidence.before.md`; no previous body changed.

Manifest: `output/research/react-lint-stable-recheck-2026-10-05/review-inputs.json`, SHA256 `5a59c803c85c3474763e7aa34a10762db02599510a5ee64c408031fb7b8b6a52`. All **86 retained source identities**, sizes and hashes were independently verified. This packet intentionally retains source files without duplicating archives/binaries; its policy is not an assertion of separate immutable storage.

| Material input | SHA256 |
| --- | --- |
| Producer document, 45,314 bytes | `a2d1d50670a3a45766487373a65162db1e238999206ca94ba349d148c1c6a027` |
| Before document, 42,698 bytes | `ae2f8a87c378147461d7606616ce5118cf83e10bcb3e5889091d7ef8f0d87964` |
| New `receipt.json` | `876ea07706e1bc15d0c30aa6993f6baace789c1d45d3ba2d5bbed55d3172a312` |
| Inspected `run_recheck.py` | `468fcbb4a623dd5c236632e449125e87ab433e1bf4d3d1cf390fdd68eb63b731` |
| Published JS archive | `04441961a07abc710dda63f798550b37169d7ad527acbe6e880785987b6116d4` |
| Published Windows x64 native archive | `f9ee4df9a3a661aa210e52c0a63ad1d314485df14c44b878c283df1757d2c91c` |

## Independent inspection and reproduction

Read the producer script before execution. It downloads/unpacks and writes evidence, so it was **not rerun**. Instead, independently checked both archived packages' SHA-512 against their official metadata and compared all 18 JS-package files and three native-package files to the actual unpacked tool. No installation or lifecycle script ran. Artifact association does not verify signatures, attestations or source-to-binary build provenance.

Directly executed all **14 recorded existing fixture commands**, with their exact working directory and configurations, using the retained published Node entry/native tool. Confirmed only read-only lint modes, with no fixes or experimental rules. Every exit code, diagnostic-code multiset, reported file/rule count and empty stderr matches the new receipt and the earlier 1.86.0 evidence. Saved stdout/stderr content hashes also match the receipt after its text-write newline normalization. Versions independently report Node `v24.14.0` and Oxlint `Version: 1.87.0`; the full parsed `--rules --format json` inventory matches the retained inventory.

| Witness group | Reproduced behavior and limit |
| --- | --- |
| Namespace valid/control; conditional namespace, custom Hook and Hook-shaped import alias; missing namespace Effect dependency | Valid control exits 0. Recorded violations exit 1 with the expected Hook/dependency diagnostic. |
| `useState` renamed `state`; `useEffect` renamed `effect` | Both invalid fixtures exit 0 without diagnostics: detection remains incomplete. |
| Shared custom-Effect configuration | Missing dependency exits 0 without diagnostics. |
| Direct rule-level `additionalHooks`; valid dependency control; CLI override | Direct invalid case exits 1; valid control exits 0. The recorded override combination again exits 0 on the invalid case. No corrected configuration or general option-equivalence claim follows. |
| Invalid configuration; absent input; seven-file directory | Config/no-input fail with exit 1. Directory yields the same four-diagnostic multiset. Empty parsed diagnostics cannot turn a command/configuration failure into success. |

The inventory lacks the exact React IDs `component-hook-factories`, `config` and `gating`; that does not disprove every equivalent diagnostic. The two fresh tagged files independently fetched from official primary URLs exactly match the retained and prior-tag bytes: `rules_of_hooks.rs` SHA256 `35e4a166253a27d0990bddfdb66b14772b986db2af5ea2083f4cfa1da2d4682b`, `exhaustive_deps.rs` SHA256 `0c9a8372f5a72398dd63a747d35a978b4015626cd40d50573cf4fcfa062ddd3d`. Inspected callee-name classification and rule-level/shared option handling as supporting source evidence; these two files do not establish unchanged whole-binary behavior or build provenance.

Fresh read-only [official npm latest metadata](https://registry.npmjs.org/oxlint/latest) independently reports 1.87.0. The [official release](https://github.com/oxc-project/oxc/releases/tag/oxlint_v1.87.0) and GitHub API corroborate non-draft/non-prerelease status and `2026-10-05T11:04:25Z`. Official registry metadata corroborates hook plugin 7.1.1's `@babel/core ^7.24.4`, gensync latest `1.0.0-beta.2` and highest non-prerelease `0.1.0`. This updates dated metadata observations without rerunning or accepting the earlier complete Babel/React graph.

[React Hook rules](https://react.dev/reference/eslint-plugin-react-hooks/lints/rules-of-hooks) and [Effect dependency guidance](https://react.dev/reference/eslint-plugin-react-hooks/lints/exhaustive-deps) support the semantic oracle and custom-Effect options; upstream checker alias behavior was not inferred. [Oxlint's plugin policy](https://oxc.rs/docs/guide/usage/linter/plugins.html) still identifies native compiler analysis as experimental. No such rule was enabled or adopted. All ten protected application/source/original-study guard hashes remain unchanged after reproduction.

## Remaining obligations

Enforceable alias/custom-Effect/configuration policy, broader recommended-preset dispositions, real application coverage, retained ESLint/TypeScript/refresh behavior, editor/CI failure handling, full latest-mutually-compatible stable graph, reproducible selected locks, security/licence/provenance review, runtime/browser validation, MA-013 and independent/founder acceptance remain open. A stable release label, integrity match or accurate evidence PASS cannot close them. No fix, dependency/configuration change, application execution, installation, deployment, model revision or production selection was performed. Only this receipt was authored.

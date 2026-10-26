# Native hook conformance evidence — independent v1 review

Date: 2026-10-05. Reviewer: `review_semantic_preparation_v1`, independent of
the producer. Verdict: **PASS**, bounded evidence accuracy; candidate unselected.
Task status: DOING. No complete graph, production configuration or Phase 1 approval.

## Exact inputs and review boundary

The [frozen input manifest](../../../output/research/native-lint-conformance-2026-10-05/review-inputs.json)
has SHA-256 `d61a3d279a383648619d0765938be8e14c5fdf28a567a0353b4330f77f332201`.
Independently verified all 52 listed files against their exact hashes and byte sizes
before and after review. The manifest retains the complete input identity list.

| Principal input | SHA-256 |
|---|---|
| Preserved `refresh-evidence.reviewed.md` | `0ddacac850efef76d26b9044043dee1c683714988b59271bdad5c405cf8c6325` |
| `run_probe.py` | `749219e45932f92ab8b73c9489a4adcf9597e240b745c770fedc3758d09d3ca7` |
| `receipt.json` | `ad2050d7537d5adde4cf4ef8aed268b930b7e5e3ce5c4427cdd76cdd4b7606ca` |
| `tag-source-receipt.json` | `fe3a7c312a94594299a37267f67f22edde0d6eafbb3248b5331e6c9151300b97` |
| Tagged `exhaustive_deps.rs` | `0c9a8372f5a72398dd63a747d35a978b4015626cd40d50573cf4fcfa062ddd3d` |
| Tagged `rules_of_hooks.rs` | `35e4a166253a27d0990bddfdb66b14772b986db2af5ea2083f4cfa1da2d4682b` |
| `native-lint-recommended-coverage.json` | `86bbe2d8e65bde10d1719cd2c822e8739e4de78fb0f1590451749e0a920ca123` |

Scope is the earlier 17-rule inventory at preserved refresh lines 274–304 and the
new Native hook conformance and configuration boundaries section, lines 403–438,
including its fixtures, commands, raw outputs, oracle, source and protection claims.
Other registry/resolver, audit, SBOM, licence, binary/provenance and build subjects
in the same document retain their prior review scopes and are not accepted here.
Current AGENTS/constitution stable-graph, experimental-rule exclusion, protected
prototype, independent review and evidence-versus-runtime rules control this review.

## Independent CLI and source verification

Inspected the producer script without executing it. Independently invoked each
of its 14 recorded read-only CLI commands directly, using the existing isolated
Oxlint entry point, frozen configurations/fixtures and recorded working directory.
Nothing was installed, generated, fixed or written by these commands. Current
version commands reproduce Node `v24.14.0` and Oxlint `Version: 1.86.0`.
Compared exit codes, diagnostic-code multisets, file counts, active-rule counts
and empty stderr against the captured results; all reproduced. Timing and diagnostic
ordering are not asserted byte-identical.

| Cases | Reproduced result |
|---|---|
| Namespace valid Effect | Exit 0; no diagnostic. |
| Namespace conditional state, custom conditional `useSession`, hook-shaped import alias `useCounter` | Each exits 1 with `react-hooks(rules-of-hooks)`. |
| Namespace Effect missing `value` | Exit 1 with `react-hooks(exhaustive-deps)` at the actual missing dependency. |
| Hook renamed `state`; Effect renamed `effect` | Each exits 0 with no diagnostic despite the semantic violation. |
| Invalid JSON configuration; absent source path | Each exits 1. Configuration error is plain text; absent path explicitly says no files and prefixes its JSON fragment. A caller cannot require pure JSON or mistake empty diagnostics for success. |
| Seven-file base directory | Exit 1; seven files, four diagnostics: three hook-order and one dependency violation. No broader application discovery is proved. |
| Shared `settings.react-hooks.additionalEffectHooks` custom Effect | Missing dependency exits 0 with no diagnostic. |
| Rule-level `additionalHooks`, config-only invocation | Missing dependency exits 1; complete `[value]` exits 0. |
| Same rule-level option with paired CLI allow/deny combination | Missing dependency exits 0. The observation isolates the combination, not one individual flag. |

All twelve parsed lint invocations report exactly two active rules. Config-only
custom-Effect probes disable the default correctness category and explicitly retain
the two errors/options; base/override probes use `--allow all` followed by the two
named `--deny` flags. No compiler or JavaScript plugin rule, fix flag, experimental
analysis, application source invocation or production lint script was executed.
Independently matched the ten named protected files to both before/after maps and
current bytes, then checked them again after the read-only runs. This finite
protection check is not a whole-repository forensic proof.

Fetched both recorded `oxlint_v1.86.0` source URLs read-only into memory; hashes
and byte lengths match the preserved source receipt. Inspected relevant code:
ExhaustiveDeps config uses camelCase `additionalHooks` and its matcher; RulesOfHooks
recognizes hook names, and separately reads the shared setting for Effect Event
context. Thus the dependency fixture's shared-setting miss must not be generalized
to every use of shared settings. Source correspondence is not a source-to-binary
attestation.

## Official oracle and recommended-rule inventory

Checked [React's hook-order rules](https://react.dev/reference/rules/rules-of-hooks)
and [dependency/custom-Effect guidance](https://react.dev/reference/eslint-plugin-react-hooks/lints/exhaustive-deps)
on 2026-10-05. Conditional calls remain invalid when an imported callable is renamed;
omitted reactive values remain omitted. The custom-Effect fixture tests the declared
callback/dependency contract; its absent implementation module is not runtime-tested.
Expectations come from that contract, not copied native classifier logic. The
evidence expressly declines upstream alias parity; no upstream plugin was executed.

[React's recommended preset](https://react.dev/reference/eslint-plugin-react-hooks)
still lists the same 17 identifiers and includes compiler diagnostics without
requiring compiler adoption. Independently reran only `--rules --format json`:
the complete metadata of all 14 matching identifiers agrees with the inventory;
`component-hook-factories`, `config` and `gating` have no identical registered
React identifier. This is registration correspondence, not renamed/aggregate parity.
Checked all twelve listed compiler per-rule pages and
[Oxlint's plugin policy](https://oxc.rs/docs/guide/usage/linter/plugins.html): those
matches use compiler analysis, whose native group remains experimental/off by
default. Listing them did not execute them. Context7 `/websites/oxc_rs_guide_usage`
was queried on this date for configuration, hook rules and CLI precedence;
official pages and tagged source supply the precise evidence. Earlier direct HTTP
documentation failures remain recorded rather than relabeled successful downloads.

## Findings and remaining obligations

No actionable finding in the evidence claims. The observed misses and invocation
trap are already explicit held limitations, not a successful conformance or coverage
waiver. A production proposal still needs enforceable naming/configuration policy,
owned custom-Effect coverage, stable disposition for the broader preset, actual
ESLint/TypeScript/refresh behavior, editor/CI/file-scope failure propagation, full
coupled platform/build/lock/provenance evidence and founder compatibility acceptance.

Only this review receipt was written. This PASS neither selects Oxlint/Node nor
proves full semantic detection, upstream parity, application behavior, enterprise
readiness or production stability. No dependency/settings/source change, installation,
experimental-rule execution, commit, push or deployment is authorized or performed.

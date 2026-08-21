# Phase 1 Foundation SEO Evidence Review — Iteration 1

**Verdict:** REVISE

**Review date:** 2026-07-19 (Asia/Karachi)

**Finding count:** 2 MEDIUM; 0 BLOCKER; 0 HIGH; 0 LOW

**Revision cycle:** Iteration 1 of a maximum two coordinator revision cycles

## Reviewer independence

I reviewed this foundation slice independently and did not produce artifacts 01
through 07. I did not modify the producer artifacts, application source,
dependencies, infrastructure, governance state, external systems, public content,
or search accounts. The original market/SEO producer was interrupted after
creating and locally validating artifact 02; this review assessed the stable file
and its evidence directly rather than treating the interruption as a completed
handoff.

## Scope and inputs

The review tested whether the current market/reference evidence is authoritative,
fairly qualified, and correctly translated into entity, intent, route, semantic
HTML, canonical, status, schema, sitemap, robots, crawler, editorial, conversion,
measurement, and claims rules.

The following inputs were read in full:

- `AGENTS.md`, `.specify/memory/constitution.md`, `PROJECT.md`,
  `PROJECT_STATE.yaml`, `TASKS.md`, `DECISIONS.md`, and `RISKS.md`;
- `docs/software-definition/README.md`, `01-system-boundaries.md`,
  `02-ai-dev-tooling-and-mcp.md`, and
  `03-autonomous-ai-development-workflow.md`;
- `docs/decisions-log.md` as routed by the software-definition README;
- `docs/phase-1-foundation/README.md`; and
- foundation artifacts `01-product-requirements.md` through
  `07-decision-requirement-traceability.csv`.

The initial reviewer contract named three nonexistent software-definition files.
The coordinator confirmed that this was a contract path mistake and directed use
of the existing approved four-file software-definition package plus the detailed
decision log. This correction is an input limitation, not a project finding.

Approved decisions were treated as superior to proposed requirements, research,
hypotheses, prototype evidence, and reference-site patterns.

## Method and current-source verification

The audit combined complete repository inspection, parsing of both JSON ledgers
and the CSV traceability matrix, the repository's read-only foundation validator,
and a bounded current-source check. No paid source, account, form, contact, public
submission, cookie acceptance, or third-party write was used.

All sources below were accessed on 2026-07-19. The check was deliberately limited
to the claims used by this slice.

| Evidence area | Current primary source | Verification result |
|---|---|---|
| JavaScript SEO and initial HTML | [Google JavaScript SEO basics](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics) | Current guidance still describes crawl, render, and index phases; recommends meaningful status codes and crawlable links; and states that server-side rendering or prerendering remains useful because it is faster and not every bot executes JavaScript. Artifact 02 correctly treats complete initial HTML as a stricter project requirement and a multi-audience reliability benefit, not as a ranking guarantee. |
| Canonicalization | [Google canonicalization methods](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls) | Current guidance, updated 2026-07-10 UTC, still distinguishes redirects and `rel="canonical"` as strong signals, sitemap inclusion as weaker, and consistent internal links as helpful. It also warns against using `robots.txt` for canonicalization or `noindex` to influence canonical selection. This supports the clean-host/path policy but exposes finding SEO-R1-02. |
| Structured-data truthfulness | [Google structured-data policies](https://developers.google.com/search/docs/appearance/structured-data/sd-policies) | Current guidance requires markup to represent visible, current, relevant content and does not guarantee a rich result. The slice's conservative schema allowlist and visible-evidence gates are sound. |
| People-first and AI-assisted content | [Google people-first guidance](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) and [generative-AI guidance](https://developers.google.com/search/docs/fundamentals/using-gen-ai-content) | Current guidance continues to emphasize original value, sourcing, identifiable expertise, accuracy, quality, and relevance; scaled pages without user value may violate spam policy. The slice's named review, original-value, evidence, and anti-mass-generation rules are supported. |
| Robots and `noindex` separation | [Google robots meta guidance](https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag) | Current guidance states that a crawler must be allowed to access a page to read its page-level directive. The slice correctly makes authentication/publication isolation the control for private content and does not treat `robots.txt` as privacy or access control. |
| Google model-use token | [Google common crawlers](https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers) | Current guidance, updated 2026-07-14 UTC, says `Google-Extended` is a robots token rather than a separate request user agent, controls both specified Gemini training and grounding uses, and does not affect Google Search inclusion or ranking. The mixed-purpose nature is not represented in the downstream class model; see SEO-R1-01. |
| OpenAI crawler distinctions | [OpenAI crawler documentation](https://developers.openai.com/api/docs/bots) and [publisher FAQ](https://help.openai.com/en/articles/12627856-publishers-and-developers-faq) | Current guidance distinguishes `OAI-SearchBot`, `GPTBot`, and user-triggered `ChatGPT-User`; the first two controls are independent, while `ChatGPT-User` is not an automatic crawler and robots rules may not apply. Artifact 02 accurately distinguishes search and training bots but omits the user-triggered control boundary; see SEO-R1-01. |
| Core Web Vitals | [web.dev threshold methodology](https://web.dev/articles/defining-core-web-vitals-thresholds) | The current table still defines good p75 thresholds as LCP at most 2.5 seconds, INP at most 200 milliseconds, and CLS at most 0.1. The figures are translated consistently across artifacts 01, 03, 04, and 07. |
| Search reporting | [Search Console performance metrics](https://support.google.com/webmasters/answer/7576553), [branded-query analysis](https://support.google.com/webmasters/answer/17010961), and [dimension/data limitations](https://support.google.com/webmasters/answer/17011259) | Clicks, impressions, CTR, average position, query/page/country/device dimensions, canonical-URL attribution, anonymized queries, and row truncation remain documented. The branded filter may be unavailable at low impression volume and classifications may be imperfect; the slice appropriately treats platform data as diagnostic and blocked until ownership, but this remains a launch measurement limitation. |
| Search notification and Bing | [IndexNow protocol](https://www.indexnow.org/documentation) and [Bing Webmaster API](https://learn.microsoft.com/en-us/bingwebmaster/) | IndexNow still says an HTTP 200 indicates receipt of the URL, not indexing. The Bing API page still documents registered-site traffic, link, keyword, crawl, URL, and sitemap capabilities, though its displayed update date is 2022-10-13. No account, ownership, or capability-tested state was inferred. |

### Source access and limitations

- All cited official pages above were reachable during this review. The OpenAI
  Help FAQ, which artifact 02 records as returning `403` to its validation client,
  was readable through the current web path. That difference is an automated
  client-access condition, not an artifact correctness defect.
- The founder references and cited supporting pages returned HTTP 200 in bounded
  current GET checks. The initial-response signatures remained consistent with
  artifact 02: ScienceSoft exposed extensive conventional semantic content;
  Lusion exposed text, links, and canvas-led presentation with no initial
  canonical observed; Bruno Simon's main route remained canvas-led while
  `/html/` exposed a text-and-link alternative; and Active Theory's initial work
  response remained JavaScript-dependent.
- This reviewer did not repeat a site-wide crawl, backlink analysis, keyword
  dataset, accessibility conformance audit, commercial due diligence, or complete
  rendered-browser audit. Dynamic rendered states can change. Artifact 02 already
  limits its conclusions to a page-level dated snapshot and does not present
  “not observed” as proof of site-wide absence.

## Evidence-quality assessment

### Reference-category fairness

PASS. ScienceSoft is treated as a broad enterprise-services benchmark; Lusion and
Active Theory as indirect immersive-studio references; and Bruno Simon as an
individual portfolio/substitute experience. The comparison uses common dimensions
without ranking unlike businesses. Vendor facts are described as what the sites
publish, not independently verified Hengshi facts. The report expressly prohibits
copying identities, taxonomies, interaction, claims, scale, clients, awards, or
outcomes.

### Observation, inference, hypothesis, and decision separation

PASS. Artifact 02 defines and uses all four labels. Its reference-page statements
are observations, cross-site synthesis is identified as inference, and Hengshi
applications are hypotheses or implications. Approved audience, sector,
conversion, proof, semantic, and language rules are isolated as existing
decisions. Artifact 03 keeps keyword clusters and cornerstone briefs as
hypotheses; artifact 04 similarly labels jobs and metrics whose baselines do not
exist. No competitor fact is silently converted into an approved requirement.

### Entity collision and naming boundary

PASS. Current official pages confirm multiple unrelated “Hengshi” entities,
including HENGSHI SENSE in an adjacent enterprise Data/AI category, an electronics
supplier, and fiberglass businesses. The inference that the full “Hengshi Design”
name and verified entity package are needed is proportionate. The evidence does
not claim trademark unavailability, infringement, or measured consumer confusion.
Legal identity, domain control, naming clearance, verified profiles, people, and
contact facts remain founder/legal gates.

### Keyword-hypothesis quality

PASS. Candidate phrases derive from the approved service taxonomy, audience, and
sector order and are expressly unmeasured. No search volume, difficulty, rank,
traffic, market share, or conversion forecast is invented. The validation sequence
requires proof readiness, buyer-language evidence, location-aware result-intent
sampling, one-primary-page mapping, and post-launch reporting before priority is
approved. “Best,” “top,” price, customer, location, and compliance terms remain
evidence-gated.

## Policy translation assessment

| Area | Assessment |
|---|---|
| Semantic HTML and WebGL | PASS. Each indexable route must expose meaningful initial HTML, ordinary links, and conversion without JavaScript or canvas. The 3D route is optional enhancement and links to canonical semantic pages. |
| Canonical, redirects, and status codes | PASS except SEO-R1-02. Host/path normalization, one-hop redirects, meaningful `404`, deliberate `410`, bounded `503`, and soft-404 avoidance align with current guidance. The mixed query-variant machine rule is not deterministic. |
| Structured data | PASS. The eight-type allowlist is truthful and deliberately narrow. `Service`, `Article`, `Person`, `ImageObject`, and `VideoObject` are gated by visible evidence; reviews, ratings, offers, prices, awards, locations, certifications, and invented people are prohibited. Rich results are not promised. |
| Sitemaps and route activation | PASS. The active immutable publication manifest is the source; only canonical `200` indexable instances enter sitemaps. Collection and detail patterns remain out until an approved public state exists. The proposed `/industries` parent remains clearly founder-gated. |
| Robots, privacy, and unpublished content | PASS. Public crawl policy is distinct from authentication, authorization, release isolation, and status/`noindex` controls. Draft, rejected, preview, admin, session, staging, and defense content stay out of public artifacts and search/AI notification. |
| Provider crawler policy | REVISE. The policy remains gated and dated, but its classes do not yet model user-triggered and mixed-purpose controls correctly; see SEO-R1-01. |
| Editorial integrity | PASS. Named qualified review, primary evidence, original Hengshi value, limitations, ownership, independent review, founder approval, and anti-scaled-content rules are explicit. Work, Demos, Insights, Experts, and Trust remain separate evidence classes. |
| Search and conversion measurement | PASS with stated limitation. Qualified organic bookings lead; traffic and average position remain diagnostic. Search reporting limitations, cookieless aggregate measurement, unknown attribution, no causal inference, and unavailable baselines are preserved across artifacts 03 and 04. |
| Claims and proof quarantine | PASS. All 33 ledger entries use fail-closed dispositions; all six prototype seeds and placeholder media remain quarantined. No unverified legal fact, expert, profile, office, contact, client, result, certification, or current assurance is publication-eligible. |

## Cross-artifact consistency

- Artifacts 02 and 03 consistently preserve audience, agriculture/mining order,
  entity disambiguation, no-volume keyword hypotheses, semantic-first output,
  ethical authority, and founder/legal gates.
- Artifact 04 uses the same direct 30-minute qualified-booking outcome and keeps
  AI, human help, WebGL, proof review, budget, and unapproved fields optional. It
  introduces no SEO volume, rank, or causal claim.
- Artifact 05 is fail-closed and consistent with the route and schema gates in
  artifacts 03 and 06.
- Artifact 06 contains 33 unique route paths/patterns, exactly five wing hubs and
  ten service routes, the eight allowed schema types, and seven excluded-surface
  classes. Static and detail-route activation is conditioned on approved content
  and the atomic release.
- Artifact 07 covers D-001 through D-024 exactly and keeps later Phase 1
  dependencies visible.
- No cross-artifact contradiction was found outside the two policy-specific
  findings below.

## Findings

| ID | Severity | Artifact and location | Problem | Evidence | Required correction |
|---|---|---|---|---|---|
| SEO-R1-01 | MEDIUM | `02-market-competitor-seo-evidence.md` §7.5; `03-seo-entity-route-editorial-strategy.md` §8.2; requirement SEO-013 | The crawler model distinguishes automatic search and training bots but combines “user-triggered fetchers” with user-facing answer/search crawlers and provides no mixed-purpose class. That is not sufficient for current provider behavior: `ChatGPT-User` is user-triggered and robots rules may not apply, while `Google-Extended` is one token covering both specified training and grounding uses. A simple allow-search/block-training mapping is therefore not technically separable for every provider. | Current [OpenAI crawler documentation](https://developers.openai.com/api/docs/bots) and [Google common-crawler documentation](https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers). Artifact 02 itself correctly says separation is expressible only for some providers, but artifact 03's operational classes cannot preserve that nuance. | Add a dated evidence/control matrix that separately represents automatic search/answer crawlers, training crawlers, user-triggered fetchers, and mixed-purpose tokens. For each current example, record token or request identity, purpose, whether robots applies, whether uses are separable, verification source/date, proposed default, and founder/legal/privacy/security gate. Explicitly state that `ChatGPT-User` cannot be governed as if it were `OAI-SearchBot`, and that `Google-Extended` couples the documented Gemini uses. Keep exact production directives unapproved and temporal. |
| SEO-R1-02 | MEDIUM | `06-canonical-route-inventory.json` excluded surface “/search, filter URLs, tracking parameters, and sort variants”; `03-seo-entity-route-editorial-strategy.md` §§5.3 and 8.2 | The machine-readable value `noindex_or_canonical_to_clean_document` merges different URL classes and leaves the operative control as an unresolved “or.” Internal search, tracking parameters, filters, and sort variants do not necessarily share the same response/canonical rule. A generator or validator cannot determine whether to emit `noindex`, a clean canonical, a redirect, or only clean internal links, and could create conflicting signals. | Current [Google canonicalization guidance](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls) distinguishes canonical signals and warns against using `robots.txt` for canonicalization or `noindex` to influence canonical choice; [robots meta guidance](https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag) requires crawl access for `noindex` to be read. Artifact 03 already gives tracking and internal-search variants different prose treatment, confirming that one combined enum is insufficient. | Split the machine-readable entry into deterministic classes at minimum for internal search, tracking parameters, and filter/sort variants. Assign each class one explicit status/indexing/canonical/internal-link/sitemap rule and any parameter allowlist. Make the validator reject ambiguous `*_or_*` indexability values and reject an undocumented combination of `noindex` and canonicalization signals. Keep private data behind access controls, not URL directives. |

## Verdict

**REVISE.** There are no BLOCKER or HIGH findings, and the evidence, reference
qualification, entity boundary, keyword boundary, semantic publication model,
schema allowlist, claims quarantine, editorial rules, and measurement model are
otherwise strong. PASS is not available in iteration 1 because both MEDIUM
policy-correctness findings affect deterministic crawler and indexing behavior.
They are narrow enough for one bounded coordinator revision followed by validator
rerun and independent iteration-2 verification.

## Residual risks and human gates

The following are not artifact defects and remain outside this reviewer's
authority:

- legal entity, controller, jurisdiction, contact/disclosure facts, domain
  ownership, naming/trademark clearance, and approved profiles;
- public category/positioning language and every substantive public claim;
- verified cases, demos, experts, authors, reviewers, owners/backups, images,
  datasets, rights, outcomes, awards, certifications, and sector expertise;
- founder acceptance or rejection of `/industries`;
- exact crawler registry and policy after founder, legal, privacy, and security
  review;
- paid research, buyer surveys/interviews, or keyword tooling;
- Search Console, Bing Webmaster, IndexNow, DNS, and production notification;
- conversion baselines, targets, attribution windows, and named operating owners;
  and
- complete Phase 1, application, publication, UAT, or launch acceptance.

Current source pages and reference sites may change after the review date. Search
engines retain discretion over crawling, canonical selection, indexing, snippets,
rich results, ranking, and answer inclusion. No implementation or outcome
guarantee follows from this review.

## Validation evidence

Before authoring this report, the inspected read-only command
`docs/phase-1-foundation/validation/validate-foundation.ps1` completed with
**37 passes and `RESULT: PASS`**. It confirmed JSON/CSV parsing, 112 unique
requirements, 33 unique fail-closed claim entries, six quarantined seeds, 33
unique route paths/patterns, allowed schema types, seven exclusions, exact
D-001–D-024 traceability, local-link integrity, marker/secret scans, whitespace,
and `git diff --check`. That structural pass does not resolve the two semantic
policy findings above.

Post-write report-only checks found no unresolved marker, local-link target,
secret-shaped value, excessive source quotation, or invalid whitespace. The
report ends with a newline, and `git diff --check --
docs/phase-1-foundation/reviews/seo-evidence-review-iteration-1.md` returned exit
code 0. The full foundation validator was rerun after report creation and remained
at 37 passes with `RESULT: PASS`.

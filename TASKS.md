# Hengshi Design v1 — delivery tasks

Status: DOING. D-097 approved 2026-10-25. Commits and pushes remain deferred.

The founder assigns one outcome from the discussion chat; finish, report and stop.
Read AGENTS.md, constitution and PROJECT_STATE.yaml; use relevant [definitions](docs/software-definition/04-reconciliation-map.md).
D-097 supersedes the universal Phase 1 build gate and hard correction counters.

## Delivery sequence — full agreed scope retained

| Increment | Status | Exit |
|---|---|---|
| I1 Brand application and shared foundations | DOING | HSD-001 designs founder-accepted; local homepage/navigation verified; commit deferred. |
| I2 Complete semantic website/content platform | DOING | HSD-002 assigned; Services designs prepared; broader public/staff scope remains. |
| I3 Complete 2D service journeys | TODO | AI, consent/privacy, human handoff, booking and recovery work end to end with truthful external-state boundaries. |
| I4 Full 3D World | TODO | Accepted campus, movement/streaming, sound, department/help journeys and four-stream parity implemented and verified. |
| I5 Integrated launch qualification | TODO | Required operational, legal/content, account, device/load/accessibility, staging and deployment gates satisfied. |

All fourteen subjects and [accepted scope](docs/software-definition/05-consolidated-goal.md) remain; unfinished B01/3D do not hold unrelated 2D delivery.

## HSD-001 — homepage and navigation

Status: DOING. Founder accepted references 246:7658 / 246:7883 and navigation.
Local implementation: `apps/web/site`; previous nine Chromium passes were rerun
successfully in HSD-002's combined sixteen-test suite 2026-10-26; commit deferred.
Homepage and Services preview: http://127.0.0.1:5174/; other destinations remain outside this package.

## HSD-002 — semantic Services browsing

Status: DOING. Founder accepted the presented designs/copy and authorized implementation 2026-10-26.
Reuse D-097, PROJECT taxonomy, canonical route inventory and approved UX §4.4.
Six corrected Figma references in GOmLP6Cv96l768ueSrZ5Dg (desktop / 320px):
Services `262:4660 / 262:4767`; wing `262:4903 / 262:4980`; detail `262:5072 / 262:5161`. Exports: `artifacts/hsd-002/design/final/`.
One independent design review found footer/utility/arrow defects; corrected; final pixels inspected.
All five wings/ten services have fit proofs at both widths; static checks, not runtime or WCAG proof.
Accepted local copy: `artifacts/hsd-002/design/content.json`; no invented evidence/people; publication held.
TODO later: enrich colour/graphics across the website using the accepted rich brand after functional delivery; current restrained designs may proceed per founder 2026-10-26.
Implemented existing React prerender/hydration and Vite middleware extensions; shared
Header/Footer/tokens, one catalogue, index/wing/detail templates, ordinary links,
breadcrumbs, direct HTML, metadata, canonical redirects and semantic HTTP404. No new package.
Use [Vite5 SSR/SSG](https://v5.vite.dev/guide/ssr) and [React18 hydration](https://18.react.dev/reference/react-dom/client/hydrateRoot), queried via Context7 2026-10-26.
Existing nine-root build/test lock closure inspected (182 records incl. optional platforms); no upgrade/production qualification; preserve prior site/prototype.
New checks: build/typecheck PASS; affected checks then combined16 Chromium tests PASS on built preview (9 homepage +7 Services); representative axe scans found0 violations; actual1440/320 pages inspected. This is local behavior, not launch/WCAG certification.

## Completion and retained gates

DONE requires relevant tests and an approved commit; report deferred commit separately.
Launch qualification remains separate; state stays within50 lines. Stop after HSD-002.
No automatic next task/chat/goal. Git, migrations, destructive actions, providers/credentials,
spending, publication and deployment require applicable approval.

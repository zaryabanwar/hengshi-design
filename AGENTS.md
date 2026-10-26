
## Hengshi Design Project Rules

Current delivery authority: **D-097 (2026-10-25)**. Deliver the accepted brand,
then the complete 2D website/platform, then the full 3D experience, then launch
qualification. Preserve the full agreed v1 scope. This supersedes the blanket
Phase 1 implementation hold, B01-as-universal-prerequisite sequencing and hard
revision caps in older documents, frozen contracts and skills for this project.
Read the current task, then only the subject definitions it needs; historical
review packets are evidence, not a mandatory startup reading list.

Starting point for every repository-changing task:

1. `AGENTS.md`
2. `.specify/memory/constitution.md`
3. `PROJECT.md`, `DECISIONS.md`, and `PROJECT_STATE.yaml`
4. `docs/software-definition/README.md`
5. The relevant approved feature spec under `specs/`
6. `TASKS.md` and the active plan/task artifacts named there, when applicable.

For Spec Kit features, read the active `spec.md`, `research.md`, `data-model.md`,
contracts, `plan.md`, and `tasks.md` before implementation when those files exist.
Use the authority order in the constitution: current founder approval and
governance, approved decisions, approved requirements, approved software/design
artifacts, current implementation evidence, then unreconciled or historical
material. A material conflict blocks only the affected work and must be recorded.

Workflow approval gates:

1. If the task changes product scope, architecture, workflow rules, app structure,
   API contracts, auth, security, infrastructure, data, production UI, 3D, AI, or
   publication behavior, confirm the relevant approved docs/specs exist before
   coding.
2. Implementation requires the relevant increment's approved scope, design,
   contracts and qualified coupled dependencies, not completion of every future
   increment. Unfinished 3D definitions do not block unrelated 2D delivery.
3. Work one user-assigned outcome through definition, implementation and relevant
   tests, then stop and report. Review coherent design batches and changes touching
   money, security or external systems independently; also review when requested.
   Do not commission independent reviews for routine prose, links or every fix.
   There is no hard two/three-cycle cap. Continue safe in-scope corrections while
   evidence shows progress; diagnose repeated failures and escalate only an actual
   scope/risk/cost/authority decision or missing input, not a counter.
   This applies to safe local corrections; provider retry/rate/spend limits and
   deployment/authentication safety stops are not waived.
4. Record safe, reversible, unambiguous assumptions. Stop for a founder decision
   when a missing choice materially changes scope, risk, cost, public claims, or
   architecture.
5. Do not create branches, commits, remotes, migrations, paid activations,
   external design writes, credential changes, production promotions, deployments,
   or other irreversible changes without their explicit applicable approval.
   D-098 below supplies standing approval for scoped commits and normal pushes.

Standing Git authorization — D-098 (2026-10-26):
- When an assigned task/session finishes its coherent work and relevant checks
  pass, commit that work to local `main` and push to the existing `origin/main`.
  Do not ask for commit/push permission again. This applies to Hengshi Design
  across Codex and Claude until the founder changes it; it is not a global hook.
- This supersedes older commit/push deferrals in prompts, skills and checkpoints,
  including `commit_authorized: false`. A later explicit founder hold takes priority.
- Stage only the assigned outcome and its necessary docs/tests/assets. Preserve
  unrelated or concurrent work; do not sweep it into a session-close commit.
  Read-only/discussion sessions with no changes need no empty commit.
- Verify branch, staged diff and existing remote before committing. Never force
  push, reset, discard edits or rewrite shared history. If not on main, or a
  conflict/divergence prevents safe delivery, report the specific Git blocker;
  do not silently switch branches with dirty work or overwrite remote changes.
- Do not commit secrets, machine-local credentials, browser profiles or caches.
  Failed/incomplete work is not DONE merely because a session ends. Report the
  test result, commit hash and confirmed push result separately; retain a clear
  checkpoint if checks or push fail. No automatic next task or deployment.
- Scope/design acceptance, migrations, new remotes, destructive actions, provider
  changes, spending, external design writes, publication and deployment retain
  their own gates. Git approval does not grant those actions.

For UI work, generate or reference the relevant approved Google Stitch or Figma
screen before implementation. Every indexable route must produce complete semantic
HTML before JavaScript, and Quick Access must provide an equivalent accessible
non-WebGL journey.

For version-sensitive framework, library, API, cloud, browser, CI, container, and
Blender decisions, use Context7 and official primary documentation first. Confirm
the release in the official registry, evaluate coupled packages as a compatibility
graph, and record the dated evidence and rollback. Preview, beta, RC, nightly, and
experimental dependencies cannot be production requirements.

First-production v1 rules, reaffirmed by the founder 2026-10-04:

- The product and its current production-definition package are v1. No agent may
  describe this first development as a v2/v3 product or invent a later release.
  Keep real dependency, API/schema-format and historical evidence identifiers
  accurate; those identifiers are not product release numbers.
- Select the latest mutually compatible stable set across the complete coupled
  graph. Independently newest versions are observations only, never a selected
  stack. Peer ranges alone do not prove compatibility: resolve, test, review and
  reproducibly lock the set. Apply this to every tool/framework/library/runtime,
  renderer/exporter, browser, database and external API used by the project.
- Remove contradictory standalone all-latest instructions from current authority
  and templates. A blocked newest release needs concrete incompatibility evidence
  and the approved exception/recheck process; convenience alone is not a reason.
- Europe is the first target market; no European office/location is implied.
- Deployment/provider/cost planning is deferred. Azure and AWS are candidates;
  neither is selected. Prefer the lowest feasible cost/free services when planning
  resumes, without assuming a free tier satisfies product/privacy/recovery needs.
- Microsoft 365 subscription/setup is not a prerequisite. Retain Outlook/Teams
  integration intent and verify each required account/API capability separately.

Testing rules, reaffirmed by the founder 2026-10-04:

- Derive expected outcomes from approved requirements and independently verified
  external contracts; exercise the actual implementation at its public boundary.
  Do not copy implementation logic into the test's expected result.
- Use focused unit tests for meaningful logic, integration tests for database/API
  and adapter behavior, and browser tests for user journeys. Include failures,
  authorization denial, boundary inputs and concurrency where the feature needs
  them. Reuse framework fixtures and run affected tests before a broad batch run.
- Documentation phrase/count/hash checks are artifact-integrity checks only.
  They cannot establish feature correctness, accessibility, security or readiness.
  Do not add tests for ordinary prose edits or brittle wording assertions.
- Schema fixtures test the schema/validator only until the application's actual
  request, persistence or publication boundary is exercised. OpenAPI declarations
  and mocked browser responses likewise do not prove backend enforcement.
- Report artifact validation and runtime test results separately. Never use a
  large check count or a passing definition validator as product-completion proof.

For frontend UI/UX changes, run Playwright browser verification for the changed
surfaces; when Playwright MCP/browser automation is exposed by the active agent
host, use it for live inspection and screenshots in addition to Playwright CLI
tests.

MCP source of truth:

- The canonical local MCP inventory is the VS Code user config at
  `%APPDATA%\Code\User\mcp.json`.
- Before reporting that Context7, Stitch, Playwright MCP, Postgres MCP, GitHub MCP,
  or another MCP is “not set up”, inspect that config or the documented inventory.
- Installed, configured, authenticated, protocol-tested, and capability-tested are
  distinct states. Report the exact verified state.
- If a configured server is absent from the active tool list, report an active-host
  exposure gap and use the documented safe direct MCP/CLI fallback when allowed.
- Never copy API keys, bearer tokens, connection strings, or other secret values
  from `mcp.json` into source, docs, logs, evidence, or chat.

Figma workflow, clarified by the founder 2026-10-15 (D-095):

- Prefer Figma MCP within the 20-call allowance; batch related preparation,
  construction and verification rather than spending calls on routine checks.
  Use verified provider included-call availability for routing; attempted and
  conservatively metered ledger counts are separate from actual quota consumed.
- Once that allowance is used, continue through computer use in Figma. Use
  available included Figma AI features, including the Figma Design agent for
  native canvas work and Make where suitable for interactive prototypes, to help
  complete the agreed design work. Check actual capability/credits; do not assume
  that a generated prototype also supplies editable native design references.
- This instruction supersedes the native-only/no-AI method restriction in D-094
  and repeated per-call/method approvals for already-approved design scope.
  It does not authorize extra MCP allowance, paid activation, publication,
  sharing/account changes, destructive cleanup or new product scope.
- Preserve existing references, use the approved requirements and brand, and
  inspect generated results. AI output does not replace independent review or
  founder acceptance. Never treat a tool-route preference as a ban on AI.

Current non-negotiables:

- Hengshi Design positions as an evidence-led, premium, platform-oriented
  innovation delivery company.
- Preserve the existing application and exterior GLB as protected prototype
  evidence; neither is production authority.
- Frontend families remain React + TypeScript + Vite + TailwindCSS + React Three
  Fiber on the approved latest-mutually-compatible stable matrix.
- Backend families remain FastAPI + SQLAlchemy + Alembic + PostgreSQL on the
  approved latest-mutually-compatible stable matrix.
- Target PostgreSQL 18's current stable minor when GA in the eventual approved provider/region;
  otherwise use the newest regional GA major under an ADR and quarterly recheck.
- Provider selection is deferred to a later Azure/AWS comparison; historical
  deployment plans cannot select it. WebGL remains the production 3D renderer;
  WebGPU is experimental only.
- Auth remains JWT + bcrypt, extended with approved Entra staff identity and
  controlled local break-glass access. No Tailwind removal without explicit
  founder approval.
- Stabilize known fatal defects before upgrades; execute toolchain, React, 3D,
  backend, database, and cloud modernization as separately reversible waves.
- Production UI must be designed or referenced in Stitch/Figma first.
- Folder moves must be mechanical and verified separately from feature work.

Session delivery under D-097:
- The founder uses the discussion chat to issue a bounded prompt for each new work
  chat and brings its result back. No automatic next task, chat or active-goal edit.
- Read TASKS.md and PROJECT_STATE.yaml; reconcile current Git/runtime before work.
- Reuse accepted brand, requirements, contracts and prototype evidence. Derive
  reversible implementation details within the assigned scope; do not reopen
  settled choices or restart the entire definition campaign.
- Qualify all dependencies actually coupled to the increment. Defer unused 3D
  tooling and hosting qualification to their increments; do not omit transitive
  dependencies or declare the complete platform graph qualified prematurely.
- Keep relevant product docs current, at most two per work slice. Do not generate
  routine review narratives or hash packets. Existing frozen evidence stays intact.
- Use TODO/DOING/DONE/BLOCKED. DONE requires relevant tests and an approved commit;
  if commits remain deferred, report verified work and the separate commit gate.
  Launch credentials, sign-off, load/accessibility qualification and deployment
  stay on the launch checklist; affected behavior still receives automated tests.


## Hengshi Design Project Rules

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
2. No application feature development begins until the Phase 1 definition, SEO,
   design, architecture, security/privacy, QA/deployment, and compatibility
   package is approved.
3. Every material phase follows `create -> validate -> inspect -> independent
   review -> revise -> validate again -> founder approval`. Use at most two
   revision cycles by default and three for brand, UI, motion, and 3D.
4. Record safe, reversible, unambiguous assumptions. Stop for a founder decision
   when a missing choice materially changes scope, risk, cost, public claims, or
   architecture.
5. Do not create branches, commits, remotes, migrations, paid activations,
   external design writes, credential changes, production promotions, deployments,
   or other irreversible changes without their explicit applicable approval.

For UI work, generate or reference the relevant approved Google Stitch or Figma
screen before implementation. Every indexable route must produce complete semantic
HTML before JavaScript, and Quick Access must provide an equivalent accessible
non-WebGL journey.

For version-sensitive framework, library, API, cloud, browser, CI, container, and
Blender decisions, use Context7 and official primary documentation first. Confirm
the release in the official registry, evaluate coupled packages as a compatibility
graph, and record the dated evidence and rollback. Preview, beta, RC, nightly, and
experimental dependencies cannot be production requirements.

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

Current non-negotiables:

- Hengshi Design positions as an evidence-led, premium, platform-oriented
  innovation delivery company.
- Preserve the existing application and exterior GLB as protected prototype
  evidence; neither is production authority.
- Frontend families remain React + TypeScript + Vite + TailwindCSS + React Three
  Fiber on the approved latest-mutually-compatible stable matrix.
- Backend families remain FastAPI + SQLAlchemy + Alembic + PostgreSQL on the
  approved latest-mutually-compatible stable matrix.
- Target PostgreSQL 18's current stable minor when GA in the approved Azure region;
  otherwise use the newest regional GA major under an ADR and quarterly recheck.
- Target Azure rather than the obsolete AWS plan. WebGL remains the production 3D
  renderer; WebGPU is experimental only.
- Auth remains JWT + bcrypt, extended with approved Entra staff identity and
  controlled local break-glass access. No Tailwind removal without explicit
  founder approval.
- Stabilize known fatal defects before upgrades; execute toolchain, React, 3D,
  backend, database, and cloud modernization as separately reversible waves.
- Production UI must be designed or referenced in Stitch/Figma first.
- Folder moves must be mechanical and verified separately from feature work.

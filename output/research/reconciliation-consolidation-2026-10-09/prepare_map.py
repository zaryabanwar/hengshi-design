"""Consolidate navigation only; preserve the exact predecessor and source index."""
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
MAP_REL = "docs/software-definition/04-reconciliation-map.md"
README_REL = "docs/software-definition/README.md"
before_dir = HERE / "before"
if before_dir.exists():
    raise SystemExit("Preserve previously prepared consolidation")
original = (ROOT / MAP_REL).read_bytes()
text = original.decode("utf-8")
section = text.split("## One controlling source per subject", 1)[1].split("## Engineering responsibility", 1)[0]
subjects = []
for line in section.splitlines():
    if line.startswith("| "):
        fields = line.split("|")
        if fields[1].strip() != "Subject":
            subjects.append({"subject": fields[1].strip(), "entry": fields[2].strip(),
                             "prior_context": "|".join(fields[3:-1]).strip()})
if len(subjects) != 46:
    raise SystemExit(f"Unexpected original subject inventory: {len(subjects)}")
before_dir.mkdir()
(before_dir / "04-reconciliation-map.md").write_bytes(original)
readme_before = (ROOT / README_REL).read_bytes()
(before_dir / "README.md").write_bytes(readme_before)
(HERE / "prior-subject-index.json").write_bytes((json.dumps(subjects, ensure_ascii=False, indent=2) + "\n").encode())

intro = """# System definition and reconciliation map — v1

Status: DOING. Consolidated 2026-10-09. This is navigation for the current Phase 1 package; it grants no application, dependency, model, external-write, Git or deployment permission. The [exact preceding map](../../output/research/reconciliation-consolidation-2026-10-09/before/04-reconciliation-map.md) preserves its evidence history; its same-folder links resolve from `docs/software-definition`. Detailed obligations and review limits live in the controlling documents below.

## The system being defined

Hengshi Design is an evidence-led innovation delivery platform for Europe first. Visitors land on a complete semantic website with services, industries, evidence and booking, then may explicitly enter the World. Detailed, Balanced, Simplified 3D and Quick Access preserve equivalent content/actions; automatic capability selection and the accepted override are separate from World entry. Quick Access needs no WebGL or visitor account.

The selected campus is an original organic central reception and five service wings in a connected landscape. D-071 accepts composition only. Desktop mouse/mobile touch support free steering and walking alongside destinations; WASD is not selected. Nearby spatial streaming handles reversals, independently of graphics detail. Optional sound starts off and follows context with persistent controls. This is an aspirational design vision, without environmental-performance claims.

Semantic pages, World information boards and approved-knowledge AI share eligible published truth. Staff content review/publication, genuine availability, consented human handoff and discovery booking retain the accepted authority boundaries. React/TypeScript/Vite/Tailwind/React Three Fiber and FastAPI/SQLAlchemy/Alembic/PostgreSQL remain the families, on the complete latest-mutually-compatible stable graph. WebGL is the production renderer. The application, Atlanta GLB and accepted layout-study sources remain protected evidence; the study's orbit viewer does not implement walking.

## Engineering responsibility and the client brief

Translate the founder's vision into researched input/camera, collision/traversal, connected-area loading/residency, rendering and authoritative content/help designs. The [campus engineering specification](../phase-1-3d/CAMPUS_ASSET_BUILD_SPEC.md#researched-engineering-recommendation) owns that proposal. After applicable approval, prove one arrival → reception → eligible department → information/help → booking journey before expanding. Appearance, physical-device comfort, geometry, rights and numerical calibration keep their own evidence requirements.

## One controlling source per subject

Apply [governance](../../AGENTS.md), the [constitution](../../.specify/memory/constitution.md) and [decisions](../../DECISIONS.md) first. The following directory retains every preceding subject and its source links. Use each owning document's current amendments and scoped receipts; the preceding map is historical support, not a second live authority. A PASS covers only its frozen inputs/scope. Schema, source, metadata or supplied-image checks establish no application enforcement, whole-process accessibility, physical-phone behavior or integrated acceptance.

| Subject | Controlling entry point |
|---|---|
"""
directory = "\n".join(f"| {item['subject']} | {item['entry']} |" for item in subjects)
directory += "\n| Rights intake and verified response | [Privacy-channel workflow](../phase-1-architecture/contracts/SECURITY_PRIVACY_CONTRACT.md#rights-intake-and-verified-response-proposal--2026-10-09) and [deletion-route separation](../phase-1-architecture/contracts/INTERFACE_CATALOG.md#rights-channel-and-deletion-interface-separation--2026-10-09). The separate initial/correction receipts retain their exact logical/source scopes. |\n"
tail = """
## Coverage against the fourteen Phase 1 deliverables

Accepted baselines and bounded reviews remain in their owning packages; the statuses below describe completion of the coherent package, not reopening settled decisions. Real production facts and deferred operating choices do not become new founder-input blockers.

| Deliverable | Status | Remaining definition/acceptance obligation |
|---|---|---|
| 1. Product requirements | DOING | [Foundation](../phase-1-foundation/README.md): reconcile current amendments and trace every required journey/control into the same definitions and references; preserve D-025 and current requirements/conversion authority. |
| 2. Claims/content evidence | DOING | [Company/content rules](06-entity-and-public-contact.md): finish quarantine, evidence/rights and operator-disclosure obligations. D-076 permits fictional non-sensitive local data; real records, public registration/validity/address and alias ownership are deferred. Verify eligible actual facts before publication. |
| 3. SEO/content strategy | DOING | [Controlling SEO strategy](../phase-1-foundation/03-seo-entity-route-editorial-strategy.md): complete semantic route/content/metadata/structured-data, canonical/sitemap/redirect and release-parity definitions and traceable future HTTP/no-JS/browser criteria. Actual rendering and crawlability evidence follows approved implementation. |
| 4. Brand/identity | DOING | D-026/D-035 accepted [strategy/identity](../phase-1-brand-identity/README.md); preserve exact assets and interface/evidence/accessibility rules. Reconcile D-067 scene materials without inventing a new logo/palette or accepting production appearance. |
| 5. UX/journeys | DOING | [Flows](../phase-1-ux-architecture/FLOWS.md) and [recovery](../phase-1-ux-architecture/STATES_AND_RECOVERY.md): finish controls, profiles, equivalent access and visual references under accepted D-036/D-064/D-076; integrated acceptance remains. |
| 6. Production UI references | DOING | [B01 execution brief](../phase-1-ui-reference-production/B01_EXECUTION_BRIEF.md#current-directory-checkpoint--2026-10-08): complete full-resolution inspection, missing states/axes, interactions/accessibility, editable export/restore/_EXIT and founder pilot acceptance. Then gated B02–B09 complete the [nine-batch plan](../phase-1-ui-reference-design/design-batch-plan.csv). Created frames/scaled previews do not prove complete coverage. |
| 7. Production 3D definition | DOING | [World](../phase-1-3d/WORLD_EXPERIENCE.md), [storyboard](../phase-1-3d/SPATIAL_STORYBOARD.md), [assembly](../phase-1-3d/SCENE_ASSEMBLY_CONTRACT.md) and [measurement profile](../phase-1-3d/WORLD_MEASUREMENT_PROFILE.md): close production geometry/clearance/entrance/river continuity, resource/collider/profile registration, controls, audio rights, named workloads/budgets and appearance references. B07 owns World-control references, B09 cross-surface proof. D-071's three normal study revisions are used; further substantial model correction needs an exception. |
| 8. Architecture/ADRs | DOING | Retain D-065's exact [boundary baseline](../phase-1-architecture/ARCHITECTURE.md), amended by current movement, v1 and cloud deferral. Complete detailed bindings/ADRs and integrated acceptance without reopening the responsibility split. |
| 9. API/data/publication contracts | DOING | [Interfaces](../phase-1-architecture/contracts/INTERFACE_CATALOG.md), [data](../phase-1-architecture/contracts/DATA_CONTRACT.md) and [publication](../phase-1-architecture/contracts/PUBLICATION_CONTRACT.md): close required directional/resource/proof/transaction/copy/retention and provider definitions, with traceable failure/concurrency/rollback criteria. Schema/parser observations and mocked responses do not establish actual boundary enforcement. |
| 10. Security/privacy/AI controls | DOING | [Security/privacy](../phase-1-architecture/contracts/SECURITY_PRIVACY_CONTRACT.md): finish identity/session/permission mechanisms, exact purpose/basis/notice/copy bindings, proposed retention adoption, rights/incident handling and applicable legal/accessibility review. AI eligibility/grounding/private routing stay in [publication](../phase-1-architecture/contracts/PUBLICATION_CONTRACT.md). No administrator inheritance, self-approval, automatic operational grants or compliance claim. |
| 11. QA/recovery strategy | DOING | [QA/recovery](../phase-1-architecture/contracts/QA_RECOVERY.md): finish named devices/workloads, operating/measurement/recovery profiles and future authorized drill/acceptance criteria. D-074's corrected browser releases are settled; targets and scoped definition reviews are not measured uptime, recovery, WCAG or SLA results. |
| 12. Compatibility graph | DOING | [Compatibility authority](../phase-1-compatibility/README.md#current-authority-and-dated-evidence): complete coupled stable selection/locks, platforms, provenance/licences, deployed inventory/exclusion and rollback. D-072 is dev/CI lint-only through 2027-01-05; D-077 permits only the evaluated Three184 pair, with recheck by 2027-01-07/on fix/before adoption and separate rollback/adoption. Neither accepts the full graph or app upgrade. The 43-package native trial is pending permission; the 45-package identity dry run does not expand it. Original npm CLI SBOM failure remains separate from the bounded supplement. |
| 13. Costed operating envelope | TODO | D-068 explicitly defers provider/region/cost/hosting planning. Azure/AWS remain candidates; prefer lowest feasible cost/free services later without presuming free-tier suitability. No SKU, spend or provider is selected. Entra/private-AI constraints and Outlook/Teams intent remain, without a Microsoft 365 prerequisite. |
| 14. Legacy/feature reconciliation | DOING | [Historical successors](../active/Documentation_Index.md#current-successors-for-historical-documents) and [feature index](../../specs/README.md): reconcile current requirements/contracts/review scope without duplicating product authority. Historical security research/data/plan and task placeholder are not executable; approved implementation plans/tasks follow Phase 1 acceptance. Later reference edits do not inherit earlier feature PASS. |

## Later contract refinements

### Booking qualification and email ownership

[Qualification/email controls and encodings](../phase-1-architecture/contracts/INTERFACE_CATALOG.md#booking-qualification-and-email-review-navigation--2026-10-08) own current admission, correction, consent, challenge, dispatch, replay and verified-state proposals plus their exact reviews. Keep verification, proof cleanup and scheduling history separate; reviewed shape/control is not implemented email or booking behavior.

### Scheduling and calendar effects

[Scheduling contract](../phase-1-architecture/contracts/BOOKING_SCHEDULING.md) owns availability/slot/create/reconcile/reschedule/cancel definitions and their separate logical/HTTP/schema receipts. Preserve known local receipt versus provider outcome, complete availability and unknown reconciliation truth. Numeric resource targets remain unmeasured; actual provider/account and runtime qualification follow their gates.

## Retain, supersede and retire

Keep governance, accepted requirements/designs, canonical contracts/specs and exact review/asset evidence. Legacy SRS/SAD, SPEC/BACKLOG and diagrams are prototype/history; their [successor catalogue](../active/Documentation_Index.md#current-successors-for-historical-documents) controls current reading. Protected prototype `require_admin` evidence keeps R-004 open. [D-068 deployment entry](../../specs/005-azure-deployment-launch/README.md) governs both historical cloud folders. Replace duplicated live prose with references; this consolidation deletes no artifact and moves no folder. The preceding map remains byte-identical supporting history, with its review claims limited to their exact original inputs.

## Current scoped founder inputs

D-076 settles visitor access at 30 minutes inactivity or authorized End, with no absolute conversation duration; accessible warning/More time and staff's separate 30-minute idle/eight-hour absolute clocks remain. Production facts, public registration/address/validity, alias ownership and D-068 hosting/cost choices are deferred. Privacy recommendations need reviewed adoption, rather than arbitrary new duration questions. No settled brand, architecture, movement or composition choice is reopened.

B01's [five-sheet full-resolution export](../../output/research/b01-directory-full-resolution-2026-10-08/preparation.json) awaits fresh CB-06/CB-07 per-call approval. All 52 directory pixels remain uninspected at full resolution; [ledger](../phase-1-ui-reference-production/validation/mcp-call-ledger.csv) owns attempts/quota observations, with actual balance unknown. The separately prepared [43-package native qualification plan](../../output/research/backend-crypto-graph-2026-10-08/qualification-plan.json) also awaits explicit execution approval. No new Figma/native permission follows from this map. Founder visual acceptance is requested when the required package is reviewable.

## Route to a coherent checkpoint

Finish and reconcile non-deferred definitions → complete required visual references and compatibility evidence → validate/inspect → independent integrated review and bounded revisions → founder acceptance. The [task exit contract](../../TASKS.md#exit-and-later-phases) controls. Define future actual-boundary HTTP, movement, accessibility, privacy, recovery and provider qualification here; application feature implementation and its runtime evidence follow later approval, not circular Phase 1 prerequisites. Missing required designs, material choices and adopted policies remain acceptance gaps. Commits and pushes stay deferred. Consolidation review is pending; this map certifies no whole package, application or release readiness.
"""
new_map = (intro + directory + tail).encode("utf-8")
(ROOT / MAP_REL).write_bytes(new_map)
old = b"and [later contract refinements](04-reconciliation-map.md#later-contract-refinements)\r\nretain the detailed review navigation. A receipt applies to its frozen inputs and\r\nscope; later edits do not replace its hashes or inherit its PASS. Definition,"
new = b"and [later contract refinements](04-reconciliation-map.md#later-contract-refinements)\r\ndirect readers to the controlling documents and their scoped review receipts. The\r\nmap preserves its exact earlier evidence history as supporting material, without\r\nmaintaining another live review journal. A receipt applies to its frozen inputs\r\nand scope; later edits do not replace its hashes or inherit its PASS. Definition,"
if readme_before.count(old) != 1:
    raise SystemExit("Expected exact README navigation paragraph")
(ROOT / README_REL).write_bytes(readme_before.replace(old, new, 1))

# Capture only the actual navigation authorities plus unchanged governing records.
paths = [MAP_REL, README_REL, "AGENTS.md", ".specify/memory/constitution.md", "PROJECT.md",
         "DECISIONS.md", "TASKS.md", "PROJECT_STATE.yaml", "docs/software-definition/05-consolidated-goal.md"]
for target in re.findall(r"\]\(([^)]+)\)", new_map.decode()):
    if target.startswith(("http:", "https:", "#")):
        continue
    p = ((ROOT / MAP_REL).parent / target.split("#", 1)[0]).resolve()
    if p.exists() and p.is_file():
        paths.append(p.relative_to(ROOT).as_posix())
    else:
        raise SystemExit(f"Broken navigation file: {target}")
paths += [p.relative_to(ROOT).as_posix() for p in HERE.rglob("*") if p.is_file()]
packet = HERE / "review"
packet.mkdir()
inputs = []
for rel in dict.fromkeys(paths):
    raw = (ROOT / rel).read_bytes()
    snap = packet / "inputs" / rel
    snap.parent.mkdir(parents=True, exist_ok=True)
    snap.write_bytes(raw)
    inputs.append({"path": rel, "snapshot": snap.relative_to(ROOT).as_posix(),
                   "sha256": hashlib.sha256(raw).hexdigest(), "bytes": len(raw)})
manifest = packet / "review-inputs.json"
manifest.write_bytes((json.dumps({"status": "DOING", "revision_cycle": 0,
    "scope": "Reconciliation-map navigation consolidation and one README reference segment",
    "inputs": inputs}, indent=2) + "\n").encode())
print(json.dumps({"original_bytes": len(original), "map_bytes": len(new_map),
    "retained_subjects": len(subjects), "added_rights_subject": True, "inputs": len(inputs),
    "manifest_sha256": hashlib.sha256(manifest.read_bytes()).hexdigest()}))

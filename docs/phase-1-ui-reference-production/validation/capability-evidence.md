# Figma capability evidence — MA-025 §3.5

## Current-host observation — 2026-10-05

The Codex plugin inventory reports Figma installed, and Figma tool metadata is
exposed in this host. Following immediate founder approval under CB-06, one
read-only `whoami` call succeeded on 2026-10-05 and returned an authenticated
identity on the Starter tier with a Full seat. Account identifiers are not
reproduced here. The observation supersedes the earlier current-host installation
and identity gaps; file access and canvas writes have not been tested.

The [call ledger](mcp-call-ledger.csv) records one October project Figma call and
zero documented metered October calls. Account-wide usage and remaining allowance
are unknown. This single-call approval is consumed: each subsequent Figma call
still requires immediate founder permission. B01 remains `future_not_authorized`;
successful identity verification does not authorize its pilot or design changes.

The [official rate-limit documentation](https://developers.figma.com/docs/figma-mcp-server/rate-limits-access/)
was read through the web tool on 2026-10-05, without a Figma MCP call. It names
`whoami` as exempt and still describes Starter as 20 calls/month. This does not
establish outside-project usage or canvas-write exemption; the current plan and
seat above come from the approved identity response. Preserve the existing
budget/ledger rules until their approved update.
The September observations below belong to that dated Claude session, not today's
Codex capability state. Retain them as evidence rather than silently promoting
them into a fresh connection or write test.

## September capability record — preserved evidence

**Observation date:** 2026-09-06
**Recorded by:** producer, after founder approval of MA-025
**Authority:** `UI_REFERENCE_PRODUCTION_CONTRACT.md` §3.5 and §7.2; trace rows
TR-015, TR-030, TR-034
**Status of this file:** capability record only. It is not batch evidence, not an
external write, and not a pilot acceptance.

This file exists only because MA-025 was approved. Before that approval the
deterministic validator asserted its absence; that assertion is a pre-approval
boundary and is now superseded by an explicit lifecycle state rather than deleted.
See `validation-report.md` and the `PRE_APPROVAL`/`POST_APPROVAL` states in the
validator.

---

## 1. Enablement path taken

Contract §3.5 offers Path A (agent MCP) or Path B (human operator working directly
in Figma). **Path A is the path that completed.**

| Step | State | Evidence |
|---|---|---|
| Endpoint registered | Complete | `https://mcp.figma.com/mcp`, registered at **user scope**, outside the repository |
| Repository cleanliness | Complete | `.mcp.json` absent; `%APPDATA%\Code\User\mcp.json` absent; no endpoint or credential in any tracked file |
| Authenticated | Complete | Founder completed the provider OAuth flow on 2026-09-06. The credential was never seen, requested, or recorded by the producer. |
| Protocol-tested | Complete | Claude Code restarted 2026-09-06; the Figma MCP server's tool set is bound into the session and 42 `mcp__figma__*` tools are enumerable. |
| **Capability-tested** | **Complete** | `whoami` executed and returned a well-formed authenticated identity. See §2. |

Against the status vocabulary in `docs/software-definition/02-ai-dev-tooling-and-mcp.md`,
Figma has now reached **Capability-tested** — the highest state — for read-side
operation. Canvas writing is **not** capability-tested; no write has been attempted.

## 2. Capability test performed

**Tool:** `whoami`. Chosen deliberately: it is read-only, it writes nothing to any
canvas, it touches no project material, and Figma's own documentation lists it as
**exempt from rate limits**, so the test consumed no quota.

Result, recorded without account secrets and with the seat identity summarized
rather than transcribed per the MA-025 secret-handling rule:

| Field | Value |
|---|---|
| Authenticated | Yes |
| Team | one team, `starter` tier |
| Seat | `Full` (the seat class that permits editing) |
| Plans | exactly one |

No token, session URL, cookie, or file key appears in this record. The account
email returned by the tool is deliberately **not** transcribed here.

## 3. The five §7.2 limits — verification result

Contract §7.2 recorded five limits as `[MUST VERIFY AT GATE]` and forbade
asserting them. Verified against the provider's own current documentation,
resource `file://figma/docs/rate-limits-access.md`, retrieved 2026-09-06:

| # | §7.2 item | Verified? | Finding |
|---|---|---|---|
| 1 | Starter design-file count and pages-per-file | **No** | Not addressed by the access documentation. Still unasserted. |
| 2 | Starter version-history retention | **No** | Not addressed. Still unasserted. §9.4 already makes the repository export the authoritative rollback artifact, so this is not on the critical path. |
| 3 | Starter editor/collaborator caps | **Partial** | This account holds a `Full` seat, which is the editing seat class. The cap itself is not stated. |
| 4 | Dev Mode availability on Starter | **Partial** | The remote MCP server is documented as available on all seats and plans, and it responded. Dev Mode as a product surface is not separately confirmed. |
| 5 | **Provider MCP tool-call allowance** | **YES — and it blocks** | **20 tool calls per month.** See §4. |

Four of five remain unverified and are still not asserted. The fifth is verified
and is a hard constraint.

## 4. The verified allowance, and the SC-05 stop

### 4.1 What the documentation says

| Seat | Starter | Professional | Organization | Enterprise |
|---|---|---|---|---|
| View, Collab | **Up to 20/month** | Up to 6/month | Up to 6/month | Up to 6/month |
| Dev, Full | *(same cell)* | 200/day, 10/min | 200/day, 15/min | 600/day, 20/min |

The Starter column is a single cell spanning **both** seat rows. A `Full` seat on
Starter therefore does **not** receive the 200/day allowance. This reading is not an
inference from table markup alone — the provider's own remediation text states it
directly: *"If you're on a Starter plan (20 tool calls per month), upgrade to a Pro,
Organization, or Enterprise plan."*

**Verified allowance for this account: 20 tool calls per month.**

No per-minute limit is stated for Starter.

### 4.2 What is metered, and what is not asserted

Metered: *"Rate limits apply to Figma MCP server tools that read data from Figma."*

Exempt: the documentation says *"Some tools, such as those that write to Figma
files, are exempt"* — but enumerates only three:

- `add_code_connect_map`
- `create_new_file`
- `whoami`

**The general sentence and the specific list do not agree in scope.** Whether
`use_figma`, `generate_figma_design`, and `upload_assets` are metered is
**NOT ASSERTED**. Treating them as exempt on the strength of the general sentence
would repeat exactly the error §7.2 was written to prevent. The call budget
therefore assumes **every** call is metered until measurement proves otherwise.

The provider also reserves the right to change these limits.

### 4.3 The exact shortfall — SC-05

`SC-05` fires on *"a verified free-tier limit blocks contracted evidence"*, with
programme scope and the action *"halt and report the limit and the exact shortfall
and do not purchase"*.

The shortfall, computed from the contract's own evidence rules and counting only
structurally unavoidable reads, before any visual evidence at all:

| Rule | Requirement | Calls |
|---|---|---:|
| `EC-25` | Record the page and frame inventory, once per batch | 7 |
| `EC-28` | Export the named `_PRE` archive before the first write of a batch | 7 |
| `EC-29` | Export the named `_EXIT` archive at batch exit | 7 |
| | **Floor across the seven authorized batches** | **21** |

**21 minimum against 20 per month** — the programme exceeds a single month's
allowance before one frame is captured. Actual demand is far higher: `EC-10`
requires up to seven viewports, and `EC-01`–`EC-06` require frame, focused-frame,
variant, annotation, prototype, and route-instance evidence per template.
Realistic demand is in the **hundreds** of calls.

**No purchase has been made or proposed by the producer.** MA-010 remains the only
route to a paid envelope and only the founder may open it.

### 4.4 Founder disposition, 2026-09-06

The founder was shown the verified limit and the shortfall above, and directed:
**"stay on course we will use 20 calls per month very precisely."**

This is an explicit, informed acceptance of the constraint. It does **not** waive
`SC-05`; it resolves it. The recorded resumption is: remain on the free tier,
extend the programme across calendar months, and ration every call under a written
budget. See `mcp-call-budget.csv`.

The consequence the founder has accepted, stated plainly: the seven batches will
span **multiple months**, and the exact number of months cannot be stated until B01
measures real consumption.

## 5. What B01 now additionally does

B01 was already a gated pilot under MA-025 item 5. It now carries a second purpose
that costs nothing extra: it is the **metering experiment**. It is the cheapest
batch, so it is the correct place to learn the true per-batch call cost and to
discover empirically which tools are metered.

B01 exit must therefore report, alongside its normal evidence:

1. Total Figma MCP calls made.
2. Calls by tool name.
3. Whether any rate-limit response was observed, and at what cumulative count.
4. A measured per-batch projection for B02–B06 and B08.

Until that projection exists, **no schedule for the programme may be stated.**

## 6. Boundary

This record establishes provider connectivity and one read-only capability call.
It does **not** establish: that canvas writing works, that the contracted evidence
volume is achievable, that any batch may begin, or that any of the four unverified
§7.2 limits is safe. B01 may begin only under the call budget, and it halts at its
gated pilot acceptance as MA-025 already requires.

No external write has been performed. No evidence directory exists. B07, B09, and
`docs/ui/UI_SPEC.md` remain deferred to MA-026 and `SC-10` still refuses them.

## Current-host pilot preflight — 2026-10-06

The [B01 execution brief](../B01_EXECUTION_BRIEF.md) restates the existing scope;
it neither releases the pilot nor authorizes a provider call. The 2026-10-05
whoami observation remains identity evidence only. Contract §3.5 specifically
requires read-only file/node capability before a write; this host has no recorded
file/node test or designated production-reference file. The September read-side
capability label above must not be read as proof of that narrower requirement.

Exposed tool metadata supports file creation, node inspection and scripted canvas
work; it exposes no full editable-file archive operation or project-creation tool.
The bundled use_figma API typings expose node exportAsync but no
saveVersionHistoryAsync declaration. Official Figma docs do document
[saveVersionHistoryAsync](https://developers.figma.com/docs/plugins/api/figma/#saveversionhistoryasync)
and [node exports](https://developers.figma.com/docs/plugins/api/properties/nodes-exportasync/).
Official API documentation does not prove this host implements those operations.
Contract §9.2 still requires _PRE/_EXIT named versions and full editable archives;
node exports/screenshots/JSON are not an accepted replacement. A native editor
path must be verified or a scoped founder amendment obtained before proceeding.

The [official rate-limit page](https://developers.figma.com/docs/figma-mcp-server/rate-limits-access/)
was read through the web tool on 2026-10-06, without a Figma call. It still states
Starter 20/month and names create_new_file and whoami as exempt. It does not
establish remaining account allowance or the metering of use_figma. Preserve the
approved conservative budget, ledger and individual-call gates. No new identity,
file read, canvas write, quota measurement, provider setting or account action
was performed by this preflight. Earlier reviewed bytes remain dated evidence.

### Subsequent approved identity observation — 2026-10-06

After the preflight and initial ordering-proposal reviews, the founder stated this
is a new project with no Figma file. The approved get_metadata check was not
attempted because it has no target; it was not substituted with another tool.
The founder then separately approved one whoami call for plan-key resolution.
That call succeeded: one authenticated Starter plan, Full seat. The required key
is retained only transiently; no account identifier is stored in this record.
The [sanitized observation](../../../output/research/b01-preflight-2026-10-06/identity-observation.json)
and ledger record October project calls two, documented metered calls zero;
account-wide usage/remaining allowance stays unknown. This one-call approval is
consumed. No file, project, design or sharing setting was created or changed.

The proposed first-file ordering amendment remains unapplied and requires its
own founder acceptance. Identity resolution cannot approve it, the create-file
operation, B01 execution or any later design write. File/privacy/archiving checks
and all existing budget and pilot gates remain held. These subsequent observations
are outside the frozen preflight/proposed-amendment review inputs, whose exact
prior bytes and receipts remain evidence rather than today's capability state.

### Approved first-file bootstrap — 2026-10-06

[D-073](../../../DECISIONS.md#d-073--first-file-bootstrap-ordering-and-one-blank-figma-file)
accepts the reviewed ordering amendment and one empty create_new_file operation
in Drafts. The two contract/scope documents now contain that accepted exception;
the earlier proposal receipts retain their exact, unapplied reviewed inputs.
The call succeeded and returned the single
[Hengshi Design v1 — UI References file](https://www.figma.com/design/GOmLP6Cv96l768ueSrZ5Dg).
The [creation observation](../../../output/research/b01-preflight-2026-10-06/file-creation-observation.json)
and ledger record October project calls three, documented metered calls zero;
account-wide usage/remaining allowance stays unknown. The creation permission is
consumed. No design content, new project, sharing setting, seat or account setting
was changed. File/node, privacy, named-version/editable-archive checks and _PRE
remain prerequisites for content work; D-073 does not release B01 or later batches.

### Approved page-list capability observation — 2026-10-06

The founder-approved get_metadata check was executed once against D-073's
confirmed new file, without another create or a substituted identity call.
It returned the [one-page inventory](../../../output/research/b01-preflight-2026-10-06/file-pages-observation.txt):
Page 1, id 0:1. This proves authenticated top-level page listing on this host;
it does not inspect node children or prove blankness, private sharing state,
canvas writes, named-version support or full editable-file export. No design,
sharing or account setting was changed. The one-call permission is consumed.
October project calls are four; conservatively counted metered calls are one,
not a measured provider counter. Account-wide usage/remaining quota stays unknown.
The accepted first-file exception and all pre-design/pilot gates remain in force.

### Browser editor access observation — 2026-10-06

The approved file-opening attempt timed out. Subsequent browser inventory
confirmed the single Hengshi file tab at the returned URL; no second file or tab
was created to retry it. Both direct binding and the documented user-tab claim
path returned `Debugger unattached`. Browser inventory visibility therefore does
not establish editor control, private sharing or an archive download.

The bundled use_figma API guide explicitly excludes version-history saves.
No Figma call was spent probing that unsupported operation. Native editor
privacy, version-history and Save local copy observations have been requested
from the founder without changing sharing or creating a version. October counts
remain four project calls and one conservatively counted metered call; remaining
account allowance is unknown. No content write or B01 execution occurred.
These live observations are subsequent to the exact reviewed preflight inputs.

### Founder editor screenshots — 2026-10-06

The founder supplied two editor screenshots in this chat. The Share dialog shows
`Anyone — can view` and the account owner. This is not restricted private access;
no design content may be written under §3.5 until privacy is resolved. The second
image shows the Hengshi v1 file in Drafts, Page 1 with an empty visible Layers
panel, and a `Show version history` menu item. This is visual evidence only,
not complete node inventory or a successful named-version save.

The visible `Export…` item does not establish full editable-file archiving.
Save local copy and an actual restorable archive remain unverified. The founder
has been asked to restrict view access to invited people and inspect the main
File menu for Save local copy. No sharing change, version save, export or content
write has been executed by the agent. Figma project call counts are unchanged.
Screenshots are the two founder attachments ending `38d39afd-7214-49bd-ac23-f07613e7f799.png`
and `aa169c8e-29c5-4ca0-bde4-c76611bdbe25.png`; no account identifiers are copied here.

### Subsequent founder editable-file export — 2026-10-06

The next screenshot shows the confirmed Hengshi file URL, File > Save local copy,
Save to version history and a completed `Hengshi Design v1 — UI References.fig`
download. The actual downloaded file was found and preserved as
[bootstrap-empty.fig](../../../output/research/b01-preflight-2026-10-06/founder-export/bootstrap-empty.fig),
31,969 bytes, SHA-256 `88afa124fab4dbde263c90af24b78a5c262f33675f119aeddb06945ea693b2ad`.
The [observation](../../../output/research/b01-preflight-2026-10-06/founder-export/observation.json)
and [bounded ZIP integrity check](../../../output/research/b01-preflight-2026-10-06/founder-export/container-check.json)
record four entries, 31,260 total uncompressed bytes and passing CRC checks.
This verifies the download/container, not proprietary contents or Figma restore.

The native editable-export path and named-save menu are now observed. No actual
named _PRE version/linkage, restore import or restricted sharing is confirmed;
the last Share evidence remains Anyone-can-view. Do not label this bootstrap
copy the B01 _PRE archive. No agent version save, sharing change, duplicate file,
design content or additional Figma call occurred. The founder's export is separate
from agent MCP counts, which remain four October project calls/one conservative
metered call. File/privacy inspection and B01 execution retain their gates.

Figma's official [local-copy guidance](https://help.figma.com/hc/en-us/articles/8403626871063-Save-a-local-copy-of-files)
was verified 2026-10-06: Design exports are .fig, exclude comments/version history
and reimport as a new file. No unapproved reimport is attempted. Its
[version-history guidance](https://help.figma.com/hc/en-us/articles/360038006754-View-a-file-s-version-history)
distinguishes viewing from editor naming/restoring; Starter/Drafts history has a
30-day access window. Independent repository archives remain required by §9.2.

### Founder privacy confirmation and account usage screenshot — 2026-10-06

The founder explicitly confirmed that sharing was changed to private. This
supersedes the earlier Anyone-can-view observation for the current checkpoint;
it is a founder confirmation, not an agent inspection of the updated Share dialog.
No agent sharing change or additional Figma call occurred.

The supplied Starter Usage screenshot shows 19 monthly MCP calls available,
three connections, AI credits 0/500 monthly and 0/150 daily used, and files 2/3.
This is an account UI observation at capture time, not a live provider-counter
probe or a guarantee of future allowance. Connections are not separate quotas;
AI credits are not MCP calls. October project calls remain four, conservatively
counted metered calls one. Node inspection, named _PRE/archive linkage and B01
execution retain their existing gates. No library, community tool or provider
AI feature was invoked by this observation.

### Approved page-node inspection denied by authentication — 2026-10-06

The founder separately approved one get_metadata call for Page 1, node 0:1,
in the confirmed existing file. It returned `UNAUTHORIZED`, requiring connection
reauthentication before further actions. No XML/page contents were returned;
the read-only inspection did not succeed. No retry, substituted whoami, design,
sharing, credential or account change occurred. The one-call approval is consumed.

October project call attempts now total five, conservatively counted metered
attempts two. The previous screenshot's 19 available is a pre-attempt observation;
the failed call's actual debit and current remaining allowance are unverified.
Record reconnect/reauthentication as the affected Figma capability prerequisite,
not a loss of the existing file or a reason to create another. Child-node
inspection, named _PRE/archive linkage and B01 execution remain held.

### Reconnected page-node inspection succeeded — 2026-10-06

The founder reported Figma connected, then separately approved one fresh
get_metadata call for the existing file's known Page 1 node 0:1. It succeeded,
returning `<canvas id="0:1" name="Page 1" x="0" y="0" width="0" height="0" />`
with no child nodes. This establishes authenticated access and an empty page in
the metadata response; it does not verify canvas writing, current account/seat
identity, private sharing settings, a named-version save or restoration.
Founder-confirmed private sharing and the earlier actual .fig export remain
separate observations. No design, sharing or account change occurred.

October project attempts are six; conservatively counted metered attempts three.
No provider-counter debit or fresh remaining allowance is verified. The call's
permission is consumed. Actual named _PRE/archive linkage, B01 execution and
each subsequent call remain separately gated; the authentication failure is
superseded for this successful read, without deleting the earlier failure record.

### Current Starter limits and B01 organisation proposal — 2026-10-06

This dated primary-source check supersedes the unresolved provider-documentation
items in the September §3 table only where stated below. It creates no design,
plan change, sharing change, independent review verdict or pilot acceptance.

| §7.2 item | Current evidence and limit |
|---|---|
| Files / pages | [Starter overview](https://help.figma.com/hc/en-us/articles/13838684089751-Starter-plan-overview) distinguishes unlimited Drafts from the folder's three combined Design/Sites files. [Page guidance](https://help.figma.com/hc/en-us/articles/360038511293-Create-and-manage-pages) and [Plugin API](https://developers.figma.com/docs/plugins/api/properties/figma-createpage/) specify three Design pages for Starter team files. Do not infer unlimited pages in this Drafts file. One existing page is observed; no page creation/cap probe occurred. |
| History | Starter has 30 days of version history. Actual named `HSD_UIR_B01_PRE` save and its full editable archive linkage remain pending; the earlier bootstrap download is separate. |
| Collaborators | Starter Drafts can be shared with viewers, but cannot invite other editors. The authenticated owner has the previously observed Full seat. No invitation, seat change or reviewer's editor access is assumed. |
| Dev Mode | Starter has no Dev Mode. The [documented desktop MCP enablement](https://developers.figma.com/docs/figma-mcp-server/local-server-installation/) requires Dev Mode; therefore that documented path is unavailable under the verified Starter entitlement. This is an entitlement inference, not a fresh local-server probe. Remote node reading succeeded separately. |
| MCP calls | [Current access documentation](https://developers.figma.com/docs/figma-mcp-server/rate-limits-access/) specifies Starter up to 20/month and names `add_code_connect_map`, `create_new_file` and `whoami` exemptions. It does not explicitly name `use_figma` as exempt. Six project attempts / three conservatively metered attempts remain; current account balance is unverified. |

The Context7 query to `/figma/mcp-server-guide` returned an older six-call/month
excerpt from the guide's GitHub README. The freshly read primary access page
explicitly states twenty/month; use that current dated source, while retaining
the conservative ledger and per-call approvals. No Figma call was used for this
documentation check.

Starter also excludes team libraries and AI image tools. The production contract
§1.2 rationale mentions a published library and a multi-page/multi-library system;
those capabilities are not established for this plan. Its normative B01 scope
and WS-P-03 require reusable PRIM components within the single approved file.
Propose organising B01's foundation components and complete contracted reference
coverage in named sections of the existing Page 1, using file-local components,
without team-library publication or additional pages. This changes organisation,
not template/state/viewport/mode/stream coverage, stable IDs or review obligations.
Founder confirmation of this organisation and explicit B01 execution remain held;
it is not an approved substitute for any unmet normative requirement. Later-batch
page capacity and evidence volume remain unproven. If an actual free-tier limit
blocks contracted evidence, SC-05 still requires a founder decision, not a purchase
or silent workaround. Independent design/accessibility reviews remain required;
the separate review-agent credit failure supplies no verdict.

### Founder B01 execution and organisation approval — 2026-10-06

D-075 records the founder's **“Approve B01”** reply to the defined batch and
existing Page 1/file-local component organisation above. That execution and
organisation decision is resolved; do not request it again. The named
`HSD_UIR_B01_PRE` save, full editable archive linkage, individual Figma-call
permissions, independent reviews, frozen exit and founder pilot acceptance remain
separate requirements. No design write or additional Figma call follows from
recording this approval. The Downloads inspection still found only the earlier
31,969-byte bootstrap .fig; no new named-PRE receipt/archive is verified.

### B01 read-only file/style/font preflight — 2026-10-06

The founder's **“approved b01 call”** authorises the pending single read-only
`use_figma` preflight, not construction or another call. The saved script ran
successfully against file key `GOmLP6Cv96l768ueSrZ5Dg` and Page 1 (`0:1`).
Its [actual provider result](../../../output/research/b01-preflight-2026-10-06/read-only-font-style-check/provider-result.json)
returns one page, zero canvas children, zero local paint/text styles, no truncated
inventories, and empty created/mutated-node lists. Both Arial Regular and Arial
Bold availability checks return **false**. The root name is **Document**, differing
from the earlier bootstrap title; this discrepancy is unresolved. Do not infer
another file, a renamed original, or general write capability from this response.

The prepared foundation script remains unexecuted: its exact-title guard and
approved Arial fallback guard would stop before creation. Do not silently replace
the font, weaken file identity checks, or claim its first design write succeeded.
Named `HSD_UIR_B01_PRE` and full editable archive linkage also remain unverified.
Switching to the known Page 1 changed selection only; no design content or sharing
was changed. This call establishes these read capabilities, not full B01 readiness.

October project attempts are **seven**, conservatively metered attempts **four**.
Actual debit/current provider allowance remain unknown; no rate-limit response
was returned. This one-call approval is consumed. A fresh approved call would be
needed to inspect actual available font names or resolve file identity; the
current output does not establish any approved system-stack font is available.

### B01 font inventory and native PRE — 2026-10-06

The founder explicitly approved the next read-only font inventory. The
[prepared script](../scripts/b01-font-inventory.js), SHA-256
`df5b0302b93e1f565352552474052efc6bbf40415361f02caa9c26b4f087821a`,
ran successfully against the same file key/Page 1. The [actual result](../../../output/research/b01-preflight-2026-10-06/font-inventory/provider-result.json),
SHA-256 `d16e39cb2fd9986eb2292efc4acc78568c7ce25729f5a17540c077af3ee4d928`,
reports 8,927 font styles/1,938 families. The complete documented-candidate scan
finds Cascadia Mono in ten styles, including Regular/Bold; Arial, Helvetica,
Segoe UI, Segoe UI Mono and Consolas are absent. Only the general family sample
is truncated. Do not infer that unlisted families are absent or verified usable.
No node/style/sharing change occurred. October attempts: eight; conservatively
metered: five. Actual balance/debit unknown; one-call permission consumed.

Browser control subsequently opened the exact approved file URL in authenticated
Edge. Its native title is Hengshi Design v1 — UI References, with empty Page 1.
This verifies native identity; it does not explain why MCP root.name is Document.
Through native Save to version history, the agent saved **HSD_UIR_B01_PRE** and
verified that exact entry and description in history. The [screenshot](../../../output/research/b01-preflight-2026-10-06/native-pre-checkpoint/version-history.png)
has SHA-256 `8e24332c031ec6de8938db68a841f3108c1982590d14443969c85e5d02fd215f`.
Native Save local copy downloaded a fresh 31,971-byte .fig at 11:47 local time;
the browser download waiter timed out, but the actual Downloads file exists.
It is preserved as [HSD_UIR_B01_PRE.fig](../../../output/research/b01-preflight-2026-10-06/native-pre-checkpoint/HSD_UIR_B01_PRE.fig),
matching source/archive SHA-256
`aea663332bc62ba412e6c02477f7faa63f1f7f176bd11a16733d9b06d86cf272`.
The bootstrap export is unchanged. No canvas write followed; restore remains
unverified and _EXIT remains future work. Native save/export consumed no additional
Figma MCP call. Starter history visibly notes its 30-day window; no paid upgrade.

Primary [Figma font guidance](https://help.figma.com/hc/en-us/articles/360039956894-Add-a-font-to-Figma),
checked 2026-10-06, describes built-in Google/Apple fonts, desktop or font-helper
access to local .TTF/.OTF, and account-uploaded fonts for MCP/Figma agents.
Local installation alone does not prove this MCP host sees a font. Uploading
requires rights/storage authorization; no font installation, upload, licence
confirmation or typography change has occurred. Built-in reference fallback versus
licensed upload remains a founder choice under D-035; no new standalone check
call is proposed. Bundle applicable live font loading, content/style guards,
coherent construction, returned IDs/bounds and visual evidence into the next
approved productive call. Native history/export cannot be fabricated in Plugin API.

### B01 initial combined construction — 2026-10-06

The founder replied **approved** to Inter for Figma references only and one
combined construction call. The website's D-035 system-font policy is unchanged.
No font file was uploaded, installed or redistributed. The existing native PRE
and editable archive above preceded this first canvas write.

The [prepared script](../scripts/b01-initial-composition.js), SHA-256
`672309ef2835091fa4d0780e06ff3e8ff387f839213cf9568f0d85630188a1b4`, ran once.
It bundled identity/page/empty-baseline guards, exact Inter Regular/Bold and
Cascadia Mono Regular discovery/loading, foundations, an action component,
six editable wide/narrow navigation/search/recovery compositions and returned
IDs/bounds plus one screenshot. No external library, new page or sharing change.
This founder-selected bespoke scope uses local D-035 foundations; library search
and imports were excluded from this approved single-call deliverable, not
asserted unavailable. Existing screens and Code Connect mappings were absent.

[Actual provider result](../../../output/research/b01-initial-composition-2026-10-06/provider-result.json)
has SHA-256 `1806df45118f82fbbb5dc4f0e9f1faf9022667fb0f6713f06889870d25445cee`.
It returns every affected node ID, eight variables/one collection, three text
styles and component `14:18`. Frame IDs are `14:20`, `14:41`, `14:62`, `14:84`,
`14:106` and `14:124`; widths are 1440/390 for each template. The returned
`B01Complete` is false. This result proves execution, not visual correctness.

The [actual navigation preview](../../../output/research/b01-initial-composition-2026-10-06/navigation-preview.png),
SHA-256 `0c4ac0c2367bc9d0af827d79fa7f3a7a9da12cf16f2468119d1f6a30b8043429`,
was inspected: the long mode advisement overlaps the Apply button. Narrow text
reflow and other compositions need inspection and targeted repair before review;
identical wide/narrow returned heights are not evidence of correct wrapping.
No repair or second MCP call was executed. Full PRIM/state/mode/stream coverage,
editable post-write exports, independent design/accessibility review, _EXIT and
founder pilot acceptance remain unfinished. Do not build later batches on this
unvalidated initial composition or report B01 accepted.

October project attempts are nine; conservatively metered attempts are six.
Actual provider debit/balance are unknown; no rate-limit response was returned.
The one-call permission is consumed. A targeted repair requires a fresh CB-06/07
approval; this record authorizes neither that call nor later-batch execution.

### B01 text-reflow attempt — 2026-10-06

The founder approved one targeted repair call for the existing six drafts plus
their six previews. The [repair script](../scripts/b01-text-reflow-repair.js),
SHA-256 `6ad6107a0ea874516ac53015cb52d6826e7cd1add5f7348d79fa0704cbd8b431`,
was submitted once through use_figma with the mandatory skill loaded.
The provider returned **This app connection requires reauthentication before
other actions on this app can succeed.** Its [actual error receipt](../../../output/research/b01-text-reflow-2026-10-06/provider-result.json)
has SHA-256 `bec513c2e76ae599619b65fda6cf4e3832d9c6a4e27a4bcbfeb6b1cf7bf27a56`.
No mutation receipt, current-canvas read or preview was returned. Do not report
a successful repair or infer current file contents from this error.

The script's syntax check passed before submission; that is not execution proof.
The preceding successful first-write IDs/preview and native PRE remain preserved
as dated evidence. No extra inspection, automatic retry, credential/provider or
account change followed. October project attempts: ten; conservatively metered:
seven. Actual balance/debit remain unknown; no rate-limit response was returned.
Permission is consumed. Reconnect the Figma app, then obtain fresh immediate
CB-06/CB-07 approval for any retry. The draft defect, full pilot coverage,
exports/review/_EXIT and founder acceptance remain unfinished.

### B01 successful reflow and final draft screenshot — 2026-10-06

The founder-authorized retry succeeded. The [actual retry receipt](../../../output/research/b01-text-reflow-2026-10-06/retry-11/provider-result.json),
SHA-256 `ebeab3fbba0a07ca70a13fcd59f05bab30b0186d2134dde5a5c09771f520a27f`,
records existing mutated IDs, no created nodes and six frame bounds. Five previews
were returned and inspected; the narrow recovery preview was missing. This
supersedes the unsuccessful repair observation above for execution, without
erasing the dated authentication failure or asserting a credential change.

The founder then approved one read-only `get_screenshot` call for `14:124`.
The [actual 390 × 818 screenshot](../../../output/research/b01-text-reflow-2026-10-06/screenshot-12/narrow-recovery.png),
SHA-256 `050841772b9b85f25abcdfd6e55529f36626ef4e6f5c3dbb19dc512111805137`,
shows readable text and actions without visible overlap or clipping. All six
initial draft views have now been visually inspected. The [local receipt](../../../output/research/b01-text-reflow-2026-10-06/screenshot-12/result.json)
omits the short-lived asset URL. No canvas write occurred in this screenshot call.

Use the [ledger](mcp-call-ledger.csv) for current counts: October project attempts
12, conservatively metered attempts 9; actual debit/balance remain unknown.
The one-call approval is consumed. Initial drafts remain incomplete: contracted
320-pixel references, primitive/state/mode/stream and interaction evidence,
editable post-write exports, independent design/accessibility review, restore,
_EXIT and founder pilot acceptance remain. This visual inspection is not runtime
accessibility evidence or full B01 acceptance.

### B01 combined navigation references — 2026-10-06

The founder approved the pending combined call. The exact [prepared script](../../../output/research/b01-navigation-preparation-2026-10-06/figma-call.js), SHA-256 `0f5733e1e05b716c81120ac4df928616192d282c868325864de6b893731069f6`, ran once after its file/page, six-draft, action, font/style and palette guards. This adds to the existing private Page 1; it does not recreate the initial six frames, change sharing or publish a library.

The [actual provider receipt](../../../output/research/b01-navigation-composition-2026-10-06/provider-result.json) and [state ledger](../../../output/research/b01-navigation-composition-2026-10-06/state-ledger.json), SHA-256 `f078e20b6fca5deec68a8876d83922d03064036aa797fb719cd6cae6d594da2b`, retain every returned node/variable ID and bounds. Created: 20 editable navigation views, 16 file-local stream/state variants in component set `21:289`, nine D-035 spacing variables and 20 separate annotations. Composition root `21:290`; narrow open Detailed 3D frame `21:291`; wide equivalent `21:907`.

The returned traversal found no invalid bounds or horizontal overflow within the 20 frames. The actual [320px open preview](../../../output/research/b01-navigation-composition-2026-10-06/preview-1.png), SHA-256 `b7456f9b8ad726ec8a4cbe1b27978f3f413c0af1de04e01ac64cd7d1ca03ca09`, and [1440px open preview](../../../output/research/b01-navigation-composition-2026-10-06/preview-2.png), SHA-256 `d2688e2b6833450ce4d4c3166f9c9cfa6263cf40d6519355e360b6650f323dfd`, show readable controls/advisement and separate Apply without visible clipping or overlap. These two representative screenshots do not visually inspect all 20 views or establish native radio, keyboard, live-announcement, storage or runtime accessibility behavior.

Coverage added: four streams across open, stream-changed, preference-read-failed and preference-write-failed at 320px; four wide open references. Four capability-ceiling refusal fixtures remain held for coherent capability/prior-stream facts under D-057. Other contracted profiles/templates/primitives, full visual inspection, independent review, editable post-write exports, restore, _EXIT and founder acceptance remain. B01 is DOING; this is not integrated Phase 1 acceptance or application implementation. October attempts 13, conservatively metered 10; actual provider balance/debit unknown, no rate-limit response. This one-call approval is consumed.

### B01 read-only navigation inspection — 2026-10-07

The founder's "all approved including figma" authorized the prepared read-only
attempt 14. The [actual provider result](../../../output/research/b01-navigation-inspection-2026-10-07/provider-result.json)
reports no created/mutated nodes and no reported structural issues across twenty
existing frames, with sixteen variants and nine spacing variables still present.
The script requested eighteen screenshots, but the response supplied only five
PNG blocks. The [producer inspection](../../../output/research/b01-navigation-inspection-2026-10-07/inspection.json)
records the five returned/inspected views and thirteen still missing. Returned
views show readable content and separate Apply without visible overlap/clipping;
structural checks cannot stand in for the missing pixels.

An available-browser fallback reached the private file's sign-in screen; no
authenticated Figma browser tab was exposed. The temporary tab was closed without
authentication, sharing or design changes. A local read-only byte-export script
is prepared to return the thirteen missing PNGs as ID-labelled JSON instead of
inline image blocks; it has not run and requires fresh immediate approval.
October attempts are now 14, conservatively metered 11; actual debit/balance
remain unknown. This call's permission is consumed. Coverage, interaction,
independent design/accessibility review, editable exports/restore/_EXIT and
founder pilot acceptance remain unfinished; no application or Phase 1 approval.

### B01 single-image navigation recovery — 2026-10-07

Status: DOING. The founder approved one temporary comparison-sheet export and
cleanup. Attempt 16 returned a complete 1744 × 6706 native PNG containing the
thirteen previously missing references. The [exact executed script and provider
receipt](../../../output/research/b01-navigation-recovery-2026-10-07/provider-result.json),
[comparison image](../../../output/research/b01-navigation-recovery-2026-10-07/comparison-sheet.png)
and [producer inspection](../../../output/research/b01-navigation-recovery-2026-10-07/inspection.json)
are preserved. Each tile was cropped at its returned bounds and inspected at full
resolution. All thirteen show readable navigation, choices, separate Apply,
explanation/status and footer without visible clipping or overlap. The four active
stream labels/statuses agree in changed/write-failed specimens; wide open specimens
intentionally distinguish the current stream from the pending radio selection.
All twenty created navigation references now have producer pixel inspection.

The receipt reports all 183 created temporary nodes removed, original source
geometry/text fingerprints and positions unchanged, and parent order restored.
Its `exportCompleted` flag remained its initial false value because that assignment
was absent from the exact executed script; the complete returned native PNG is
the export evidence. No retry or original-design correction followed. October
attempts 16, conservatively metered 13; actual provider debit/balance unknown.
This single-call permission is consumed.

Static copied pixels establish no interaction, native radio semantics, keyboard,
storage, live announcement or runtime accessibility result. Other contracted B01
profiles/templates/primitives, independent review, editable post-write exports,
restore, _EXIT and founder acceptance remain held. Earlier receipts retain their
exact limited scopes; no integrated Phase 1 or application approval follows.

## B01 directory call 17 — connection rejected, 2026-10-07

Status: DOING. Founder approved the prepared 52 directory/search references and
two file-local components with **“two approvals granted”**. The exact script's
SHA-256 is `4c811c9122bc049af4b5a01561a97b563c5eed849e9fab20809cdb54b67b62b8`.
The [provider result](../../../output/research/b01-directory-call17-2026-10-07/provider-result.json)
returned `isError: true`, `UNAUTHORIZED` and connection reauthentication required.
No creation receipt, node IDs or representative previews were returned, so this
attempt establishes no directory composition, validation or acceptance.

October attempts: 17; conservative metered attempts: 14. Actual debit/balance is
unknown. The [call receipt](../../../output/research/b01-directory-call17-2026-10-07/receipt.json)
and approved prepared script are preserved. Permission was consumed; no retry,
additional checking call, sharing change or account action was made. Prior six
initial drafts and twenty inspected navigation views retain their own evidence.
Reconnection and fresh per-call approval are required; full B01 coverage, independent
review, restore/_EXIT and founder acceptance remain held.


## B01 directory call 18 — return-size rejection, 2026-10-08

Status: DOING. Founder said **“reconnected—approve one retry.”** One attempt ran
the same prepared 52 directory/search references and two file-local components,
with preflight and representative previews in that call. The script SHA256 remains
`4c811c9122bc049af4b5a01561a97b563c5eed849e9fab20809cdb54b67b62b8`.
The [exact provider result](../../../output/research/b01-directory-call18-2026-10-08/provider-result.json)
is `INVALID_ARGUMENT`: return value 43,790 bytes exceeds 20,480 bytes. The provider
explicitly says **canvas edits were not committed** and returns
`safeToRetryWithoutCanvasRead: true`. No design IDs or preview images were returned.
This is provider rollback evidence, not an independent subsequent canvas reread.

The [receipt](../../../output/research/b01-directory-call18-2026-10-08/receipt.json)
records October attempt18 / conservative metered15; actual debit/balance unknown.
Permission is consumed; no retry, separate inspection or identity call followed.
Prepare a smaller lossless returned report without reducing the approved visual
scope; another call still needs fresh CB-06/CB-07 approval. Previous designs retain
their own evidence. Full coverage, inspection, independent review, native
exports/restore, _EXIT and founder pilot acceptance remain held.


## B01 directory call 19 — corrected return succeeded, 2026-10-08

Status: DOING. Founder approved one corrected retry. The [exact executed source](../../../output/research/b01-directory-call19-2026-10-08/executed-call.js)
SHA256 is `5a84f47c0b09d8d2ac3d922840db2a2e2a480a151a4c9b5d501950db6a1af404`.
Construction bytes match the prior prepared scope; only the returned report is
losslessly compacted. The [provider result](../../../output/research/b01-directory-call19-2026-10-08/provider-result.json)
returned `isError: false`, a complete 15,080-byte report and two native PNGs.

The [decoded result](../../../output/research/b01-directory-call19-2026-10-08/decoded-design-result.json)
contains 2,674 unique created IDs, 52 frame/annotation pairs, two components,
48 narrow320 and four wide1440 views, with zero reported invalid-size or horizontal
overflow findings. Composition is `27:381`; sources `27:372`; components
`27:374` / `27:377`. Existing Page1/style/variable/component preflight ran in the
same call. No separate identity, metadata, font or checking call was used.

[Producer inspection](../../../output/research/b01-directory-call19-2026-10-08/inspection.json)
finds no obvious clipping/overlap in the two returned previews, but they are
scaled: narrow132x1024 and wide720x829. The other fifty view pixels were not
returned; all52 full-resolution typography/layout inspection remains held.
Two illustrative screenshots establish no working search, focus, radio, storage,
keyboard, screen-reader or physical-device behavior. Required design/accessibility
review is separately commissioned at fifteen frozen inputs, not complete yet.

The [receipt](../../../output/research/b01-directory-call19-2026-10-08/receipt.json)
records October attempt19 / conservative metered16; actual debit/balance unknown.
Permission is consumed. No further call, new page/library, sharing change,
application implementation or full B01/Phase1 acceptance follows. Native
post-write exports/restore, _EXIT, complete coverage and founder acceptance remain.

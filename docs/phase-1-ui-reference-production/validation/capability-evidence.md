# Figma capability evidence — MA-025 §3.5

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

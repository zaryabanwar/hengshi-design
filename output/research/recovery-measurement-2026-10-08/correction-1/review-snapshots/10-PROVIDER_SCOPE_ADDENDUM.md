# Provider and Microsoft integration scope — v1

Status: DOING. Current founder amendment D-068, recorded 2026-10-04. This
addendum reconciles the accepted D-065 boundaries with later provider deferral;
it does not alter the frozen architecture or select an implementation adapter.

## What remains accepted

Retain the web application and modular API, PostgreSQL durable truth, derived
publication artifacts/search and ephemeral presence/cache. Server authorization,
review/approval separation, durable external intent and reconciliation, eligible
release fencing and privacy-safe recovery remain requirements. Approved Entra
staff identity and the approved Azure Europe personal/confidential AI route are
unchanged. NVIDIA remains restricted to eligible data under its separate gate.

## What is deferred

The founder has an Azure account, does not use or plan Microsoft 365 setup, and
is open to Azure or AWS hosting. Deployment/provider/region/SKU/cost planning is
deferred; no exclusive hosting target is selected by an earlier Azure/AWS mapping.
Prefer the lowest feasible cost/free services when planning resumes. Do not infer
that a free tier meets residency, capacity, recovery or licensing requirements.
Europe is the first market, not an automatically chosen hosting region or office.

Keep the deployment obligation visible for later acceptance and launch. This
deferral neither accepts the complete Phase 1 package nor authorizes application
development, resources, account changes, purchases, migrations or deployment.

## Outlook/Teams intent and actual API capabilities

Retain Outlook/Teams for the intended calendar, meeting and staff workflows.
Microsoft 365 subscription/setup is not a blanket project prerequisite. The
founder's chosen apps and the API needed by a particular automated workflow are
separate capability questions. Official primary documentation checked 2026-10-04:

| Capability | Official observation | Project implication |
|---|---|---|
| Teams personal use | [Microsoft support](https://support.microsoft.com/en-us/teams/personal/get-started/sign-in-sign-up-sign-out-and-add-a-new-account-in-microsoft-teams-personal) says a Microsoft account is sufficient; Outlook.com users already have one. | Retain the founder's free/personal app intent; no blanket Microsoft 365 purchase requirement. |
| Calendar event creation | [Graph v1.0 create event](https://learn.microsoft.com/en-us/graph/api/user-post-events?view=graph-rest-1.0) lists delegated personal-account `Calendars.ReadWrite`. | A personal calendar integration is a candidate, not proof the actual company mailbox has the required account, permission or meeting provider. |
| Direct onlineMeeting creation | [Graph v1.0 create onlineMeeting](https://learn.microsoft.com/en-us/graph/api/application-post-onlinemeetings?view=graph-rest-1.0) lists personal delegated accounts as unsupported; work/school delegated and application routes have separate permissions. | Do not promise this endpoint works with a personal Teams account or infer that creating a calendar event creates an eligible Teams meeting. Exact supported route remains held. |
| Graph presence lookup | [Graph v1.0 get presence](https://learn.microsoft.com/en-us/graph/api/presence-get?view=graph-rest-1.0) lists personal delegated accounts as unsupported. | Do not label staff online based on a guessed API or app sign-in. Preserve the accepted authoritative availability and stale/offline recovery requirements. |

These are documented API capabilities, not capability tests on the founder's
account. Mailbox ownership, scopes/consent, permitted calendar/meeting operations,
presence freshness, adapter retries/lookups and notification permissions still
need verification in a later authorized integration slice. Do not purchase a
license, remove Outlook/Teams, replace Entra or choose a different provider to
silently resolve a missing capability.

Booking must retain its confirmed/pending/unknown truth and duplicate prevention;
calendar creation alone cannot establish the complete booking outcome. Human
handoff still needs explicit current staff availability and consent. A personal
app observation cannot satisfy those runtime acceptance obligations.

## Reconciliation references

Current authority: D-068–D-070, constitution, AGENTS.md and the software-definition
entry points. This scoped amendment applies when interpreting older cloud service
names in the accepted architecture and proposed interface/data/QA records. It
changes provider planning authority, not the accepted component responsibilities
or data policy. MA-005 is deferred; MA-006 retains actual capability verification.

No API/account calls, mail messages, app registrations or paid activations were
performed for this addendum. Full Phase 1 and integration acceptance remain held.

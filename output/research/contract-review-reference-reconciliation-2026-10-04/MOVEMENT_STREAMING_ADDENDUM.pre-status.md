# Movement and spatial-streaming architecture addendum

Status: DOING. Date: 2026-10-04. D-064/D-066/D-067 define selected scope;
the decomposition below is PROPOSED for independent review and acceptance.

The earlier [World/addendum independent review](../phase-1-3d/reviews/world-reconciliation-2026-10-04.md)
covers its recorded hashes only. The release-pin clarification below was added
after that review and awaits independent assessment; the frozen D-065 baseline
is unchanged.

## Accepted baseline and targeted amendment

D-065 accepts the exact reviewed [architecture](ARCHITECTURE.md) and
[authority map](authority-map.csv). Preserve their reviewed bytes and provenance.
D-064 supersedes the baseline's directed-only exploration and statement that no
free-roam requirement is introduced. Free movement supplements destinations;
WASD stays unselected. All unrelated baseline constraints remain accepted.

The [World definition](../phase-1-3d/WORLD_EXPERIENCE.md) defines the selected
journey and proposed controls, loading behavior and sound. Its unaccepted details
do not silently amend accepted delivery-stream or privacy policy.

## Responsibilities

| Component | Additional responsibility | Authority it does not acquire |
|---|---|---|
| Web immersive runtime | Position, camera, collision-safe travel, chunk scheduling, measured residency, audio-zone playback and semantic panel interaction | Publication approval, staff availability truth, bookings, durable personal data or provider credentials. |
| Published scene artifacts | Versioned immutable chunk/asset manifest, canonical content associations, collision/export metadata and visual variants | A second content database or independent release activation. |
| API publication | Enforce role-separated evidence review/founder approval and generate/validate consistent scene-manifest references with other public derivatives | Trusting visitor-chosen asset URLs or bypassing content review for scenery/panels. |
| API handoff | Existing explicit availability, consent and auditable human session | Inferring staff presence from an avatar, room occupancy or ambient sound. |
| Shared semantic surface | Equivalent routes/actions and accessible World controls | Requiring GPU resources, live movement or sound to read/help/book. |

No additional deployable or microservice is selected. Model chunks are static
release artifacts, not per-movement database calls. Browser position is session
state; do not add movement histories, precise paths or device fingerprints to
analytics. Aggregate cookieless measurement stays within accepted policy.

## Failure and consistency contract

1. Entry resolves an eligible approved immutable release. Subsequent scene reads
   retain that visit's eligible release pin under the publication contract;
   an active-pointer change does not independently switch each chunk. Asset
   mismatches fail safely, and a valid checksum alone cannot grant eligibility.
2. Loading cannot expose drafts, mix releases or create a false service-open state.
3. Movement may cross a boundary only after safe collision/ground data is ready.
4. Failed loading preserves position, interaction/process state and semantic access;
   user-visible recovery cannot claim completion of any external operation.
5. Resident areas and asset ownership must be disposed safely on eviction/exit.
6. Audio/controls/animation have session cleanup; absence of any one preserves
   equivalent content and booking/handoff processes.

Use the proposed [publication refresh/eligibility contract](contracts/PUBLICATION_CONTRACT.md#visitor-release-refresh-and-eligibility)
and [World refresh behavior](../phase-1-3d/WORLD_EXPERIENCE.md#release-changes-during-a-visit)
for ordinary refresh, urgent withdrawal, late responses and safe destination
resolution. Public context refresh cannot duplicate or change the confirmed truth
of a private handoff/booking lineage. Server eligibility/action authorization
remains authoritative; no offline serving guarantee or client-controlled drain.

Exact manifest schema, scheduling/freshness limits, release cutover, budgets and
tests still require reviewed downstream contracts. This addendum selects no new backend endpoint,
database table, package/version, provider, paid resource or automatic tier change.

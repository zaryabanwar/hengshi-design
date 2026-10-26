# Staff sign-in walkthrough — independent v1 translation review

Date: 2026-10-06. Reviewer: `review_staff_signin_boundary_v1`, independent of
the producer. Verdict: **PASS for the bounded visual translation**; no actionable
finding. Task status: DOING; commits remain deferred. This does not accept the
full board, production staff UI, authentication implementation or Phase 1.

## Scope and exact inputs

Reviewed only `definition-walkthrough.html:47–53` (`details#staff-sign-in`) and
the new `Staff identity and sessions` row at `README.md:32`. Independently removing
only that details element and row reproduces both preserved predecessors exactly,
including line endings. All other content, styles and scripts are unchanged.
Canonical producer files equal their preserved reviewed snapshots.

The [22-input manifest](../../../output/playwright/staff-signin-walkthrough-2026-10-06/review-inputs.json)
has SHA-256 `f6fb18f802733d368f9613bfe47bfd3b07a6a9a4b835956589b1afae717995ec`.
All 22 hashes were independently recomputed before review and again after writing
this receipt. Its governance, feature, package/lock and evidence inputs retain
their frozen identities. Exact key inputs are:

| Input | SHA-256 |
|---|---|
| HTML and reviewed snapshot | `da1ebd5ca572b54af1f72950f8466e45add94b7dd394e7ef4e39d6c157f1c573` |
| HTML predecessor | `0cc349364c8911acc5660649b6c5b09d974e833752c9eb28edbbe3b8538e19c1` |
| README and reviewed snapshot | `d02783261a2f55c6a732f232743ff1ed75400b8853837d2f498e24a9f7d6027d` |
| README predecessor | `bb666897e105df28616d4fe71f085f691c214ec28913220ad386093d91e72a3c` |
| Current security contract | `50f3c00d5e6aed36bb4fa99e864ba337cc3dc3f76c0665ff30e0f765782ad00a` |
| Bounded contract-review receipt | `33c15ae66c8fae70ce86cf1ef42b3aad52a3f39076e6beb1e0660fed31ea215a` |
| Security feature spec | `47704c411b72195a2a4f8b832b07b30d90b00673647afe50d8ac98b917939d99` |
| [Complete desktop capture](../../../output/playwright/staff-signin-walkthrough-2026-10-06/desktop.png) | `0f0fe25981ef5f9be11d0a4d7db6ee93a299ad099b98173b29da15c05dfaa9da` |
| [Complete mobile capture](../../../output/playwright/staff-signin-walkthrough-2026-10-06/mobile.png) | `c10d90bdba97ac1e3f8420a09e0252de6bce9f57a8bc1bf129c1488184e5353b` |
| [Producer browser observations](../../../output/playwright/staff-signin-walkthrough-2026-10-06/browser-observations.json) | `ae0e642fad585f2dcd5c3a1eed5a1d45a6bdc2d1a1c551660830d9b9ea128e60` |

The current contract's later review-reference notice explicitly lies outside the
earlier engineering receipt. Independently compared recommendation, admission,
session/failure and research obligations are unchanged from the engineering
correction-2 bytes (`e02a0129dbf616013f6627ab717885a23d1c46e2e4b35fb482423870d316f094`).
This visual review neither changes that proposal nor transfers its verdict to
later unrelated bytes.

## Source, pixels and meaning

The reviewer opened **both** PNGs with `view_image` at original detail. Each shows
the complete expanded panel: summary, proposal notice, four steps, both explanatory
cards, all held-policy text and both source links. Desktop columns and the mobile
single-column sequence are readable without observed text clipping or overlap.
The visible focused review link is consistent with the supplied capture state;
screenshots alone do not establish keyboard behavior or accessible names.

The native details/summary, ordered steps, cards and local source links translate
the controlling proposal and FSC-01–FSC-06 coherently. The links resolve to the
existing sign-in proposal and final correction-2 verdict heading. Microsoft sign-in
identifies a principal; Hengshi separately admits eligible staff and checks current
action/record/state authority. The panel does not grant editor publication powers,
change identity to a local account, infer integration permissions, impose Microsoft
365 or automatically activate emergency access. Protected cookie/JavaScript
separation, 30-minute idle/eight-hour absolute limits and held exact policies remain.

On 2026-10-06 the reviewer independently read the primary Microsoft
[revocation guidance](https://learn.microsoft.com/en-us/entra/identity/users/users-revoke-access)
and [OIDC single-sign-out guidance](https://learn.microsoft.com/en-us/entra/identity-platform/v2-protocols-oidc#single-sign-out)
through read-only direct HTTPS requests (HTTP 200). Application-issued sessions
require application authorization/revocation; Entra cannot directly revoke them.
Coordinated front-channel logout needs app-registration configuration and application
session clearing. Thus the panel's conditional statement that the same bound
Hengshi identity may remain after Microsoft logout elsewhere, subject to Hengshi
rules, is accurate. It promises neither indefinite access nor immediate provider
revocation, and selects no coordinated-sign-out policy or account setting.

Producer observations separately report summary Space/Enter behavior, Tab to the
two links, no horizontal overflow and no console errors/warnings at desktop/mobile
interaction viewports. Those interactions were **not replayed independently** in
this review. Independent evidence here is source/link inspection, predecessor/hash
comparison and inspection of the complete supplied pixels; it is not a live-browser,
physical-phone or assistive-technology test.

## Held gates and limits

The panel explicitly explains a proposed system and functioning sign-in is absent.
Its status label reports the underlying bounded engineering review, not founder
approval of mechanisms or this visual. Exact account/tenant/guest/grant policy,
callback/CSRF/key/rotation/revocation/freshness/outage controls, MFA, retention/legal,
Microsoft capabilities, stable graph, approved staff designs and actual behavioral
evidence remain held. Founder and integrated Phase 1 acceptance, B01/external
design writes, commits, activation and deployment remain separate. No package,
account, credential or security policy was selected or changed. No prose/runtime
tests or application changes were performed; only this review receipt was written.
PASS certifies bounded translation consistency, not security enforcement,
accessibility conformance, production UI approval or complete-board acceptance.

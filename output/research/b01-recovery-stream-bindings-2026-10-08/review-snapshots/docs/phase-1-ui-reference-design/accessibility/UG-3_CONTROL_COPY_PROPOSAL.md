# UG-3 — Delivery-stream control copy and radio order

**Accepted definition under D-057; independent nonauthor review PASS.**
Date: 2026-10-03. Independent accessibility specification author, D-044 pattern.
Definition approval only: this exact copy/order bundle is approved, not implemented or published, and no conformance, consent, legal-basis or storage-success claim is established. No Figma write, publication, commit or push is authorized.

Founder approved the complete bundle on 2026-10-03. Proposal headings and the
original decision request below are retained as provenance, superseded by D-057.

## Recommended peer labels and order

| Order | Stream | Proposed exact radio label |
|---|---|---|
| 1 | S-HIGH | Detailed 3D |
| 2 | S-MEDIUM | Balanced 3D |
| 3 | S-LOW | Simplified 3D |
| 4 | S-SEMANTIC | Quick Access |

Retain the provisional accepted-table order for continuity, without treating it as quality, importance or destination ranking. Equal radio treatment; no recommended/best badge or default implied by position. Capability rules determine the initial in-force value, not order. “Simplified” describes visual fidelity only. Proposed persistent peer explanation: **“Every option offers the same destinations and core journeys. The 3D options differ in visual detail. Quick Access presents the journey without a 3D scene.”** Labels never describe Quick Access as a fallback or failure. Label meanings and order must be approved together.

## Proposed exact phrases

Braced values below are runtime substitution slots, not public literal text. `{active_label}` and `{selected_label}` use only the four approved labels; destination slots use approved public names. `{verified_capability_reason}` must name an established client fact, not an inferred device tier or invented threshold. No identity or sensitive saved-location inference.

| Context | Proposed wording |
|---|---|
| Legend / group accessible name | “Delivery stream — currently {active_label}” |
| Apply visible label and accessible name | “Apply selection” |
| Persistent advance advisement, before Apply | “Selecting an option does not change your experience. Apply selection re-enters the experience only when you choose a different option, keeping your current location where available. If that location has no match, you will arrive at the nearest available parent destination and be told where you are. Applying the current option makes no change.” |
| Above-ceiling option reason | “This option is unavailable on this device: {verified_capability_reason}. Your current stream remains active.” |
| Changed selection, same shell | “{selected_label} is now active. You are still at {destination}.” |
| Changed selection, destination shell arrival | “{selected_label} is now active. You have arrived at {destination}.” |
| Nearest mapped ancestor arrival | “{selected_label} is now active. {requested_destination} has no matching location in this stream. You have arrived at {ancestor_destination}, its nearest available parent destination.” |
| Already-active Apply / no-op | “{active_label} is already active. Your experience has not changed.” |
| Change failed | “We could not apply {selected_label}. {active_label} remains active.” |
| Preference write failed, after session application | “{selected_label} is active for this visit, but we could not save your choice for future visits. You can choose a stream again. Read Privacy and storage for details.” |
| Preference read failed, destination shell | “We could not read your saved stream choice. This visit is using {active_label}. You can choose a stream again. Read Privacy and storage for details.” |
| Privacy link visible/accessibility name | “Privacy and storage” — target `/privacy` |
| Preference-reset action | “Clear saved stream choice” |
| Reset warning, before any deletion | “Clearing your saved stream choice removes it for future visits. Future visits will use capability-based selection unless you choose a stream again. Your current stream and this visit will stay unchanged. Clear your saved choice?” |
| Reset confirmation action | “Confirm reset” |
| Reset cancellation action | “Cancel” |
| Cancelled reset status | “Reset cancelled. Your saved stream choice and current visit are unchanged.” |
| Verified reset success status | “Your saved stream choice was cleared. {active_label} remains active for this visit. You can choose a stream again. Read Privacy and storage for details.” |
| Reset failure or unverifiable clearing status | “We could not verify that your saved stream choice was cleared. {active_label} remains active for this visit. Read Privacy and storage for details.” |
| Reselection action | “Choose a stream” |

## Usage safeguards and authority

Persistent peer explanation and advance advisement stay visible in the fieldset before Apply in DOM and visual order, associated with group and button; not tooltip-only or screen-reader-only. Group name retains the in-force label while the checked radio identifies only the pending selection. Announcements are polite status messages after explicit activation; radio movement does not announce application. Same-shell focus, route, scroll and panels remain preserved; cross-shell arrival follows the accepted named destination-control focus rule. A nearest-ancestor message replaces the normal arrival message when applicable, avoiding contradictory announcements.

No-op Apply stays enabled under D-053 and performs no reload, transition or persistence mutation. “For this visit” is used only after application has actually succeeded for the session. A read failure does not claim stored data is absent or erased. Reset success wording requires verified persistent clearing; failed or unverifiable clearing uses the limitation message. No deletion occurs before Confirm reset; Cancel preserves choice/session. Preference reset neither applies a stream nor delays staff sign-out. Privacy wording is a link name, not approval of final legal content or a consent exemption. Native-radio rendering and backed scene-focus decisions are unchanged.

Local authority: amendment UG-3; accepted `DELIVERY_STREAM_ACCESSIBILITY_OBLIGATIONS.md` OBL-CTRL-01/02/05, OBL-ADV-01 and OBL-STATE-04; style guide §§8.2.4/8.2.6; DECISIONS D-045 and D-051–D-056. Device thresholds, geometry, token values and final legal content remain separately gated.

**Founder decision requested:** approve this complete proposed phrase-and-order bundle, or identify requested wording/order changes. Approval would authorize definition reconciliation only; browser/user validation and application/visual production remain separate gates.

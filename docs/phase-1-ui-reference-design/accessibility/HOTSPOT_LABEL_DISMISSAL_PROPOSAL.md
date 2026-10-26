# Hotspot expanded-label dismissal

**Accepted definition under D-058; corrected nonauthor review PASS.**
Date: 2026-10-03. Addresses MA-029 accessibility finding A-01 and OBL-TRACE-02; Close label action wording is accepted for definition use under D-058; no implementation, publication, visual approval or conformance claim.

Founder accepted the complete mechanism on 2026-10-03. Proposal headings and
original choice below are historical provenance superseded by D-058; browser
validation and implementation gates remain.

## Recommended mechanism

Keep the existing visible base label, accessible hotspot name, static focus cue and activation action. The additional expanded label appears on hotspot hover or keyboard focus; it is supplementary descriptive content, not a modal, navigation panel or replacement for the hotspot's accessible name.

- **Hoverable:** moving the pointer from the hotspot onto its expanded label, including its dismissal affordance, keeps it open. The hotspot and label form one continuous hover region; crossing between them must not cause disappearance. Geometry must later provide a usable path at magnification and with a large pointer; exact geometry remains gated.
- **Persistent:** while either keyboard focus anywhere in the combined hotspot/expanded-label region (including Close label) or hover within that combined region remains, the expansion stays visible without timeout, unless deliberately dismissed or its information becomes invalid. Removing only one trigger does not close it while the other remains.
- **Dismissible:** Escape dismisses expanded hotspot labels without moving pointer position or keyboard focus, activating a hotspot, closing a panel, going back or navigating. Only the additional expansion closes; the base label, accessible name and persistent focus indicator remain.
- Include a visible, accessibly named **Close label** action within each expanded label. Pointer activation must preserve existing keyboard focus; keyboard activation retains focus on the hotspot or restores it there when the disappearing dismissal action had focus. Neither dismissal action activates the hotspot. D-058 accepts Close label as the action wording for definition use; implementation/publication remain gated.

## Escape precedence — proposed scoped rule

1. Focus inside the delivery-stream radios or Apply: retain the accepted D-045/UG-8 exception unchanged. Escape dismisses nothing, cancels nothing, applies nothing and does not navigate. No hotspot label handler may override this rule.
2. Otherwise, if expanded hotspot labels are visible because of hover or focus: one Escape dismisses those expansions only; it is not also handled as host close-panel/go-back. Dismiss all currently visible expansions to avoid ambiguity when hover and focus belong to different hotspots.
3. Otherwise: retain existing host close-panel/go-back behavior. Never assign dismissal to Enter or Space; those retain hotspot activation. Do not alter non-label dialogs, navigation panels or other component key contracts.

If a hover label is visible while focus is inside the delivery-stream control, use its Close label action; pointer activation must leave control focus unchanged. This overlapping-trigger case requires explicit browser/keyboard/magnifier review before implementation acceptance; do not claim Escape is available in that protected scope or silently weaken the control exception.

## Dismissal latch and return

Recommend keeping a dismissed expansion collapsed until **both** hover has left its combined region and focus has left its hotspot/label, then a subsequent hover or focus entry starts a fresh episode. No immediate reopening on rerender, pointer movement within the region, focus retained on the hotspot, or a timeout. This latch is a new proposed interaction choice, not an existing approved rule; it prevents the dismissal from being undone by the trigger still present. The base name and activation remain available throughout.

## Acceptance scope and founder decision

Later tests must cover hover-only, focus-only and simultaneous different hover/focus hotspots; pointer movement onto the label; Escape precedence with panels and the protected stream control; Close label activation without unwanted focus movement; re-entry after dismissal; large pointer, 400% zoom, reduced motion and forced colours, independently in applicable streams. No canvas-only action/name, focus loss or navigation side effect is acceptable. In S-SEMANTIC, test any equivalent hover/focus expansion if present; absence of a canvas does not waive an applicable content-on-hover obligation.

Source: W3C Understanding SC 1.4.13 explains dismissibility without moving hover/focus, hoverability and persistence. Its non-obscuring-content exception is **not** assumed here. Requirement-level reconciliation must follow approval, including the existing style-guide focus row's expanded-label promise being qualified for explicit dismissal.

**Founder choice:** approve the scoped Escape/Close label mechanism and the leave-both-then-re-enter latch, or request another mechanism. This proposal authorizes no handler implementation, full UI acceptance, Figma calls, publication, commits or pushes.

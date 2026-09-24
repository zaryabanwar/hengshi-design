# Notice

A standing notice on a raised inverse panel with an amber rule, for a limitation the reader must not miss. Hand-written from `docs/phase-1-brand-identity/visual-boards/identity-board.css` (`.clearance`), where it carries the trademark clearance status; maps to the static half of PRIM-057 Notification and live status region.

**When to use.** Persistent limitations and conditions: clearance status, held content, a gate that has not closed, a route that is unavailable with its alternative.

**Provide.** One paragraph of plain language; optionally a leading `<strong>` status in the evidence face ("EXPLORATORY, UNREGISTERED, TRADEMARK NOT CLEARED"). For live announcements add `role="status"` and let the text change without moving focus.

**Anatomy.** `.hd-notice`: `hd-surface-inverse-raised` (graphite in the light theme, mist in the dark), `hd-text-inverse`, a 4px `hd-signal-amber-on-inverse` left rule (`hd-stroke-notice-rule`), padding `hd-space-4`, square corners, no shadow.

**Do.** Keep the measure at or under 72ch; state the next action; keep it readable in print and forced colours (the border is its boundary).

**Don't.** Use it for success or marketing; animate it; rely on the amber rule alone to say "attention" (the text does that).

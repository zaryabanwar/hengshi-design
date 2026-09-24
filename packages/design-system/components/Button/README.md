# Button

The one conversion action per surface (Book) as a primary fill, everything else as a bordered secondary. Hand-written from `docs/phase-1-brand-identity/visual-boards/identity-board.css` (`.actions a`, `.secondary`); covers PRIM-014 Primary booking CTA and PRIM-015 General action button.

**When to use.** One primary button per surface, always the booking or next accountable action; secondary buttons for adjacent routes ("See verified work", "Quick Access"). A link that only navigates within content is a text link, not a button.

**Provide.** The label in sentence case (`hd-action` style, weight 800); an `<a href>` for navigation or a `<button type>` for an action; `disabled` or `aria-disabled="true"` when the action is held, together with visible text saying why and the next route.

**Anatomy.** `.hd-button` plus `.hd-button--primary` or `.hd-button--secondary`. Padding 0.8rem 1rem, radius `hd-radius-control` (8px), 1px border. Group buttons in `.hd-actions` (0.8rem gaps, wrapping). Inside `.hd-inverse` the primary becomes `hd-signal-cyan-on-inverse` with `hd-text-primary`, and the secondary takes `hd-text-inverse` with an `hd-text-muted-on-inverse` border.

**Do.** Keep the label to a verb phrase; keep at least 24 by 24 CSS px of target; let long labels wrap (`overflow-wrap: anywhere`); rely on the global focus ring.

**Don't.** Colour a button amber to mean danger (amber is attention, not destructive); use all caps; put two primaries on one surface; hide the reason a button is disabled.

**Undecided in the source.** Hover and pressed colour pairings are not approved yet: hover underlines, pressed keeps the native state.

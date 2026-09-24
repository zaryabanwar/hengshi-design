# Card

A bordered raised block for one collection item, with an inverse recommended variant. Hand-written from `docs/phase-1-brand-identity/visual-boards/identity-board.css` (`.direction`, `.direction.recommended`); covers the item-card half of PRIM-010 Collection item card or row.

**When to use.** Items in a collection (work, demos, insights, experts, trust topics, services, industries) where each needs a title, summary, evidence state and one canonical action. Prefer open sections over nested cards on detail pages.

**Provide.** An `<h3>` title; a summary paragraph; optionally a `<dl>` of label and value pairs; an EvidenceStateLabel; a Tag when the item is recommended; the canonical link as text inside the card, never the whole card as the only link.

**Anatomy.** `.hd-card`: `hd-surface-raised`, 1px `hd-border-subtle`, padding 1.25rem, square corners, no shadow. `.hd-card--recommended`: `hd-surface-inverse` with a 3px `hd-signal-cyan-on-inverse` frame and a title in `hd-text-muted-on-inverse`. Lay cards out in `.hd-card-grid` (auto-fit columns, 1.5rem gaps) so they reflow to one column at narrow widths.

**Do.** Let titles and labels wrap without truncation; keep the card readable with images missing; keep focus visible beyond the border.

**Don't.** Add a coloured left rule (that is the Notice); use shadow or radius for hierarchy; make the card itself the link; show an empty placeholder card.

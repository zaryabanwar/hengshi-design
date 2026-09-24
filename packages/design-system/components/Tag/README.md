# Tag

A short solid amber label such as "Recommended" that flags one item among peers. Hand-written from `docs/phase-1-brand-identity/visual-boards/identity-board.css` (`.tag`); the identity board uses it once, on the recommended direction card.

**When to use.** One word or two beside or above a title when a single item needs to stand out for a stated reason: recommended, new, current. It is not an evidence state; use EvidenceStateLabel for proof status and the release label primitive (PRIM-008) for availability.

**Provide.** The text, in sentence case. Nothing else.

**Anatomy.** `.hd-tag`: `hd-status-attention-fill` (amber) with `hd-text-on-signal` (ink), padding 0.25rem 0.5rem, weight 800, square corners. Ink on amber reads at 10.49:1 in both themes.

**Do.** Keep it small and rare (signal colour stays under about 10% of a composition); pair it with the reason in nearby text.

**Don't.** Stack several tags; use it as a button; round it into a pill (pills are `hd-radius-status`, for short status labels with visible text); mean danger by it.

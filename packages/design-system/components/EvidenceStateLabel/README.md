# EvidenceStateLabel

A visible evidence label with its frozen marker shape and rail pattern, so proof type never depends on colour. Hand-written from `docs/phase-1-brand-identity/semantic-tokens.json` (`evidenceState`) and the identity board `.state` chips; covers PRIM-007 Evidence state label.

**When to use.** Beside any claim, item, collection entry or media that carries evidence status: verified work, Hengshi-owned demonstrations, proposed methods and requirements, conditional items, held or unavailable content, and errors.

**Provide.** The state modifier (`--verified`, `--demo`, `--proposed`, `--conditional`, `--unavailable`, `--error`); the glyph and rail SVGs exactly as in the preview (16-unit glyph, 48-unit rail, `currentColor`); the label text with its context: source and date for Verified, the exact condition for Review needed, the next route for Held, the recovery action for Error.

**Anatomy.** `.hd-evidence-state` sets the `hd-evidence` monospace style in `hd-text-primary`; the modifier sets `--hd-state` from `hd-status-*`; glyph and rail inherit it. Inside `.hd-inverse` the modifiers switch to the `hd-signal-*-on-inverse` tokens.

**Do.** Keep the full label; let it wrap; keep marker and rail visible in grayscale and forced colours (they are shapes, so they survive); repeat the state in body text where the label is the only mention.

**Don't.** Show "Verified" before the evidence and publication gates are satisfied; reuse these markers for data series; drop the label and keep only the glyph; tint error content amber (only its boundary is amber).

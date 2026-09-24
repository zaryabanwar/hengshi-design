# Hengshi Design System export

Status: derived, non-authoritative. Extracted 2026-09-23 from the Phase 1 identity package at commit `989af66`. Published as the Design System artifact at https://claude.ai/artifact/GneryeqprmQm8yg7HKPJZZ; this folder mirrors that artifact's `project/` tree so the artifact can be rebuilt from the repository.

## Authority

- The identity source layer (`hd-color-*`, type roles, spacing, radius, stroke, layout) copies `docs/phase-1-brand-identity/semantic-tokens.json` and `visual-boards/identity-board.css` exactly, using the reserved code names from `docs/phase-1-ui-reference-design/DESIGN_SYSTEM_IMPLICATIONS.md` section 2.2.
- The semantic aliases (`hd-surface-*`, `hd-text-*`, `hd-border-*`, `hd-focus-*`, `hd-action-*`, `hd-status-*`, `hd-data-series-*`) are **[PROPOSED]** resolutions of the families section 2.3 leaves unspecified. They carry no accepted authority, do not amend the freeze file, and are input to the R-039 design-system amendment contract (D-045 gate G-6), not a substitute for it.
- Not covered here, still open under R-039: the delivery-stream axis, the stream-control component, the four `DS-S-*` stream tokens, and the 3D focus-ring token.
- Logo and specimen SVGs under `assets/` are byte-identical copies of `docs/phase-1-brand-identity/assets/`, which remains the original with its hashes in `asset-manifest.json`. All marks are EXPLORATORY, UNREGISTERED, TRADEMARK NOT CLEARED.

## Layout

| Path | Content |
|---|---|
| `README.md` | Brand book: principles, voice, colour, type, spacing, focus, iconography, logo, imagery, modes |
| `tokens.json` | Tokens in the Design System artifact format; `meta.source` records provenance |
| `guidelines/` | Logo system, evidence states and data series, motion/sound/3D, component inventory (all 62 primitives, built status) |
| `components/bundle.css` | CSS-only component layer consuming semantic tokens |
| `components/<Name>/` | Guideline README and static preview per component; `Cover/` is the artifact cover |
| `assets/` | Logo and specimen copies with a README per group |
| `design-system.json` | Artifact index (asset records, namespace, last change) |

The artifact page generates `tokens.css` from `tokens.json`; no compiled CSS is committed. To republish, read the artifact index, change files here, and publish only the changed paths to the artifact URL.

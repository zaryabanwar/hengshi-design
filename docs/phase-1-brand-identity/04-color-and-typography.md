# Color and Typography

## Color philosophy

Architectural mineral neutrals carry most surfaces. Luminous signals identify a
small number of meaningful actions and states. Color is always paired with text,
shape, line pattern, icon, position, or data marker.

## Core palette

| Token | Hex | Role | Usage limit |
|---|---|---|---|
| `color.ink` | `#0B0F14` | Primary dark canvas and dark text | Default dark foundation |
| `color.graphite` | `#161D26` | Raised dark surfaces | Never a subtle-on-ink text color |
| `color.slate` | `#2A3542` | Borders, secondary dark surfaces | Pair with white/paper text only |
| `color.stone` | `#D8D3C8` | Warm structural neutral | Large fields and dividers; not small text on paper |
| `color.mist` | `#F3F1EA` | Soft light surface | Light surface with ink/graphite text |
| `color.paper` | `#FAF9F6` | Primary light canvas | Light foundation |
| `color.white` | `#FFFFFF` | High-contrast text and print field | Avoid as ambient glow |

## Surface-specific signal tokens

| Token | Hex | Surface | Semantic role |
|---|---|---|---|
| `color.signal.cyan.onDark` | `#00D4FF` | Ink/graphite | Primary action, active connection, current path |
| `color.signal.amber.onDark` | `#FFB000` | Ink/graphite | Attention and conditional state |
| `color.signal.lime.onDark` | `#B6F36B` | Ink/graphite | Verified state and data series |
| `color.signal.violet.onDark` | `#A98CFF` | Ink/graphite | Demonstration state and spatial resonance |
| `color.signal.cyan.onLight` | `#006D82` | Paper/mist/white | Cyan semantic equivalent for text, focus, icons, and lines |
| `color.signal.amber.onLight` | `#8A5600` | Paper/mist/white | Amber semantic equivalent for text, icons, and lines |
| `color.signal.lime.onLight` | `#4F7D18` | Paper/mist/white | Lime semantic equivalent for text, icons, and lines |
| `color.signal.violet.onLight` | `#6D52B5` | Paper/mist/white | Violet semantic equivalent for text, icons, and lines |

Signal color occupies no more than approximately 10% of a typical composition.
This is an art-direction control, not a measured accessibility threshold.

## Declared WCAG 2.2 contrast pairings

Ratios are calculated from sRGB hex values using WCAG relative luminance:

`(lighter luminance + 0.05) / (darker luminance + 0.05)`

| Foreground | Background | Ratio | Permitted text/use |
|---|---|---:|---|
| Paper `#FAF9F6` | Ink `#0B0F14` | 18.25:1 | All text and controls |
| Mist `#F3F1EA` | Graphite `#161D26` | 15.01:1 | All text and controls |
| Stone `#D8D3C8` | Graphite `#161D26` | 11.37:1 | All text and controls |
| Cyan `#00D4FF` | Ink `#0B0F14` | 10.86:1 | Text, focus, icons, graphics |
| Amber `#FFB000` | Ink `#0B0F14` | 10.49:1 | Text, attention, icons, graphics |
| Lime `#B6F36B` | Ink `#0B0F14` | 14.66:1 | Text and data markers |
| Violet `#A98CFF` | Ink `#0B0F14` | 7.21:1 | Text and data markers |
| White `#FFFFFF` | Slate `#2A3542` | 12.45:1 | All text and controls |
| Slate `#2A3542` | Paper `#FAF9F6` | 11.83:1 | All text and controls |
| Muted slate `#64748B` | Paper `#FAF9F6` | 4.52:1 | Normal text only at tested size; not thin/small metadata |
| Cyan on-light `#006D82` | Paper `#FAF9F6` | 5.68:1 | Text, focus, icons, graphics on paper |
| Cyan on-light `#006D82` | Mist `#F3F1EA` | 5.29:1 | Text, focus, icons, graphics on mist |
| Amber on-light `#8A5600` | Paper `#FAF9F6` | 5.85:1 | Text, icons, and conditional graphics on paper |
| Lime on-light `#4F7D18` | Paper `#FAF9F6` | 4.66:1 | Text, icons, and verified graphics on paper |
| Violet on-light `#6D52B5` | Paper `#FAF9F6` | 5.66:1 | Text, icons, and demonstration graphics on paper |

All declared normal-text pairings meet or exceed 4.5:1. Large text is not used to
excuse lower contrast in this definition. Focus and meaningful non-text graphics
target at least 3:1 against adjacent colors, but the declared signal pairings are
held to the stronger text threshold. Disabled content remains readable and is
not used for required actions.

## Status encoding

| State | Color | Shape/line | Required label |
|---|---|---|---|
| Verified | Lime | Filled circle plus solid rail | `Verified` with source/date context |
| Hengshi-owned demo | Violet | Open diamond plus dash-dot rail (`10 4 2 4`) | `Hengshi-owned capability demonstration` |
| Proposed/requirement | Cyan | Filled square plus short-dash rail (`8 6`) | `Proposed` or `Requirement` |
| Review needed/conditional | Amber | Filled triangle plus long-dash rail (`16 7`) | `Review needed` or exact condition |
| Unavailable/held | Neutral | Filled bar plus dotted rail (`2 7`) | `Unavailable` or `Held` with next route |
| Error | Amber boundary with neutral content | Open octagon plus two parallel solid rails | Plain-language error and recovery action |

No state uses color alone. “Verified” may appear only when the applicable
evidence and publication gates are satisfied.

## Typography hierarchy

No font file included. No font file is downloaded, embedded, purchased, or
redistributed. Preview
stacks use locally available system fonts and CSS generic families.

| Role | Stack | Weight/size guidance | Use |
|---|---|---|---|
| Display | `system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Arial, sans-serif` | 650/700; 40–72 px; 0.95–1.05 line height | Entity, promise, decisive headings |
| Text | `system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Arial, sans-serif` | 400–500; 16–20 px; 1.5–1.7 line height | Body, navigation, forms, explanations |
| Evidence/meta | `ui-monospace, "Cascadia Mono", "Segoe UI Mono", Consolas, monospace` | 500–600; 12–14 px; 1.4–1.6 line height | Evidence state, version, date, source, measurement |

### Provenance, license, and availability

| Family/token | Provenance/status | Availability | Redistribution status |
|---|---|---|---|
| CSS `system-ui`, `ui-sans-serif`, `ui-monospace` | Browser/platform generic selections; no single font asset | Platform dependent | No font software included |
| Segoe UI / Segoe UI Mono | Microsoft proprietary system fonts | Common on supported Windows systems; not guaranteed elsewhere | Not redistributed; platform license governs use |
| San Francisco through `-apple-system` | Apple proprietary system font mapping | Apple platforms only | Not redistributed; platform license governs use |
| Arial / Helvetica | Proprietary fallbacks supplied on many platforms | Variable by platform | Not redistributed; platform license governs use |
| Cascadia Mono | Microsoft-origin monospaced family; may be installed separately | Not assumed present | No file included; separate license/availability check required before relying on it |
| Consolas | Microsoft proprietary monospaced fallback | Common on supported Windows systems | Not redistributed; platform license governs use |
| CSS generic `sans-serif` / `monospace` | User-agent selection | Always resolves to an available family | No font software included |

The system does not claim cross-platform metric identity. Later implementation
must test line breaks, controls, zoom, reflow, and language expansion on the
approved browser matrix. Any paid or externally hosted brand font requires a
separate cost, license, privacy/performance, accessibility, and founder gate.

## Typographic rules

- Use sentence case for headings, labels, buttons, and navigation.
- Keep the full entity name and formal service names intact.
- Do not use type below 12 CSS px for meaningful content; 16 CSS px is the body
  default.
- Avoid ultra-light weights, condensed essential text, justified paragraphs,
  decorative ligatures, and all-caps paragraphs.
- Keep line length near 45–75 characters for sustained reading.
- Use tabular numerals only where comparison benefits; provide clear headers and
  units.
- Evidence/meta text is supplemental, never the sole location of a limitation or
  essential instruction.

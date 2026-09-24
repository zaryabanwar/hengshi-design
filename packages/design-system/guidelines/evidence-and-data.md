# Evidence states and data series

Evidence states tell a reader what kind of proof they are looking at; data series are illustrative chart encodings. The two grammars are separate and never share a marker or line pattern. No state or series uses colour alone: each has a shape, a line pattern and a visible label, and all three survive grayscale, forced colours and an unavailable font.

## The six evidence states

| State | Token | Marker | Rail (stroke-dasharray) | Required visible label |
|---|---|---|---|---|
| Verified | `hd-status-verified` | Filled circle | Solid | "Verified" with source and date |
| Hengshi-owned demo | `hd-status-demo` | Open diamond | Dash-dot `10 4 2 4` | "Hengshi-owned capability demonstration" |
| Proposed or requirement | `hd-status-proposed` | Filled square | Short dash `8 6` | "Proposed" or "Requirement" |
| Review needed or conditional | `hd-status-attention` | Filled triangle | Long dash `16 7` | "Review needed" or the exact condition |
| Unavailable or held | `hd-status-held` | Filled bar | Dotted `2 7` | "Unavailable" or "Held" with the next route |
| Error | `hd-status-error` | Open octagon | Two parallel solid rails | Plain-language error and recovery action |

- Markers sit on a 16-unit grid: filled shapes at 12 units, open shapes with a 2-unit stroke (`hd-icon-stroke`). Rails are 3 units on a 48-unit run, square caps, mitre joins.
- On `hd-surface-inverse` swap the state tokens for `hd-signal-lime-on-inverse`, `hd-signal-violet-on-inverse`, `hd-signal-cyan-on-inverse`, `hd-signal-amber-on-inverse` and `hd-text-muted-on-inverse` (held), which the EvidenceStateLabel component does inside `.hd-inverse`.
- "Verified" is an evidence status, not a visual synonym for positive. It appears only when the evidence and publication gates are satisfied.
- Error is an amber boundary around neutral content; the content itself is never tinted.

Markup, using the component in `components/bundle.css`:

```html
<span class="hd-evidence-state hd-evidence-state--verified">
  <svg class="hd-evidence-state__glyph" viewBox="0 0 16 16" aria-hidden="true"><circle cx="8" cy="8" r="6" fill="currentColor"/></svg>
  <svg class="hd-evidence-state__rail" viewBox="0 0 48 16" aria-hidden="true"><path d="M0 8 H48" stroke="currentColor" stroke-width="3"/></svg>
  Verified · producer inspection · 2026-07-20
</span>
```

## The five data series

The single current mapping for illustrative chart series. Each series is named at its line endpoint (direct labels, never a detached legend as the only key), and the same mapping is repeated in semantic text or an exact-value table.

| Series | Token | Marker | Line pattern (stroke-dasharray) |
|---|---|---|---|
| Context baseline | `hd-data-series-context-baseline` | Plus | `1 5 9 5` |
| Dependency map | `hd-data-series-dependency-map` | Ring | `12 3 3 3 3 3` |
| Decision frame | `hd-data-series-decision-frame` | Cross | Solid |
| Evidence depth | `hd-data-series-evidence-depth` | Hexagon | `5 5` |
| Risk view | `hd-data-series-risk-view` | X | `13 4 4 4` |

The former generic circle, triangle, square and diamond series table is superseded because it collided with the evidence grammar; do not use it.

## Chart rules

- Every chart has a title, unit, time period, sample or scope, source, limitations and a plain-language summary. Endpoint labels are at least 12 CSS px; a table gives exact values.
- Zero baselines are not truncated where that distorts comparison. No three-dimensional chart, decorative area fill, animated count-up or unsupported benchmark.
- Proposed targets use dashed outlines and the label "Target". Measured values use solid marks only after source and method are approved. Missing values remain missing and labelled; no visual interpolation without explicit method disclosure. Confidence uses a labelled interval plus pattern, never opacity alone.
- At narrow widths replace a scaled plot with the responsive direct-labelled series list (the DataSeriesKey component) so every name stays at 12 CSS px or larger.
- Axes, grid and labels take `hd-text-secondary` and `hd-border-strong`; series take their `hd-data-series-*` token. The `assets/Specimens` group holds the source's evidence-and-data specimen for comparison.

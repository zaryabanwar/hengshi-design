# DataSeriesKey

The responsive direct-labelled key for the five illustrative data series, each with its marker, line pattern and name. Hand-written from the identity board `.responsive-series-chart` and `docs/phase-1-brand-identity/semantic-tokens.json` (`dataSeries`); the legend half of PRIM-059 Data visualization.

**When to use.** Under or beside any chart that plots the five series, and in place of a scaled plot at narrow widths so every name stays at 12 CSS px or larger. Always alongside an exact-value table.

**Provide.** One `<li>` per series with its modifier (`--context`, `--dependency`, `--decision`, `--evidence`, `--risk`), the key (marker SVG plus the pattern rail), the series name, and the written marker and pattern mapping so grayscale and forced-colours readers get the same information.

**Anatomy.** `.hd-series` list; `.hd-series__key` in the `hd-series-key` monospace style coloured by `hd-data-series-*`; `.hd-series__label` in `hd-text-primary`; `.hd-series__pattern` in `hd-text-secondary`. Markers: plus, ring, cross, hexagon, X; dash arrays `1 5 9 5`, `12 3 3 3 3 3`, solid, `5 5`, `13 4 4 4`.

**Do.** Keep the names exactly as the source writes them; repeat the mapping in the chart accessible description.

**Don't.** Reuse these markers or patterns as evidence states; describe a series as "verified"; drop the pattern text and keep colour only.

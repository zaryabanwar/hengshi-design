# Asset Provenance Record — HSD-ASSET-001

**Asset:** `hengshi-hq-atlanta-exterior-web.glb` (HQ exterior building model)
**Record created:** 2026-09-06
**Purpose:** satisfy the MA-004 evidence requirement — a reviewed asset-manifest
entry showing commercial use, modification, attribution, provenance, and security
status.
**Status:** `resolved` — provenance and rights verified and recorded; both open
founder decisions taken on 2026-09-06 (§6a). MA-004 is closed.

This record is documentation only. It does not authorize 3D implementation,
publication, or any batch of visual production.

## 1. Repository identity

| Field | Value |
|---|---|
| Primary path | `apps/web/public/models/hengshi-hq-atlanta-exterior-web.glb` |
| Build copy | `apps/web/dist/models/hengshi-hq-atlanta-exterior-web.glb` |
| SHA-256 (both, identical) | `4767CAB4D346207A2109FFC1584E256E82AE1CECC110780B99C4406A9586AAFE` |
| File size | 10,002,012 bytes |
| Container | glTF binary (`glTF` magic), glTF version 2.0 |
| Generator string | `Khronos glTF Blender I/O v5.0.21` |
| Embedded `asset.copyright` | **absent** |

Both copies share one hash, so `dist/` is a build output of `public/` rather than a
second asset. One record governs both.

### Geometry inventory

| Field | Value |
|---|---|
| Triangles | 37,302 |
| Vertices | 61,967 |
| Meshes | 13 |
| Materials | 13 |
| Images (embedded textures) | 23 |
| Nodes | 28 |

Counts were read directly from the file's JSON chunk on 2026-09-06 by parsing the
accessor table. No Blender session, import, or modification was performed.

## 2. Verified upstream source

| Field | Value | Evidence |
|---|---|---|
| Source page | `https://sketchfab.com/3d-models/free-atlanta-corperate-office-building-d96380fb001345cca9a9be121f3e43d5` | Founder-supplied, fetched read-only 2026-09-06 |
| Title | `[FREE] Atlanta, Corperate Office Building` | Source page |
| Author | `99.Miles` (username; no separate display name shown) | Source page |
| Published | 2 August 2023 | Source page |
| Categories | Architecture; Places & Travel | Source page |
| Downloads reported | 52,278 | Source page |
| Stated triangles | 37.3k | Source page |
| Stated vertices | 32.8k | Source page |
| License label | **CC Attribution**, linking `creativecommons.org/licenses/by/4.0/` | Source page |
| Download availability | Yes; exact offered formats not stated on the page | Source page |

## 3. Identity corroboration

The repository file was matched to the upstream listing without downloading the
source, using the only two figures the page publishes:

| Measure | Upstream page | Repository file | Result |
|---|---|---|---|
| Triangles | 37.3k | 37,302 | **match** |
| Vertices | 32.8k | 61,967 | expected divergence, see below |

The vertex divergence is **not** a mismatch. glTF export duplicates a vertex at every
normal, UV, or material seam, so an exported vertex count routinely exceeds the
modelling-tool count while the triangle count is preserved exactly. Triangles are
therefore the load-bearing identity signal, and they agree to the page's stated
precision.

**Conclusion:** the repository asset is a glTF export of the named Sketchfab model.
The founder independently confirmed this is the same asset on 2026-09-06.

## 4. Rights determination

License verified against the canonical deed at `creativecommons.org/licenses/by/4.0/`
on 2026-09-06.

| Right | Determination | Basis |
|---|---|---|
| Commercial use | **Permitted** | "for any purpose, even commercially" |
| Modification / derivative works | **Permitted** | remix, transform, and build upon the material |
| Redistribution | **Permitted** | copy and redistribute in any medium or format |
| Attribution | **Required** | see §5 |
| Additional restrictions by us | **Not permitted** | "No additional restrictions" term |
| Warranty from licensor | **None given** | deed disclaims warranties |
| Licensor endorsement | **Must not be implied** | attribution "not in any way that suggests the licensor endorses you" |

Short name and version: **CC BY 4.0**.

The Creative Commons deed states it "is not a license and has no legal value"; the
legal code is the operative document. This record is an engineering determination,
not legal advice, and the founder retains the legal decision.

## 5. Attribution obligation

CC BY 4.0 requires the licensee to "give appropriate credit, provide a link to the
license, and indicate if changes were made," in any reasonable manner that does not
suggest endorsement. Appropriate credit means supplying, where available, the
creator's name, any copyright and license notices, a disclaimer notice, and a link to
the material. Version 4.0 additionally requires flagging our own modifications and
retaining any indication of earlier ones.

Three obligations attach to this asset. Their placement was decided by the founder on
2026-09-06; see §6a for the decision and the exact text.

| ID | Obligation | Current state |
|---|---|---|
| ATTR-01 | Public-facing credit naming `99.Miles`, linking the source page and the CC BY 4.0 deed | **Decided, not built** — footer "Asset Credits" link to `/credits` |
| ATTR-02 | Statement that the asset was modified | **Decided** — "modified for Hengshi Design" is carried in the §6a text |
| ATTR-03 | Embedded `asset.copyright` in the glTF, or an equivalent in-repository notice | **Open** — the field is absent, and writing it is an asset modification deferred to authorized 3D production |

ATTR-01 carried a consequence the accepted route inventory does not cover: D-025
accepted 33 canonical routes and none is an attribution or credits surface. `/credits`
is therefore a 34th route requiring reconciliation, assigned to the CR-002 revision
window in §6a rather than to a separate change request.

## 6. Modification status

The generator string is `Khronos glTF Blender I/O v5.0.21`, so the repository file is
already a Blender re-export rather than an untouched upstream download. The asset is
consequently a **derivative work** as of today, before any planned surroundings work.

The exact pre-existing modifications are unknown: the file carries no change history,
and the original download was never recorded. Under ATTR-02 the safe and compliant
statement is that the model has been modified, without asserting an unverified
specific delta.

All planned surroundings work — ground plane, context massing, sky, lighting, camera
staging — will extend this derivative and must be recorded as further modification.

## 6a. Founder decisions — 2026-09-06

Both open questions were decided by the founder on 2026-09-06. This section records
the decisions; §7 is retained as the reasoning that produced them.

### D-A — NoAI disposition: narrow reading adopted

The founder directed: *"we are not feeding the model into any ai. you will just be
working on it and expanding it, we can maybe even contribute to the model later, so
you are just the tool user i am the one telling you what to do."*

This selects **option 1** of §7. The operative distinction is that the asset is not
supplied to a generative system as training data or as generative input; it is edited
with Blender, a deterministic tool, under human direction. Authorship and direction
remain with the founder.

Binding operating rule that follows from this decision:

| Rule | Statement |
|---|---|
| AR-01 | The mesh, its textures, and its geometry must never be submitted to a model as training data, fine-tuning data, or generative input. |
| AR-02 | Permitted work is deterministic Blender operations — placement, staging, lighting, surroundings modelling, export — authored as scripts or direct edits under founder direction. |
| AR-03 | No generative-3D or image-model step may produce or derive geometry or textures from this asset. |
| AR-04 | If a future step would breach AR-01 or AR-03, stop and return to the founder rather than reinterpreting this decision. |

AR-01 through AR-04 are the reason the narrow reading holds in practice rather than
only on paper: the workflow is constrained so the prohibited use cannot occur
incidentally.

### D-B — Attribution surface: `/credits`

The founder directed a subtle but accessible footer link named **"Asset Credits"**
leading to a durable credits page, with the full attribution there, explicitly not
requiring prominent homepage placement, and required to remain reasonably
discoverable and legible.

**Selected route: `/credits`.** The founder offered `/credits` or
`/legal/asset-credits`. The accepted D-025 inventory contains no `/legal/*` family —
the nearest surface is `/trust` — so `/legal/asset-credits` would introduce an
otherwise empty parent segment for a single leaf. `/credits` is one flat addition and
is more directly discoverable. The founder may override this selection.

**Exact attribution text to render:**

> "Atlanta Corporate Office Building" by 99.Miles, licensed under CC BY 4.0,
> modified for Hengshi Design.
> Source: https://sketchfab.com/3d-models/free-atlanta-corperate-office-building-d96380fb001345cca9a9be121f3e43d5
> License: https://creativecommons.org/licenses/by/4.0/

This text satisfies all three CC BY 4.0 components in one block: creator credit, a
link to the licence, and an explicit statement that changes were made.

### Obligation status after these decisions

| ID | Obligation | Status |
|---|---|---|
| ATTR-01 | Public-facing credit | **Resolved in principle** — `/credits` plus a footer "Asset Credits" link; not yet built |
| ATTR-02 | Modification statement | **Resolved** — "modified for Hengshi Design" is in the exact text |
| ATTR-03 | Embedded/in-repository notice | **Open** — the GLB `asset.copyright` field is still absent and must be written |

### Consequential reconciliation this creates

`/credits` is a **34th route**. D-025 accepted 33, and the route inventory is carried
in `foundation-route-coverage.csv` inside the frozen D-037 package. This addition is
founder-directed and therefore authorized, but it is **not yet reconciled** into:

- the D-025 canonical route inventory and SEO route plan;
- `docs/phase-1-ux-architecture/` wayfinding and journey records;
- `foundation-route-coverage.csv` and `traceability.csv` in the D-037 package;
- the footer component in the accepted primitive set, which must gain the link.

To avoid a third concurrent change request for a single route, this reconciliation is
assigned to the **CR-002 revision window**, which already reopens route coverage for
the four-stream model. It is recorded here so it cannot be lost: `/credits` must
appear in every stream, including the no-WebGL semantic stream, because the licence
obligation does not vary by delivery tier.

ATTR-03 requires writing `asset.copyright` into the GLB. That is an asset
modification and is therefore **out of scope until 3D production is authorized**; the
frozen file is untouched today.

## 7. Reasoning of record — the NoAI notice

The source page carries a notice separate from the license:

> "NoAI: This model may not be used in datasets for, in the development of, or as
> inputs to generative AI programs."

This matters because the approved delivery method for the surroundings is Blender
driven by an AI coding agent. Two readings are defensible and the difference is
material:

- **Narrow reading.** The notice targets training data and generative pipelines that
  consume the model to synthesise new assets. Scripted, deterministic Blender
  operations that place, light, and stage an existing mesh are tool-assisted editing,
  not generative input. Under this reading our use is permitted.
- **Broad reading.** Any workflow in which an AI agent processes the asset is
  "input to a generative AI program," which would prohibit the planned method.

There is a further unresolved tension: CC BY 4.0's "No additional restrictions" term
bars a licensor from applying legal terms that restrict what the license permits, so
it is genuinely unclear whether the NoAI notice is an enforceable licence condition,
a platform-level machine-readable opt-out signal, or a statement of preference.

**Decided on 2026-09-06 — see §6a.** The founder adopted the narrow reading. The
three dispositions that were available were:

1. Adopt the narrow reading, proceed, and record the reasoning.
2. Avoid the question entirely: keep the asset human-edited only, and have the agent
   author Blender scripts for the surroundings without the agent ingesting the
   building mesh.
3. Replace the asset with one carrying no NoAI notice.

## 8. Security status

| Check | Result |
|---|---|
| Container parses as valid glTF 2.0 | Pass |
| External URI references | None; textures are embedded |
| Executable or script payload | None; glTF carries no code |
| Read method | JSON-chunk parse only; never imported or executed |

No scene import or execution was performed, so no runtime behaviour has been
observed. Any later Blender import is a separate bounded step.

## 9. What this record does and does not establish

**Established:** the upstream source, author, exact licence and version, commercial
and modification rights, geometry inventory, cryptographic identity, derivative
status, and security posture.

**Not established:** the legal effect of the NoAI notice; the attribution surface's
placement in the UI; the licence status of any future surroundings asset; whether the
model's real-world building depiction raises separate trademark, property-release, or
publicity considerations, which CC BY 4.0 explicitly does not grant.

## 10. Gate linkage

- **MA-004** — **closed 2026-09-06.** The provenance, licence, attribution,
  modification, and security evidence it required is supplied, and both founder
  decisions are recorded in §6a. Geometry reuse is authorized subject to AR-01
  through AR-04 and the outstanding ATTR-03 embedded notice.
- **CR-002** — the four-tier delivery streams depend on this asset. Its revision
  window also carries the `/credits` route reconciliation recorded in §6a. The
  attribution obligation applies to every stream, including the no-WebGL stream.
- **MA-025** — unaffected. No batch of Figma production depends on this record.

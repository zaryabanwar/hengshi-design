# CR-002 signal-portability verification — U-01, U-02, U-03

**Verification date:** 2026-09-06
**Authority:** `CHANGE_REQUEST_CR-002.md` §7; risk **R-030**; D-039
**Method:** MDN Web Docs Baseline availability banners, read directly from each
feature's primary page. Baseline is the cross-vendor interoperability signal
maintained by the W3C WebDX Community Group.
**Status:** U-01 resolved, U-02 resolved with a split result, U-03 **not resolvable
by documentation and still open**.

> **Scope limit, stated up front.** MDN renders its per-version browser-compat
> tables dynamically and they did not render in these retrievals. What was obtained
> is the **Baseline tier banner** on each page, quoted verbatim below, plus the
> specification venue. Exact minimum version numbers per browser were **not**
> obtained and are **not asserted**. The Baseline tier is sufficient to decide
> portability, which is the only question §7 asked; it is not sufficient to write a
> version matrix, and none is written here.

---

## 1. Result summary

| ID | Question | Result |
|---|---|---|
| **U-01** | Are connection signals portable? | **NO.** Resolved unfavourably. |
| **U-02** | Are device-capability signals portable? | **SPLIT.** Memory: no. Processor count: yes. |
| **U-03** | What are the tier thresholds? | **OPEN.** Not answerable from documentation. |

**The four-stream model survives. The stream-selection rule as written does not.**

---

## 2. U-01 — Connection signals are not portable

### Network Information API (`navigator.connection`, `effectiveType`, `saveData`)

> **Limited availability** — "This feature is not Baseline because it does not work
> in some of the most widely-used browsers."

Specification venue: `wicg.github.io/netinfo/` — a **WICG incubation draft**, not a
W3C Recommendation-track or WHATWG living standard.

### `prefers-reduced-data` (the CSS alternative)

> **Limited availability** — same Baseline wording, **plus** an Experimental banner
> and an explicit warning: *"This feature is not supported by any user agent and its
> specifics are subject to change."*

### Finding

Both the scripted and the declarative route to a user's network condition are
outside Baseline. There is **no portable way to read a declared network class in the
browser.** U-01 is resolved exactly as §7 feared.

---

## 3. U-02 — Device-capability signals split cleanly

### `navigator.deviceMemory` — NOT portable

> **Limited availability** — "This feature is not Baseline because it does not work
> in some of the most widely-used browsers."

Specification venue: a W3C `/TR/` Device Memory document, without multi-vendor
implementation. The value is additionally **coarsened to a power of two and clamped
to implementation-defined bounds** as an anti-fingerprinting measure, so even where
it exists it is a bucket, not a measurement. The page also notes the bounds "may
change over time", so a hard-coded maximum would be a defect.

### `navigator.hardwareConcurrency` — PORTABLE

> **Baseline — Widely available.** "This feature is well established and works
> across many devices and browser versions. It's been available across browsers
> since **March 2022**."

Specification venue: the **WHATWG HTML Standard**, Workers chapter. Fully
standardized, non-experimental.

One caveat carried from the primary source: the browser may deliberately report a
lower number than the machine has, and MDN says *"don't treat this as an absolute
measurement of the number of cores."* It is a tier hint, which is all the stream
rule needs.

### `prefers-reduced-motion` — PORTABLE

> **Baseline — Widely available.** "It's been available across browsers since
> **January 2020**."

This matters more than it looks: CR-002's accessibility-preference precedence
depends on it, and it is the **oldest and most solidly supported** signal in the
whole selection rule. The accessibility half of the model rests on firm ground.

### Finding

Capability-based tiering is achievable. Memory-based tiering is not. U-02 is
resolved in favour of the model, using different inputs than assumed.

---

## 4. U-03 — Remains open, and correctly so

No documentation can supply the thresholds that separate high from medium from low.
They require measurement of the real asset on real hardware. U-03 stays
`[MUST VERIFY AT SPECIFICATION]` and is now explicitly reclassified as
**implementation-phase evidence**, not a documentation gap. It cannot close in
Phase 1.

---

## 5. Consequence for the approved selection rule

CR-002 §7 anticipated this outcome and pre-authorized the substitution:

> "...would make connection-based selection unavailable for a meaningful share of
> visitors and force a different strategy — **measured load performance rather than
> declared network class**."

That substitution is now required rather than hypothetical. The founder's stated
intent — streams selected "on the basis of device and connection" — remains
satisfiable, but the two halves are satisfied by different means:

| Half of the rule | Assumed mechanism | Verified mechanism |
|---|---|---|
| Device | `deviceMemory` + processor count | **`hardwareConcurrency`** plus a **WebGL context probe**; no memory input |
| Connection | `effectiveType` / `saveData` | **Measured runtime performance**, since no declared class is portable |
| Accessibility precedence | `prefers-reduced-motion` | Unchanged — confirmed Baseline since 2020 |

### Does this trigger the R-030 stop?

**No, and the distinction is worth being exact about.** R-030 halts and returns
Option B to the founder if *portable stream selection proves unachievable*. It has
not. Selection is achievable — one of its two inputs must change mechanism, and
CR-002 §7 named that exact replacement in advance as the fallback design. Adopting
it is inside the approved change, not beyond it.

What would trigger the stop is a later finding that measured-performance selection
is itself unworkable. That is not established either way and is **not asserted**.

### The fallback principle now binds harder

CR-002 §7 requires that when a signal is missing, the rule selects "the stream most
likely to succeed, not the most impressive one." With connection class unavailable
in Firefox and Safari, the missing-signal path is no longer an edge case — it is
the **default path for a large share of real visitors**. The conservative default
must therefore be the designed-for case, not an exception handler.

---

## 6. What this changes, and what it does not

**Changes:** CR-002's stream-selection rule must be specified against
`hardwareConcurrency`, a WebGL capability probe, measured performance, and
`prefers-reduced-motion` — not against `effectiveType`, `saveData`, or
`deviceMemory`. Any target text implying a declared network class needs amendment
in the CR-002 revision window.

**Does not change:** the four peer streams, equivalent core journeys, the user
override, accessibility-preference precedence, B07's reclassification to core, or
B07's continued deferral to MA-026. D-039 stands.

**Still forbidden:** no schedule estimate, because U-03 is open and unmeasurable in
Phase 1. No implementation — application and 3D work remain blocked until complete
Phase 1 approval.

## 7. Evidence not obtained

Recorded so it is not mistaken for verified:

- **Per-browser minimum versions.** BCD tables did not render; only Baseline tiers
  were read.
- **Vendor standards positions.** A retrieval of Mozilla's standards-positions data
  returned HTTP 404 for the path attempted, and the rendered index requires
  JavaScript. Mozilla's and WebKit's formal positions on the Network Information and
  Device Memory APIs are therefore **not sourced here** and no rationale is
  attributed to either vendor.
- **Whether measured-performance selection is workable.** Untested. It is the
  proposed replacement mechanism, not a verified one.

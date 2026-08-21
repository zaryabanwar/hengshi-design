# LibreOffice DOCX-to-PDF Capability Evidence

**Date:** 2026-07-19
**Purpose:** Close R-019 only after a real control conversion, target conversion,
complete page rendering, visual inspection, and independent review.

## Verified capability

- Installed product: LibreOffice 26.2.4.2 (X86_64).
- CLI version command exited successfully.
- A generated one-page control DOCX converted to a structurally valid one-page
  PDF and rendered to a readable PNG.
- The historical 24-page project consolidation converted to a structurally valid
  24-page PDF.
- Exactly 24 sequential page PNGs rendered at 850 x 1100; all were non-empty and
  visually inspected. Higher-resolution checks were also inspected for pages 1,
  12, and 24.
- Poppler opened both PDFs without a suspect-file warning. Their embedded producer
  identifies LibreOffice 26.2.4.2.

## Evidence identity

| Artifact | Bytes | SHA-256 |
|---|---:|---|
| Generated control DOCX | 5,082 | `9888A09CDE2076617FABAA51AE484DA357D45175CE44B887BDD7AF3AF127E699` |
| Generated control PDF | 24,395 | `14C9DAEA5E09C251B82FD3E7F95E67E0D7A65374168B384841872090C8D11442` |
| Historical consolidation DOCX | 29,131 | `D95FBF5FABBEA68F454BCE66686580C92CA914F57BFA4430B245E4483CACC293` |
| Generated historical consolidation PDF | 435,870 | `83B34E3890A0BB9ADA7F1D829BB90278FE343EA2F1DCAF94F8EE1F4F7CD43911` |

Generated binaries and page renders remain in ignored
`test-results/libreoffice-26.2.4-verify/`; this record retains their reproducible
identity and review result without adding generated binaries to project authority.

## Independent review

The independent `hengshi-qa-engineer` review returned **PASS**. It verified the
installed version, DOCX/PDF structure, producer metadata, page counts, hashes,
render sequence and dimensions, and all 24 page images.

The reviewer confirmed that page 2's blank table of contents exists in the source
DOCX structure and that the sparse continuation pages follow explicit source page
breaks. These are historical source-layout limitations, not converter crashes,
missing output, corrupt rendering, or approval of the old document's content.

## Closure and residual control

R-019 is closed as a repaired local-converter incident. Every future material DOCX
visual-QA gate must still perform a fresh harmless control conversion and inspect
the complete rendered target document. This evidence does not make the February
2026 consolidation current product authority and does not approve its layout or
claims.

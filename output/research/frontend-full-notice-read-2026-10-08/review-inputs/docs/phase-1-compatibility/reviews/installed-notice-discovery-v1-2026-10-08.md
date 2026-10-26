# Installed notice discovery — bounded independent review

Status: DOING. Reviewed 2026-10-08 by `/root/review_notice_discovery_current`;
receipt preserved by the producer. No commit or complete compatibility acceptance.

Verdict: **PASS — bounded discovery evidence accuracy.** No consequential
discrepancy in the recorded identities, associations, enumeration or term matches.

## Exact scope and reproduction

The [eight-input manifest](../../../output/research/frontend-notice-discovery-2026-10-08/review-inputs.json)
SHA256 is `4dc5d04d30d6a6c7e2b5139a217606e3c0082bea295e7da2f763c9e9f0620d6b`.
The reviewer independently reproduced its eight snapshots and eight live sources,
bytes/hashes initially and finally, the candidate lock identity, and all eleven
prior-inventory / installed-metadata / lock associations. All 394 own-file
identities, exclusions and saved term-hit records matched; final rereads of those
files, inputs, manifest and lock remained identical. The raw observation timestamp
is UTC; PowerShell's parsed display converted it to local time.

Counts: 394 own files; 356 eligible text files; 129 hit files across eleven
packages; 281 retained match excerpts. There are 38 extension exclusions and
126 eligible files larger than the 8,192-byte inspected prefix, including 69 hit
files. One nested `stats-gl/node_modules` subtree was pruned; no symlinks or
junctions were found. These are discovery counts, not recovered-notice counts.

## Limits retained from independent review

- `probe_notices.py:45` caps each file at twelve matching lines. MediaPipe's
  `vision.d.ts` has 32 matching prefix lines; twenty were omitted from saved
  excerpts. Neither a complete match list nor complete notice is recorded.
- `probe_notices.py:38` calls excluded extensions “non-text content not
  interpreted”. Thirty-one excluded `.map` files are valid JSON text. Describe
  the 38 as outside-whitelist files, never as 38 binary files.
- `maath` and the Rolldown binding match only metadata. Natural Compare's README
  links to licence text; GSAP headers point to external terms; Fiber's embedded
  React headers refer to an absent root licence. Declaration-only matches, links
  and copyright headers need separate interpretation. Eleven matching packages
  do not establish eleven recovered applicable notices.
- The whitelist, prefix boundary, twelve-line cap and 240-character excerpts
  omit potentially relevant content and nonmatching clauses. No hit establishes
  complete attribution obligations.

No producer execution, installation, download or writes occurred during review.
No archive authenticity, provenance, legal/safety clearance, deployed-artifact
coverage, complete graph acceptance or adoption follows. Phase 1, deferred Git
operations and D-077's temporary evaluated renderer boundary remain intact.

The [earlier supply-chain receipt](frontend-supply-chain-v1-2026-10-06.md)
retains its exact dated scope; this discovery extends the evidence only.

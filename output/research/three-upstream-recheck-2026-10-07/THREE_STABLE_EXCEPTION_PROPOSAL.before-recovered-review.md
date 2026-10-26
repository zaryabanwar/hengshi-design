# Three renderer compatibility exception proposal — v1

Status: DOING. Proposed 2026-10-07; no founder selection or application change.

## Decision requested

Recommend permitting root `three 0.184.0` with `@types/three 0.184.1` as the
temporary renderer candidate in the eventual complete compatible stable graph.
Keep React/Fiber and the other accepted technology families. This is a narrowly
dated D-069 exception, not acceptance of the existing candidate lock or whole stack.

## Evidence and cause

The [failed strict candidate](reviews/frontend-candidate-declaration-gate-v1-2026-10-06.md)
uses Three 0.186.1, types 0.186.0, Drei 10.7.9 and three-stdlib 2.36.1.
With `skipLibCheck=false`, two public loader declarations produce TS2430/TS2416.
The [matched candidate review](reviews/frontend-three-remedy-evaluation-v1-2026-10-06.md)
verifies finite checker, build and browser evidence with the proposed 184 pair.
Prior 185 declaration comparisons also fail; peer ranges alone do not settle this.

The [7 October official-registry observations](../../output/research/three-upstream-recheck-2026-10-07/observations.json)
show no newer stable release of those five evaluated renderer/helper packages.
The 184 pair are the newest published stable patches in their respective 184 lines.
[Upstream PR 433](https://github.com/pmndrs/three-stdlib/pull/433) merged the
declaration correction on 26 June, but the current npm package predates it.
The [integrity-verified published-file comparison](../../output/research/three-upstream-recheck-2026-10-07/source-comparison.json)
matches both files to the previously failing installation and shows their
differences from the exact merge commit. A closed issue is not a released fix.
No merge-commit build, Git dependency, declaration patch or check suppression is proposed.

## Conditions before adoption

- Founder approval applies only to this exception; full graph/MA-013 acceptance,
  latest-compatible re-resolution, reproducible locks and independent review remain.
- Repeat the strict public-loader and actual coupled fixture checks immediately
  before the separately approved modernization wave. Retain a failing-input control.
- Complete required supply-chain, licence, advisory and deployment-exclusion
  evidence. D-072 remains lint-only and expires separately on 2027-01-05.
- The candidate's nested stats-gl Three 0.170.0 is a separate graph node; this
  exception does not approve sharing objects across renderer copies or erase it.
- Retain the prior protected prototype and exact candidate manifests/locks;
  no application upgrade, model replacement, migration or deployment follows here.

## Recheck and rollback

If accepted, recheck no later than 2027-01-07 and before any modernization/adoption;
also recheck when a stable three-stdlib/Drei release advertises the relevant fix.
Re-evaluate the whole coupled set rather than replacing a single package blindly.
At that date, continuing the exception requires a fresh founder decision.
Rollback of a later authorized wave restores its reviewed previous source/lock
and generated assets together, under that wave's rollback plan; never mutate an
eligible published release in place. The current application needs no rollback
because it has not changed. Existing Clock warnings and finite-device/test limits
remain open; this proposal establishes neither performance nor production readiness.


Independent review attempt, 2026-10-07: the required reviewer terminated with
"Your workspace is out of credits. Add credits to continue." No review verdict
was returned. The frozen proposal/evidence remains unreviewed; producer checks
do not replace independent review or authorize founder selection/adoption.

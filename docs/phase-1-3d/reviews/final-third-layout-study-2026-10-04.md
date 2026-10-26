# Final third campus layout study review — v1

Date: 2026-10-04. Independent bounded review. Disposition: **PASS for the isolated study's documented observations and limits**. No layout, appearance, safety or production acceptance.

## Scope and authority

Reviewed the new layout generator, inspection script, editable master, GLB, source/geometry records, viewer, three Blender renders, four retained browser screenshots, producer Playwright inspection source, selected concept, and the final-third subsection of `SPATIAL_STORYBOARD.md:162–192`. The World and feature definitions supply requirements and scope limits; this receipt does not approve those full definitions.

AGENTS.md and constitution require independent inspection and preserve the original application/Atlanta asset. The earlier accounting review and its verified reference correction remain intact: initial creation consumed no cycle; stopped refinement was conservatively cycle 1; composition rebuild was cycle 2; this isolated study consumes the final third cycle. No further substantial geometry revision is authorized without the applicable founder exception. Pipeline corrections before this first independent review are not inferred to be separate hidden reviewed cycles.

The later browser board `spatial-storyboard.html`, its additional board screenshots and the subsequently updated checkpoint are excluded from this receipt. Their reference integration needs its own bounded inspection. Whole-file hashes below bind source identities without extending this verdict to unrelated sections, phases or contracts.

## Findings and disposition

No actionable contradiction was found between this study's retained evidence and its stated bounded claims. The README and spatial subsection accurately describe the finite diagnostic, simple materials, over-budget whole export, absent runtime features and lack of appearance acceptance. This is a reviewable private layout study, not a completed feature.

The following remain real obligations before any production acceptance; this PASS does not discharge them:

- **Appearance/layout:** the concept's richly layered planting, mountain silhouettes, realistic timber/earthen materials, room furnishing and landscape composition are not closely reproduced. Founder visual disposition is still required.
- **Traversability:** finite render-mesh rays do not establish authored body collision, continuous/full-width ground, rail or structural safety, slope/accessibility clearance, arrivals or all interior routes. Separate connected collision and threshold/closed-room behavior remain required.
- **Transfer/performance:** the 20,860,132-byte single GLB is over the accepted initial 8 MB desktop / 4 MB mobile caps, regardless of the MB/MiB interpretation. No production chunk/LOD/transfer manifest, decoded-memory or named-device performance proof exists.
- **Runtime/product:** free movement, Stop/cancellation, spatial streaming, sound, eligible published service information, actual staff presence, assistance/booking and equivalent semantic product journeys are not implemented by this viewer.
- **Rights/compatibility:** original procedural source supports the stated absence of imported scenery/Atlanta mesh inputs; it does not clear all production rights/provenance or select a compatible Blender/exporter/browser/runtime matrix.

These are explicit remaining gates, not hidden failures reclassified as feature completion or requests for another unapproved model correction.

## Independently verified evidence

### Exact geometry and source correspondence

The raw GLB header declares glTF binary format version 2 and length 20,860,132, matching its actual bytes. Its JSON contains 117 meshes and 117 mesh-bearing nodes, 16 materials, zero images, zero textures and zero animations. Material extensions are `KHR_materials_transmission` and `KHR_materials_ior`. This technical format version is not a product-release number.

The layout-observation source SHA256 equals the current `build_layout.py` bytes. The geometry-inspection GLB SHA256 equals the exported bytes and the spatial subsection's listed identity. Source `mesh_groups:112` is not a conflicting exported count: the generator's 112 grouped meshes are accompanied by five text objects converted into mesh nodes on export; the imported inventory names and raw node count agree.

I inspected the builder without executing model generation. It authors reception and the five canonical service-wing volumes, varied two/three-lobed roofs, promenade geometry, piers/rails, branching reception supports, procedural terrain/plants and one representative Strategy information/consultation fixture. The source saves the separate master and export at lines 278–279 and only then changes cameras for the three renders. The browser camera positions apply the Blender-to-glTF axis conversion to the same export. No wing is represented as a live operational department, and the Strategy fixture does not change the accepted AI + Data first-wing sequence.

### Actual independent read-only diagnostic

Used the existing Blender 5.0.1 executable with `--background --factory-startup --python-expr`. The Python expression loaded `inspect_layout.py` as text, set its original `__file__`, and replaced only its exact output-writing line:

```python
(root/'geometry-inspection.json').write_text(json.dumps(result,indent=2),encoding='utf8')
```

with a stdout print of the same `result` object. No source, model, render or producer observation file was changed. This preserved the producer's diagnostic output while executing its import and BVH calculation on the actual GLB. Exit was 0. The entire resulting object, including all 117 inventory entries and all route results, equals the retained `geometry-inspection.json` object. This corroborates the method's reproducibility; it is not an independent safety oracle.

Imported world-space coordinates are finite for every recorded mesh. The inventory totals 569,809 vertices and 726,056 triangles. Factory-startup objects are excluded from the imported inventory, avoiding a default-cube count. The method uses 81 centreline points plus offsets -1.35, 0 and +1.35 per route, vertical floor/terrain/water rays and centreline segments at proposed floor + 1.4.

| Connector | Floor samples | Missing named floor | Tested obstacle segment hits | Terrain above sampled floor | Water-under samples |
|---|---:|---:|---:|---:|---:|
| Strategy & Transformation | 243 | 0 | 0 | 0 | 0 |
| Digital Products & Growth | 243 | 0 | 0 | 0 | 0 |
| AI, Data & Automation | 243 | 0 | 0 | 0 | 0 |
| Immersive & Creative | 243 | 0 | 0 | 0 | 44 |
| Cloud, Reliability & Trust | 243 | 0 | 0 | 0 | 51 |

The obstacle filter covers the named glazing/frame/reception branching-column/welcome-desk meshes, not every object or a swept body. Lateral floor samples are within the proposed 3.2-unit promenade width; they do not prove every point across that width. Water-under counts describe sampled plan locations, not dangerous intersections or certified bridge support. Visible piers/rails and the viewer's “supported crossings” wording describe authored visual supports, not a tested engineering conclusion. No collision controller or approved real-world architectural units follows from these results.

### Visual inspection

Viewed the selected three-panel concept and all three same-model Blender renders plus the four browser screenshots. The study retains a central reception, surrounding wings, roof openings, connecting paths, river crossings, vegetation and landscape depth. It replaces the prior mountain-wall arrangement with continuous terrain and forest. Its roofs share a repeated procedural language; the simplified crowns, flat PBR colours, sparse room furnishing and distant scenery clearly differ from the concept.

The arrival and department renders show the same roof/entrance/board/furniture relationships that appear in their browser cameras. Different framing and lighting do not imply different models. The department board visibly states “Prototype - no live staff”; no people or simulated availability are present. The browser's 390-pixel department view crops spatial lettering, so the retained mobile screenshot is not readable-content parity or accessibility proof. Appearance acceptance is honestly held.

### Actual independent viewer behavior

Used the already-installed Playwright CLI under the Playwright skill and created separate browser contexts; no installation, app sign-in, producer screenshot overwrite or application feature run occurred. Independently observed:

- One GLB loaded with `meshCount:117`, `revisionCycle:3` and the three expected cameras.
- Overview, Arrival and Department buttons each selected their `aria-pressed` state and corresponding visible note.
- At 390 × 844, no document horizontal overflow; focused Department activated with Enter.
- A separate no-JavaScript context loaded all three render alternatives.
- No page errors or console errors were observed during these checks.

The retained desktop screenshots use 1440 × 960. I inspected the retained producer script's scenario and screenshots and reproduced its bounded camera/mobile/no-script behavior without writing new images. These are dated viewer observations, not continuing health, physical-phone performance, general WCAG certification, WebGL failure-recovery coverage or production journey tests.

## Protected inputs and integrity

The earlier composition source, master and GLB match the commissioned protected identities. The original three World sources and five application dependency files match the earlier independently reviewed baselines. The Atlanta GLB's current bytes also match its HEAD blob and recorded SHA256 `4767CAB4D346207A2109FFC1584E256E82AE1CECC110780B99C4406A9586AAFE`. The application diff lists only the pre-existing API README change; this receipt makes no global claim about unrelated worktree changes.

No authoring/model change, installation, dependency upgrade, migration, credential/provider operation, commit or canonical status change was performed. Source/render/hash checks establish artifact identity and bounded observation, not correctness of unimplemented features. The original accounting receipt remains unchanged.

## Exact inspected input identities

SHA256 is over exact file bytes. Paths are repository-relative.

| Input | Bytes | SHA256 |
|---|---:|---|
| `AGENTS.md` | 7686 | `55405CB02A96D05F7F6D68E56A588D743F83877FB2691A5A9F2C736126ADBCC5` |
| `.specify/memory/constitution.md` | 16234 | `33EC0BB02B0D0D9A55D0971589BD19F7242F5D56DA130F8F496BC1D31A8B5D23` |
| `DECISIONS.md` | 70865 | `C843AE17EE0AA7B9E5DD0BE39595310B5B25C31BEA2B97ECE4E6EBD34C2DADBF` |
| `docs/phase-1-3d/SPATIAL_STORYBOARD.md` | 19237 | `4BA32224DFB5D8E793CB6AF7CFE0F761250050F8B6DD91EC26B37766B38C9308` |
| `docs/phase-1-3d/WORLD_EXPERIENCE.md` | 17201 | `08070FFF75BB8566B1A863279A42FC23ADE83669A80646E00772D1D0E5D4918A` |
| `specs/003-3d-experience-completion/spec.md` | 25605 | `2ACEEFA18E51BD11A450D79B2C75D0A2F3A0783BAAC785DE12E56956FA03D4F9` |
| `docs/phase-1-foundation/01-product-requirements.md` | 66587 | `5B33D8BD87BDB3B093EF319DB3EA3BB64DEAEDDF2706F5D21505BFB66035AA39` |
| `docs/phase-1-3d/reviews/model-revision-accounting-2026-10-04.md` | 8343 | `B9A89D3E6C6D271AD3B3D76318353956B5E01B204BB611F10D39F043E652B715` |
| `docs/phase-1-3d/concepts/nature-campus-direction-2026-10-04.png` | 3338624 | `E514E603EB211250459C02763D06F35A4D03F606CD017C318F40FD11E4DAAC79` |
| `artifacts/nature-campus-layout-study/build_layout.py` | 14943 | `D127A6429B7B32E6954BCD51E2C2BEAF4A5560BDC29EFCABD00CE264C6A984C6` |
| `artifacts/nature-campus-layout-study/inspect_layout.py` | 3837 | `C5AB00255296E1216C803A699EB2D99EDB05671CEF05B0CFE550983EE4B901E9` |
| `artifacts/nature-campus-layout-study/README.md` | 4033 | `7150FCA4AEBB517396ABBFCE28DDB9CCE1D6AB005923F4A8F151792C854787B2` |
| `artifacts/nature-campus-layout-study/index.html` | 6688 | `4FBB70E6C39FA3689C4B72E6F3DAD43ACBDD0DC0BB5AFE96F03DE58F2F5A8738` |
| `artifacts/nature-campus-layout-study/layout-observations.json` | 45292 | `3209364B282F987BDCB5FD089E4A256D524AE69031BBA869AAEF974CFF3311FF` |
| `artifacts/nature-campus-layout-study/geometry-inspection.json` | 17813 | `D7E445F64455FEA8F69AEBC88726040BB6EE6B0072A218105B919A799314C49A` |
| `artifacts/nature-campus-layout-study/nature-campus-layout.glb` | 20860132 | `E2161710DC0576EC62E3D096C60E32927E827AA59198A33361E729EC8A7B43C0` |
| `artifacts/nature-campus-layout-study/nature-campus-layout.blend` | 8732595 | `C377B877779DF01211C2312AFDE3D0F0769E2874E3409B2A1BAA6BEED1CEB4B8` |
| `artifacts/nature-campus-layout-study/overview.png` | 1435752 | `1D60F0823A840A1783220BA8179C99FD23CA81CC5124D9A637F5BA1E59D10493` |
| `artifacts/nature-campus-layout-study/arrival.png` | 1179430 | `406F233B1E18559AB3BA99649CE16C19D6E68D4D7682550E221649096EAE51E8` |
| `artifacts/nature-campus-layout-study/department.png` | 1029284 | `BF0F24F051CC98632A81AB7E8A88D100C804D93CB9BF4CA2BBBCC290C1B59D13` |
| `output/playwright/inspect-layout-study.cjs` | 2382 | `41D7E6DEE49C8FAB378C0849C40702F61617E7FB8F4BA94BB1268290C2ADF935` |
| `output/playwright/layout-study-overview-2026-10-04.png` | 1234461 | `B83AB8CEB2C7A94A25F53BE79F703EFCAE9E77DE8B9EA9327006FEF0827E4A8E` |
| `output/playwright/layout-study-arrival-2026-10-04.png` | 519103 | `64E1710AF389CB0AEE53AFF5F3EE118F4C518022B02F47328BB3C44C2C6DB41B` |
| `output/playwright/layout-study-department-2026-10-04.png` | 181472 | `B85CE3A745CD111DB1136DF9A5EF86D2275625B0C59E693073F1FBE906A4B26F` |
| `output/playwright/layout-study-mobile-2026-10-04.png` | 55549 | `03166DB9EA978A8EDA2E9F03F939095B5BD0B3F87369F10321D145D0ADD4A86E` |
| `artifacts/nature-campus-prototype/build_composition.py` | 10182 | `8A2A8E6814A3EDBA881B1B9807B2837638BC6B5B3C3E56AA25413C57F5198972` |
| `artifacts/nature-campus-prototype/nature-campus.glb` | 8945052 | `7AD9EE472B2E0F51A7E5E2107A88060258E43D87A9DDEDCEB887B6EBBA0B94D8` |
| `artifacts/nature-campus-prototype/nature-campus-composition.blend` | 4971900 | `2B2E05259DFE2BA66849448246D56A475A8D1EB6C77C0DCB90E200CC43E15AB0` |
| `apps/web/public/models/hengshi-hq-atlanta-exterior-web.glb` | 10002012 | `4767CAB4D346207A2109FFC1584E256E82AE1CECC110780B99C4406A9586AAFE` |
| `apps/web/src/world/WorldCanvas.tsx` | 5704 | `8A13414D7CF091584841F278C6FBB9B19A65ADF06073DCCF49F071CB42D66847` |
| `apps/web/src/world/ExteriorScene.tsx` | 6649 | `CCA5F46A456DCB29362BF2FB89AB4052727F0AF37501ABEF16BA50E9BC74CBC0` |
| `apps/web/src/world/WorldHUD.tsx` | 4574 | `A95C352FB7BDD4B9CF4351E98BBEB730CE8200745F62C3A835F69D67F12EBB24` |
| `package.json` | 538 | `A07F9F12C83736625D621781A1B30C8430452EF7E698FA626902CF16CEF7946B` |
| `package-lock.json` | 76835 | `D2DA4D7206344BA45645D7BAFE4EC692BB738EA0C1C98C2680522688B5733908` |
| `apps/web/package.json` | 1136 | `83E4178348EC081922DD3D53D00C51446B655091D056EC09DDE52A2496B04E2A` |
| `apps/web/package-lock.json` | 179000 | `35486FB012489DE4C3B363198304A25F44A0396707DB328190D7E056C06D416D` |
| `apps/api/requirements.txt` | 137 | `B99F98E119CB6653F38B19D1EE83CC7F33D92A699083645CA19369A8912E89BD` |

## Final disposition

**PASS** for the isolated final-third study's evidence accuracy, reproduced finite diagnostic and bounded viewer behavior. Layout/concept-match, safety, loading budgets, rights/compatibility, physical-mobile behavior and production acceptance remain held. Founder visual disposition follows; any further substantial model revision requires the applicable revision-limit decision. This receipt does not reopen or extend the phase.


from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[4]
OUT=Path(__file__).resolve().parent
INITIAL=OUT.parent
BOARD=ROOT/'docs/software-definition/definition-walkthrough.html'
RECEIPT=ROOT/'docs/software-definition/reviews/world-walking-walkthrough-v1-2026-10-06.md'
assert RECEIPT.exists() and 'REVISE' in RECEIPT.read_text(encoding='utf-8'), 'Wait for exact initial disposition'
if (OUT/'definition-walkthrough.html.reviewed').exists(): raise SystemExit('Already repaired; inspect rather than rerun.')
before=BOARD.read_bytes()
assert before==(INITIAL/'definition-walkthrough.html.reviewed').read_bytes()
old=b'WORLD_EXPERIENCE.md#mouse-touch-traversal-and-camera-profile-proposal--2026-10-06'
new=b'WORLD_EXPERIENCE.md'
assert before.count(old)==1
after=before.replace(old,new,1)
assert after.replace(b'href="../phase-1-3d/WORLD_EXPERIENCE.md">Controlling movement',b'href="../phase-1-3d/'+old+b'">Controlling movement',1)==before
(OUT/'initial-review.md').write_bytes(RECEIPT.read_bytes())
(OUT/'definition-walkthrough.html.before').write_bytes(before)
BOARD.write_bytes(after)
(OUT/'definition-walkthrough.html.reviewed').write_bytes(after)
(OUT/'scope-observations.json').write_text(json.dumps({'correction_cycle':1,'limit':3,'change':'Remove only guessed Markdown fragment from the new controlling movement source link. Same title, description, rendered content, CSS, diagram, controls, sources and layout.','original_capture_scope':'Original complete desktop/mobile PNGs remain exact reviewed captures of unchanged rendered content; no claimed new physical device or runtime inspection.','predecessor_restoration_equal':True},indent=2)+'\n',encoding='utf-8')
print('Only new source-link fragment removed; initial disposition and reviewed bytes preserved.')

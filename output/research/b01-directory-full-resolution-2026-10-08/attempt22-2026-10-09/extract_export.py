"""Decode one preserved Figma response and crop its exact reported tile bounds."""
from pathlib import Path
from io import BytesIO
import base64, hashlib, json
from PIL import Image

here = Path(__file__).resolve().parent
if (here / 'export-report.json').exists():
    raise SystemExit('Refuse repeat extraction')
raw = (here / 'provider-result.json').read_bytes()
result = json.loads(raw)
assert not result.get('isError')
report = json.loads(next(c['text'] for c in result['content'] if c['type'] == 'text'))
images = [c for c in result['content'] if c['type'] == 'image']
assert len(images) == report['plannedImageCount'] == 5
assert len(report['tiles']) == report['originalFrameCount'] == 52
assert all(report[key] for key in ('exportCompleted', 'originalGeometryTextUnchanged', 'originalPositionsRestored', 'parentOrderRestored', 'allCreatedNodesRemoved'))
decoded = []
for index, content in enumerate(images):
    data = base64.b64decode(content['data'], validate=True)
    image = Image.open(BytesIO(data))
    image.load()
    assert list(image.size) == report['sheetBounds'][index]
    (here / f'sheet-{index + 1}.png').write_bytes(data)
    decoded.append(image)
tiles = here / 'tiles'
tiles.mkdir()
inventory = []
for index, (source, clone, sheet, x, y, width, height) in enumerate(report['tiles']):
    assert all(isinstance(n, int) for n in (sheet, x, y, width, height))
    assert 0 <= x < x + width <= decoded[sheet].width and 0 <= y < y + height <= decoded[sheet].height
    name = f'{index + 1:02d}-{source.replace(":", "-")}.png'
    decoded[sheet].crop((x, y, x + width, y + height)).save(tiles / name)
    inventory.append({'ordinal': index + 1, 'source_id': source, 'file': 'tiles/' + name, 'dimensions': [width, height], 'sha256': hashlib.sha256((tiles / name).read_bytes()).hexdigest()})
comparisons = here / 'comparisons'
comparisons.mkdir()
for group in range(13):
    members = inventory[group * 4:group * 4 + 4]
    rows = [Image.open(here / item['file']).convert('RGB') for item in members]
    # First twelve are four 320px stream references; wide group uses two rows.
    columns = 4 if group < 12 else 2
    cell_width, cell_height = max(im.width for im in rows), max(im.height for im in rows)
    canvas = Image.new('RGB', (columns * cell_width, ((len(rows) + columns - 1) // columns) * cell_height), 'white')
    for n, image in enumerate(rows):
        canvas.paste(image, ((n % columns) * cell_width, (n // columns) * cell_height))
    canvas.save(comparisons / f'group-{group + 1:02d}.png')
(here / 'export-report.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
(here / 'pixel-inventory.json').write_text(json.dumps(inventory, indent=2) + '\n', encoding='utf-8')
receipt = {'product_release': 'v1', 'status': 'DOING', 'october_attempt': 22, 'conservative_metered': 19, 'is_error': False, 'images_returned': 5, 'frame_tiles': 52, 'source_preservation_checks': 'PASS', 'temporary_nodes_removed': report['removedCreatedNodeCount'], 'authorization_consumed': True, 'retry_authorized': False, 'visual_inspection': 'TODO', 'provider_result_sha256': hashlib.sha256(raw).hexdigest(), 'scope': 'Static scale-one Figma pixels and reported cleanup only; no interaction, accessibility certification, full B01 coverage, native restore/EXIT, independent acceptance or production implementation.'}
(here / 'receipt.json').write_text(json.dumps(receipt, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'images': len(images), 'tiles': len(inventory), 'comparison_groups': 13, 'source_preservation': 'PASS'}))

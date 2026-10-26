import hashlib
import json
from pathlib import Path
from PIL import Image, ImageDraw

base = Path(__file__).parent
receipt = json.loads((base / 'receipt.json').read_text(encoding='utf-8'))
source = json.loads((base / 'input.json').read_text(encoding='utf-8'))
images = [Image.open(base / f'comparison-{i + 1:02}.png').convert('RGB') for i in range(5)]
assert [list(image.size) for image in images] == receipt['sheetBounds']
assert len(receipt['frames']) == len(receipt['tiles']) == len(source['references']) == 28
assert sorted(tile[2] for tile in receipt['tiles']) == list(range(28))
records = []
for tile in receipt['tiles']:
    unit, clone, index, image_index, x, y, width, height = tile
    assert all(isinstance(v, int) for v in (index, image_index, x, y, width, height))
    assert x >= 0 and y >= 0 and x + width <= images[image_index].width and y + height <= images[image_index].height
    frame, frame_index, frame_width, frame_height = receipt['frames'][index]
    assert frame_index == index and width == frame_width == source['references'][index]['width']
    crop = images[image_index].crop((x, y, x + width, y + height))
    crop_name = f'unit-{index:02}.png'
    crop.save(base / crop_name)
    view_name = f'view-{index:02}.png'
    crop.crop((0, 0, frame_width, frame_height)).save(base / view_name)
    records.append({'input_index': index, 'frame_id': frame, 'unit_id': unit, 'temporary_clone_id': clone,
                    'comparison_file': f'comparison-{image_index + 1:02}.png', 'box': [x, y, width, height],
                    'unit_file': crop_name, 'view_file': view_name, 'frame_size': [frame_width, frame_height],
                    'reference': source['references'][index],
                    'sha256': hashlib.sha256((base / crop_name).read_bytes()).hexdigest()})
for image_index in range(5):
    boxes = [r['box'] for r in records if r['comparison_file'] == f'comparison-{image_index + 1:02}.png']
    for a_index, a in enumerate(boxes):
        for b in boxes[a_index + 1:]:
            assert not (a[0] < b[0] + b[2] and a[0] + a[2] > b[0] and a[1] < b[1] + b[3] and a[1] + a[3] > b[1])
for group_index in range(7):
    group = records[group_index * 4:group_index * 4 + 4]
    widths = [r['frame_size'][0] for r in group]
    heights = [r['frame_size'][1] for r in group]
    sheet = Image.new('RGB', (sum(widths) + 5 * 24, max(heights) + 60), 'white')
    draw = ImageDraw.Draw(sheet)
    left = 24
    for r in group:
        draw.text((left, 10), f"{r['input_index']:02} {r['reference']['streamId']}", fill='black')
        sheet.paste(Image.open(base / r['view_file']).convert('RGB'), (left, 36))
        left += r['frame_size'][0] + 24
    sheet.save(base / f'inspection-group-{group_index + 1:02}.png')
(base / 'crop-inventory.json').write_text(json.dumps(records, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'native_images': [list(image.size) for image in images], 'exact_crops': len(records),
                  'all_tiles_inside': True, 'nonoverlapping_tiles': True, 'visual_inspection': 'pending'}))

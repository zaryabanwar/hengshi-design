import hashlib
import json
from pathlib import Path
from PIL import Image, ImageDraw
base=Path(__file__).parent
r=json.loads((base/'receipt.json').read_text(encoding='utf-8'))
s=json.loads((base/'input.json').read_text(encoding='utf-8'))
returned=json.loads((base/'returned-images.json').read_text(encoding='utf-8'))
assert len(r['frames'])==len(r['units'])==len(r['tiles'])==len(s['references'])==48
assert sorted(t[2] for t in r['tiles'])==list(range(48))
images={}
mappings=[]
for entry in returned['images']:
    image=Image.open(base/entry['file']).convert('RGB')
    matching=[i for i,b in enumerate(r['sheetBounds']) if list(image.size)==b]
    assert len(matching)==1, 'Ambiguous image dimensions'
    sheet=matching[0]
    assert sheet not in images
    images[sheet]=image
    mappings.append({'returned_file':entry['file'],'planned_image_index':sheet,'dimensions':list(image.size),'basis':'unique native dimensions; producer visual content inspection still required'})
records=[]
missing=[]
for t in r['tiles']:
    unit,clone,index,sheet,x,y,width,height=t
    frame,frame_index,fw,fh=r['frames'][index]
    assert frame_index==index and fw==width==s['references'][index]['width']==320
    assert width>0 and height>0 and x>=0 and y>=0
    expected=r['sheetBounds'][sheet]
    assert x+width<=expected[0] and y+height<=expected[1]
    assert [r['units'][index][0],index,width,height]==r['units'][index]
    record={'input_index':index,'frame_id':frame,'unit_id':unit,'temporary_clone_id':clone,'planned_image_index':sheet,'box':[x,y,width,height],'frame_size':[fw,fh],'reference':s['references'][index]}
    if sheet not in images:
        missing.append(record)
        continue
    crop=images[sheet].crop((x,y,x+width,y+height))
    unit_file=f'unit-{index:02}.png'
    view_file=f'view-{index:02}.png'
    crop.save(base/unit_file)
    crop.crop((0,0,fw,fh)).save(base/view_file)
    record.update({'unit_file':unit_file,'view_file':view_file,'unit_sha256':hashlib.sha256((base/unit_file).read_bytes()).hexdigest(),'comparison_file':next(m['returned_file'] for m in mappings if m['planned_image_index']==sheet)})
    records.append(record)
for sheet in range(5):
    boxes=[t[4:] for t in r['tiles'] if t[3]==sheet]
    for i,a in enumerate(boxes):
        for b in boxes[i+1:]:
            assert not(a[0]<b[0]+b[2] and a[0]+a[2]>b[0] and a[1]<b[1]+b[3] and a[1]+a[3]>b[1])
for group_index in range((len(records)+3)//4):
    group=records[group_index*4:group_index*4+4]
    sheet_image=Image.new('RGB',(len(group)*320+(len(group)+1)*24,max(v['frame_size'][1] for v in group)+70),'white')
    draw=ImageDraw.Draw(sheet_image)
    for offset,record in enumerate(group):
        left=24+offset*344
        ref=record['reference']
        draw.text((left,10),f"{record['input_index']:02} {ref['templateId']}",fill='black')
        draw.text((left,28),f"{ref['streamId']} {ref['modeId']}",fill='black')
        sheet_image.paste(Image.open(base/record['view_file']).convert('RGB'),(left,50))
    sheet_image.save(base/f'inspection-group-{group_index+1:02}.png')
inventory={'product':'Hengshi Design v1','returned_images':mappings,'records':records,'missing':missing,'exact_crops':len(records),'missing_pixel_views':len(missing),'all_tiles_inside':True,'all_tiles_nonoverlapping':True,'visual_inspection':'pending','independent_review':'pending'}
(base/'crop-inventory.json').write_text(json.dumps(inventory,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'returned_images':len(images),'exact_crops':len(records),'missing_views':len(missing),'missing_image_indices':sorted(set(v['planned_image_index'] for v in missing)),'inspection_groups':(len(records)+3)//4}))

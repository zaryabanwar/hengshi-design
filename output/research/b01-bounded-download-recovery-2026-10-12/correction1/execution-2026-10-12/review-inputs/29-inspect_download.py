import hashlib,json
from pathlib import Path
from PIL import Image
base=Path(__file__).parent
r=json.loads((base/'prepare-receipt.json').read_text(encoding='utf-8'))
i=json.loads((base/'prepare-input.json').read_text(encoding='utf-8'))
d=json.loads((base/'download-result.json').read_text(encoding='utf-8'))
assert d['downloaded'] is True
assert r['sheetBounds']==[[3808,1996]]
image=Image.open(base/'comparison.png').convert('RGBA')
assert image.size==(3808,1996)
assert len(r['tiles'])==len(i['expected'])==11
records=[]
for t,e in zip(r['tiles'],i['expected'],strict=True):
    unit,clone,index,number,x,y,w,h=t
    assert [unit,index,w,h]==[e['unitId'],e['inputIndex'],e['width'],e['height']]
    assert number==0 and w==320 and x>=0 and y>=0 and x+w<=image.width and y+h<=image.height
    u=image.crop((x,y,x+w,y+h)); v=u.crop((0,0,e['frameWidth'],e['frameHeight']))
    un=f'unit-{index:02}.png';vn=f'view-{index:02}.png'
    u.save(base/un);v.save(base/vn)
    assert Image.open(base/un).convert('RGBA').tobytes()==u.tobytes()
    assert Image.open(base/vn).convert('RGBA').tobytes()==v.tobytes()
    records.append({'input_index':index,'unit_id':unit,'frame_id':e['frameId'],'temporary_clone_id':clone,'reference':e['frameName'],'box':[x,y,w,h],'frame_size':[e['frameWidth'],e['frameHeight']],'unit_file':un,'view_file':vn,'unit_sha256':hashlib.sha256((base/un).read_bytes()).hexdigest(),'view_sha256':hashlib.sha256((base/vn).read_bytes()).hexdigest()})
for group in range(3):
    selected=records[group*4:(group+1)*4]
    canvas=Image.new('RGBA',(320*len(selected),max(x['box'][3] for x in selected)),(255,255,255,255))
    for pos,entry in enumerate(selected):canvas.paste(Image.open(base/entry['unit_file']).convert('RGBA'),(pos*320,0))
    canvas.save(base/f'inspection-group-{group+1:02}.png')
(base/'crop-inventory.json').write_text(json.dumps({'source_image':'comparison.png','native_dimensions':[3808,1996],'records':records,'crop_equality':'Exact RGBA subregions of downloaded PNG; actual rendered content inspection separate','cleanup':'Held: attempt33 inventory guard failed before removals','review':'pending'},indent=2)+'\n',encoding='utf-8')
print(json.dumps({'native_width':320,'unit_crops':11,'frame_crops':11,'exact_rgba_subregions':True,'cleanup':'HELD'}))

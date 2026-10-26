"""Correct this batch's SVG design sources; no application code is touched."""
from pathlib import Path
import xml.etree.ElementTree as ET
import copy, math

ROOT=Path(__file__).parent
NS='http://www.w3.org/2000/svg'
ET.register_namespace('',NS)
tag=lambda name:f'{{{NS}}}{name}'

def wrap(value, width, size):
    cap=max(10,math.floor(width/(size*.57)))
    lines=[]; current=''
    for word in value.split():
        if current and len(current)+len(word)+1>cap:
            lines.append(current);current=word
        else: current+=(' ' if current else '')+word
    if current:lines.append(current)
    return lines

def correct(path):
    root=ET.parse(path).getroot()
    width=float(root.get('width'));mobile=width==320;pad=24 if mobile else 64
    children=list(root); replacements={};removed=set();shifts=[]
    i=0
    while i<len(children):
        node=children[i]
        if node.tag!=tag('text') or node.get('fill')!='#006D82':i+=1;continue
        group=[node];j=i+1;size=float(node.get('font-size'))
        while j<len(children):
            other=children[j]
            if other.tag!=tag('text') or other.get('fill')!=node.get('fill') or other.get('font-size')!=node.get('font-size') or abs(float(other.get('y'))-float(group[-1].get('y'))-size*1.35)>.01:break
            group.append(other);j+=1
        value=' '.join(n.text or '' for n in group)
        if value.endswith('↗'):
            lines=wrap(value[:-1].strip(),width-2*pad-40,size)
            replacements[node]=(group,lines,size)
            removed.update(group)
            cutoff=float(group[-1].get('y'))+size*.35
            shifts.append((cutoff,(len(lines)-len(group))*size*1.35))
        i=j
    offset=lambda y:sum(delta for cutoff,delta in shifts if y>cutoff+.01)
    output=[]
    for node in children:
        if node in replacements:
            group,lines,size=replacements[node]
            baseline=float(node.get('y'))+offset(float(node.get('y')))
            for k,line in enumerate(lines):
                new=copy.deepcopy(node);new.text=line;new.set('y',str(baseline+k*size*1.35));output.append(new)
            arrow=ET.Element(tag('path'),{'d':'M2 20 L20 2 M4 2 H20 V18','transform':f'translate({width-pad-24} {baseline-size+4})','fill':'none','stroke':'#006D82','stroke-width':'2'})
            output.append(arrow)
        if node in removed:continue
        if node.get('y') is not None:
            y=float(node.get('y'));node.set('y',str(y+offset(y)))
            if node.tag==tag('rect') and node.get('height'):
                height=float(node.get('height'));node.set('height',str(height+offset(y+height)-offset(y)))
        output.append(node)
    root[:]=output
    old_height=float(root.get('height'))+sum(delta for _,delta in shifts)
    # Three desktop utility controls have their own positions and labels.
    if not mobile:
        utility=next(n for n in root if n.tag==tag('text') and (n.text or '').startswith('Search        '))
        root.remove(utility)
        for label,x in [('Search',982),('Accessibility settings',1060),('3D World ↗',1270)]:
            n=copy.deepcopy(utility);n.text=label;n.set('x',str(x));root.append(n)
    privacy=next(n for n in root if n.tag==tag('text') and (n.text or '').startswith('Privacy policy'))
    copyright=next(n for n in root if n.tag==tag('text') and (n.text or '').startswith('©'))
    brands=[n for n in root if n.tag==tag('text') and n.text=='Hengshi Design']
    brand=brands[-1];by=float(brand.get('y'));py=float(privacy.get('y'))
    root.remove(privacy)
    for label,yy in [('About · Trust · Contact',py if mobile else by),('Search',(py if mobile else by)+28),('Accessibility settings',(py if mobile else by)+56)]:
        n=copy.deepcopy(privacy);n.text=label;n.set('x',str(pad if mobile else 720));n.set('y',str(yy));n.set('font-size','12');root.append(n)
    copyright.set('x',str(pad if mobile else 1170))
    copyright.set('y',str(py+96 if mobile else by+24))
    # Preserve the accepted secondary Contact action in the shared CTA.
    note=next(n for n in root if n.tag==tag('text') and n.text=='30-minute introductory call.')
    ny=float(note.get('y'))
    contact=copy.deepcopy(note);contact.text='Contact us ↗';contact.set('font-size','16');contact.set('fill','#FAF9F6');contact.set('y',str(ny+38));root.append(contact)
    if mobile:
        # Make room for Contact and the accepted footer links.
        for node in root:
            if node is contact:continue
            if node.get('y') and float(node.get('y'))>ny+1:node.set('y',str(float(node.get('y'))+40))
        new_height=old_height+110
    else:
        # Accepted footer is one row: brand, navigation, copyright.
        new_height=old_height
    for node in root:
        if node.tag==tag('rect') and float(node.get('y','0'))>1000 and node.get('fill')=='#0B0F14':node.set('height',str(new_height-float(node.get('y'))))
        if node.tag==tag('rect') and node.get('width')==str(int(width)) and node.get('fill')=='#FAF9F6':node.set('height',str(new_height))
    root.set('height',str(math.ceil(new_height)));root.set('viewBox',f'0 0 {int(width)} {math.ceil(new_height)}')
    root.set('data-design-state','review-corrected-awaiting-founder')
    ET.ElementTree(root).write(path,encoding='unicode')

for filename in ['index-desktop.svg','index-mobile.svg','wing-desktop.svg','wing-mobile.svg','detail-desktop.svg','detail-mobile.svg']:
    path=ROOT/filename
    before=ROOT/(path.stem+'-before-correction.svg')
    if not before.exists():before.write_bytes(path.read_bytes())
    correct(path)
print('Corrected 6 design sources: footer navigation, utility spacing, separate link arrows.')

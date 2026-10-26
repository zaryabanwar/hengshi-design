"""Design-only variable-content proofs; not application routes or runtime tests."""
from pathlib import Path
import json, html, math
from PIL import Image, ImageDraw, ImageFont
import cairosvg

ROOT = Path(__file__).parent
data = json.loads((ROOT / 'content.json').read_text(encoding='utf-8'))
INK, PAPER, LINK, SLATE, STONE = '#0B0F14', '#FAF9F6', '#006D82', '#2A3542', '#D8D3C8'

def proof(kind, index, mobile):
    width, pad = (320, 24) if mobile else (1440, 64)
    available, y, nodes, overflow = width - pad * 2, 32, [], []
    def text(value, size=16, color=INK, limit=None):
        nonlocal y
        limit = limit or available
        linked = value.endswith('↗')
        if linked:
            value = value[:-1].strip()
            limit -= 40
            nodes.append(f'<path d="M2 20 L20 2 M4 2 H20 V18" transform="translate({width-pad-24} {y+4})" fill="none" stroke="{LINK}" stroke-width="2"/>')
        # Same conservative line lengths used by the six editable Figma references.
        cap = max(10, math.floor(limit / (size * .57)))
        lines, current = [], ''
        for word in value.split(' '):
            if current and len(current) + len(word) + 1 > cap:
                lines.append(current)
                current = word
            else:
                current += (' ' if current else '') + word
        lines.append(current)
        font = ImageFont.truetype('C:/Windows/Fonts/arial.ttf', size)
        for line in lines:
            measured = font.getlength(line)
            if measured > limit: overflow.append({'text': line, 'measured': measured, 'limit': limit})
            nodes.append(f'<text x="{pad}" y="{y+size}" font-family="Arial" font-size="{size}" fill="{color}">{html.escape(line)}</text>')
            y += size * 1.35
        y += 20
    def label(value): text(value.upper(), 12, LINK)
    if kind == 'wing':
        wing = data['wings'][index]
        text('Home / Services / ' + wing['title'], 14, LINK)
        label('Service wing')
        text(wing['title'], 40 if mobile else 72, limit=available if mobile else 1100)
        text(wing['summary'], 18 if mobile else 24, SLATE, available if mobile else 800)
        label(str(len(wing['services'])) + ' formal service' + ('s' if len(wing['services']) != 1 else ''))
        for service_index in wing['services']:
            service = data['details'][service_index]
            text(service['title'] + ' ↗', 24 if mobile else 32, LINK)
            text(service['summary'], color=SLATE, limit=available if mobile else 780)
            y += 32
    else:
        service = data['details'][index]
        wing = data['wings'][service['wing']]
        text('Home / Services / ' + wing['title'] + ' / ' + service['title'], 14, LINK)
        label('Formal service')
        text(service['title'], 40 if mobile else 72, limit=available if mobile else 1100)
        text(service['summary'], 18 if mobile else 24, SLATE, available if mobile else 800)
        label('Your decision')
        text(service['decision'], 28 if mobile else 40)
        label('Possible focus')
        for focus in service['focus']: text(focus, 20 if mobile else 26)
        label('Scope and boundaries')
        text(service['boundary'], color=SLATE, limit=available if mobile else 800)
        label('Keep exploring')
        text('Back to ' + wing['title'] + ' ↗', 20 if mobile else 28, LINK)
        for sibling in wing['services']:
            if sibling != index: text(data['details'][sibling]['title'] + ' ↗', 20, LINK)
    text('All services ↗', color=LINK)
    y += 20
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{math.ceil(y)}"><rect width="100%" height="100%" fill="{PAPER}"/>{"".join(nodes)}</svg>'
    name = f'fit-{kind}-{index+1:02}-' + ('320' if mobile else '1440')
    (ROOT / (name+'.svg')).write_text(svg, encoding='utf-8')
    cairosvg.svg2png(bytestring=svg.encode(), write_to=str(ROOT / (name+'.png')))
    return {'name': name, 'width': width, 'height': math.ceil(y), 'overflow': overflow}

records = [proof(kind, i, mobile) for kind, count in [('wing',5), ('detail',10)] for i in range(count) for mobile in [False,True]]
(ROOT / 'fit-measurements.json').write_text(json.dumps(records, indent=2), encoding='utf-8')
for kind, start, end in [('wing',1,6),('detail',1,6),('detail',6,11)]:
    panels = [Image.open(ROOT/f'fit-{kind}-{i:02}-320.png').convert('RGB') for i in range(start,end)]
    sheet = Image.new('RGB', (len(panels)*344+24, max(p.height for p in panels)+72), '#D8D3C8')
    draw = ImageDraw.Draw(sheet)
    for i,panel in enumerate(panels):
        x=24+i*344
        draw.text((x,16),f'{kind} {start+i:02} / 320px',fill=INK)
        sheet.paste(panel,(x,48))
    sheet.save(ROOT/f'fit-{kind}-{start:02}-{end-1:02}-sheet.png')
print(json.dumps({'proofs':len(records),'overflows':[r for r in records if r['overflow']]}))

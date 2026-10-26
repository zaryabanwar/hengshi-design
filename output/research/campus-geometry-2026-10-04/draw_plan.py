"""Render a standalone SVG diagnostic from actual exported mesh projections."""
import html
import json
from pathlib import Path

root=Path(__file__).parent
data=json.loads((root/"inspection.json").read_text(encoding="utf-8"))
fx=lambda x:90+(x+54)*1020/111
fy=lambda y:100+(65-y)*1020/111
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="1400" viewBox="0 0 1200 1400">',
'<rect width="1200" height="1400" fill="#fafaf5"/>',
'<style>text{font-family:Arial,sans-serif;fill:#24302d} .caption{font-size:20px} .small{font-size:18px}</style>']
def text(x,y,value,size=22,anchor="middle",weight="normal"):
 parts.append(f'<text x="{x:.2f}" y="{y:.2f}" font-size="{size}" text-anchor="{anchor}" font-weight="{weight}">{html.escape(value)}</text>')
text(600,42,"Current campus: connector obstructions",32,weight="bold")
text(600,76,"Selected exported meshes; generator routes are not approved walking paths",20)
for tick in (-40,-20,0,20,40,60):
 parts.append(f'<line x1="90" y1="{fy(tick):.2f}" x2="1110" y2="{fy(tick):.2f}" stroke="#deded7"/>')
 text(78,fy(tick)+6,str(tick),16,anchor="end")
for tick in (-40,-20,0,20,40):
 parts.append(f'<line x1="{fx(tick):.2f}" y1="100" x2="{fx(tick):.2f}" y2="1120" stroke="#deded7"/>')
 text(fx(tick),1144,str(tick),16)
parts.append('<defs><clipPath id="plot"><rect x="90" y="100" width="1020" height="1020"/></clipPath></defs><g clip-path="url(#plot)">')
for mesh in sorted(data["plan_meshes"],key=lambda m:"river" not in m["name"].lower()):
 name=mesh["name"].lower(); verts=mesh["world_vertices"]
 for triangle in mesh["triangles"]:
  points=" ".join(f"{fx(verts[i][0]):.2f},{fy(verts[i][1]):.2f}" for i in triangle)
  if "glazing" in name:
   parts.append(f'<polygon points="{points}" fill="none" stroke="#af872a" stroke-width="1"/>')
  else:
   color="#b6dae0" if "river" in name else "#e2ddcb"
   parts.append(f'<polygon points="{points}" fill="{color}" fill-opacity="0.85"/>')
for route in data["routes"]:
 points=" ".join(f"{fx(row['xy'][0]):.2f},{fy(row['xy'][1]):.2f}" for row in route["samples"])
 parts.append(f'<polyline points="{points}" fill="none" stroke="#324e47" stroke-width="2" stroke-dasharray="8 5"/>')
 for row in route["samples"]:
  if row["water"]:parts.append(f'<circle cx="{fx(row["xy"][0]):.2f}" cy="{fy(row["xy"][1]):.2f}" r="2.8" fill="#287d9b"/>')
 for hit in route["centreline_obstruction_hits"]:
  x,y=map(lambda v:v,hit["point"][:2]); px,py=fx(x),fy(y)
  parts.append(f'<path d="M{px-7:.2f},{py-7:.2f}L{px+7:.2f},{py+7:.2f}M{px-7:.2f},{py+7:.2f}L{px+7:.2f},{py-7:.2f}" stroke="#b13535" stroke-width="3"/>')
parts.append(f'<path d="M{fx(-3):.2f},{fy(-42):.2f}L{fx(-3):.2f},{fy(12):.2f}" stroke="#324e47" stroke-width="2" stroke-dasharray="8 5"/>')
for label,x,y in [("Reception",-3,12),("1 · Strategy",-29,-5),("2 · Digital",-32,27),("3 · AI + Data",-6,49),("4 · Immersive",28,39),("5 · Cloud",36,-3)]:
 px,py=fx(x),fy(y+2.8)
 parts.append(f'<rect x="{px-90:.2f}" y="{py-23:.2f}" width="180" height="31" fill="#fafaf5" fill-opacity="0.92"/>')
 text(px,py,label,20,weight="bold")
parts.append('</g><rect x="90" y="100" width="1020" height="1020" fill="none" stroke="#9fa89c"/>')
text(600,1174,"Blender plan X / Y · unverified model units",20)
legend=[("#e2ddcb","Paving / terrace projection"),("#b6dae0","Exported river projection"),("#af872a","Glazing projection")]
for i,(color,label) in enumerate(legend):
 x=100+i*355
 parts.append(f'<rect x="{x}" y="1210" width="24" height="20" fill="{color}"/>')
 text(x+33,1226,label,18,anchor="start")
text(600,1265,"Dashed lines: generator centrelines · Red X: mesh hit at diagnostic Z = 1.4",20)
text(600,1294,"Blue dots: sampled centreline above the exported water surface",20)
text(600,1334,"All five routes intersect Reception glazing; three also intersect the welcome desk.",20)
text(600,1362,"Sampled support does not prove bridge structure, full-width clearance or navigation.",19)
text(600,1389,"Read-only Blender 5.0.1 inspection · no geometry changed · no navigation runtime tested",18)
parts.append('</svg>')
(root/"connector-obstructions.svg").write_text("\n".join(parts),encoding="utf-8")
print("SVG diagnostic exported from observed mesh coordinates and ray hits.")

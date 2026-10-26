from pathlib import Path
import json, hashlib, subprocess
ROOT=Path(__file__).resolve().parents[3]
OUT=Path(__file__).resolve().parent
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
raw=(OUT/'command-02.stdout.txt').read_text(encoding='utf-8')
assert raw.startswith('### Result\n') or raw.startswith('### Result\r\n')
observations=json.JSONDecoder().raw_decode(raw.split('### Result',1)[1].lstrip())[0]
assert observations['pass']
(OUT/'browser-observations.json').write_text(json.dumps(observations,indent=2)+'\n',encoding='utf-8')
(OUT/'tool-observations.json').write_text(json.dumps({'computer_use_attempt':'cua.getState()','computer_use_result':'failed to write kernel assets: The system cannot find the path specified. (os error 3)','fallback':'Existing Playwright CLI, isolated cached Chromium at explicit executablePath.','limits':'CLI 0.1.19 and cached Chromium 149 are not a selected compatible production browser/tool graph; source-provenance mismatch retained from prior tooling evidence. Desktop resize is not physical mobile inspection. No installs, machine configuration or account/profile access.'},indent=2)+'\n',encoding='utf-8')
guards=json.loads((OUT/'protected-before.json').read_text(encoding='utf-8'))
assert all(digest(ROOT/x['path'])==x['sha256'] for x in guards)
assert (ROOT/'docs/software-definition/definition-walkthrough.html').read_bytes()==(OUT/'definition-walkthrough.html.reviewed').read_bytes()
diff=subprocess.run(['git','-c','core.autocrlf=false','-c','core.whitespace=blank-at-eol,blank-at-eof,space-before-tab,cr-at-eol','diff','--check','--','docs/software-definition/definition-walkthrough.html'],cwd=ROOT,capture_output=True)
assert diff.returncode==0, diff.stdout+diff.stderr
files=[p for p in OUT.iterdir() if p.is_file() and p.name!='review-inputs.json']
sources=['docs/software-definition/definition-walkthrough.html','AGENTS.md','.specify/memory/constitution.md','PROJECT.md','PROJECT_STATE.yaml','DECISIONS.md','TASKS.md','docs/software-definition/README.md','docs/phase-1-3d/WORLD_EXPERIENCE.md','docs/phase-1-3d/WORLD_MEASUREMENT_PROFILE.md','docs/phase-1-3d/reviews/world-traversal-profile-v1-2026-10-06.md','docs/phase-1-3d/reviews/world-measurement-profile-v1-2026-10-06.md','specs/003-3d-experience-completion/spec.md']
inputs=[{'path':p.relative_to(ROOT).as_posix(),'sha256':digest(p)} for p in files]+[{'path':p,'sha256':digest(ROOT/p)} for p in sources]
packet={'scope':'Only new walking section and its nav link; retained full-board bytes are context, no earlier section reviewed anew. Exact snapshots and complete desktop/mobile pixels.','inputs':inputs,'protected_guard_count':len(guards),'guard_match':True,'whitespace_pass':True,'runtime_and_full_accessibility_not_tested':True}
(OUT/'review-inputs.json').write_text(json.dumps(packet,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'input_count':len(inputs),'packet_sha256':digest(OUT/'review-inputs.json'),'guard_count':len(guards),'whitespace':True}))

"""Existing cached CLI/browser, isolated static-board evidence profile."""
from pathlib import Path
import os
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
CLI = Path('C:/Users/Zaryab/AppData/Local/npm-cache/_npx/31e32ef8478fbf80/node_modules/@playwright/cli/playwright-cli.js')
NODE = ROOT / 'output/research/frontend-build-evaluation-2026-10-06/runtime/node.exe'
env = {k: os.environ[k] for k in ('SystemRoot', 'WINDIR', 'COMSPEC', 'ProgramFiles',
                                 'ProgramFiles(x86)', 'PROGRAMDATA') if k in os.environ}
for directory in ('profile', 'tmp', 'appdata', 'localappdata'):
    (OUT / directory).mkdir(exist_ok=True)
env.update({'USERPROFILE': str(OUT / 'profile'), 'TEMP': str(OUT / 'tmp'),
            'TMP': str(OUT / 'tmp'), 'APPDATA': str(OUT / 'appdata'),
            'LOCALAPPDATA': str(OUT / 'localappdata'),
            'PATH': str(NODE.parent) + os.pathsep + str(Path(env['SystemRoot']) / 'System32'),
            'PLAYWRIGHT_BROWSERS_PATH': 'C:/Users/Zaryab/AppData/Local/ms-playwright'})
result = subprocess.run([str(NODE), str(CLI), '-s=hengshi-qa-review-reference-20261006',
                         *sys.argv[1:]], cwd=OUT, env=env, capture_output=True, timeout=55)
number = len(list(OUT.glob('command-*.stdout.txt'))) + 1
(OUT / f'command-{number:02}.stdout.txt').write_bytes(result.stdout)
(OUT / f'command-{number:02}.stderr.txt').write_bytes(result.stderr)
print(result.stdout.decode('utf-8', errors='replace'))
if result.stderr:
    print(result.stderr.decode('utf-8', errors='replace'), file=sys.stderr)
sys.exit(result.returncode)

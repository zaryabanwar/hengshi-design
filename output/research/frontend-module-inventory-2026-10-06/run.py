"""Run one existing-vendor build with a clean, task-owned environment; no install."""
import json
import os
from pathlib import Path
import subprocess
import time

evidence = Path(__file__).resolve().parent
repo = evidence.parents[2]
node = repo / 'output/research/frontend-build-evaluation-2026-10-06/runtime/node.exe'
environment = {name: os.environ[name] for name in (
    'SYSTEMROOT', 'WINDIR', 'COMSPEC', 'PATHEXT', 'PROGRAMFILES',
    'PROGRAMFILES(X86)', 'PROGRAMDATA') if name in os.environ}
environment['PATH'] = str(node.parent) + os.pathsep + str(Path(environment['SYSTEMROOT']) / 'System32')
for name, directory in [('TEMP', 'tmp'), ('TMP', 'tmp'), ('USERPROFILE', 'profile'),
                        ('APPDATA', 'appdata'), ('LOCALAPPDATA', 'localappdata')]:
    target = evidence / 'runtime' / directory
    target.mkdir(parents=True, exist_ok=True)
    environment[name] = str(target)
(evidence / 'environment.json').write_text(json.dumps(environment, indent=2) + '\n', encoding='utf-8')
command = [str(node), str(evidence / 'inspect.mjs')]
started = time.time()
with (evidence / 'build.stdout.txt').open('wb') as stdout, (evidence / 'build.stderr.txt').open('wb') as stderr:
    result = subprocess.run(command, cwd=evidence, env=environment, stdout=stdout, stderr=stderr, timeout=150)
receipt = {'command': command, 'cwd': str(evidence), 'exitCode': result.returncode,
           'elapsedSecondsObservationOnly': time.time() - started,
           'environmentKeys': sorted(environment), 'networkRequestedByThisScript': False}
(evidence / 'run-receipt.json').write_text(json.dumps(receipt, indent=2) + '\n', encoding='utf-8')
print(json.dumps(receipt, indent=2))
raise SystemExit(result.returncode)

from pathlib import Path
import json, os, subprocess, sys, time, urllib.request

out = Path(__file__).resolve().parent
root = out.parents[2]
node = root / 'output/research/frontend-build-evaluation-2026-10-06/runtime/node.exe'
cli = Path('C:/Users/Zaryab/AppData/Local/npm-cache/_npx/31e32ef8478fbf80/node_modules/@playwright/cli/playwright-cli.js')
browser = out / 'browser'
browser.mkdir(exist_ok=True)
env = json.loads((out / 'environment.json').read_text(encoding='utf-8'))
env['PLAYWRIGHT_BROWSERS_PATH'] = 'C:/Users/Zaryab/AppData/Local/ms-playwright'
sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

if sys.argv[1] == 'start-preview':
    config = {'browser': {'browserName': 'chromium', 'isolated': True,
        'launchOptions': {'executablePath': 'C:/Users/Zaryab/AppData/Local/ms-playwright/chromium-1228/chrome-win64/chrome.exe', 'headless': True},
        'contextOptions': {'viewport': {'width': 1280, 'height': 900}}},
        'network': {'allowedOrigins': ['http://127.0.0.1:5281']}, 'outputDir': str(browser)}
    (browser / 'browser-config.json').write_text(json.dumps(config, indent=2), encoding='utf-8')
    command = [str(node), str(root / 'output/research/frontend-three-remedy-evaluation-2026-10-06/candidate/node_modules/vite/bin/vite.js'), 'preview', '--outDir', str(out / 'build-dist'), '--host', '127.0.0.1', '--port', '5281', '--strictPort']
    proc = subprocess.Popen(command, cwd=out / 'workspace', env=env, stdin=subprocess.DEVNULL,
        stdout=(browser / 'preview.stdout.txt').open('wb'), stderr=(browser / 'preview.stderr.txt').open('wb'), creationflags=subprocess.CREATE_NO_WINDOW)
    (browser / 'preview-start.json').write_text(json.dumps({'pid': proc.pid, 'command': command, 'cwd': str(out / 'workspace')}, indent=2), encoding='utf-8')
    for attempt in range(50):
        if proc.poll() is not None: raise RuntimeError('Preview stopped before ready')
        try:
            with urllib.request.urlopen('http://127.0.0.1:5281', timeout=1) as response:
                assert response.status == 200
            print('Preview ready, pid ' + str(proc.pid)); break
        except OSError: time.sleep(0.1)
    else: raise RuntimeError('Preview readiness failed')
else:
    command = [str(node), str(cli), '-s=hengshi-three-independent-20261006', *sys.argv[1:]]
    proc = subprocess.run(command, cwd=browser, env=env, capture_output=True, timeout=100, creationflags=subprocess.CREATE_NO_WINDOW)
    index = len(list(browser.glob('command-*.json'))) + 1
    name = 'command-' + str(index).zfill(2)
    for stream in ['stdout', 'stderr']: (browser / (name + '.' + stream + '.txt')).write_bytes(getattr(proc, stream))
    (browser / (name + '.json')).write_text(json.dumps({'command': command, 'cwd': str(browser), 'exit': proc.returncode}, indent=2), encoding='utf-8')
    print(proc.stdout.decode('utf-8'))
    if proc.stderr: print(proc.stderr.decode('utf-8'), file=sys.stderr)
    sys.exit(proc.returncode)

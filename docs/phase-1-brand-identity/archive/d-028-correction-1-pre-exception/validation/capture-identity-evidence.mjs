import { createRequire } from 'node:module';
import { existsSync } from 'node:fs';
import { mkdir, rm } from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const require = createRequire(import.meta.url);
const { chromium } = require('../../../apps/web/node_modules/playwright');
const validationDir = path.dirname(fileURLToPath(import.meta.url));
const identityDir = path.resolve(validationDir, '..');
const assetsDir = path.join(identityDir, 'assets');
const boardUrl = pathToFileURL(path.join(identityDir, 'visual-boards', 'index.html')).href;
const scaleUrl = pathToFileURL(path.join(identityDir, 'visual-boards', 'scale-evidence.html')).href;
const profileRoot = path.join(os.tmpdir(), `hengshi-brand-i3-${process.pid}-${Date.now()}`);

if (path.resolve(profileRoot).toLowerCase().startsWith(path.resolve(identityDir).toLowerCase())) {
  throw new Error('Temporary browser profile must be outside the deliverable.');
}

await mkdir(assetsDir, { recursive: true });

async function capture(name, url, viewport, options = {}) {
  const profile = path.join(profileRoot, name.replace(/\.png$/, ''));
  const context = await chromium.launchPersistentContext(profile, {
    headless: true,
    viewport,
    deviceScaleFactor: 1,
    forcedColors: options.forcedColors ? 'active' : 'none',
    colorScheme: 'light',
    reducedMotion: 'reduce'
  });
  try {
    await context.route('**/*', route => {
      const requestUrl = route.request().url();
      return requestUrl.startsWith('file:') || requestUrl.startsWith('data:') ? route.continue() : route.abort();
    });
    const page = context.pages()[0] || await context.newPage();
    await page.goto(url, { waitUntil: 'load' });
    await page.emulateMedia({ media: options.print ? 'print' : 'screen', forcedColors: options.forcedColors ? 'active' : 'none', reducedMotion: 'reduce' });
    if (options.grayscale) {
      await page.addStyleTag({ content: 'html { filter: grayscale(1) !important; }' });
    }
    await page.evaluate(async () => document.fonts?.ready);
    await page.screenshot({ path: path.join(assetsDir, name), fullPage: true, animations: 'disabled' });
    const dimensions = await page.evaluate(() => ({ width: document.documentElement.scrollWidth, height: document.documentElement.scrollHeight }));
    process.stdout.write(`${name}: ${dimensions.width}x${dimensions.height}\n`);
  } finally {
    await context.close();
  }
}

const requested = new Set(process.argv.slice(2));
const jobs = [
  ['identity-board-wide.png', boardUrl, { width: 1440, height: 900 }, {}],
  ['identity-board-preview.png', boardUrl, { width: 1440, height: 900 }, {}],
  ['identity-board-medium.png', boardUrl, { width: 900, height: 900 }, {}],
  ['identity-board-narrow.png', boardUrl, { width: 390, height: 844 }, {}],
  ['identity-board-forced-colors.png', boardUrl, { width: 900, height: 900 }, { forcedColors: true }],
  ['identity-board-grayscale.png', boardUrl, { width: 900, height: 900 }, { grayscale: true }],
  ['identity-board-print.png', boardUrl, { width: 1200, height: 900 }, { print: true }],
  ['identity-scale-evidence.png', scaleUrl, { width: 1200, height: 900 }, {}]
];
try {
  for (const [name, url, viewport, options] of jobs) {
    if (requested.size === 0 || requested.has(name)) await capture(name, url, viewport, options);
  }
} finally {
  await rm(profileRoot, { recursive: true, force: true });
}

if (existsSync(profileRoot)) {
  throw new Error(`Temporary browser profile cleanup failed: ${profileRoot}`);
}
process.stdout.write(`Temporary profiles removed: ${profileRoot}\n`);

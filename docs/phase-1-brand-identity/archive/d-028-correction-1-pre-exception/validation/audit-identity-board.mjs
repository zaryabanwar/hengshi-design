import { createRequire } from 'node:module';
import { existsSync } from 'node:fs';
import { readFile, rm, writeFile } from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const require = createRequire(import.meta.url);
const { chromium } = require('../../../apps/web/node_modules/playwright');
const axeSource = await readFile(require.resolve('../../../apps/web/node_modules/axe-core/axe.min.js'), 'utf8');
const validationDir = path.dirname(fileURLToPath(import.meta.url));
const identityDir = path.resolve(validationDir, '..');
const profile = path.join(os.tmpdir(), `hengshi-brand-a11y-i3-${process.pid}-${Date.now()}`);
const checks = [
  { id: 'board-wide', file: 'visual-boards/index.html', viewport: { width: 1440, height: 900 } },
  { id: 'board-medium', file: 'visual-boards/index.html', viewport: { width: 900, height: 900 } },
  { id: 'board-narrow', file: 'visual-boards/index.html', viewport: { width: 390, height: 844 } },
  { id: 'scale-evidence', file: 'visual-boards/scale-evidence.html', viewport: { width: 1200, height: 900 } }
];
const results = [];

const context = await chromium.launchPersistentContext(profile, { headless: true, deviceScaleFactor: 1, reducedMotion: 'reduce' });
try {
  await context.route('**/*', route => {
    const url = route.request().url();
    return url.startsWith('file:') || url.startsWith('data:') ? route.continue() : route.abort();
  });
  const page = context.pages()[0] || await context.newPage();
  for (const check of checks) {
    await page.setViewportSize(check.viewport);
    await page.goto(pathToFileURL(path.join(identityDir, check.file)).href, { waitUntil: 'load' });
    await page.addScriptTag({ content: axeSource });
    const audit = await page.evaluate(async () => {
      const result = await globalThis.axe.run(document, { runOnly: { type: 'tag', values: ['wcag2a', 'wcag2aa', 'wcag21aa', 'wcag22aa'] } });
      return {
        violations: result.violations.map(v => ({ id: v.id, impact: v.impact, nodes: v.nodes.length, help: v.help })),
        incomplete: result.incomplete.map(v => ({ id: v.id, impact: v.impact, nodes: v.nodes.length, targets: v.nodes.map(n => n.target.join(' ')), summaries: v.nodes.map(n => n.failureSummary || '') }))
      };
    });
    results.push({ ...check, violationCount: audit.violations.length, violations: audit.violations, incomplete: audit.incomplete });
  }
} finally {
  await context.close();
  await rm(profile, { recursive: true, force: true });
}

const report = {
  schemaVersion: 1,
  document: 'Hengshi Design identity board automated accessibility evidence',
  iteration: 3,
  date: '2026-07-19',
  tool: 'axe-core from existing repository dependency, injected into local file pages',
  scope: 'WCAG 2 A/AA, WCAG 2.1 AA, WCAG 2.2 AA automated rules; manual review still required',
  network: 'all non-file and non-data requests aborted',
  temporaryProfileRemoved: !existsSync(profile),
  checks: results,
  totalViolations: results.reduce((sum, item) => sum + item.violationCount, 0)
};
await writeFile(path.join(validationDir, 'browser-audit-report.json'), `${JSON.stringify(report, null, 2)}\n`, 'utf8');
process.stdout.write(`${JSON.stringify(report, null, 2)}\n`);
if (!report.temporaryProfileRemoved || report.totalViolations !== 0) process.exitCode = 1;

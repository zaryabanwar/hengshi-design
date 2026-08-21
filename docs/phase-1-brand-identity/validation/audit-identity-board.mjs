import { createRequire } from 'node:module';
import { existsSync } from 'node:fs';
import { readFile, rm, writeFile } from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const require = createRequire(import.meta.url);
const { chromium } = require('../../../apps/web/node_modules/playwright');
const playwrightVersion = require('../../../apps/web/node_modules/playwright/package.json').version;
const axePackage = require('../../../apps/web/node_modules/axe-core/package.json');
const axeSource = await readFile(require.resolve('../../../apps/web/node_modules/axe-core/axe.min.js'), 'utf8');
const validationDir = path.dirname(fileURLToPath(import.meta.url));
const identityDir = path.resolve(validationDir, '..');
const boardUrl = pathToFileURL(path.join(identityDir, 'visual-boards', 'index.html')).href;
const profile = path.join(os.tmpdir(), `hengshi-brand-d034-contrast-completion-audit-${process.pid}-${Date.now()}`);
const textSpacingCss = `
  * { line-height: 1.5 !important; letter-spacing: 0.12em !important; word-spacing: 0.16em !important; }
  p { margin-bottom: 2em !important; }
`;
const checks = [
  { id: 'board-wide', viewport: { width: 1440, height: 900 } },
  { id: 'board-medium-900', viewport: { width: 900, height: 900 } },
  { id: 'board-narrow-390', viewport: { width: 390, height: 844 } },
  { id: 'board-narrow-320', viewport: { width: 320, height: 800 } },
  { id: 'board-text-spacing-320', viewport: { width: 320, height: 800 }, textSpacing: true },
  { id: 'board-forced-colors', viewport: { width: 900, height: 900 }, forcedColors: true },
  { id: 'board-grayscale', viewport: { width: 900, height: 900 }, grayscale: true },
  { id: 'board-print', viewport: { width: 1200, height: 900 }, print: true },
  { id: 'board-asset-failure-320', viewport: { width: 320, height: 800 }, assetFailure: true }
];
const results = [];
const externalRequests = [];

const context = await chromium.launchPersistentContext(profile, {
  headless: true,
  deviceScaleFactor: 1,
  reducedMotion: 'reduce'
});
const chromiumVersion = context.browser()?.version() || 'playwright-managed Chromium';
try {
  await context.route('**/*', route => {
    const url = route.request().url();
    if (url.startsWith('file:') || url.startsWith('data:')) return route.continue();
    externalRequests.push(url);
    return route.abort();
  });

  for (const check of checks) {
    const page = await context.newPage();
    const consoleErrors = [];
    const pageErrors = [];
    let expectedSvgFailures = 0;
    page.on('console', message => {
      if (message.type() === 'error') consoleErrors.push(message.text());
    });
    page.on('pageerror', error => pageErrors.push(error.message));
    if (check.assetFailure) {
      await page.route('**/*.svg', route => {
        expectedSvgFailures += 1;
        return route.abort('failed');
      });
    }
    await page.setViewportSize(check.viewport);
    await page.goto(boardUrl, { waitUntil: 'load' });
    await page.emulateMedia({
      media: check.print ? 'print' : 'screen',
      forcedColors: check.forcedColors ? 'active' : 'none',
      reducedMotion: 'reduce'
    });
    if (check.grayscale) await page.addStyleTag({ content: 'html { filter: grayscale(1) !important; }' });
    if (check.textSpacing) await page.addStyleTag({ content: textSpacingCss });
    await page.evaluate(async () => document.fonts?.ready);

    const measurements = await page.evaluate(({ forcedColors }) => {
      const root = document.documentElement;
      const responsiveLabels = [...document.querySelectorAll('.responsive-series-chart .series-label')]
        .filter(element => getComputedStyle(element).display !== 'none' && element.getClientRects().length)
        .map(element => ({ name: element.textContent.trim(), fontSizeCssPx: Number.parseFloat(getComputedStyle(element).fontSize) }));
      const specimen = document.querySelector('.data-specimen');
      const specimenVisible = specimen && getComputedStyle(specimen).display !== 'none' && specimen.getClientRects().length > 0;
      const svgEndpointLabelCssPx = specimenVisible ? 15 * specimen.getBoundingClientRect().width / 960 : null;
      const application = document.querySelector('.application-grid')?.getBoundingClientRect();
      const hero = document.querySelector('.hero-sample')?.getBoundingClientRect();
      const evidence = document.querySelector('.evidence-sample')?.getBoundingClientRect();
      const proposed = document.querySelector('p[data-evidence-state="proposed"]');
      const parseRgb = value => {
        const match = value.match(/rgba?\((\d+)[, ]+(\d+)[, ]+(\d+)(?:[, /]+([\d.]+))?\)/);
        return match ? [Number(match[1]), Number(match[2]), Number(match[3]), match[4] === undefined ? 1 : Number(match[4])] : null;
      };
      const luminance = rgb => {
        const channels = rgb.slice(0, 3).map(value => {
          const channel = value / 255;
          return channel <= 0.04045 ? channel / 12.92 : ((channel + 0.055) / 1.055) ** 2.4;
        });
        return 0.2126 * channels[0] + 0.7152 * channels[1] + 0.0722 * channels[2];
      };
      const contrast = (foreground, background) => {
        const light = Math.max(luminance(foreground), luminance(background));
        const dark = Math.min(luminance(foreground), luminance(background));
        return (light + 0.05) / (dark + 0.05);
      };
      const effectiveBackground = element => {
        for (let node = element; node; node = node.parentElement) {
          const parsed = parseRgb(getComputedStyle(node).backgroundColor);
          if (parsed && parsed[3] === 1) return parsed;
        }
        return [255, 255, 255, 1];
      };
      const forcedColorSelectors = ['body', '.masthead h1', '.masthead .lede', '.direction p', '.dark h2', '.variant-grid figure:not(.reverse) figcaption', '.variant-grid figure.reverse figcaption', '.responsive-series-chart figcaption', '.dependency-key', '.evidence-sample p', '.gate h2', 'footer'];
      const forcedColorContrasts = forcedColors ? forcedColorSelectors.flatMap(selector => [...document.querySelectorAll(selector)]).filter(element => getComputedStyle(element).display !== 'none' && element.getClientRects().length).map(element => {
        const foreground = parseRgb(getComputedStyle(element).color);
        const background = effectiveBackground(element);
        return { selector: element.matches('.variant-grid figure.reverse figcaption') ? '.reverse > figcaption' : element.tagName.toLowerCase(), ratio: foreground && background ? Number(contrast(foreground, background).toFixed(2)) : 0 };
      }) : [];
      return {
        clientWidth: root.clientWidth,
        scrollWidth: root.scrollWidth,
        specimenVisible,
        svgEndpointLabelCssPx,
        responsiveLabels,
        semanticSeriesOrder: [...document.querySelectorAll('.series-list [data-series] strong')].map(node => node.textContent.trim()),
        responsiveSeriesOrder: [...document.querySelectorAll('.responsive-series-chart [data-series] .series-label')].map(node => node.textContent.trim()),
        actions: [...document.querySelectorAll('.actions a')].map(node => ({ name: node.textContent.trim(), width: node.getBoundingClientRect().width, height: node.getBoundingClientRect().height })),
        applicationBounds: application ? { left: application.left, right: application.right, width: application.width } : null,
        heroBounds: hero ? { left: hero.left, right: hero.right, width: hero.width } : null,
        evidenceBounds: evidence ? { left: evidence.left, right: evidence.right, width: evidence.width } : null,
        proposedStateHasAriaLabel: proposed?.hasAttribute('aria-label') ?? null,
        proposedStateText: proposed?.textContent.trim() ?? null,
        forcedColorContrasts,
        minimumForcedColorContrast: forcedColorContrasts.length ? Math.min(...forcedColorContrasts.map(item => item.ratio)) : null,
        bodyText: document.body.innerText
      };
    }, { forcedColors: Boolean(check.forcedColors) });
    const cleanConsoleErrors = consoleErrors.filter(message => !(check.assetFailure && /ERR_FAILED|Failed to load resource/i.test(message)));
    await page.addScriptTag({ content: axeSource });
    const audit = await page.evaluate(async ({ forcedColors }) => {
      const options = { runOnly: { type: 'tag', values: ['wcag2a', 'wcag2aa', 'wcag21aa', 'wcag22aa'] } };
      if (forcedColors) options.rules = { 'color-contrast': { enabled: false } };
      const result = await globalThis.axe.run(document, options);
      return {
        colorContrastRule: forcedColors ? 'replaced_by_computed_system_palette_check' : 'axe_enabled',
        violations: result.violations.map(v => ({ id: v.id, impact: v.impact, nodes: v.nodes.length, help: v.help })),
        incomplete: result.incomplete.map(v => ({ id: v.id, impact: v.impact, nodes: v.nodes.length, targets: v.nodes.map(n => n.target.join(' ')) }))
      };
    }, { forcedColors: Boolean(check.forcedColors) });
    const minimumLabel = measurements.specimenVisible
      ? measurements.svgEndpointLabelCssPx
      : Math.min(...measurements.responsiveLabels.map(item => item.fontSizeCssPx));
    results.push({
      ...check,
      violationCount: audit.violations.length,
      colorContrastRule: audit.colorContrastRule,
      violations: audit.violations,
      incomplete: audit.incomplete,
      cleanConsoleErrors,
      pageErrors,
      expectedSvgFailures,
      measurements: {
        clientWidth: measurements.clientWidth,
        scrollWidth: measurements.scrollWidth,
        minimumVisibleEndpointLabelCssPx: Number(minimumLabel.toFixed(2)),
        svgEndpointLabelCssPx: measurements.svgEndpointLabelCssPx === null ? null : Number(measurements.svgEndpointLabelCssPx.toFixed(2)),
        responsiveLabels: measurements.responsiveLabels,
        semanticSeriesOrder: measurements.semanticSeriesOrder,
        responsiveSeriesOrder: measurements.responsiveSeriesOrder,
        actions: measurements.actions,
        applicationBounds: measurements.applicationBounds,
        heroBounds: measurements.heroBounds,
        evidenceBounds: measurements.evidenceBounds,
        proposedStateHasAriaLabel: measurements.proposedStateHasAriaLabel,
        proposedStateText: measurements.proposedStateText,
        forcedColorContrasts: measurements.forcedColorContrasts,
        minimumForcedColorContrast: measurements.minimumForcedColorContrast,
        requiredAssetFailureTextPresent: check.assetFailure ? ['Framework Relay','Context baseline','Dependency map','Decision frame','Evidence depth','Risk view','Open Quick Access example','Review optional immersive principles'].every(value => measurements.bodyText.includes(value)) : null
      }
    });
    await page.close();
  }
} finally {
  await context.close();
  await rm(profile, { recursive: true, force: true });
}

const report = {
  schemaVersion: 3,
  document: 'Hengshi Design D-034 contrast completion browser and accessibility evidence',
  correction: 'D-034 contrast completion',
  date: '2026-07-20',
  toolVersions: { node: process.version, playwright: playwrightVersion, chromium: chromiumVersion, axeCore: axePackage.version },
  scope: 'Wide, 900, 390, 320, text-spacing, forced-colors, grayscale, print, and asset-failure board states; WCAG automated rules plus deterministic system-palette and layout measurements',
  network: 'all non-file and non-data requests aborted',
  externalRequests,
  temporaryProfileRemoved: !existsSync(profile),
  checks: results,
  totalViolations: results.reduce((sum, item) => sum + item.violationCount, 0),
  totalIncomplete: results.reduce((sum, item) => sum + item.incomplete.length, 0),
  totalCleanConsoleErrors: results.reduce((sum, item) => sum + item.cleanConsoleErrors.length, 0),
  totalPageErrors: results.reduce((sum, item) => sum + item.pageErrors.length, 0)
};
await writeFile(path.join(validationDir, 'browser-audit-report.json'), `${JSON.stringify(report, null, 2)}\n`, 'utf8');
process.stdout.write(`${JSON.stringify(report, null, 2)}\n`);

const failed = !report.temporaryProfileRemoved || report.externalRequests.length || report.totalViolations || report.totalIncomplete || report.totalCleanConsoleErrors || report.totalPageErrors || results.some(item => {
  const m = item.measurements;
  return m.scrollWidth !== m.clientWidth || m.minimumVisibleEndpointLabelCssPx < 12 || m.semanticSeriesOrder.join('|') !== m.responsiveSeriesOrder.join('|') || m.actions.map(action => action.name).join('|') !== 'Open Quick Access example|Review optional immersive principles' || m.proposedStateHasAriaLabel !== false || m.proposedStateText !== '■ ┅ Proposed method' || (item.forcedColors && (m.minimumForcedColorContrast === null || m.minimumForcedColorContrast < 21)) || (item.assetFailure && (!m.requiredAssetFailureTextPresent || item.expectedSvgFailures < 1));
});
if (failed) process.exitCode = 1;

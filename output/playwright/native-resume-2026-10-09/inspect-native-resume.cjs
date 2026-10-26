const fs = require('node:fs/promises');
const path = require('node:path');
const { chromium } = require('../../../apps/web/node_modules/playwright');

(async () => {
  const browser = await chromium.launch({ headless: true });
  try {
    const context = await browser.newContext({ viewport: { width: 1440, height: 1000 } });
    const page = await context.newPage();
    const errors = [];
    const requests = [];
    page.on('pageerror', error => errors.push(error.message));
    page.on('response', response => {
      const url = new URL(response.url());
      if (url.hostname === '127.0.0.1' && url.port === '8001') {
        requests.push({ path: url.pathname, status: response.status() });
      }
    });
    await page.goto('http://127.0.0.1:5173/admin/login');
    const credentialFile = path.join(process.env.LOCALAPPDATA,
      'HengshiDesign', 'postgres-walkthrough', 'walkthrough-admin.json');
    const account = JSON.parse(await fs.readFile(credentialFile, 'utf8'));
    await page.getByPlaceholder('Email', { exact: true }).fill(account.email);
    await page.getByPlaceholder('Password', { exact: true }).fill(account.password);
    const serviceResponse = page.waitForResponse(response =>
      new URL(response.url()).pathname === '/api/admin/services' && response.status() === 200,
      { timeout: 20000 });
    await page.getByRole('button', { name: 'Sign in', exact: true }).click();
    await page.waitForURL('**/admin/services', { timeout: 20000 });
    const serviceRows = await (await serviceResponse).json();
    if (!Array.isArray(serviceRows) || !serviceRows.length) throw new Error('Service fixture unavailable');
    await page.getByText(`Total: ${serviceRows.length}`, { exact: true }).waitFor();
    await page.getByText(serviceRows[0].title, { exact: true }).first().waitFor();
    const renderedRows = await page.getByRole('button', { name: 'Edit', exact: true }).count();
    if (renderedRows !== serviceRows.length) throw new Error('Service list did not settle');
    await page.screenshot({ path: path.join(__dirname, 'admin-services-settled.png') });
    console.log(JSON.stringify({ signedIn: true, route: new URL(page.url()).pathname,
      headings: await page.locator('h1').allTextContents(), renderedRows, requests, pageErrors: errors,
      scope: 'Existing native prototype sign-in and service-page reads only; no role enforcement or production readiness certification' }));
    await context.close();
    for (const [name, width, height, section] of [
      ['desktop', 1440, 1000, 'system'], ['narrow', 390, 844, 'journey']
    ]) {
      const definitionContext = await browser.newContext({ viewport: { width, height }, reducedMotion: 'reduce' });
      const definitionPage = await definitionContext.newPage();
      const definitionErrors = [];
      definitionPage.on('pageerror', error => definitionErrors.push(error.name));
      await definitionPage.goto(`http://127.0.0.1:8766/docs/software-definition/definition-walkthrough.html#${section}`);
      await definitionPage.evaluate(async sectionId => {
        await document.fonts.ready;
        document.getElementById(sectionId).scrollIntoView({ behavior: 'instant', block: 'start' });
      }, section);
      const bounds = await definitionPage.locator(`#${section}`).boundingBox();
      const overflow = await definitionPage.evaluate(() => document.documentElement.scrollWidth > innerWidth);
      if (!bounds || bounds.y < -1 || bounds.y >= height || overflow || definitionErrors.length) throw new Error('Definition view unavailable');
      await definitionPage.screenshot({ path: path.join(__dirname, `definition-${name}-settled.png`) });
      console.log(JSON.stringify({ definitionViewport: name, section, horizontalOverflow: overflow, pageErrors: definitionErrors,
        scope: 'Unchanged definition presentation loads at the named section; no WCAG, production UI or feature acceptance' }));
      await definitionContext.close();
    }
  } finally {
    await browser.close();
  }
})().catch(error => {
  console.error(JSON.stringify({ inspectionFailed: true, errorType: error.name,
    credentialsAndErrorDetailsSuppressed: true }));
  process.exitCode = 1;
});


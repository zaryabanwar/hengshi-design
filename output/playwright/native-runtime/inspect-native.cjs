const fs = require('node:fs/promises');
const path = require('node:path');
const { chromium } = require('../../../apps/web/node_modules/playwright');

(async () => {
  const browser = await chromium.launch({ headless: false });
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
    await page.getByRole('button', { name: 'Sign in', exact: true }).click();
    await page.waitForURL('**/admin/services', { timeout: 20000 });
    await page.locator('h1').waitFor();
    await page.screenshot({ path: path.join(__dirname, 'admin-services.png') });
    console.log(JSON.stringify({ signedIn: true, route: new URL(page.url()).pathname,
      headings: await page.locator('h1').allTextContents(), requests, pageErrors: errors,
      scope: 'Existing native prototype sign-in and service-page reads only; no role enforcement or production readiness certification' }));
    await context.close();
  } finally {
    await browser.close();
  }
})().catch(error => {
  console.error(JSON.stringify({ inspectionFailed: true, errorType: error.name,
    credentialsAndErrorDetailsSuppressed: true }));
  process.exitCode = 1;
});

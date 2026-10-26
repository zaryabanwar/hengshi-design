async (page) => {
  const errors = [];
  page.on('pageerror', e => errors.push(e.message));
  await page.reload();
  const directory = 'C:/Users/Zaryab/Documents/Hengshi Design/hengshi-design/output/playwright/definition/';
  const inspect = () => ({
    viewport: innerWidth,
    documentWidth: document.documentElement.scrollWidth,
    overflow: document.documentElement.scrollWidth > innerWidth,
    flowColumns: getComputedStyle(document.querySelector('#staff .flow')).gridTemplateColumns,
    cardColumns: getComputedStyle(document.querySelector('#staff .grid')).gridTemplateColumns,
    imagesReady: [...document.images].every(i => i.complete && i.naturalWidth > 0),
    scripts: document.scripts.length,
    forms: document.forms.length,
    audio: document.querySelectorAll('audio').length,
    brokenLocalFragments: [...document.querySelectorAll('a[href^="#"]')].map(a => a.getAttribute('href')).filter(h => !document.getElementById(h.slice(1)))
  });
  await page.setViewportSize({width: 1440, height: 1000});
  await page.locator('#staff').evaluate(el => el.scrollIntoView({block: 'start', behavior: 'instant'}));
  const desktop = await page.evaluate(inspect);
  await page.screenshot({path: directory + 'staff-flow-desktop.png'});
  const summary = page.locator('#staff summary');
  await summary.focus();
  await page.keyboard.press('Enter');
  await summary.scrollIntoViewIfNeeded();
  const keyboard = await page.evaluate(() => ({
    open: document.querySelector('#staff details').open,
    focusedTag: document.activeElement.tagName,
    outlineStyle: getComputedStyle(document.activeElement).outlineStyle,
    outlineWidth: getComputedStyle(document.activeElement).outlineWidth
  }));
  await page.locator('#staff details').screenshot({path: directory + 'staff-roles-desktop.png'});
  await page.setViewportSize({width: 390, height: 844});
  await page.locator('#staff').evaluate(el => el.scrollIntoView({block: 'start', behavior: 'instant'}));
  const mobile = await page.evaluate(inspect);
  await page.screenshot({path: directory + 'staff-flow-mobile.png'});
  await page.locator('#staff details').screenshot({path: directory + 'staff-roles-mobile.png'});
  await page.setViewportSize({width: 1440, height: 1000});
  await page.locator('#staff').evaluate(el => el.scrollIntoView({block: 'start', behavior: 'instant'}));
  return {desktop, mobile, keyboard, pageErrors: errors, scope: 'Local definition board only; no application consultation or authorization tested'};
}

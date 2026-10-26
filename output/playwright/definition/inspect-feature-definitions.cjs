async (page) => {
  const errors = [];
  page.on('pageerror', error => errors.push(error.message));
  await page.goto('http://127.0.0.1:8766/docs/software-definition/definition-walkthrough.html?inspection=' + Date.now() + '#features');
  const directory = 'C:/Users/Zaryab/Documents/Hengshi Design/hengshi-design/output/playwright/definition/';
  const inspect = () => ({
    viewport: innerWidth,
    documentWidth: document.documentElement.scrollWidth,
    pageOverflow: document.documentElement.scrollWidth > innerWidth,
    imagesReady: [...document.images].every(image => image.complete && image.naturalWidth > 0),
    scripts: document.scripts.length,
    forms: document.forms.length,
    audio: document.querySelectorAll('audio').length,
    brokenFragments: [...document.querySelectorAll('a[href^="#"]')]
      .map(link => link.hash).filter(hash => !document.getElementById(hash.slice(1)))
  });
  await page.setViewportSize({width: 1440, height: 1000});
  await page.locator('#features').evaluate(element => element.scrollIntoView({block: 'start', behavior: 'instant'}));
  const desktop = await page.evaluate(inspect);
  await page.locator('#features').screenshot({path: directory + 'feature-definitions-desktop.png'});
  const summary = page.locator('#features summary');
  await summary.focus();
  await page.keyboard.press('Enter');
  const keyboard = await summary.evaluate(element => ({
    focused: document.activeElement === element,
    expanded: element.parentElement.open,
    outlineStyle: getComputedStyle(element).outlineStyle,
    outlineWidth: getComputedStyle(element).outlineWidth
  }));
  await page.keyboard.press('Enter');
  const links = [];
  for (const link of await page.locator('#features a').all()) {
    const target = await link.evaluate(element => element.href);
    const response = await page.request.get(target);
    links.push({name: await link.textContent(), status: response.status()});
  }
  await page.setViewportSize({width: 390, height: 844});
  await summary.evaluate(element => element.blur());
  await page.locator('#features').evaluate(element => element.scrollIntoView({block: 'start', behavior: 'instant'}));
  const mobile = await page.evaluate(inspect);
  await page.screenshot({path: directory + 'feature-definitions-mobile.png'});
  await page.locator('#features .callout').evaluate(element => element.scrollIntoView({block: 'center', behavior: 'instant'}));
  await page.screenshot({path: directory + 'feature-definitions-mobile-ownership.png'});
  await page.setViewportSize({width: 1440, height: 1000});
  await page.locator('#features').evaluate(element => element.scrollIntoView({block: 'start', behavior: 'instant'}));
  return {desktop, mobile, keyboard, links, pageErrors: errors,
    scope: 'Definition presentation, disclosure interaction and local links only; no application, performance benchmark or full accessibility conformance tested'};
}

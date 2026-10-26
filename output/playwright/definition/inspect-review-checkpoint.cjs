async (page) => {
  const errors = [];
  page.on('pageerror', error => errors.push(error.message));
  await page.reload();
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
  await page.locator('#checkpoint').evaluate(element => element.scrollIntoView({block: 'start', behavior: 'instant'}));
  const desktop = await page.evaluate(inspect);
  await page.locator('#checkpoint').screenshot({path: directory + 'review-checkpoint-desktop.png'});
  await page.setViewportSize({width: 390, height: 844});
  await page.locator('#checkpoint').evaluate(element => element.scrollIntoView({block: 'start', behavior: 'instant'}));
  const mobile = await page.evaluate(inspect);
  const region = page.getByRole('region', {name: 'Review checkpoint table'});
  await region.focus();
  const before = await region.evaluate(element => element.scrollLeft);
  await page.keyboard.press('ArrowRight');
  await page.waitForTimeout(200);
  const keyboard = await region.evaluate((element, previous) => ({
    focused: document.activeElement === element,
    outlineStyle: getComputedStyle(element).outlineStyle,
    outlineWidth: getComputedStyle(element).outlineWidth,
    scrollBefore: previous,
    scrollAfter: element.scrollLeft,
    clientWidth: element.clientWidth,
    scrollWidth: element.scrollWidth
  }), before);
  await page.screenshot({path: directory + 'review-checkpoint-mobile-keyboard.png'});
  await region.evaluate(element => { element.scrollLeft = 0; });
  await page.locator('#checkpoint').evaluate(element => element.scrollIntoView({block: 'start', behavior: 'instant'}));
  await page.screenshot({path: directory + 'review-checkpoint-mobile.png'});
  const links = [];
  for (const name of ['independent amendment review', 'native operating instructions']) {
    const target = await page.getByRole('link', {name, exact: true}).evaluate(element => element.href);
    const response = await page.request.get(target);
    links.push({name, status: response.status()});
  }
  await page.setViewportSize({width: 1440, height: 1000});
  await page.locator('#checkpoint').evaluate(element => element.scrollIntoView({block: 'start', behavior: 'instant'}));
  return {desktop, mobile, keyboard, links, pageErrors: errors,
    scope: 'Definition presentation and local links only; no application, database or full accessibility conformance tested'};
}

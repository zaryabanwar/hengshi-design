async (page) => {
  const errors = [];
  page.on('pageerror', error => errors.push(error.message));
  await page.goto('http://127.0.0.1:8766/docs/software-definition/definition-walkthrough.html?compatibility=' + Date.now() + '#checkpoint');
  const directory = 'C:/Users/Zaryab/Documents/Hengshi Design/hengshi-design/output/playwright/definition/';
  const inspect = () => ({
    viewport: innerWidth,
    documentWidth: document.documentElement.scrollWidth,
    pageOverflow: document.documentElement.scrollWidth > innerWidth,
    imagesReady: [...document.images].every(image => image.complete && image.naturalWidth > 0)
  });
  await page.setViewportSize({width: 1440, height: 1000});
  await page.locator('#checkpoint').evaluate(element => element.scrollIntoView({block: 'start', behavior: 'instant'}));
  const desktop = await page.evaluate(inspect);
  await page.locator('#checkpoint').screenshot({path: directory + 'compatibility-checkpoint-desktop.png'});
  const links = [];
  for (const name of ['Backend resolution and source review', 'Dependency notice evidence review']) {
    const link = page.getByRole('link', {name, exact: true});
    const target = await link.evaluate(element => element.href);
    const response = await page.request.get(target);
    links.push({name, status: response.status()});
    await link.focus();
    links[links.length - 1].focused = await link.evaluate(element => document.activeElement === element);
  }
  await page.setViewportSize({width: 390, height: 844});
  await page.locator('#checkpoint').evaluate(element => element.scrollIntoView({block: 'start', behavior: 'instant'}));
  const mobile = await page.evaluate(inspect);
  await page.screenshot({path: directory + 'compatibility-checkpoint-mobile.png'});
  const table = page.getByRole('region', {name: 'Review checkpoint table'});
  await table.focus();
  await table.evaluate(element => {element.scrollLeft = element.scrollWidth;});
  const scroll = await table.evaluate(element => ({
    focused: document.activeElement === element,
    clientWidth: element.clientWidth,
    scrollWidth: element.scrollWidth,
    scrollLeft: element.scrollLeft
  }));
  await page.screenshot({path: directory + 'compatibility-checkpoint-mobile-columns.png'});
  await page.setViewportSize({width: 1440, height: 1000});
  await table.evaluate(element => {element.scrollLeft = 0; element.blur();});
  await page.locator('#checkpoint').evaluate(element => element.scrollIntoView({block: 'start', behavior: 'instant'}));
  return {desktop, mobile, scroll, links, pageErrors: errors,
    scope: 'Local definition presentation, focus, table scrolling and review links only; not application compatibility, physical-phone or accessibility conformance proof'};
}

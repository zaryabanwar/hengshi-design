async (page) => {
  const errors = [];
  page.on('pageerror', e => errors.push(e.message));
  await page.goto('http://127.0.0.1:8766/docs/software-definition/definition-walkthrough.html?review=qa-correction-20261006');
  const output = 'C:/Users/Zaryab/Documents/Hengshi Design/hengshi-design/output/playwright/qa-review-reference-2026-10-06/';
  await page.setViewportSize({width:1440,height:1000});
  await page.locator('nav a[href="#features"]').focus();
  await page.keyboard.press('Enter');
  await page.locator('#features').evaluate(e => e.scrollIntoView({block:'start',behavior:'instant'}));
  const desktop = await page.evaluate(() => ({fragment:location.hash,
    overflow:document.documentElement.scrollWidth > innerWidth,
    focused:document.activeElement.getAttribute('href'),
    cards:document.querySelectorAll('#features article').length,
    interactiveControls:document.querySelectorAll('#features button,#features input,#features form,#features canvas').length}));
  await page.locator('#features').screenshot({path:output+'desktop.png'});
  await page.setViewportSize({width:390,height:844});
  const mobile = await page.evaluate(() => ({overflow:document.documentElement.scrollWidth > innerWidth}));
  await page.locator('#features').screenshot({path:output+'mobile.png'});
  const links=[];
  for (const url of await page.locator('#features a').evaluateAll(es => es.map(e=>e.href))) {
    const response = await page.request.get(url.split('#')[0]);
    links.push({url,status:response.status()});
  }
  return {scope:'Static QA status/reference correction only; producer browser evidence, not accessibility or physical-phone qualification.',
    desktop,mobile,links,pageErrors:errors,
    pass:desktop.fragment==='#features' && !desktop.overflow && !mobile.overflow && desktop.cards===4
      && desktop.interactiveControls===0 && links.every(e=>e.status===200) && errors.length===0};
}

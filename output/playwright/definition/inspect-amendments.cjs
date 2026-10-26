async (page) => {
  const faults = [];
  page.on('pageerror', e => faults.push(e.message));
  page.on('console', m => { if (m.type() === 'error') faults.push(m.text()); });
  const views = [];
  for (const [name, width, height] of [['desktop',1440,1000],['mobile',390,844]]) {
    await page.setViewportSize({width,height});
    await page.goto('http://127.0.0.1:8766/docs/software-definition/definition-walkthrough.html#system');
    await page.getByText('Market, company details and contact channels', {exact:true}).click();
    await page.getByText('Technology and deferred hosting decisions', {exact:true}).click();
    const dimensions = await page.evaluate(() => ({width:innerWidth, scroll:document.documentElement.scrollWidth, images:[...document.images].map(i => ({loaded:i.complete && i.naturalWidth>0, src:i.getAttribute('src')}))}));
    if (dimensions.scroll > width || dimensions.images.some(i => !i.loaded)) throw new Error(JSON.stringify(dimensions));
    await page.screenshot({path:'output/playwright/definition/amendments-'+name+'.png',fullPage:true});
    views.push({name,dimensions,title:await page.title()});
  }
  await page.setViewportSize({width:1440,height:1000});
  await page.goto('http://127.0.0.1:8766/docs/software-definition/definition-walkthrough.html#system');
  console.log(JSON.stringify({views,faults}));
  if (faults.length) throw new Error(faults.join('; '));
}

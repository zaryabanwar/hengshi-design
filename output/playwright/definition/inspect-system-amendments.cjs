async (page) => {
  const results = [];
  for (const [name, width, height] of [['desktop',1440,1000],['mobile',390,844]]) {
    await page.setViewportSize({width,height});
    await page.goto('http://127.0.0.1:8766/docs/software-definition/definition-walkthrough.html#system');
    await page.reload();
    await page.getByText('Market, company details and contact channels', {exact:true}).click();
    await page.getByText('Technology and deferred hosting decisions', {exact:true}).click();
    await page.locator('#system').screenshot({path:'output/playwright/definition/amendments-system-'+name+'.png'});
    results.push(await page.evaluate(() => ({width:innerWidth, scroll:document.documentElement.scrollWidth, open:[...document.querySelectorAll('#system details[open] summary')].map(s=>s.textContent)})));
  }
  await page.setViewportSize({width:1440,height:1000});
  await page.reload();
  return results;
}

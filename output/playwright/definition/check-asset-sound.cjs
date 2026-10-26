async (page) => {
  const errors = [];
  page.on('pageerror', e => errors.push(String(e)));
  page.on('console', m => { if (m.type() === 'error') errors.push(m.text()); });
  await page.setViewportSize({width:1440,height:1000});
  await page.goto('http://127.0.0.1:8766/docs/phase-1-3d/spatial-storyboard.html#asset-kit');
  await page.reload();
  await page.locator('#asset-kit').screenshot({path:'output/playwright/definition/asset-kit-desktop.png'});
  await page.locator('#sound-zones').screenshot({path:'output/playwright/definition/sound-zones-desktop.png'});
  const desktop = await page.evaluate(() => ({overflow:document.documentElement.scrollWidth>innerWidth, assetCards:document.querySelectorAll('#asset-kit .card').length,soundCards:document.querySelectorAll('#sound-zones .card').length}));
  await page.setViewportSize({width:390,height:844});
  await page.reload();
  await page.locator('#asset-kit').screenshot({path:'output/playwright/definition/asset-kit-mobile.png'});
  await page.locator('#sound-zones').screenshot({path:'output/playwright/definition/sound-zones-mobile.png'});
  const mobile = await page.evaluate(() => ({overflow:document.documentElement.scrollWidth>innerWidth, assetsColumns:getComputedStyle(document.querySelector('#asset-kit .grid')).gridTemplateColumns, soundColumns:getComputedStyle(document.querySelector('#sound-zones .grid')).gridTemplateColumns, imagesReady:[...document.images].every(i=>i.complete&&i.naturalWidth>0), externalAssets:[...document.querySelectorAll('script[src],link[href],audio[src],img[src]')].map(e=>e.src||e.href).filter(u=>u.startsWith('http')&&!u.startsWith(location.origin))}));
  await page.locator('#asset-kit a').focus();
  const focus = await page.evaluate(() => ({text:document.activeElement.textContent,outline:getComputedStyle(document.activeElement).outlineStyle}));
  await page.setViewportSize({width:1440,height:1000});
  await page.locator('#asset-kit').scrollIntoViewIfNeeded();
  console.log(JSON.stringify({desktop,mobile,focus,errors}));
}


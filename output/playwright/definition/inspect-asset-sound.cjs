async (page) => {
  const inspect = () => ({width:innerWidth,overflow:document.documentElement.scrollWidth>innerWidth,assetCards:document.querySelectorAll('#asset-kit .card').length,soundCards:document.querySelectorAll('#sound-zones .card').length,columns:getComputedStyle(document.querySelector('#asset-kit .grid')).gridTemplateColumns,imagesReady:[...document.images].every(i=>i.complete&&i.naturalWidth>0),scripts:document.scripts.length,audio:document.querySelectorAll('audio').length});
  await page.setViewportSize({width:1440,height:1000});
  const desktop=await page.evaluate(inspect);
  await page.setViewportSize({width:390,height:844});
  const mobile=await page.evaluate(inspect);
  await page.locator('#asset-kit a').focus();
  const focus=await page.evaluate(()=>({text:document.activeElement.textContent,outline:getComputedStyle(document.activeElement).outlineStyle}));
  await page.setViewportSize({width:1440,height:1000});
  await page.locator('#asset-kit').scrollIntoViewIfNeeded();
  return {desktop,mobile,focus};
}

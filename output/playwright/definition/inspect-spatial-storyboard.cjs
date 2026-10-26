async (page) => {
  const errors=[];const results=[];
  page.on('pageerror',e=>errors.push(e.message));
  page.on('console',m=>{if(m.type()==='error')errors.push(m.text())});
  for(const [name,width,height] of [['desktop',1440,1000],['mobile',390,844]]){
    await page.setViewportSize({width,height});
    await page.goto('http://127.0.0.1:8766/docs/phase-1-3d/spatial-storyboard.html');
    await page.waitForFunction(()=>[...document.images].every(i=>i.complete&&i.naturalWidth>0));
    const layout=await page.evaluate(()=>({viewport:innerWidth,pageWidth:document.documentElement.scrollWidth,images:document.images.length,diagram:document.querySelector('svg').getAttribute('viewBox')}));
    if(layout.pageWidth>width)throw new Error('Page overflow '+JSON.stringify(layout));
    await page.screenshot({path:'output/playwright/definition/spatial-storyboard-'+name+'.png',fullPage:true});
    await page.locator('.plan').screenshot({path:'output/playwright/definition/spatial-plan-'+name+'.png'});
    results.push({name,layout});
  }
  await page.setViewportSize({width:1440,height:1000});
  return {results,errors};
}

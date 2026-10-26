async (page) => {
  const errors=[];
  page.on('pageerror',error=>errors.push(error.message));
  const observations=[];
  for(const [path,section] of [
    ['docs/phase-1-3d/spatial-storyboard.html','#layout-study'],
    ['docs/software-definition/definition-walkthrough.html','#campus']
  ]) {
    await page.setViewportSize({width:1440,height:960});
    await page.goto('http://127.0.0.1:8766/'+path+section);
    await page.locator(section).scrollIntoViewIfNeeded();
    const images=await page.locator(section+' img').evaluateAll(items=>items.map(image=>({loaded:image.complete&&image.naturalWidth>0,source:image.getAttribute('src')})));
    const modelLink=page.locator(section+' a[href="../../artifacts/nature-campus-layout-study/index.html"]');
    observations.push({path,desktop:{images,modelLink:await modelLink.first().getAttribute('href')},visibleText:await page.locator(section).innerText()});
    if(images.some(image=>!image.loaded))throw new Error('Unloaded section image: '+path);
    await page.setViewportSize({width:390,height:844});
    await page.locator(section).scrollIntoViewIfNeeded();
    const overflow=await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth);
    if(overflow)throw new Error('Viewport overflow: '+path);
    await modelLink.first().focus();
    await page.keyboard.press('Enter');
    await page.waitForURL('**/artifacts/nature-campus-layout-study/index.html');
    observations[observations.length-1].mobile={overflow,modelNavigation:page.url()};
  }
  if(errors.length)throw new Error(JSON.stringify(errors));
  return {observations,errors};
}

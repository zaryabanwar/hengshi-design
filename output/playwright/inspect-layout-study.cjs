async (page) => {
  const base='http://127.0.0.1:8766/artifacts/nature-campus-layout-study/index.html';
  const errors=[];
  page.on('pageerror',e=>errors.push(e.message));
  page.on('console',m=>{if(m.type()==='error')errors.push(m.text())});
  await page.setViewportSize({width:1440,height:960});
  await page.goto(base);
  await page.waitForFunction(()=>window.prototypeLoaded===true);
  const results=[];
  for(const view of ['Overview','Arrival','Department']){
    const button=page.getByRole('button',{name:view,exact:true});
    await button.click();
    if(await button.getAttribute('aria-pressed')!=='true')throw new Error('Camera state failed '+view);
    await page.screenshot({path:'output/playwright/layout-study-'+view.toLowerCase()+'-2026-10-04.png'});
    results.push({view,selected:true});
  }
  await page.setViewportSize({width:390,height:844});
  await page.getByRole('button',{name:'Arrival',exact:true}).click();
  const overflow=await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth);
  if(overflow)throw new Error('Horizontal viewport overflow');
  await page.getByRole('button',{name:'Department',exact:true}).focus();
  await page.keyboard.press('Enter');
  if(await page.getByRole('button',{name:'Department',exact:true}).getAttribute('aria-pressed')!=='true')throw new Error('Keyboard camera activation failed');
  await page.screenshot({path:'output/playwright/layout-study-mobile-2026-10-04.png'});
  const rendered=await page.evaluate(()=>window.layoutInspection);
  const browser=page.context().browser();
  const plain=await browser.newContext({javaScriptEnabled:false,viewport:{width:390,height:844}});
  const plainPage=await plain.newPage();await plainPage.goto(base);
  const renders=await plainPage.locator('#fallback img').evaluateAll(imgs=>imgs.map(i=>({src:i.getAttribute('src'),loaded:i.complete&&i.naturalWidth>0})));
  if(renders.length!==3||renders.some(i=>!i.loaded))throw new Error('No-script render alternatives failed');
  await plain.close();
  await page.setViewportSize({width:1440,height:960});
  await page.getByRole('button',{name:'Overview',exact:true}).click();
  if(errors.length)throw new Error(JSON.stringify(errors));
  console.log(JSON.stringify({rendered,desktopCameras:results,mobileViewport:{width:390,height:844,overflow:false,keyboardActivation:true},noScriptRenders:renders,errors},null,2));
}

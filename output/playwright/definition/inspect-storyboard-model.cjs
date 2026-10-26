async (page) => {
  const errors=[];
  page.on('pageerror', e=>errors.push(e.message));
  await page.setViewportSize({width:1440,height:1000});
  await page.reload();
  await page.waitForFunction(()=>window.prototypeLoaded===true,{timeout:30000});
  for (const [view, label] of [['overview','Campus overview'],['arrival','Arrival'],['department','Department']]) {
    await page.getByRole('button',{name:label,exact:true}).click();
    await page.screenshot({path:'output/playwright/definition/storyboard-'+view+'.png'});
  }
  if(errors.length) throw new Error(errors.join('; '));
  return {title:await page.title(),loaded:await page.evaluate(()=>window.prototypeLoaded===true),errors,viewControls:await page.getByRole('button').count()};
}

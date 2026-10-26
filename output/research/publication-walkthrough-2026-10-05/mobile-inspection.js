async (page) => {
  await page.emulateMedia({reducedMotion:'reduce'});
  const section=page.locator('#publication-flow');
  await section.evaluate(el=>el.scrollIntoView({block:'start',behavior:'instant'}));
  await page.evaluate(()=>new Promise(resolve=>requestAnimationFrame(()=>requestAnimationFrame(resolve))));
  const mobile=await section.evaluate(el=>({open:el.open,viewport:innerWidth,documentWidth:document.documentElement.scrollWidth,scrollY,
    grid:getComputedStyle(el.querySelector('.flow')).gridTemplateColumns,
    bounds:(()=>{const b=el.getBoundingClientRect();return {x:b.x,y:b.y,width:b.width,height:b.height};})(),
    cardBounds:[...el.querySelectorAll('.flow li')].map(x=>{const b=x.getBoundingClientRect();return {x:b.x,y:b.y,width:b.width,height:b.height};})
  }));
  await section.screenshot({path:'output/playwright/definition-consolidation/publication-flow-mobile-2026-10-05.png',animations:'disabled'});
  return {mobile,capturePreference:'reduced motion; viewport emulation, not a physical phone'};
}

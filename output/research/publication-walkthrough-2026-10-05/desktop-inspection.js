async (page) => {
  const section = page.locator('#publication-flow');
  await section.evaluate(el=>el.scrollIntoView({block:"start",behavior:"instant"}));
  const desktop = await section.evaluate(el => ({
    open: el.open, viewport: innerWidth, documentWidth: document.documentElement.scrollWidth,
    grid: getComputedStyle(el.querySelector('.flow')).gridTemplateColumns,
    cardBounds: [...el.querySelectorAll('.flow li')].map(x => { const b=x.getBoundingClientRect();return {x:b.x,y:b.y,width:b.width,height:b.height}; }),
    sectionBounds: (() => {const b=el.getBoundingClientRect();return {width:b.width,height:b.height};})(),
    links: [...el.querySelectorAll('a')].map(x=>x.href)
  }));
  const links=[];
  for (const url of desktop.links) { const response=await page.request.get(url.split('#')[0]);links.push({url,status:response.status()}); }
  await section.screenshot({path:'output/playwright/definition-consolidation/publication-flow-desktop-2026-10-05.png'});
  return {desktop,links};
}



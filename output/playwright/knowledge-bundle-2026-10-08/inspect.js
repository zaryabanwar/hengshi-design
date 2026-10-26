async (page) => {
  const section = page.locator('#ai-grounding');
  const width = page.viewportSize().width;
  await section.scrollIntoViewIfNeeded();
  const summary = section.locator('summary');
  await summary.focus();
  await page.keyboard.press('Space');
  const closedByKeyboard = await section.evaluate(el => !el.open);
  await page.keyboard.press('Enter');
  const openedByKeyboard = await section.evaluate(el => el.open);
  const focusedOutline = await summary.evaluate(el => ({
    active: document.activeElement === el,
    style: getComputedStyle(el).outlineStyle,
    width: getComputedStyle(el).outlineWidth
  }));
  await page.keyboard.press('Tab');
  const firstLinkReached = await section.locator('.source-links a').first().evaluate(el => document.activeElement === el);
  await section.evaluate(el => el.scrollIntoView({block:'start',behavior:'instant'}));
  const layout = await section.evaluate(el => ({
    viewport: innerWidth,
    documentWidth: document.documentElement.scrollWidth,
    flowColumns: getComputedStyle(el.querySelector('.flow')).gridTemplateColumns,
    cardColumns: getComputedStyle(el.querySelector('.grid')).gridTemplateColumns,
    bounds: [...el.querySelectorAll('.flow li,.card')].map(x => {
      const b=x.getBoundingClientRect();
      return {x:b.x,width:b.width,right:b.right,height:b.height};
    }),
    height: el.getBoundingClientRect().height,
    links: [...el.querySelectorAll('.source-links a')].map(x=>x.href)
  }));
  const links=[];
  for (const url of layout.links) {
    const response=await page.request.get(url.split('#')[0]);
    links.push({url,status:response.status()});
  }
  if (!closedByKeyboard || !openedByKeyboard || !firstLinkReached) throw new Error('Native disclosure/source-link keyboard inspection failed');
  if (layout.documentWidth > width || layout.bounds.some(b=>b.x<0 || b.right>width)) throw new Error('Page/section horizontal overflow');
  if (links.some(link=>link.status!==200)) throw new Error('Source response unavailable');
  const screenshot='output/playwright/knowledge-bundle-2026-10-08/knowledge-'+width+'.png';
  await section.screenshot({path:screenshot});
  return {layout,links,closedByKeyboard,openedByKeyboard,firstLinkReached,focusedOutline,screenshot,
    limits:'Static documentation inspection only; no production UI, legal compliance, full accessibility, phone hardware or data-processing runtime proof'};
}

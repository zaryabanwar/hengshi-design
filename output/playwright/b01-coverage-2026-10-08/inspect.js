async (page) => {
 const width=page.viewportSize().width;
 const row=page.getByRole('row').filter({has:page.getByRole('rowheader',{name:'Production UI references',exact:true})});
 const panel=page.getByRole('region',{name:'Review checkpoint table',exact:true});
 await row.scrollIntoViewIfNeeded();
 const links=await row.getByRole('link').evaluateAll(ns=>ns.map(n=>({label:n.textContent,url:n.href})));
 const statuses=[];
 for(const link of links){const r=await page.request.get(link.url);statuses.push({...link,status:r.status()});}
 const layout=await panel.evaluate(el=>({width:el.clientWidth,scrollWidth:el.scrollWidth,tabindex:el.tabIndex,role:el.getAttribute('role'),label:el.getAttribute('aria-label')}));
 const documentWidth=await page.evaluate(()=>document.documentElement.scrollWidth);
 await row.screenshot({path:'output/playwright/b01-coverage-2026-10-08/row-'+width+'.png'});
 let keyboardScroll=null;
 if(width===320){await panel.focus();const before=await panel.evaluate(e=>e.scrollLeft);for(let i=0;i<20;i++) await page.keyboard.press('ArrowRight');await page.waitForTimeout(300);const after=await panel.evaluate(e=>e.scrollLeft);keyboardScroll={before,after};await row.screenshot({path:'output/playwright/b01-coverage-2026-10-08/row-'+width+'-end.png'});}
 return {width,documentWidth,layout,statuses,keyboardScroll};
}
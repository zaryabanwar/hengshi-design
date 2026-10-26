async (page) => {
 const width=page.viewportSize().width;const results=[];
 for(const name of ['Human consultation messages','Publication, privacy, recovery']){
  const row=page.getByRole('row').filter({has:page.getByRole('rowheader',{name,exact:true})});
  await row.scrollIntoViewIfNeeded();
  const links=await row.getByRole('link').evaluateAll(ns=>ns.map(n=>({label:n.textContent,url:n.href})));
  const statuses=[];for(const link of links){const response=await page.request.get(link.url);statuses.push({...link,status:response.status()});}
  await row.screenshot({path:'output/playwright/checkpoint-privacy-2026-10-08/'+(name.startsWith('Human')?'timing':'privacy')+'-'+width+'.png'});
  results.push({name,statuses});
 }
 const panel=page.getByRole('region',{name:'Review checkpoint table',exact:true});
 const layout=await panel.evaluate(e=>({width:e.clientWidth,scrollWidth:e.scrollWidth,tabindex:e.tabIndex}));
 const documentWidth=await page.evaluate(()=>document.documentElement.scrollWidth);
 return {width,documentWidth,layout,results,scope:'Static documentation rows and source links only; no production enforcement or accessibility certification'};
}
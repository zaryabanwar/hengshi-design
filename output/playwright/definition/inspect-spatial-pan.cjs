async (page) => {
 await page.setViewportSize({width:390,height:844});
 await page.reload();
 const plan=page.locator('.plan');await plan.focus();
 const before=await plan.evaluate(e=>e.scrollLeft);
 await page.keyboard.press('ArrowRight');
 await page.waitForFunction(()=>document.querySelector('.plan').scrollLeft>0);
 const after=await plan.evaluate(e=>e.scrollLeft);
 await plan.evaluate(e=>e.scrollLeft=e.scrollWidth-e.clientWidth);
 await plan.screenshot({path:'output/playwright/definition/spatial-plan-mobile-right.png'});
 await page.setViewportSize({width:1440,height:1000});
 await plan.screenshot({path:'output/playwright/definition/spatial-plan-desktop.png'});
 return {before,after,pageWidth:await page.evaluate(()=>document.documentElement.scrollWidth),viewport:1440};
}

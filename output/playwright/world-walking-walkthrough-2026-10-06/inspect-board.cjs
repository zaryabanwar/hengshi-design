async (page) => {
  const errors = [], external = [];
  page.on('pageerror', e => errors.push(e.message));
  page.on('request', r => { if (!r.url().startsWith('http://127.0.0.1:8766/') && !r.url().startsWith('data:')) external.push(r.url()); });
  await page.reload();
  const out = 'C:/Users/Zaryab/Documents/Hengshi Design/hengshi-design/output/playwright/world-walking-walkthrough-2026-10-06/';
  const inspect = () => ({
    viewport: innerWidth, documentWidth: document.documentElement.scrollWidth,
    overflow: document.documentElement.scrollWidth > innerWidth,
    controlColumns: getComputedStyle(document.querySelector('#walking-controls')).gridTemplateColumns,
    loadingColumns: getComputedStyle(document.querySelector('#walking-loading')).gridTemplateColumns,
    scripts: document.scripts.length, forms: document.forms.length,
    runtimeControls: document.querySelector('#walking').querySelectorAll('button,input,canvas,audio').length,
    duplicateIds: [...document.querySelectorAll('[id]')].map(e=>e.id).filter((id,i,all)=>all.indexOf(id)!==i),
    brokenLocalFragments: [...document.querySelectorAll('a[href^="#"]')].map(a=>a.getAttribute('href')).filter(h=>!document.getElementById(h.slice(1))),
    figureName: document.getElementById('walking-diagram-title').textContent,
    figureDescription: document.getElementById('walking-diagram-desc').textContent,
    userAgent: navigator.userAgent
  });
  await page.setViewportSize({width:1440,height:1000});
  await page.locator('nav a[href="#walking"]').focus();
  await page.keyboard.press('Enter');
  await page.locator('#walking').evaluate(e=>e.scrollIntoView({block:'start',behavior:'instant'}));
  const navigation = await page.evaluate(()=>({fragment:location.hash, heading:document.querySelector('#walking h2').textContent}));
  const summary = page.locator('#walking-targets summary');
  await summary.focus(); await page.keyboard.press('Enter');
  const keyboard = await page.evaluate(()=>({open:document.getElementById('walking-targets').open,focused:document.activeElement.tagName,outline:getComputedStyle(document.activeElement).outlineStyle,outlineWidth:getComputedStyle(document.activeElement).outlineWidth}));
  const desktop = await page.evaluate(inspect);
  await page.locator('#walking').screenshot({path:out+'desktop-complete.png'});
  await page.setViewportSize({width:390,height:844});
  const mobile = await page.evaluate(inspect);
  await page.locator('#walking').screenshot({path:out+'mobile-complete.png'});
  await page.setViewportSize({width:320,height:700});
  const narrow = await page.evaluate(inspect);
  await summary.focus(); await page.keyboard.press('Enter');
  const closed = await page.locator('#walking-targets').evaluate(e=>!e.open);
  const links=[];
  for (const href of await page.locator('#walking .source-links a').evaluateAll(es=>es.map(e=>e.href))) {
    const response = await page.request.get(href.split('#')[0]);
    links.push({url:href,status:response.status()});
  }
  const ok = [desktop,mobile,narrow].every(o=>!o.overflow && !o.scripts && !o.forms && !o.runtimeControls && !o.duplicateIds.length && !o.brokenLocalFragments.length)
    && keyboard.open && keyboard.focused==='SUMMARY' && keyboard.outline==='solid' && parseFloat(keyboard.outlineWidth)>0
    && closed && navigation.fragment==='#walking' && links.every(l=>l.status===200) && !errors.length && !external.length;
  return {scope:'Static definition board only; desktop browser with resized viewports, not physical touch/mobile or World runtime evidence.',desktop,mobile,narrow,navigation,keyboard,keyboardCloses:closed,links,pageErrors:errors,externalRequests:external,pass:ok};
}

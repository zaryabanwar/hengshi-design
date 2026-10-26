async (page) => {
  const anchor = page.locator('#walking .source-links a').first();
  const href = await anchor.getAttribute('href');
  const name = await anchor.innerText();
  const url = await anchor.evaluate(a=>a.href);
  const response = await page.request.get(url);
  return {scope:'Focused changed static source-link check only; previous layout/keyboard/pixel checks are unchanged initial evidence.',href,name,url,status:response.status(),pass:href==='../phase-1-3d/WORLD_EXPERIENCE.md' && response.status()===200};
}

async (page) => {
  await page.emulateMedia({ reducedMotion: 'reduce' });
  await page.setViewportSize({ width: 1440, height: 1100 });
  await page.reload();
  const panel = page.locator('#booking-email');
  const summary = panel.locator('summary');
  await summary.focus();
  await page.keyboard.press('Enter');
  const openedByKeyboard = await panel.evaluate(el => el.open);
  if (!openedByKeyboard) throw new Error('Keyboard did not open native details');
  await panel.screenshot({ path: 'C:/Users/Zaryab/Documents/Hengshi Design/hengshi-design/output/research/booking-email-ownership-2026-10-08/desktop.png', animations: 'disabled' });
  const measure = async () => page.evaluate(() => {
    const panel = document.getElementById('booking-email');
    const r = panel.getBoundingClientRect();
    return { viewport: innerWidth, pageWidth: document.documentElement.scrollWidth,
      panelWidth: r.width, panelHeight: r.height, panelScrollWidth: panel.scrollWidth,
      panelClientWidth: panel.clientWidth, linkCount: panel.querySelectorAll('a').length };
  });
  const desktop = await measure();
  await page.setViewportSize({ width: 320, height: 900 });
  await panel.screenshot({ path: 'C:/Users/Zaryab/Documents/Hengshi Design/hengshi-design/output/research/booking-email-ownership-2026-10-08/narrow320.png', animations: 'disabled' });
  const narrow = await measure();
  await summary.focus();
  await page.keyboard.press('Enter');
  const closedByKeyboard = !(await panel.evaluate(el => el.open));
  await page.keyboard.press('Enter');
  await page.keyboard.press('Tab');
  const tabTarget = await page.evaluate(() => ({ tag: document.activeElement.tagName,
    text: document.activeElement.textContent, inPanel: document.getElementById('booking-email').contains(document.activeElement) }));
  console.log(JSON.stringify({ scope: 'Documentation presentation only, no email/booking functionality or whole-process accessibility proof',
    openedByKeyboard, closedByKeyboard, desktop, narrow, tabTarget }));
}

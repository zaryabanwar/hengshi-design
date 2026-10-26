async (page) => {
  const panel = page.locator('#booking-email');
  await panel.locator('ol.flow').screenshot({ path: 'C:/Users/Zaryab/Documents/Hengshi Design/hengshi-design/output/research/booking-email-ownership-2026-10-08/narrow-flow.png', animations: 'disabled' });
  await panel.locator('.grid').screenshot({ path: 'C:/Users/Zaryab/Documents/Hengshi Design/hengshi-design/output/research/booking-email-ownership-2026-10-08/narrow-recovery.png', animations: 'disabled' });
  await panel.locator('.small').screenshot({ path: 'C:/Users/Zaryab/Documents/Hengshi Design/hengshi-design/output/research/booking-email-ownership-2026-10-08/narrow-limits.png', animations: 'disabled' });
}

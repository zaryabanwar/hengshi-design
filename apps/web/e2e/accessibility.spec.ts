import AxeBuilder from '@axe-core/playwright'
import { expect, test, type Page } from '@playwright/test'

async function expectNoA11yViolations(page: Page) {
  const results = await new AxeBuilder({ page }).analyze()
  expect(results.violations).toEqual([])
}

test('homepage has no automated axe violations', async ({ page }) => {
  await page.goto('/')

  await expect(page.getByRole('heading', { name: 'Hengshi Design' })).toBeVisible()
  await expectNoA11yViolations(page)
})

test('admin login has no automated axe violations', async ({ page }) => {
  await page.goto('/admin/login')

  await expect(page.getByRole('heading', { name: 'Login' })).toBeVisible()
  await expectNoA11yViolations(page)
})

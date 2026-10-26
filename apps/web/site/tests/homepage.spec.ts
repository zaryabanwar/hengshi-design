import AxeBuilder from '@axe-core/playwright'
import { expect, test } from '@playwright/test'
import { readFile } from 'node:fs/promises'
import { fileURLToPath } from 'node:url'

const screenshots = fileURLToPath(new URL('../../../../artifacts/hsd-001/local-implementation/', import.meta.url))
const headline = 'From complex ambition to accountable delivery.'

test('initial HTML and no-JavaScript mobile provide the complete core journey', async ({ browser, request }) => {
  const response = await request.get('/')
  expect(response.status()).toBe(200)
  const html = await response.text()
  expect(html).toContain('<h1 id="home-heading">' + headline + '</h1>')
  expect(html).not.toContain('<!--site-html-->')
  const context = await browser.newContext({ javaScriptEnabled: false, viewport: { width: 320, height: 800 } })
  const page = await context.newPage()
  await page.goto('/')
  await expect(page.getByRole('heading', { level: 1 })).toHaveText(headline)
  await expect(page.getByRole('heading', { name: 'Cloud, Reliability & Trust' })).toBeVisible()
  await expect(page.getByRole('heading', { name: 'Work', exact: true })).toBeVisible()
  await expect(page.getByRole('heading', { name: 'Demos', exact: true })).toBeVisible()
  await expect(page.getByRole('link', { name: 'Book a call', exact: true }).first()).toHaveAttribute('href', '/book')
  const navigation = page.getByRole('navigation', { name: 'Main navigation', exact: true })
  await expect(navigation).toBeVisible()
  const inventory = JSON.parse(await readFile(new URL('../../../../docs/phase-1-foundation/06-canonical-route-inventory.json', import.meta.url), 'utf8'))
  const canonical = new Set<string>(JSON.stringify(inventory).match(/"path":"([^"]+)"/g)?.map(path => JSON.parse('{' + path + '}').path))
  for (const route of ['/services', '/industries', '/work', '/demos', '/insights', '/experts', '/trust', '/about', '/contact', '/book']) {
    expect(canonical.has(route)).toBe(true)
    await expect(navigation.locator(`a[href="${route}"]`)).toBeVisible()
  }
  await expect(page.getByRole('link', { name: 'Enter the 3D World' })).toHaveAttribute('href', '/world')
  expect(await page.locator('canvas,audio').count()).toBe(0)
  expect(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth)).toBe(true)
  await context.close()
})

test('mobile disclosure supports keyboard dismissal, focus return and resize', async ({ page }) => {
  await page.setViewportSize({ width: 320, height: 800 })
  const errors: string[] = []
  page.on('pageerror', error => errors.push(error.message))
  await page.goto('/')
  const toggle = page.getByRole('button', { name: 'Menu', exact: true })
  const navigation = page.getByRole('navigation', { name: 'Main navigation', exact: true })
  await expect(toggle).toHaveAttribute('aria-expanded', 'false')
  await expect(navigation).toBeHidden()
  await toggle.focus()
  await page.keyboard.press('Tab')
  await expect(page.getByRole('link', { name: 'Search', exact: true }).first()).toBeFocused()
  await page.keyboard.press('Shift+Tab')
  await page.keyboard.press('Enter')
  await expect(page.getByRole('button', { name: 'Close menu' })).toHaveAttribute('aria-expanded', 'true')
  await page.keyboard.press('Tab')
  await expect(navigation.getByRole('link', { name: 'Home', exact: true })).toBeFocused()
  await page.keyboard.press('Escape')
  await expect(toggle).toBeFocused()
  await expect(navigation).toBeHidden()
  await page.keyboard.press('Space')
  await expect(navigation).toBeVisible()
  await page.getByRole('button', { name: 'Close menu' }).click()
  await expect(toggle).toBeFocused()
  await toggle.click()
  await navigation.getByRole('link', { name: 'Home', exact: true }).focus()
  await page.setViewportSize({ width: 1440, height: 1000 })
  await expect(page.getByRole('link', { name: 'Hengshi Design home' }).first()).toBeFocused()
  await page.setViewportSize({ width: 320, height: 800 })
  await expect(toggle).toHaveAttribute('aria-expanded', 'false')
  expect(errors).toEqual([])
})

test('skip link moves keyboard focus past shared navigation', async ({ page }) => {
  await page.goto('/')
  await page.keyboard.press('Tab')
  await expect(page.getByRole('link', { name: 'Skip to main content' })).toBeFocused()
  await page.keyboard.press('Enter')
  await expect(page.getByRole('main')).toBeFocused()
})

test('accepted SVG is served unchanged; failed artwork keeps name and navigation', async ({ page, request }) => {
  await page.setViewportSize({ width: 320, height: 800 })
  await page.goto('/')
  const img = page.locator('.site-header .brand img')
  const src = await img.getAttribute('src')
  expect(src).toBeTruthy()
  const imageResponse = await request.get(src!)
  expect(imageResponse.status()).toBe(200)
  expect(await imageResponse.body()).toEqual(await readFile(new URL('../../../../docs/phase-1-brand-identity/assets/mark-framework-relay.svg', import.meta.url)))
  const geometry = await img.boundingBox()
  expect(geometry?.width).toBe(32)
  expect(geometry?.height).toBe(32)
  await page.route('**/*.svg', route => route.abort())
  await page.reload()
  await expect(page.locator('.site-header .brand img')).toHaveCount(0)
  await expect(page.getByRole('link', { name: 'Hengshi Design home' }).first()).toBeVisible()
  await expect(page.getByRole('button', { name: 'Menu', exact: true })).toBeVisible()
  await expect(page.getByRole('link', { name: 'Book a call', exact: true }).first()).toBeVisible()
  await page.screenshot({ path: screenshots + 'mobile-missing-mark.png' })
})

for (const width of [320, 768, 1024, 1440]) {
  test(`responsive layout preserves content at ${width}px`, async ({ page }) => {
    await page.setViewportSize({ width, height: 1000 })
    await page.emulateMedia({ reducedMotion: 'reduce' })
    await page.goto('/')
    await expect(page.getByRole('heading', { level: 1 })).toHaveText(headline)
    expect(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth)).toBe(true)
    const outside = await page.locator('h1,h2,h3,p,a,button').evaluateAll(elements => elements.filter(element => {
      const bounds = element.getBoundingClientRect()
      return bounds.width > 0 && bounds.height > 0 && (bounds.left < -1 || bounds.right > innerWidth + 1)
    }).filter(element => !element.classList.contains('skip-link')).map(element => element.textContent))
    expect(outside).toEqual([])
    if (width === 320 || width === 1440) {
      await page.screenshot({ path: screenshots + `homepage-${width}.png`, fullPage: true })
      const results = await new AxeBuilder({ page }).analyze()
      expect(results.violations).toEqual([])
      if (width === 320) {
        await page.getByRole('button', { name: 'Menu', exact: true }).click()
        await page.screenshot({ path: screenshots + 'mobile-menu.png' })
        const openResults = await new AxeBuilder({ page }).analyze()
        expect(openResults.violations).toEqual([])
      }
    }
  })
}

test('unimplemented destinations do not masquerade as the homepage', async ({ request }) => {
  const response = await request.get('/not-an-implemented-page')
  expect(response.status()).toBe(404)
})

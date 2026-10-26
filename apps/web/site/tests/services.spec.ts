import AxeBuilder from '@axe-core/playwright'
import { expect, test } from '@playwright/test'
import { readFile } from 'node:fs/promises'
import { fileURLToPath } from 'node:url'

// Expectations come from the approved route inventory, not the page implementation.
const inventory = JSON.parse(await readFile(new URL('../../../../docs/phase-1-foundation/06-canonical-route-inventory.json', import.meta.url), 'utf8'))
type Route = { path: string; primaryEntity: string; routeType: string }
const routes: Route[] = inventory.routes.filter((r: Route) => r.path.startsWith('/services'))
const wings = routes.filter(r => r.routeType === 'service_wing')
const services = routes.filter(r => r.routeType === 'service')
const screenshots = fileURLToPath(new URL('../../../../artifacts/hsd-002/local-implementation/', import.meta.url))
const digital = '/services/digital-products-growth'
const longest = digital + '/product-design-experience-engineering'

test('homepage to Services, every wing and formal service, then breadcrumb return', async ({ page }) => {
  test.setTimeout(90_000) // One full journey covers ten services and their return paths.
  await page.goto('/')
  await page.getByRole('navigation', { name: 'Main navigation' }).getByRole('link', { name: 'Services', exact: true }).click()
  await expect(page).toHaveURL('/services')
  for (const wing of wings) {
    await page.getByRole('main').getByRole('link', { name: wing.primaryEntity, exact: true }).click()
    await expect(page.getByRole('heading', { level: 1 })).toHaveText(wing.primaryEntity)
    const contained = services.filter(r => r.path.startsWith(wing.path + '/'))
    const serviceLinks = page.getByRole('main').locator('a').filter({ has: page.locator('h3') })
    await expect(serviceLinks).toHaveCount(contained.length)
    for (const service of contained) {
      await page.getByRole('main').getByRole('link', { name: service.primaryEntity, exact: true }).click()
      await expect(page.getByRole('heading', { level: 1 })).toHaveText(service.primaryEntity)
      await expect(page.getByRole('heading', { level: 1 })).toBeFocused()
      const breadcrumbs = page.getByRole('navigation', { name: 'Breadcrumb' })
      await expect(breadcrumbs.locator('[aria-current="page"]')).toHaveText(service.primaryEntity)
      await breadcrumbs.getByRole('link', { name: wing.primaryEntity, exact: true }).click()
      await expect(page).toHaveURL(wing.path)
    }
    await page.getByRole('navigation', { name: 'Breadcrumb' }).getByRole('link', { name: 'Services', exact: true }).click()
  }
})

test('all sixteen canonical routes load complete initial HTML and work without JavaScript', async ({ browser, request }) => {
  expect(routes).toHaveLength(16)
  expect(wings).toHaveLength(5)
  expect(services).toHaveLength(10)
  const context = await browser.newContext({ javaScriptEnabled: false, viewport: { width: 320, height: 800 } })
  const page = await context.newPage()
  const titles = new Set<string>()
  for (const route of routes) {
    const response = await request.get(route.path)
    expect(response.status(), route.path).toBe(200)
    const html = await response.text()
    expect(html).not.toContain('<!--site-html-->')
    expect(html).toContain('<main')
    expect(html).toContain('name="robots" content="noindex, nofollow"')
    await page.goto(route.path)
    await expect(page.getByRole('heading', { level: 1 })).toHaveText(route.routeType === 'service_collection' ? 'Services' : route.primaryEntity)
    await expect(page.getByRole('navigation', { name: 'Main navigation' })).toBeVisible()
    await expect(page.getByRole('navigation', { name: 'Breadcrumb' })).toBeVisible()
    await expect(page.getByRole('link', { name: 'Book a call', exact: true }).first()).toHaveAttribute('href', '/book')
    await expect(page.locator('link[rel="canonical"]')).toHaveAttribute('href', 'https://hengshidesign.com' + route.path)
    const title = await page.title()
    expect(titles.has(title)).toBe(false)
    titles.add(title)
    expect(await page.locator('meta[name="description"]').getAttribute('content')).toBeTruthy()
    expect(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth)).toBe(true)
  }
  await context.close()
})

for (const width of [320, 1440]) {
  test(`all Services content reflows and hydrates without errors at ${width}px`, async ({ page }) => {
    test.setTimeout(90_000) // Sixteen documents plus three actual-page axe scans.
    await page.setViewportSize({ width, height: 1000 })
    await page.emulateMedia({ reducedMotion: 'reduce' })
    const errors: string[] = []
    page.on('pageerror', error => errors.push(error.message))
    page.on('console', message => { if (message.type() === 'error') errors.push(message.text()) })
    for (const route of routes) {
      await page.goto(route.path)
      await expect(page.getByRole('heading', { level: 1 })).toBeVisible()
      expect(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth), route.path).toBe(true)
      const outside = await page.locator('h1,h2,h3,p,a,button').evaluateAll(elements => elements.filter(element => {
        const box = element.getBoundingClientRect()
        return box.width > 0 && box.height > 0 && !element.classList.contains('skip-link') && (box.left < -1 || box.right > innerWidth + 1)
      }).map(element => element.textContent))
      expect(outside, route.path).toEqual([])
      if (width === 320) await page.getByRole('button', { name: 'Menu', exact: true }).click()
      await expect(page.getByRole('navigation', { name: 'Main navigation' }).locator('a[aria-current="page"]')).toHaveText('Services')
      if (width === 320) await page.getByRole('button', { name: 'Close menu', exact: true }).click()
      if (['/services', digital, longest].includes(route.path)) {
        await page.screenshot({ path: screenshots + `${route.path === '/services' ? 'index' : route.path === digital ? 'wing' : 'detail'}-${width}.png`, fullPage: true })
        expect((await new AxeBuilder({ page }).analyze()).violations).toEqual([])
      }
    }
    expect(errors).toEqual([])
  })
}

test('mobile keyboard navigation, breadcrumbs and disclosure retain clear focus', async ({ page }) => {
  await page.setViewportSize({ width: 320, height: 800 })
  await page.goto(longest)
  await page.keyboard.press('Tab')
  await expect(page.getByRole('link', { name: 'Skip to main content' })).toBeFocused()
  await page.keyboard.press('Enter')
  await expect(page.getByRole('main')).toBeFocused()
  const menu = page.getByRole('button', { name: 'Menu', exact: true })
  await menu.focus()
  await page.keyboard.press('Enter')
  const navigation = page.getByRole('navigation', { name: 'Main navigation' })
  await expect(navigation).toBeVisible()
  await page.keyboard.press('Tab')
  await expect(navigation.getByRole('link', { name: 'Home', exact: true })).toBeFocused()
  await page.keyboard.press('Escape')
  await expect(menu).toBeFocused()
  await expect(navigation).toBeHidden()
  const wing = page.getByRole('navigation', { name: 'Breadcrumb' }).getByRole('link', { name: 'Digital Products & Growth', exact: true })
  await wing.focus()
  await page.keyboard.press('Enter')
  await expect(page).toHaveURL(digital)
  await page.getByRole('main').getByRole('link', { name: 'Platform & Product Engineering', exact: true }).focus()
  await page.keyboard.press('Enter')
  await expect(page.getByRole('heading', { level: 1 })).toHaveText('Platform & Product Engineering')
  await page.getByRole('button', { name: 'Menu', exact: true }).click()
  await page.screenshot({ path: screenshots + 'mobile-menu.png' })
  expect((await new AxeBuilder({ page }).analyze()).violations).toEqual([])
})

test('empty evidence stays separate and cannot imply delivery, sources or booking success', async ({ page }) => {
  for (const route of services) {
    await page.goto(route.path)
    await expect(page.getByText('No client projects are published here yet.', { exact: true })).toBeVisible()
    await expect(page.getByText('No demos are published here yet. A demo will be labelled separately from client work.', { exact: true })).toBeVisible()
    await expect(page.getByText('No reviewed sources are published for this service yet.', { exact: true })).toBeVisible()
    await expect(page.getByRole('region', { name: 'Scope and boundaries', exact: true })).toBeVisible()
    await expect(page.getByRole('link', { name: 'Book a call', exact: true }).last()).toHaveAttribute('href', '/book')
    expect(await page.locator('form,canvas,audio').count()).toBe(0)
  }
})

test('unknown paths are semantic HTTP404s with useful recovery; canonical variants redirect', async ({ page, request }) => {
  for (const path of ['/services/no-such-wing', digital + '/no-such-service', '/services/ai-data-automation/strategy-architecture', '/not-an-implemented-page']) {
    const response = await page.goto(path)
    expect(response?.status()).toBe(404)
    await expect(page.getByRole('heading', { level: 1 })).toHaveText('Page not found')
    await expect(page.getByRole('main').getByRole('link', { name: 'Browse services', exact: true })).toHaveAttribute('href', '/services')
    await expect(page.locator('link[rel="canonical"]')).toHaveCount(0)
  }
  for (const path of ['/services/', '/services/index.html', longest + '/']) {
    const response = await request.get(path, { maxRedirects: 0 })
    expect(response.status()).toBe(308)
    expect(response.headers().location).toBe(path === longest + '/' ? longest : '/services')
  }
  await page.goto('/services?source=local')
  await expect(page.getByRole('heading', { level: 1 })).toHaveText('Services')
})

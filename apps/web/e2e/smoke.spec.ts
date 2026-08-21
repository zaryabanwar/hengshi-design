import { expect, test } from '@playwright/test'

const worldFixture = {
  nodes: [
    {
      id: 'node-exterior',
      key: 'exterior',
      title: 'Hengshi HQ Exterior',
      description: 'Entry node for smoke testing.',
      is_entry: true,
      sort_order: 0,
      camera_position: [0, 5, 10],
      camera_target: [0, 2, 0],
      camera_fov: 50,
      environment: {},
      created_at: '2026-06-24T00:00:00Z',
      updated_at: '2026-06-24T00:00:00Z',
      hotspots: [
        {
          id: 'hotspot-door',
          node_id: 'node-exterior',
          key: 'door',
          title: 'Enter Building',
          description: 'Entry hotspot for smoke testing.',
          kind: 'NAVIGATE_NODE',
          position: [0, 1.5, 3],
          normal: [0, 0, 1],
          radius: 0.5,
          icon: 'door',
          payload: { target_node_key: 'lobby' },
          sort_order: 0,
          is_enabled: true,
          created_at: '2026-06-24T00:00:00Z'
        }
      ]
    }
  ]
}

test.beforeEach(async ({ page }) => {
  await page.route('**/api/world', async (route) => {
    await route.fulfill({ json: worldFixture })
  })
})

test('public homepage routes into the world experience', async ({ page }) => {
  await page.goto('/')

  await expect(page.getByRole('heading', { name: 'Hengshi Design' })).toBeVisible()
  await page.getByRole('link', { name: 'Enter' }).click()

  await expect(page).toHaveURL(/\/world\?entry=1/)
  await expect(page.locator('canvas')).toBeVisible()
})

test('admin login page renders for auth workflow checks', async ({ page }) => {
  await page.goto('/admin/login')

  await expect(page.getByRole('heading', { name: 'Login' })).toBeVisible()
  await expect(page.getByPlaceholder('Email')).toBeVisible()
  await expect(page.getByPlaceholder('Password')).toBeVisible()
})

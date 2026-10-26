import { mkdir, readFile, writeFile } from 'node:fs/promises'
import { fileURLToPath } from 'node:url'
import { build } from 'vite'

const configFile = fileURLToPath(new URL('vite.config.ts', import.meta.url))
await build({ configFile })
await build({ configFile, build: { ssr: 'src/entry-server.tsx', outDir: 'dist-ssr' } })
const { render, pagePaths } = await import('./dist-ssr/entry-server.js')
const htmlFile = new URL('dist/index.html', import.meta.url)
const template = await readFile(htmlFile, 'utf8')
if (!template.includes('<!--site-html-->') || !template.includes('<!--site-head-->')) throw new Error('Missing semantic document outlets')
for (const path of [...pagePaths, '/404']) {
  const page = render(path)
  const output = path === '/404' ? new URL('dist/404.html', import.meta.url) : new URL(`dist${path === '/' ? '' : path}/index.html`, import.meta.url)
  await mkdir(new URL('.', output), { recursive: true })
  await writeFile(output, template.replace('<!--site-head-->', page.head).replace('<!--site-html-->', page.html))
}

import { readFile } from 'node:fs/promises'
import { fileURLToPath } from 'node:url'
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import tailwindcss from 'tailwindcss'
import autoprefixer from 'autoprefixer'
import { canonicalRedirect, pagePaths } from './src/routes'

const root = fileURLToPath(new URL('.', import.meta.url))

function assetPath(path: string) {
  return /^\/(?:assets\/|src\/|@|node_modules\/)/.test(path)
}

export default defineConfig({
  root,
  appType: 'custom',
  plugins: [react(), {
    name: 'local-semantic-site',
    configureServer(server) {
      return () => {
        server.middlewares.use(async (request, response, next) => {
          const path = new URL(request.url ?? '/', 'http://localhost').pathname
          if (assetPath(path)) return next()
          const redirect = canonicalRedirect(path)
          if (redirect) { response.writeHead(308, { Location: redirect }).end(); return }
          if (request.method !== 'GET' && request.method !== 'HEAD') { response.writeHead(405, { Allow: 'GET, HEAD' }).end(); return }
          try {
            const template = await server.transformIndexHtml(path, await readFile(new URL('index.html', import.meta.url), 'utf8'))
            const { render } = await server.ssrLoadModule('/src/entry-server.tsx')
            const page = render(path)
            response.statusCode = page.status
            response.setHeader('Content-Type', 'text/html; charset=utf-8')
            response.setHeader('X-Robots-Tag', 'noindex, nofollow')
            response.end(request.method === 'HEAD' ? undefined : template.replace('<!--site-head-->', page.head).replace('<!--site-html-->', page.html))
          } catch (error) {
            server.ssrFixStacktrace(error as Error)
            next(error)
          }
        })
      }
    },
    configurePreviewServer(server) {
      // Before Vite's static-file middleware: known canonical routes only;
      // no SPA fallback and no accidental 200 for an unknown document.
      server.middlewares.use(async (request, response, next) => {
        const path = new URL(request.url ?? '/', 'http://localhost').pathname
        if (assetPath(path)) return next()
        const redirect = canonicalRedirect(path)
        if (redirect) { response.writeHead(308, { Location: redirect }).end(); return }
        if (request.method !== 'GET' && request.method !== 'HEAD') { response.writeHead(405, { Allow: 'GET, HEAD' }).end(); return }
        const known = pagePaths.includes(path)
        try {
          const file = known ? `dist${path === '/' ? '' : path}/index.html` : 'dist/404.html'
          const html = await readFile(new URL(file, import.meta.url), 'utf8')
          response.writeHead(known ? 200 : 404, { 'Content-Type': 'text/html; charset=utf-8', 'X-Robots-Tag': 'noindex, nofollow' })
          response.end(request.method === 'HEAD' ? undefined : html)
        } catch (error) { next(error) }
      })
    },
  }],
  css: { postcss: { plugins: [tailwindcss({ content: [root + '/src/**/*.{ts,tsx}'] }), autoprefixer()] } },
  server: { host: '127.0.0.1', port: 5174, strictPort: true },
  preview: { host: '127.0.0.1', port: 5174, strictPort: true },
  build: { outDir: 'dist', emptyOutDir: true, assetsInlineLimit: 0 },
})

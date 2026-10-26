import { renderToStaticMarkup, renderToString } from 'react-dom/server'
import { Site } from './Site'
import { findPage } from './routes'
export { pagePaths } from './routes'

export function render(path = '/') {
  const page = findPage(path)
  const title = page.kind === 'home' ? page.title : `${page.title} | Hengshi Design`
  const canonical = page.kind === 'missing' ? undefined : `https://hengshidesign.com${path}`
  return {
    status: page.kind === 'missing' ? 404 : 200,
    html: renderToString(<Site path={path} />),
    head: renderToStaticMarkup(<><title>{title}</title><meta name="description" content={page.description} />
      <meta property="og:title" content={title} /><meta property="og:description" content={page.description} /><meta property="og:type" content="website" />
      {canonical && <><link rel="canonical" href={canonical} /><meta property="og:url" content={canonical} /></>}
    </>),
  }
}

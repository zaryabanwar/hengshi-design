import { useEffect } from 'react'
import { Homepage } from './Homepage'
import { findPage } from './routes'
import { NotFound, ServicePage, ServicesIndex, WingPage } from './Services'

export function Site({ path }: { path: string }) {
  useEffect(() => {
    // Full-document navigation keeps ordinary links and the no-JS journey intact.
    // For an internal route change, announce the newly loaded document heading.
    if (document.referrer) {
      const from = new URL(document.referrer)
      if (from.origin === location.origin && from.pathname !== path) {
        const heading = document.querySelector<HTMLElement>('h1')
        if (heading) { heading.tabIndex = -1; heading.focus() }
      }
    }
  }, [path])
  const page = findPage(path)
  switch (page.kind) {
    case 'home': return <Homepage />
    case 'index': return <ServicesIndex />
    case 'wing': return <WingPage wing={page.wing} />
    case 'service': return <ServicePage service={page.service} wing={page.wing} />
    default: return <NotFound />
  }
}

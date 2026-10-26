import { formalServices, wings } from './servicesContent'

export const pagePaths = ['/', '/services', ...wings.map(wing => wing.path), ...formalServices.map(service => service.path)]

export function findPage(path: string) {
  if (path === '/') return { kind: 'home' as const, title: 'Hengshi Design — Strategy, design and engineering', description: 'Strategy, design and engineering for digital products, AI and the systems your business relies on.' }
  if (path === '/services') return { kind: 'index' as const, title: 'Services', description: 'Find the right starting point for your project. Explore five connected areas of strategy, design and engineering.' }
  const wing = wings.find(item => item.path === path)
  if (wing) return { kind: 'wing' as const, title: wing.title, description: wing.description, wing }
  const service = formalServices.find(item => item.path === path)
  if (service) return { kind: 'service' as const, title: service.title, description: service.description, service, wing: wings.find(item => item.path === service.wingPath)! }
  return { kind: 'missing' as const, title: 'Page not found', description: 'Check the address or explore our services.' }
}

// Only known route aliases redirect. Unknown addresses keep their genuine 404.
export function canonicalRedirect(path: string) {
  const candidate = path.endsWith('/index.html') ? path.slice(0, -11) || '/' : path.replace(/\/+$/, '') || '/'
  return candidate !== path && pagePaths.includes(candidate) ? candidate : undefined
}

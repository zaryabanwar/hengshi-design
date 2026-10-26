// Accepted HSD-001 references 246:7658 / 246:7883, accepted 2026-10-26.
// This local slice supplies no publication, client evidence or booking data.
export const destinations = [
  ['Home', '/'], ['Services', '/services'], ['Industries', '/industries'],
  ['Work', '/work'], ['Demos', '/demos'], ['Insights', '/insights'],
  ['Experts', '/experts'], ['Trust', '/trust'], ['About', '/about'],
  ['Contact', '/contact'], ['Book a call', '/book'],
] as const

export { wings as services } from './servicesContent'

export const industries = [
  { title: 'Agriculture', path: '/industries/agriculture', description: 'Explore digital tools for farm operations, field data and resource planning.' },
  { title: 'Mining', path: '/industries/mining', description: 'Explore data platforms, automation and infrastructure for mining operations.' },
] as const

export const steps = [
  { title: 'Your goals', question: 'What do you want to achieve?', description: 'We start with your goals, the people involved and the problems you want to solve.', note: 'Goals and priorities' },
  { title: 'Your options', question: 'What could work?', description: 'We look at possible approaches, technical requirements and trade-offs.', note: 'Options and recommendations' },
  { title: 'Your next steps', question: 'How do we get started?', description: 'We agree the scope, responsibilities and next steps before work begins.', note: 'Scope and next steps' },
] as const

import type { ReactNode } from 'react'
import { brandStyle } from './brand'
import { Arrow, Footer, Header } from './Navigation'
import { formalServices, wings } from './servicesContent'
import type { FormalService, Wing } from './servicesContent'

export function PageShell({ children, missing = false }: { children: ReactNode; missing?: boolean }) {
  return <div className="hengshi-site services-site" style={brandStyle}>
    <a className="skip-link" href="#main-content">Skip to main content</a>
    <Header currentPath={missing ? '' : '/services'} />
    <main id="main-content" tabIndex={-1}>{children}</main>
    <Footer />
  </div>
}

function Breadcrumbs({ wing, service }: { wing?: Wing; service?: FormalService }) {
  const crumbs = [{ title: 'Home', path: '/' }, { title: 'Services', path: '/services' }, ...(wing ? [wing] : []), ...(service ? [service] : [])]
  return <nav aria-label="Breadcrumb" className="breadcrumbs page-width"><ol>{crumbs.map((crumb, index) => <li key={crumb.path}>
    {index > 0 && <span className="breadcrumb-divider" aria-hidden="true">/</span>}
    {index === crumbs.length - 1 ? <span aria-current="page">{crumb.title}</span> : <a href={crumb.path}>{crumb.title}</a>}
  </li>)}</ol></nav>
}

function Intro({ title, description, label }: { title: string; description: string; label: string }) {
  return <section className="service-intro page-width" aria-labelledby="page-heading">
    <p className="eyebrow">{label}</p><h1 id="page-heading" tabIndex={-1}>{title}</h1>
    <p className="service-lead">{description}</p>
    <p className="capability-note">Capability descriptions explain what we can discuss. They are not evidence of client delivery.</p>
  </section>
}

function TitleLink({ title, path, level = 3 }: { title: string; path: string; level?: 2 | 3 }) {
  const Heading = level === 2 ? 'h2' : 'h3'
  return <a className="service-title-link" href={path}><Heading>{title}</Heading><Arrow /></a>
}

function Evidence({ detail = false }: { detail?: boolean }) {
  return <section className="service-evidence" aria-labelledby="evidence-heading"><div className="page-width">
    <p className="eyebrow">Evidence</p><h2 id="evidence-heading">Work and demos</h2>
    <div><h3>Client work</h3><p>No client projects are published here yet.</p></div>
    <div><h3>Hengshi-owned demos</h3><p>No demos are published here yet. A demo will be labelled separately from client work.</p></div>
    {detail && <div className="related-sources"><h3>Related insights, experts and assurance sources</h3><p>No reviewed sources are published for this service yet.</p></div>}
  </div></section>
}

function Contact() {
  return <section className="service-contact dark" aria-labelledby="contact-heading"><div className="page-width">
    <p className="eyebrow">Let’s talk</p><h2 id="contact-heading">Tell us about your project.</h2>
    <p>Book a 30-minute call to discuss what you need and see how we could help.</p>
    <div className="booking-action"><a href="/book" className="primary-action">Book a call</a><p className="call-note">30-minute introductory call.</p><a className="text-action" href="/contact">Contact us <Arrow /></a></div>
  </div></section>
}

export function ServicesIndex() {
  return <PageShell><Breadcrumbs /><Intro title="Services" label="Five wings / ten services" description="Find the right starting point for your project. Explore five connected areas of strategy, design and engineering." />
    <div className="service-index page-width">{wings.map((wing, index) => {
      const contained = formalServices.filter(service => service.wingPath === wing.path)
      return <section key={wing.path} className="wing-overview" aria-labelledby={`wing-${index}`}>
        <p className="eyebrow">0{index + 1} / {contained.length} formal {contained.length === 1 ? 'service' : 'services'}</p>
        <a className="service-title-link" href={wing.path}><h2 id={`wing-${index}`}>{wing.title}</h2><Arrow /></a>
        <p className="wing-description">{wing.description}</p>
        <ul className="formal-service-links">{contained.map(service => <li key={service.path}><a className="service-title-link" href={service.path}><span>{service.title}</span><Arrow /></a></li>)}</ul>
      </section>
    })}</div><Evidence /><Contact />
  </PageShell>
}

export function WingPage({ wing }: { wing: Wing }) {
  const contained = formalServices.filter(service => service.wingPath === wing.path)
  return <PageShell><Breadcrumbs wing={wing} /><Intro title={wing.title} description={wing.description} label="Service wing" />
    <section className="wing-services page-width" aria-labelledby="wing-services-heading">
      <p className="eyebrow">{contained.length} formal {contained.length === 1 ? 'service' : 'services'}</p><h2 id="wing-services-heading">Explore this wing</h2>
      <ul>{contained.map(service => <li key={service.path}><TitleLink {...service} /><p>{service.description}</p></li>)}</ul>
      <a className="service-title-link back-services" href="/services"><span>All services</span><Arrow /></a>
    </section><Evidence /><Contact />
  </PageShell>
}

export function ServicePage({ service, wing }: { service: FormalService; wing: Wing }) {
  const siblings = formalServices.filter(item => item.wingPath === wing.path && item.path !== service.path)
  return <PageShell><Breadcrumbs wing={wing} service={service} /><Intro title={service.title} description={service.description} label="Formal service" />
    <div className="service-decision page-width">
      <section aria-labelledby="decision-heading"><p className="eyebrow">Your decision</p><h2 id="decision-heading">{service.decision}</h2><p>Start with the outcome you need, the people involved and the constraints your project must work within.</p></section>
      <section aria-labelledby="focus-heading"><p className="eyebrow">Possible focus</p><h2 id="focus-heading">What we can explore</h2><ul className="focus-list">{service.focus.map(focus => <li key={focus}>{focus}</li>)}</ul></section>
      <section aria-labelledby="scope-heading"><p className="eyebrow" id="scope-heading">Scope and boundaries</p><h2>Agree the work before it begins</h2><p>{service.boundary}</p><p>Deliverables, responsibilities, timing and costs are agreed for each engagement. This page does not make a delivery commitment.</p></section>
    </div><Evidence detail />
    <nav className="service-related page-width" aria-label="Related services"><p className="eyebrow">Keep exploring</p>
      <a className="service-title-link back-wing" href={wing.path}><span>Back to {wing.title}</span><Arrow /></a>
      {siblings.map(item => <a key={item.path} className="service-title-link" href={item.path}><span>{item.title}</span><Arrow /></a>)}
      <a className="service-title-link back-services" href="/services"><span>All services</span><Arrow /></a>
    </nav><Contact />
  </PageShell>
}

export function NotFound() {
  return <PageShell missing><section className="not-found page-width"><p className="eyebrow">404</p><h1 id="page-heading" tabIndex={-1}>Page not found</h1>
    <p>We couldn’t find this page. Check the address or explore our services.</p><a className="service-title-link" href="/services"><span>Browse services</span><Arrow /></a><a className="text-action" href="/">Return home <Arrow /></a>
  </section></PageShell>
}

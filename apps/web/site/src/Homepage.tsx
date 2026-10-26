import { brandStyle } from './brand'
import { Arrow, Footer, Header } from './Navigation'
import { industries, services, steps } from './content'

function BookingAction({ contact = false }: { contact?: boolean }) {
  return <div className={'booking-action' + (contact ? ' contact-action' : '')}>
    <a className="primary-action" href="/book">Book a call</a>
    {!contact && <a className="text-action" href="#services">View services <Arrow /></a>}
    <p className="call-note">30-minute introductory call.</p>
    {contact && <a className="text-action" href="/contact">Contact us <Arrow /></a>}
  </div>
}

export function Homepage() {
  return <div className="hengshi-site" style={brandStyle}>
    <a className="skip-link" href="#main-content">Skip to main content</a>
    <Header />
    <main id="main-content" tabIndex={-1}>
      <section className="hero dark" aria-labelledby="home-heading"><div className="page-width">
        <p className="eyebrow hero-eyebrow">Strategy, design and engineering</p>
        <h1 id="home-heading">From complex ambition to accountable delivery.</h1>
        <div className="hero-introduction">
          <p>We bring strategy, design and engineering together to help you develop digital products, use AI and improve the systems you rely on.</p>
          <BookingAction />
        </div>
        <ol className="milestones"><li>01 / Discuss your project</li><li>02 / Explore your options</li><li>03 / Plan the work</li></ol>
      </div></section>

      <section id="services" className="services-section section-pad" aria-labelledby="services-heading"><div className="page-width">
        <div className="section-heading"><div><p className="eyebrow">Services</p><p className="section-intro">Explore our services, or talk to us about your project.</p></div><h2 id="services-heading">How can we help?</h2></div>
        <ol className="service-list">{services.map((service, index) => <li key={service.path}><a href={service.path} className="service-row">
          <span className="item-number" aria-hidden="true">0{index + 1}</span>
          <div className="service-title"><h3>{service.title}</h3><p className="service-tags">{service.tags}</p></div>
          <p className="service-description">{service.description}</p><Arrow />
        </a></li>)}</ol>
      </div></section>

      <section className="industries-section section-pad" aria-labelledby="industries-heading"><div className="page-width">
        <div className="section-heading"><div><p className="eyebrow">Industries</p><p className="section-intro">Explore services for agriculture and mining.</p></div><h2 id="industries-heading">Explore ideas for your industry</h2></div>
        <div className="industry-grid">{industries.map(industry => <a key={industry.path} href={industry.path} className="industry-card"><h3>{industry.title}</h3><Arrow /><p>{industry.description}</p></a>)}</div>
      </div></section>

      <section className="evidence-section section-pad" aria-label="Work and demos"><div className="page-width evidence-grid">
        <div><p className="eyebrow">Client work</p><h2>Work</h2><p className="empty-state">No client projects are published here yet.</p><p className="evidence-note">Browse our services, or get in touch about your project.</p></div>
        <div><p className="eyebrow">Demos</p><h2>Demos</h2><p className="empty-state">No demos are published here yet.</p><p className="evidence-note">We’ll share our own prototypes and experiments here.</p></div>
      </div></section>

      <section className="process-section section-pad" aria-labelledby="process-heading"><div className="page-width">
        <div className="section-heading"><div><p className="eyebrow">Working with us</p><p className="section-intro">Clear goals, practical options and a plan for the work.</p></div><h2 id="process-heading">How we’ll work together</h2></div>
        <ol className="process-grid">{steps.map((step, index) => <li key={step.title}><h3>{step.title}</h3><span className="item-number" aria-hidden="true">0{index + 1}</span><h4>{step.question}</h4><p>{step.description}</p><p className="step-note"><span aria-hidden="true">↳ </span>{step.note}</p></li>)}</ol>
      </div></section>

      <aside className="world-section"><div className="page-width world-inner"><div><p className="eyebrow">Explore in 3D</p><p>Take a look around our virtual world.</p></div><a className="text-action" href="/world">Enter the 3D World <Arrow /></a></div></aside>

      <section className="contact-section dark" aria-labelledby="contact-heading"><div className="page-width">
        <p className="eyebrow">Let’s talk</p><div className="contact-grid"><div><h2 id="contact-heading">Tell us about your project.</h2><p>Book a 30-minute call to discuss what you need and see how we could help.</p></div><BookingAction contact /></div>
      </div></section>
    </main>
    <Footer />
  </div>
}

import { useEffect, useRef, useState } from 'react'
import mark from '../../../../docs/phase-1-brand-identity/assets/mark-framework-relay.svg'
import { destinations } from './content'

export function Brand() {
  const [missing, setMissing] = useState(false)
  const artwork = useRef<HTMLImageElement>(null)
  useEffect(() => {
    // An image can fail before hydration attaches onError.
    if (artwork.current?.complete && artwork.current.naturalWidth === 0) setMissing(true)
  }, [])
  return <a className="brand" href="/" aria-label="Hengshi Design home">
    {!missing && <img ref={artwork} src={mark} width="40" height="40" alt="" onError={() => setMissing(true)} />}
    <span>Hengshi Design</span>
  </a>
}

export function Arrow() {
  return <span className="arrow" aria-hidden="true">↗</span>
}

function RouteLinks({ currentPath }: { currentPath?: string }) {
  return destinations.map(([label, href]) => <a key={href} href={href}
    aria-current={href === currentPath ? 'page' : undefined} className={href === '/book' ? 'book-link' : undefined}>
    {label}{href === '/book' && <span className="desktop-book-arrow"><Arrow /></span>}
  </a>)
}

function Utilities() {
  return <><a href="/directory">Search</a><a href="/accessibility">Accessibility settings</a><a href="/world">3D World <Arrow /></a></>
}

export function Header({ currentPath = '/' }: { currentPath?: string }) {
  const [open, setOpen] = useState(false)
  const toggle = useRef<HTMLButtonElement>(null)
  const header = useRef<HTMLElement>(null)
  function closeMenu() {
    setOpen(false)
    toggle.current?.focus()
  }
  useEffect(() => {
    // Reset the disclosure when its mobile layout goes away. Focus must not
    // remain inside a hidden mobile menu after a resize/zoom change.
    const desktop = window.matchMedia('(min-width: 900px)')
    function resetOnDesktop() {
      if (!desktop.matches) return
      if (header.current?.contains(document.activeElement) &&
          document.activeElement?.closest('.mobile-navigation')) {
        header.current.querySelector<HTMLAnchorElement>('.brand')?.focus()
      }
      setOpen(false)
    }
    desktop.addEventListener('change', resetOnDesktop)
    return () => desktop.removeEventListener('change', resetOnDesktop)
  }, [])
  return <header ref={header} className="site-header dark" onKeyDown={event => {
    if (event.key === 'Escape' && open) { event.preventDefault(); closeMenu() }
  }}>
    <div className="header-inner">
      <div className="brand-row"><Brand /><div className="desktop-utilities"><Utilities /></div></div>
      <nav className="desktop-navigation" aria-label="Main navigation"><RouteLinks currentPath={currentPath} /></nav>
      <div className="mobile-navigation">
        <div className="mobile-controls">
          <button ref={toggle} type="button" aria-expanded={open} aria-controls="mobile-menu"
            onClick={() => setOpen(value => !value)}>{open ? 'Close menu' : 'Menu'}</button>
          {!open && <><a href="/directory">Search</a><a href="/book">Book a call</a></>}
        </div>
        <nav id="mobile-menu" aria-label="Main navigation" hidden={!open}>
          <div className="mobile-routes"><RouteLinks currentPath={currentPath} /></div>
          <div className="mobile-utilities"><Utilities /></div>
        </nav>
      </div>
      <noscript><style>{'.mobile-navigation { display: none !important; }'}</style><nav className="no-script-navigation" aria-label="Main navigation"><RouteLinks currentPath={currentPath} /><Utilities /></nav></noscript>
    </div>
  </header>
}

export function Footer() {
  return <footer className="site-footer dark"><div className="footer-inner">
    <Brand />
    <div className="footer-links"><div><a href="/about">About</a><span aria-hidden="true"> · </span><a href="/trust">Trust</a><span aria-hidden="true"> · </span><a href="/contact">Contact</a></div>
      <a href="/directory">Search</a><a href="/accessibility">Accessibility settings</a></div>
    <small className="copyright">© 2026 Hengshi Design</small>
  </div></footer>
}

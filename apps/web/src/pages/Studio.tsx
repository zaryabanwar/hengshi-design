import { useAppStore } from '../store/useAppStore'

export default function Studio() {
  const isDark = useAppStore((state) => state.theme === 'dark')
  const heading = isDark ? 'text-slate-100' : 'text-slate-900'
  const body = isDark ? 'text-slate-300' : 'text-slate-600'

  return (
    <section className="space-y-4">
      <h1 className={`text-3xl font-semibold ${heading}`}>Studio</h1>
      <p className={`max-w-2xl ${body}`}>
        Plug in R3F scenes, GSAP timelines, and CMS-driven content here. This
        scaffold keeps routing and state ready for the real build.
      </p>
    </section>
  )
}

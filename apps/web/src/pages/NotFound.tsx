import { Link } from 'react-router-dom'
import { useAppStore } from '../store/useAppStore'

export default function NotFound() {
  const isDark = useAppStore((state) => state.theme === 'dark')
  const heading = isDark ? 'text-slate-100' : 'text-slate-900'
  const body = isDark ? 'text-slate-300' : 'text-slate-600'
  const button = isDark ? 'bg-white/10 hover:bg-white/20' : 'bg-slate-900/10 hover:bg-slate-900/20'

  return (
    <section className="space-y-4">
      <h1 className={`text-3xl font-semibold ${heading}`}>Page not found</h1>
      <p className={body}>The route you hit does not exist yet.</p>
      <Link
        className={`inline-flex items-center rounded-full border border-white/10 px-4 py-2 text-sm transition ${button}`}
        to="/"
      >
        Return home
      </Link>
    </section>
  )
}

import { Link } from 'react-router-dom'

export const Home = () => {
  return (
    <main className="flex min-h-screen items-center justify-center bg-slate-950 text-white">
      <div className="text-center">
        <h1 className="text-3xl font-semibold">Hengshi Design</h1>
        <p className="mt-2 text-sm text-slate-300">
          Immersive world prototype.
        </p>
        <Link
          to="/world?entry=1"
          className="mt-6 inline-flex items-center rounded-full border border-slate-600 px-5 py-2 text-sm hover:border-white"
        >
          Enter
        </Link>
      </div>
    </main>
  )
}

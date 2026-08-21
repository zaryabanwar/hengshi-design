import { useState } from 'react'
import { useNavigate } from 'react-router-dom'

import { loginAdmin } from '../lib/api'

export const AdminLoginPage = () => {
  const navigate = useNavigate()
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [error, setError] = useState<string | null>(null)
  const [loading, setLoading] = useState(false)

  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault()
    setLoading(true)
    setError(null)
    try {
      const token = await loginAdmin(email, password)
      localStorage.setItem('admin_token', token)
      navigate('/admin/services')
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Login failed')
    } finally {
      setLoading(false)
    }
  }

  return (
    <main className="flex min-h-screen items-center justify-center bg-slate-950 text-white">
      <form
        onSubmit={handleSubmit}
        className="w-full max-w-md space-y-4 rounded-xl border border-slate-800 bg-slate-900/60 p-6 shadow-lg"
      >
        <div>
          <p className="text-xs uppercase tracking-[0.2em] text-slate-400">Admin</p>
          <h1 className="text-2xl font-semibold">Login</h1>
        </div>
        {error && <p className="text-sm text-rose-300">{error}</p>}
        <input
          className="w-full rounded border border-slate-700 bg-slate-900 px-3 py-2 text-sm"
          placeholder="Email"
          type="email"
          value={email}
          onChange={(event) => setEmail(event.target.value)}
          required
        />
        <input
          className="w-full rounded border border-slate-700 bg-slate-900 px-3 py-2 text-sm"
          placeholder="Password"
          type="password"
          value={password}
          onChange={(event) => setPassword(event.target.value)}
          required
        />
        <button
          className="w-full rounded border border-slate-600 px-4 py-2 text-sm hover:border-white"
          type="submit"
          disabled={loading}
        >
          {loading ? 'Signing in…' : 'Sign in'}
        </button>
      </form>
    </main>
  )
}

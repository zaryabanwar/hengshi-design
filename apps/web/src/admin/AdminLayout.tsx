import { NavLink, Outlet, useNavigate } from 'react-router-dom'

export const AdminLayout = () => {
  const navigate = useNavigate()

  const handleLogout = () => {
    localStorage.removeItem('admin_token')
    navigate('/admin/login')
  }

  const linkClass = ({ isActive }: { isActive: boolean }) =>
    `rounded px-3 py-2 text-sm ${isActive ? 'bg-slate-800 text-white' : 'text-slate-300 hover:text-white'}`

  return (
    <div className="min-h-screen bg-slate-950 text-white">
      <div className="flex">
        <aside className="w-60 border-r border-slate-800 p-4">
          <div className="text-xs uppercase tracking-[0.2em] text-slate-500">Admin</div>
          <div className="mt-1 text-lg font-semibold">Hengshi</div>
          <nav className="mt-6 flex flex-col gap-2">
            <NavLink to="/admin/services" className={linkClass}>
              Services
            </NavLink>
            <NavLink to="/admin/projects" className={linkClass}>
              Projects
            </NavLink>
            <NavLink to="/admin/world" className={linkClass}>
              World
            </NavLink>
          </nav>
          <button
            className="mt-6 w-full rounded border border-slate-700 px-3 py-2 text-sm text-slate-300 hover:text-white"
            onClick={handleLogout}
          >
            Logout
          </button>
        </aside>
        <main className="flex-1 p-6">
          <Outlet />
        </main>
      </div>
    </div>
  )
}

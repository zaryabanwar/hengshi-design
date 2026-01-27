import { BrowserRouter, Navigate, Route, Routes } from 'react-router-dom'

import { AdminLayout } from './admin/AdminLayout'
import { AdminLoginPage } from './admin/AdminLoginPage'
import { ProjectsAdminPage } from './admin/ProjectsAdminPage'
import { RequireAdmin } from './admin/RequireAdmin'
import { ServicesAdminPage } from './admin/ServicesAdminPage'
import { WorldAdminPage } from './admin/WorldAdminPage'
import { Home } from './pages/Home'
import { WorldPage } from './pages/WorldPage'

const App = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/world" element={<WorldPage />} />
        <Route path="/admin/login" element={<AdminLoginPage />} />
        <Route
          path="/admin"
          element={
            <RequireAdmin>
              <AdminLayout />
            </RequireAdmin>
          }
        >
          <Route index element={<Navigate to="/admin/services" replace />} />
          <Route path="services" element={<ServicesAdminPage />} />
          <Route path="projects" element={<ProjectsAdminPage />} />
          <Route path="world" element={<WorldAdminPage />} />
        </Route>
      </Routes>
    </BrowserRouter>
  )
}

export default App

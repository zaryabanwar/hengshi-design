import { Navigate } from 'react-router-dom'

type RequireAdminProps = {
  children: JSX.Element
}

export const RequireAdmin = ({ children }: RequireAdminProps) => {
  const token = localStorage.getItem('admin_token')
  if (!token) {
    return <Navigate to="/admin/login" replace />
  }
  return children
}

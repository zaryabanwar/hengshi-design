import type {
  LeadCreate,
  LeadResponse,
  Project,
  Service,
  ServiceCategoryKey,
  WorldResponse
} from './types'

const DEFAULT_API_BASE_URL = 'http://127.0.0.1:8000'
const API_BASE_URL = (import.meta.env.VITE_API_BASE_URL || DEFAULT_API_BASE_URL).replace(/\/$/, '')

type ErrorDetailItem = { msg?: string }
type ErrorResponse = { detail?: string | ErrorDetailItem[] }

async function handleResponse<T>(response: Response): Promise<T> {
  if (response.ok) {
    if (response.status === 204) {
      return undefined as T
    }
    return response.json() as Promise<T>
  }

  let detail = `Request failed (${response.status})`
  try {
    const data = (await response.json()) as ErrorResponse
    if (Array.isArray(data?.detail)) {
      const messages = data.detail
        .map((item) => item?.msg)
        .filter(Boolean)
        .join(' ')
      if (messages) {
        detail = messages
      }
    } else if (typeof data?.detail === 'string') {
      detail = data.detail
    }
  } catch {
    // Ignore JSON parse errors
  }

  throw new Error(detail)
}

export async function fetchWorld(): Promise<WorldResponse> {
  const response = await fetch(`${API_BASE_URL}/api/world`)
  return handleResponse<WorldResponse>(response)
}

type LoginResponse = { access_token: string; token_type: string }

export async function loginAdmin(email: string, password: string): Promise<string> {
  const response = await fetch(`${API_BASE_URL}/api/auth/login`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email, password })
  })
  const data = await handleResponse<LoginResponse>(response)
  return data.access_token
}

function getAuthHeaders(): HeadersInit {
  const token = localStorage.getItem('admin_token')
  if (!token) {
    return {}
  }
  return { Authorization: `Bearer ${token}` }
}

export async function fetchAdminServices(): Promise<Service[]> {
  const response = await fetch(`${API_BASE_URL}/api/admin/services`, {
    headers: getAuthHeaders()
  })
  return handleResponse<Service[]>(response)
}

export async function createAdminService(payload: Partial<Service>): Promise<Service> {
  const response = await fetch(`${API_BASE_URL}/api/admin/services`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', ...getAuthHeaders() },
    body: JSON.stringify(payload)
  })
  return handleResponse<Service>(response)
}

export async function updateAdminService(id: string, payload: Partial<Service>): Promise<Service> {
  const response = await fetch(`${API_BASE_URL}/api/admin/services/${id}`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json', ...getAuthHeaders() },
    body: JSON.stringify(payload)
  })
  return handleResponse<Service>(response)
}

export async function deleteAdminService(id: string): Promise<void> {
  const response = await fetch(`${API_BASE_URL}/api/admin/services/${id}`, {
    method: 'DELETE',
    headers: getAuthHeaders()
  })
  await handleResponse<void>(response)
}

export async function fetchAdminProjects(): Promise<Project[]> {
  const response = await fetch(`${API_BASE_URL}/api/admin/projects`, {
    headers: getAuthHeaders()
  })
  return handleResponse<Project[]>(response)
}

export async function createAdminProject(payload: Partial<Project>): Promise<Project> {
  const response = await fetch(`${API_BASE_URL}/api/admin/projects`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', ...getAuthHeaders() },
    body: JSON.stringify(payload)
  })
  return handleResponse<Project>(response)
}

export async function updateAdminProject(id: string, payload: Partial<Project>): Promise<Project> {
  const response = await fetch(`${API_BASE_URL}/api/admin/projects/${id}`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json', ...getAuthHeaders() },
    body: JSON.stringify(payload)
  })
  return handleResponse<Project>(response)
}

export async function deleteAdminProject(id: string): Promise<void> {
  const response = await fetch(`${API_BASE_URL}/api/admin/projects/${id}`, {
    method: 'DELETE',
    headers: getAuthHeaders()
  })
  await handleResponse<void>(response)
}

export async function createAdminProjectMedia(
  projectId: string,
  payload: Partial<Project['media'][number]>
): Promise<Project['media'][number]> {
  const response = await fetch(`${API_BASE_URL}/api/admin/projects/${projectId}/media`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', ...getAuthHeaders() },
    body: JSON.stringify(payload)
  })
  return handleResponse<Project['media'][number]>(response)
}

export async function updateAdminProjectMedia(
  projectId: string,
  mediaId: string,
  payload: Partial<Project['media'][number]>
): Promise<Project['media'][number]> {
  const response = await fetch(`${API_BASE_URL}/api/admin/projects/${projectId}/media/${mediaId}`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json', ...getAuthHeaders() },
    body: JSON.stringify(payload)
  })
  return handleResponse<Project['media'][number]>(response)
}

export async function deleteAdminProjectMedia(
  projectId: string,
  mediaId: string
): Promise<void> {
  const response = await fetch(`${API_BASE_URL}/api/admin/projects/${projectId}/media/${mediaId}`, {
    method: 'DELETE',
    headers: getAuthHeaders()
  })
  await handleResponse<void>(response)
}

export async function fetchAdminWorldNodes(): Promise<WorldResponse['nodes']> {
  const response = await fetch(`${API_BASE_URL}/api/admin/world/nodes`, {
    headers: getAuthHeaders()
  })
  return handleResponse<WorldResponse['nodes']>(response)
}

export async function createAdminWorldNode(payload: Partial<WorldResponse['nodes'][number]>): Promise<WorldResponse['nodes'][number]> {
  const response = await fetch(`${API_BASE_URL}/api/admin/world/nodes`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', ...getAuthHeaders() },
    body: JSON.stringify(payload)
  })
  return handleResponse<WorldResponse['nodes'][number]>(response)
}

export async function updateAdminWorldNode(
  id: string,
  payload: Partial<WorldResponse['nodes'][number]>
): Promise<WorldResponse['nodes'][number]> {
  const response = await fetch(`${API_BASE_URL}/api/admin/world/nodes/${id}`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json', ...getAuthHeaders() },
    body: JSON.stringify(payload)
  })
  return handleResponse<WorldResponse['nodes'][number]>(response)
}

export async function deleteAdminWorldNode(id: string): Promise<void> {
  const response = await fetch(`${API_BASE_URL}/api/admin/world/nodes/${id}`, {
    method: 'DELETE',
    headers: getAuthHeaders()
  })
  await handleResponse<void>(response)
}

export async function fetchAdminWorldHotspots(nodeKey?: string): Promise<WorldResponse['nodes'][number]['hotspots']> {
  const url = new URL(`${API_BASE_URL}/api/admin/world/hotspots`)
  if (nodeKey) {
    url.searchParams.set('node_key', nodeKey)
  }
  const response = await fetch(url.toString(), {
    headers: getAuthHeaders()
  })
  return handleResponse<WorldResponse['nodes'][number]['hotspots']>(response)
}

export async function createAdminWorldHotspot(payload: Partial<WorldResponse['nodes'][number]['hotspots'][number]> & { node_id: string }): Promise<WorldResponse['nodes'][number]['hotspots'][number]> {
  const response = await fetch(`${API_BASE_URL}/api/admin/world/hotspots`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', ...getAuthHeaders() },
    body: JSON.stringify(payload)
  })
  return handleResponse<WorldResponse['nodes'][number]['hotspots'][number]>(response)
}

export async function updateAdminWorldHotspot(
  id: string,
  payload: Partial<WorldResponse['nodes'][number]['hotspots'][number]>
): Promise<WorldResponse['nodes'][number]['hotspots'][number]> {
  const response = await fetch(`${API_BASE_URL}/api/admin/world/hotspots/${id}`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json', ...getAuthHeaders() },
    body: JSON.stringify(payload)
  })
  return handleResponse<WorldResponse['nodes'][number]['hotspots'][number]>(response)
}

export async function deleteAdminWorldHotspot(id: string): Promise<void> {
  const response = await fetch(`${API_BASE_URL}/api/admin/world/hotspots/${id}`, {
    method: 'DELETE',
    headers: getAuthHeaders()
  })
  await handleResponse<void>(response)
}

export async function fetchServices(category?: ServiceCategoryKey): Promise<Service[]> {
  const url = new URL(`${API_BASE_URL}/api/services`)
  if (category) {
    url.searchParams.set('category', category)
  }
  const response = await fetch(url.toString())
  return handleResponse<Service[]>(response)
}

export async function fetchProjects(params?: {
  q?: string
  tag?: string
  featured?: boolean
}): Promise<Project[]> {
  const url = new URL(`${API_BASE_URL}/api/projects`)
  if (params?.q) {
    url.searchParams.set('q', params.q)
  }
  if (params?.tag) {
    url.searchParams.set('tag', params.tag)
  }
  if (typeof params?.featured === 'boolean') {
    url.searchParams.set('featured', String(params.featured))
  }
  const response = await fetch(url.toString())
  return handleResponse<Project[]>(response)
}

export async function fetchProject(slug: string): Promise<Project> {
  const response = await fetch(`${API_BASE_URL}/api/projects/${slug}`)
  return handleResponse<Project>(response)
}

export async function createLead(payload: LeadCreate): Promise<LeadResponse> {
  const response = await fetch(`${API_BASE_URL}/api/leads`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload)
  })
  return handleResponse<LeadResponse>(response)
}

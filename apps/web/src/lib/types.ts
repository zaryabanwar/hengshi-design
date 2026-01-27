export type ServiceCategoryKey =
  | 'strategy_architecture'
  | 'platform_engineering'
  | 'ai_systems'
  | 'spatial_immersive'
  | 'product_design'
  | 'cloud_devops'
  | 'security_trust'
  | 'data_platforms'
  | 'commerce_growth'

export type Service = {
  id: string
  slug: string
  title: string
  category: ServiceCategoryKey
  summary: string
  body: string
  deliverables: string[]
  tags?: string[] | null
  is_featured: boolean
  sort_order: number
  created_at?: string
  updated_at?: string
}

export type ProjectMedia = {
  id: string
  type: 'image' | 'video'
  url: string
  caption?: string | null
  sort_order: number
  created_at: string
}

export type Project = {
  id: string
  slug: string
  title: string
  summary: string
  body: string
  tags?: string[] | null
  is_featured: boolean
  sort_order: number
  created_at?: string
  updated_at?: string
  media: ProjectMedia[]
}

export type LeadCreate = {
  name: string
  email: string
  company?: string
  phone?: string
  subject?: string
  message: string
  source_url?: string
  metadata?: Record<string, unknown>
}

export type LeadResponse = {
  id: string
  created_at: string
}

export type WorldHotspotKind = 'OPEN_PANEL' | 'NAVIGATE_NODE' | 'OPEN_URL'

export type WorldHotspot = {
  id: string
  node_id: string
  key: string
  title: string
  description?: string | null
  kind: WorldHotspotKind
  position: [number, number, number]
  normal?: [number, number, number] | null
  radius: number
  icon?: string | null
  payload?: Record<string, unknown> | null
  sort_order: number
  is_enabled: boolean
  created_at: string
}

export type WorldNode = {
  id: string
  key: string
  title: string
  description?: string | null
  is_entry: boolean
  sort_order: number
  camera_position: [number, number, number]
  camera_target: [number, number, number]
  camera_fov: number
  environment?: Record<string, unknown> | null
  created_at: string
  updated_at: string
  hotspots: WorldHotspot[]
}

export type WorldResponse = {
  nodes: WorldNode[]
}

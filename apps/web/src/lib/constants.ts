import type { ServiceCategoryKey } from './types'

export const SERVICE_CATEGORIES: { key: ServiceCategoryKey; label: string }[] = [
  { key: 'strategy_architecture', label: 'Strategy & Architecture' },
  { key: 'platform_engineering', label: 'Platform & Product Engineering' },
  { key: 'ai_systems', label: 'AI Systems & Automation' },
  { key: 'spatial_immersive', label: 'Spatial & Immersive' },
  { key: 'product_design', label: 'Product Design' },
  { key: 'cloud_devops', label: 'Cloud & DevOps' },
  { key: 'security_trust', label: 'Security & Trust' },
  { key: 'data_platforms', label: 'Data Platforms' },
  { key: 'commerce_growth', label: 'Commerce & Growth' }
]

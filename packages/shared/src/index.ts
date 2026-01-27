import { z } from 'zod'

export const EmailSchema = z.string().email()

export const UserSchema = z.object({
  id: z.string().uuid(),
  email: EmailSchema,
  displayName: z.string().min(1)
})

export type User = z.infer<typeof UserSchema>

export const ProjectSchema = z.object({
  id: z.string().uuid(),
  title: z.string().min(1),
  slug: z.string().min(1),
  summary: z.string().optional()
})

export type Project = z.infer<typeof ProjectSchema>

const kebabCaseRegex = /^[a-z0-9]+(?:-[a-z0-9]+)*$/

export const ServiceCategory = z.enum([
  'strategy_architecture',
  'platform_engineering',
  'ai_systems',
  'spatial_immersive',
  'product_design',
  'cloud_devops',
  'security_trust',
  'data_platforms',
  'commerce_growth'
])

export type ServiceCategoryType = z.infer<typeof ServiceCategory>

export const ServiceCreateSchema = z.object({
  slug: z.string().min(1).regex(kebabCaseRegex, 'Expected kebab-case'),
  title: z.string().min(2).max(120),
  category: ServiceCategory,
  summary: z.string().min(10).max(240),
  body: z.string().min(20),
  deliverables: z.array(z.string().min(1)).min(1).max(20),
  tags: z.array(z.string().min(1)).max(20).optional(),
  is_featured: z.boolean().default(false),
  sort_order: z.number().int().min(0).default(0)
})

export const ServiceUpdateSchema = ServiceCreateSchema.partial().extend({
  is_featured: z.boolean().optional()
})

export const ServiceSchema = ServiceCreateSchema.extend({
  id: z.string().uuid(),
  created_at: z.string().datetime().optional(),
  updated_at: z.string().datetime().optional()
})

export type ServiceType = z.infer<typeof ServiceSchema>
export type ServiceCreateType = z.infer<typeof ServiceCreateSchema>
export type ServiceUpdateType = z.infer<typeof ServiceUpdateSchema>

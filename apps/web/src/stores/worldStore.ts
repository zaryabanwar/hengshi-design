import { create } from 'zustand'

import {
  createLead,
  fetchProject,
  fetchProjects,
  fetchServices,
  fetchWorld
} from '../lib/api'
import type {
  LeadCreate,
  LeadResponse,
  Project,
  Service,
  ServiceCategoryKey,
  WorldNode
} from '../lib/types'

export type PanelType = 'service_category' | 'project' | 'projects' | 'contact'

export type ActivePanel = {
  type: PanelType
  payload?: Record<string, unknown>
}

export type EntryPhase = 'idle' | 'drone' | 'atDoor' | 'inside'

type WorldState = {
  nodes: WorldNode[]
  currentNodeKey: string | null
  isTransitioning: boolean
  entryPhase: EntryPhase
  activePanel: ActivePanel | null
  error: string | null
  servicesByCategory: Record<string, Service[]>
  projects: Project[] | null
  projectBySlug: Record<string, Project>
  loadWorld: () => Promise<void>
  setNode: (key: string) => void
  transitionTo: (key: string) => void
  setTransitioning: (value: boolean) => void
  setEntryPhase: (phase: EntryPhase) => void
  openPanel: (panel: ActivePanel) => void
  closePanel: () => void
  getServicesByCategory: (category: ServiceCategoryKey) => Promise<Service[]>
  getProjects: () => Promise<Project[]>
  getProject: (slug: string) => Promise<Project>
  submitLead: (payload: LeadCreate) => Promise<LeadResponse>
}

export const useWorldStore = create<WorldState>((set, get) => ({
  nodes: [],
  currentNodeKey: null,
  isTransitioning: false,
  entryPhase: 'idle',
  activePanel: null,
  error: null,
  servicesByCategory: {},
  projects: null,
  projectBySlug: {},
  loadWorld: async () => {
    try {
      const data = await fetchWorld()
      const nodes = data.nodes ?? []
      const entryNode = nodes.find((node) => node.is_entry) ?? nodes[0]
      set({
        nodes,
        currentNodeKey: entryNode ? entryNode.key : null,
        error: null
      })
    } catch (err) {
      set({ error: err instanceof Error ? err.message : 'Failed to load world data' })
    }
  },
  setNode: (key: string) => {
    const { currentNodeKey } = get()
    if (currentNodeKey === key) {
      return
    }
    set({ currentNodeKey: key, activePanel: null })
  },
  transitionTo: (key: string) => {
    const { nodes } = get()
    const targetKey =
      nodes.find((node) => node.key === key)?.key ??
      nodes.find((node) => node.key !== 'exterior')?.key ??
      nodes[0]?.key ??
      null

    if (!targetKey) {
      return
    }

    set({ currentNodeKey: targetKey, entryPhase: 'inside', activePanel: null })
  },
  setTransitioning: (value: boolean) => set({ isTransitioning: value }),
  setEntryPhase: (phase: EntryPhase) =>
    set((state) => ({
      entryPhase: phase,
      activePanel: phase === 'inside' ? state.activePanel : null
    })),
  openPanel: (panel: ActivePanel) => {
    const normalized: ActivePanel = {
      ...panel,
      type: panel.type === 'projects' ? 'project' : panel.type
    }
    set({ activePanel: normalized })
  },
  closePanel: () => set({ activePanel: null }),
  getServicesByCategory: async (category: ServiceCategoryKey) => {
    const cached = get().servicesByCategory[category]
    if (cached) {
      return cached
    }
    const services = await fetchServices(category)
    set((state) => ({
      servicesByCategory: { ...state.servicesByCategory, [category]: services }
    }))
    return services
  },
  getProjects: async () => {
    const cached = get().projects
    if (cached) {
      return cached
    }
    const projects = await fetchProjects()
    set({ projects })
    return projects
  },
  getProject: async (slug: string) => {
    const cached = get().projectBySlug[slug]
    if (cached) {
      return cached
    }

    const list = get().projects
    const fromList = list?.find((project) => project.slug === slug)
    if (fromList) {
      set((state) => ({
        projectBySlug: { ...state.projectBySlug, [slug]: fromList }
      }))
      return fromList
    }

    const project = await fetchProject(slug)
    set((state) => ({
      projectBySlug: { ...state.projectBySlug, [slug]: project }
    }))
    return project
  },
  submitLead: async (payload: LeadCreate) => createLead(payload)
}))

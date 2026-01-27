import { useMemo } from 'react'

import { useWorldStore } from '../stores/worldStore'
import type { ServiceCategoryKey, WorldNode } from '../lib/types'

const buildContactPanel = () => ({ type: 'contact' as const, payload: { panel: 'contact' } })

const SERVICE_CATEGORIES: ServiceCategoryKey[] = [
  'strategy_architecture',
  'platform_engineering',
  'ai_systems',
  'spatial_immersive',
  'product_design',
  'cloud_devops',
  'security_trust',
  'data_platforms',
  'commerce_growth'
]

const serviceCategorySet = new Set<ServiceCategoryKey>(SERVICE_CATEGORIES)

const resolveServiceCategory = (node?: WorldNode): ServiceCategoryKey => {
  const key = node?.key as ServiceCategoryKey | undefined
  if (key && serviceCategorySet.has(key)) {
    return key
  }
  return 'strategy_architecture'
}

const buildServicesPanel = (node?: WorldNode) => ({
  type: 'service_category' as const,
  payload: { panel: 'service_category', category: resolveServiceCategory(node) }
})

const buildProjectsPanel = () => ({
  type: 'project' as const,
  payload: { panel: 'project' }
})

export const WorldHUD = () => {
  const { nodes, currentNodeKey, setNode, openPanel, isTransitioning, entryPhase } =
    useWorldStore()

  if (entryPhase !== 'inside') {
    return null
  }

  const orderedNodes = useMemo(
    () =>
      [...nodes].sort((a, b) =>
        a.sort_order === b.sort_order
          ? a.title.localeCompare(b.title)
          : a.sort_order - b.sort_order
      ),
    [nodes]
  )

  const currentNodeIndex = orderedNodes.findIndex((node) => node.key === currentNodeKey)
  const currentNode = orderedNodes[currentNodeIndex] ?? orderedNodes[0]
  const hotspotCount = currentNode?.hotspots?.length ?? 0

  const goToIndex = (index: number) => {
    if (!orderedNodes.length) {
      return
    }
    const nextIndex = (index + orderedNodes.length) % orderedNodes.length
    setNode(orderedNodes[nextIndex].key)
  }

  return (
    <div className="pointer-events-none fixed inset-x-0 top-0 z-10 p-4">
      <div className="pointer-events-auto flex flex-wrap items-center justify-between gap-4 rounded-lg bg-slate-900/80 px-4 py-3 text-white shadow-lg">
        <div>
          <div className="text-sm uppercase tracking-[0.2em] text-slate-400">World</div>
          <div className="text-xl font-semibold">{currentNode?.title ?? 'Loading...'}</div>
          <div className="text-xs text-slate-400">
            Node: {currentNode?.key ?? 'none'} · Hotspots: {hotspotCount}
          </div>
        </div>

        <div className="flex flex-wrap items-center gap-2">
          <button
            className="rounded-full border border-slate-600 px-3 py-1 text-sm hover:border-white"
            onClick={() => goToIndex(currentNodeIndex - 1)}
            disabled={isTransitioning || !orderedNodes.length}
          >
            Prev
          </button>
          <button
            className="rounded-full border border-slate-600 px-3 py-1 text-sm hover:border-white"
            onClick={() => goToIndex(currentNodeIndex + 1)}
            disabled={isTransitioning || !orderedNodes.length}
          >
            Next
          </button>
          <button
            className="rounded-full border border-slate-600 px-3 py-1 text-sm hover:border-white"
            onClick={() => openPanel(buildServicesPanel(currentNode))}
            disabled={isTransitioning}
          >
            Services
          </button>
          <button
            className="rounded-full border border-slate-600 px-3 py-1 text-sm hover:border-white"
            onClick={() => openPanel(buildProjectsPanel())}
            disabled={isTransitioning}
          >
            Projects
          </button>
          <button
            className="rounded-full border border-slate-600 px-3 py-1 text-sm hover:border-white"
            onClick={() => openPanel(buildContactPanel())}
            disabled={isTransitioning}
          >
            Contact
          </button>
          <label className="ml-2 text-xs text-slate-400">
            Jump:
            <select
              className="ml-2 rounded border border-slate-600 bg-slate-900 px-2 py-1 text-sm"
              value={currentNode?.key ?? ''}
              onChange={(event) => setNode(event.target.value)}
              disabled={isTransitioning}
            >
              {orderedNodes.map((node) => (
                <option key={node.key} value={node.key}>
                  {node.title}
                </option>
              ))}
            </select>
          </label>
        </div>
      </div>
    </div>
  )
}

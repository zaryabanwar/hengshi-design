import { useEffect, useMemo, useState } from 'react'

import {
  createAdminWorldHotspot,
  createAdminWorldNode,
  deleteAdminWorldHotspot,
  deleteAdminWorldNode,
  fetchAdminWorldHotspots,
  fetchAdminWorldNodes,
  updateAdminWorldHotspot,
  updateAdminWorldNode
} from '../lib/api'
import type { WorldHotspot, WorldNode } from '../lib/types'

type NodeFormState = {
  key: string
  title: string
  description: string
  is_entry: boolean
  sort_order: number
  camera_position: string
  camera_target: string
  camera_fov: number
  environment: string
}

type HotspotFormState = {
  key: string
  title: string
  description: string
  kind: WorldHotspot['kind']
  position: string
  normal: string
  radius: number
  icon: string
  payload: string
  sort_order: number
  is_enabled: boolean
}

const emptyNodeForm = (): NodeFormState => ({
  key: '',
  title: '',
  description: '',
  is_entry: false,
  sort_order: 0,
  camera_position: '[0,1.6,6]',
  camera_target: '[0,1.6,0]',
  camera_fov: 50,
  environment: '{}'
})

const emptyHotspotForm = (): HotspotFormState => ({
  key: '',
  title: '',
  description: '',
  kind: 'OPEN_PANEL',
  position: '[0,1.2,-1]',
  normal: '',
  radius: 0.35,
  icon: '',
  payload: '{ "panel": "service_category", "category": "strategy_architecture" }',
  sort_order: 0,
  is_enabled: true
})

const parseJson = (value: string, fallback: unknown) => {
  try {
    return value ? JSON.parse(value) : fallback
  } catch {
    return fallback
  }
}

export const WorldAdminPage = () => {
  const [nodes, setNodes] = useState<WorldNode[]>([])
  const [hotspots, setHotspots] = useState<WorldHotspot[]>([])
  const [selectedNodeKey, setSelectedNodeKey] = useState<string | null>(null)
  const [nodeForm, setNodeForm] = useState<NodeFormState>(emptyNodeForm())
  const [editingNodeId, setEditingNodeId] = useState<string | null>(null)
  const [hotspotForm, setHotspotForm] = useState<HotspotFormState>(emptyHotspotForm())
  const [editingHotspotId, setEditingHotspotId] = useState<string | null>(null)
  const [error, setError] = useState<string | null>(null)

  const selectedNode = nodes.find((node) => node.key === selectedNodeKey)

  const loadNodes = async () => {
    try {
      const data = await fetchAdminWorldNodes()
      setNodes(data)
      if (!selectedNodeKey && data.length) {
        setSelectedNodeKey(data[0].key)
      }
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to load nodes')
    }
  }

  const loadHotspots = async (nodeKey?: string | null) => {
    if (!nodeKey) {
      setHotspots([])
      return
    }
    try {
      const data = await fetchAdminWorldHotspots(nodeKey)
      setHotspots(data)
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to load hotspots')
    }
  }

  useEffect(() => {
    loadNodes()
  }, [])

  useEffect(() => {
    loadHotspots(selectedNodeKey)
  }, [selectedNodeKey])

  const orderedNodes = useMemo(
    () =>
      [...nodes].sort((a, b) =>
        a.sort_order === b.sort_order
          ? a.title.localeCompare(b.title)
          : a.sort_order - b.sort_order
      ),
    [nodes]
  )

  const orderedHotspots = useMemo(
    () =>
      [...hotspots].sort((a, b) =>
        a.sort_order === b.sort_order
          ? a.title.localeCompare(b.title)
          : a.sort_order - b.sort_order
      ),
    [hotspots]
  )

  const handleNodeEdit = (node: WorldNode) => {
    setEditingNodeId(node.id)
    setNodeForm({
      key: node.key,
      title: node.title,
      description: node.description ?? '',
      is_entry: node.is_entry,
      sort_order: node.sort_order,
      camera_position: JSON.stringify(node.camera_position),
      camera_target: JSON.stringify(node.camera_target),
      camera_fov: node.camera_fov,
      environment: JSON.stringify(node.environment ?? {})
    })
  }

  const handleNodeSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault()
    setError(null)
    const payload = {
      key: nodeForm.key,
      title: nodeForm.title,
      description: nodeForm.description || undefined,
      is_entry: nodeForm.is_entry,
      sort_order: nodeForm.sort_order,
      camera_position: parseJson(nodeForm.camera_position, [0, 1.6, 6]),
      camera_target: parseJson(nodeForm.camera_target, [0, 1.6, 0]),
      camera_fov: nodeForm.camera_fov,
      environment: parseJson(nodeForm.environment, {})
    }
    try {
      if (editingNodeId) {
        await updateAdminWorldNode(editingNodeId, payload)
      } else {
        await createAdminWorldNode(payload)
      }
      setNodeForm(emptyNodeForm())
      setEditingNodeId(null)
      await loadNodes()
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Save failed')
    }
  }

  const handleNodeDelete = async (nodeId: string) => {
    if (!confirm('Delete this node and its hotspots?')) {
      return
    }
    try {
      await deleteAdminWorldNode(nodeId)
      await loadNodes()
      setSelectedNodeKey(null)
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Delete failed')
    }
  }

  const handleHotspotEdit = (hotspot: WorldHotspot) => {
    setEditingHotspotId(hotspot.id)
    setHotspotForm({
      key: hotspot.key,
      title: hotspot.title,
      description: hotspot.description ?? '',
      kind: hotspot.kind,
      position: JSON.stringify(hotspot.position),
      normal: hotspot.normal ? JSON.stringify(hotspot.normal) : '',
      radius: hotspot.radius,
      icon: hotspot.icon ?? '',
      payload: JSON.stringify(hotspot.payload ?? {}),
      sort_order: hotspot.sort_order,
      is_enabled: hotspot.is_enabled
    })
  }

  const handleHotspotSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault()
    if (!selectedNode) {
      setError('Select a node first.')
      return
    }

    const payload = {
      node_id: selectedNode.id,
      key: hotspotForm.key,
      title: hotspotForm.title,
      description: hotspotForm.description || undefined,
      kind: hotspotForm.kind,
      position: parseJson(hotspotForm.position, [0, 1.2, -1]),
      normal: hotspotForm.normal ? parseJson(hotspotForm.normal, null) : undefined,
      radius: hotspotForm.radius,
      icon: hotspotForm.icon || undefined,
      payload: parseJson(hotspotForm.payload, {}),
      sort_order: hotspotForm.sort_order,
      is_enabled: hotspotForm.is_enabled
    }

    try {
      if (editingHotspotId) {
        await updateAdminWorldHotspot(editingHotspotId, payload)
      } else {
        await createAdminWorldHotspot(payload)
      }
      setHotspotForm(emptyHotspotForm())
      setEditingHotspotId(null)
      await loadHotspots(selectedNode.key)
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Save failed')
    }
  }

  const handleHotspotDelete = async (hotspotId: string) => {
    if (!confirm('Delete this hotspot?')) {
      return
    }
    try {
      await deleteAdminWorldHotspot(hotspotId)
      await loadHotspots(selectedNodeKey)
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Delete failed')
    }
  }

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-semibold">World</h1>
        <p className="text-sm text-slate-400">Edit world nodes and hotspots.</p>
      </div>

      {error && <p className="text-sm text-rose-300">{error}</p>}

      <div className="grid gap-6 lg:grid-cols-[2fr_1fr]">
        <div className="rounded-lg border border-slate-800 bg-slate-900/40 p-4">
          <div className="mb-3 text-sm text-slate-400">Nodes</div>
          <div className="space-y-3">
            {orderedNodes.map((node) => (
              <div
                key={node.id}
                className={`flex items-start justify-between rounded border px-3 py-3 ${
                  selectedNodeKey === node.key
                    ? 'border-sky-500/60 bg-sky-500/10'
                    : 'border-slate-800'
                }`}
              >
                <button className="text-left" onClick={() => setSelectedNodeKey(node.key)}>
                  <div className="font-semibold">{node.title}</div>
                  <div className="text-xs text-slate-400">{node.key}</div>
                </button>
                <div className="flex gap-2">
                  <button
                    className="rounded border border-slate-700 px-2 py-1 text-xs hover:border-white"
                    onClick={() => handleNodeEdit(node)}
                  >
                    Edit
                  </button>
                  <button
                    className="rounded border border-rose-500/60 px-2 py-1 text-xs text-rose-200 hover:border-rose-300"
                    onClick={() => handleNodeDelete(node.id)}
                  >
                    Delete
                  </button>
                </div>
              </div>
            ))}
          </div>
        </div>

        <form
          className="rounded-lg border border-slate-800 bg-slate-900/40 p-4"
          onSubmit={handleNodeSubmit}
        >
          <div className="mb-4 text-sm text-slate-400">
            {editingNodeId ? 'Edit node' : 'Create node'}
          </div>
          <div className="space-y-3">
            <input
              className="w-full rounded border border-slate-700 bg-slate-900 px-3 py-2 text-sm"
              placeholder="Key"
              value={nodeForm.key}
              onChange={(event) => setNodeForm({ ...nodeForm, key: event.target.value })}
              required
            />
            <input
              className="w-full rounded border border-slate-700 bg-slate-900 px-3 py-2 text-sm"
              placeholder="Title"
              value={nodeForm.title}
              onChange={(event) => setNodeForm({ ...nodeForm, title: event.target.value })}
              required
            />
            <textarea
              className="min-h-[60px] w-full rounded border border-slate-700 bg-slate-900 px-3 py-2 text-sm"
              placeholder="Description (optional)"
              value={nodeForm.description}
              onChange={(event) => setNodeForm({ ...nodeForm, description: event.target.value })}
            />
            <label className="flex items-center gap-2 text-sm">
              <input
                type="checkbox"
                checked={nodeForm.is_entry}
                onChange={(event) => setNodeForm({ ...nodeForm, is_entry: event.target.checked })}
              />
              Entry node
            </label>
            <input
              className="w-full rounded border border-slate-700 bg-slate-900 px-3 py-2 text-sm"
              placeholder='Camera position JSON, e.g. [0,1.6,6]'
              value={nodeForm.camera_position}
              onChange={(event) => setNodeForm({ ...nodeForm, camera_position: event.target.value })}
            />
            <input
              className="w-full rounded border border-slate-700 bg-slate-900 px-3 py-2 text-sm"
              placeholder='Camera target JSON, e.g. [0,1.6,0]'
              value={nodeForm.camera_target}
              onChange={(event) => setNodeForm({ ...nodeForm, camera_target: event.target.value })}
            />
            <input
              className="w-24 rounded border border-slate-700 bg-slate-900 px-2 py-1 text-sm"
              type="number"
              value={nodeForm.camera_fov}
              onChange={(event) => setNodeForm({ ...nodeForm, camera_fov: Number(event.target.value) })}
              min={20}
              max={90}
            />
            <input
              className="w-24 rounded border border-slate-700 bg-slate-900 px-2 py-1 text-sm"
              type="number"
              value={nodeForm.sort_order}
              onChange={(event) => setNodeForm({ ...nodeForm, sort_order: Number(event.target.value) })}
              min={0}
            />
            <textarea
              className="min-h-[60px] w-full rounded border border-slate-700 bg-slate-900 px-3 py-2 text-sm"
              placeholder='Environment JSON (optional)'
              value={nodeForm.environment}
              onChange={(event) => setNodeForm({ ...nodeForm, environment: event.target.value })}
            />
            <button
              className="w-full rounded border border-slate-600 px-4 py-2 text-sm hover:border-white"
              type="submit"
            >
              {editingNodeId ? 'Update node' : 'Create node'}
            </button>
            {editingNodeId && (
              <button
                type="button"
                className="w-full rounded border border-slate-700 px-4 py-2 text-sm text-slate-300 hover:text-white"
                onClick={() => {
                  setEditingNodeId(null)
                  setNodeForm(emptyNodeForm())
                }}
              >
                Cancel
              </button>
            )}
          </div>
        </form>
      </div>

      <div className="grid gap-6 lg:grid-cols-[2fr_1fr]">
        <div className="rounded-lg border border-slate-800 bg-slate-900/40 p-4">
          <div className="mb-3 text-sm text-slate-400">
            Hotspots for {selectedNode?.title ?? 'Select a node'}
          </div>
          <div className="space-y-2">
            {orderedHotspots.map((hotspot) => (
              <div key={hotspot.id} className="flex items-start justify-between rounded border border-slate-800 px-3 py-2 text-sm">
                <div>
                  <div className="font-semibold">{hotspot.title}</div>
                  <div className="text-xs text-slate-400">{hotspot.key}</div>
                  <div className="text-xs text-slate-500">{hotspot.kind}</div>
                </div>
                <div className="flex gap-2">
                  <button
                    className="rounded border border-slate-700 px-2 py-1 text-xs hover:border-white"
                    onClick={() => handleHotspotEdit(hotspot)}
                  >
                    Edit
                  </button>
                  <button
                    className="rounded border border-rose-500/60 px-2 py-1 text-xs text-rose-200 hover:border-rose-300"
                    onClick={() => handleHotspotDelete(hotspot.id)}
                  >
                    Delete
                  </button>
                </div>
              </div>
            ))}
            {!orderedHotspots.length && (
              <p className="text-sm text-slate-500">No hotspots yet.</p>
            )}
          </div>
        </div>

        <form
          className="rounded-lg border border-slate-800 bg-slate-900/40 p-4"
          onSubmit={handleHotspotSubmit}
        >
          <div className="mb-4 text-sm text-slate-400">
            {editingHotspotId ? 'Edit hotspot' : 'Create hotspot'}
          </div>
          <div className="space-y-3">
            <input
              className="w-full rounded border border-slate-700 bg-slate-900 px-3 py-2 text-sm"
              placeholder="Key"
              value={hotspotForm.key}
              onChange={(event) => setHotspotForm({ ...hotspotForm, key: event.target.value })}
              required
            />
            <input
              className="w-full rounded border border-slate-700 bg-slate-900 px-3 py-2 text-sm"
              placeholder="Title"
              value={hotspotForm.title}
              onChange={(event) => setHotspotForm({ ...hotspotForm, title: event.target.value })}
              required
            />
            <textarea
              className="min-h-[60px] w-full rounded border border-slate-700 bg-slate-900 px-3 py-2 text-sm"
              placeholder="Description (optional)"
              value={hotspotForm.description}
              onChange={(event) => setHotspotForm({ ...hotspotForm, description: event.target.value })}
            />
            <select
              className="w-full rounded border border-slate-700 bg-slate-900 px-3 py-2 text-sm"
              value={hotspotForm.kind}
              onChange={(event) =>
                setHotspotForm({
                  ...hotspotForm,
                  kind: event.target.value as WorldHotspot['kind']
                })
              }
            >
              <option value="OPEN_PANEL">OPEN_PANEL</option>
              <option value="NAVIGATE_NODE">NAVIGATE_NODE</option>
              <option value="OPEN_URL">OPEN_URL</option>
            </select>
            <input
              className="w-full rounded border border-slate-700 bg-slate-900 px-3 py-2 text-sm"
              placeholder='Position JSON, e.g. [0,1.2,-1]'
              value={hotspotForm.position}
              onChange={(event) => setHotspotForm({ ...hotspotForm, position: event.target.value })}
            />
            <input
              className="w-full rounded border border-slate-700 bg-slate-900 px-3 py-2 text-sm"
              placeholder="Normal JSON (optional)"
              value={hotspotForm.normal}
              onChange={(event) => setHotspotForm({ ...hotspotForm, normal: event.target.value })}
            />
            <input
              className="w-full rounded border border-slate-700 bg-slate-900 px-3 py-2 text-sm"
              placeholder="Payload JSON"
              value={hotspotForm.payload}
              onChange={(event) => setHotspotForm({ ...hotspotForm, payload: event.target.value })}
            />
            <input
              className="w-full rounded border border-slate-700 bg-slate-900 px-3 py-2 text-sm"
              placeholder="Icon (optional)"
              value={hotspotForm.icon}
              onChange={(event) => setHotspotForm({ ...hotspotForm, icon: event.target.value })}
            />
            <div className="flex items-center gap-3 text-sm">
              <input
                className="w-24 rounded border border-slate-700 bg-slate-900 px-2 py-1 text-sm"
                type="number"
                value={hotspotForm.radius}
                onChange={(event) => setHotspotForm({ ...hotspotForm, radius: Number(event.target.value) })}
                min={0.05}
                max={5}
                step={0.05}
              />
              <input
                className="w-24 rounded border border-slate-700 bg-slate-900 px-2 py-1 text-sm"
                type="number"
                value={hotspotForm.sort_order}
                onChange={(event) => setHotspotForm({ ...hotspotForm, sort_order: Number(event.target.value) })}
                min={0}
              />
              <label className="flex items-center gap-2 text-sm">
                <input
                  type="checkbox"
                  checked={hotspotForm.is_enabled}
                  onChange={(event) => setHotspotForm({ ...hotspotForm, is_enabled: event.target.checked })}
                />
                Enabled
              </label>
            </div>
            <button
              className="w-full rounded border border-slate-600 px-4 py-2 text-sm hover:border-white"
              type="submit"
              disabled={!selectedNode}
            >
              {editingHotspotId ? 'Update hotspot' : 'Create hotspot'}
            </button>
            {editingHotspotId && (
              <button
                type="button"
                className="w-full rounded border border-slate-700 px-4 py-2 text-sm text-slate-300 hover:text-white"
                onClick={() => {
                  setEditingHotspotId(null)
                  setHotspotForm(emptyHotspotForm())
                }}
              >
                Cancel
              </button>
            )}
          </div>
        </form>
      </div>
    </div>
  )
}

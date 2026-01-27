import { useEffect, useMemo, useState } from 'react'

import {
  createAdminService,
  deleteAdminService,
  fetchAdminServices,
  updateAdminService
} from '../lib/api'
import { SERVICE_CATEGORIES } from '../lib/constants'
import type { Service, ServiceCategoryKey } from '../lib/types'

type ServiceFormState = {
  slug: string
  title: string
  category: ServiceCategoryKey
  summary: string
  body: string
  deliverables: string
  tags: string
  is_featured: boolean
  sort_order: number
}

const emptyForm = (): ServiceFormState => ({
  slug: '',
  title: '',
  category: 'strategy_architecture',
  summary: '',
  body: '',
  deliverables: '',
  tags: '',
  is_featured: false,
  sort_order: 0
})

const parseTags = (value: string) =>
  value
    .split(',')
    .map((tag) => tag.trim())
    .filter(Boolean)

const parseDeliverables = (value: string) =>
  value
    .split('\n')
    .map((item) => item.trim())
    .filter(Boolean)

export const ServicesAdminPage = () => {
  const [services, setServices] = useState<Service[]>([])
  const [form, setForm] = useState<ServiceFormState>(emptyForm())
  const [editingId, setEditingId] = useState<string | null>(null)
  const [status, setStatus] = useState<'idle' | 'loading' | 'error'>('idle')
  const [error, setError] = useState<string | null>(null)

  const orderedServices = useMemo(
    () =>
      [...services].sort((a, b) =>
        a.sort_order === b.sort_order
          ? a.title.localeCompare(b.title)
          : a.sort_order - b.sort_order
      ),
    [services]
  )

  const loadServices = async () => {
    try {
      setStatus('loading')
      const data = await fetchAdminServices()
      setServices(data)
      setStatus('idle')
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to load services')
      setStatus('error')
    }
  }

  useEffect(() => {
    loadServices()
  }, [])

  const handleEdit = (service: Service) => {
    setEditingId(service.id)
    setForm({
      slug: service.slug,
      title: service.title,
      category: service.category,
      summary: service.summary,
      body: service.body,
      deliverables: service.deliverables.join('\n'),
      tags: (service.tags ?? []).join(', '),
      is_featured: service.is_featured,
      sort_order: service.sort_order
    })
  }

  const handleDelete = async (id: string) => {
    if (!confirm('Delete this service?')) {
      return
    }
    try {
      await deleteAdminService(id)
      await loadServices()
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Delete failed')
    }
  }

  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault()
    setError(null)

    const payload = {
      slug: form.slug,
      title: form.title,
      category: form.category,
      summary: form.summary,
      body: form.body,
      deliverables: parseDeliverables(form.deliverables),
      tags: parseTags(form.tags),
      is_featured: form.is_featured,
      sort_order: form.sort_order
    }

    try {
      if (editingId) {
        await updateAdminService(editingId, payload)
      } else {
        await createAdminService(payload)
      }
      setForm(emptyForm())
      setEditingId(null)
      await loadServices()
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Save failed')
    }
  }

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-semibold">Services</h1>
        <p className="text-sm text-slate-400">Manage service listings.</p>
      </div>

      {error && <p className="text-sm text-rose-300">{error}</p>}

      <div className="grid gap-6 lg:grid-cols-[2fr_1fr]">
        <div className="rounded-lg border border-slate-800 bg-slate-900/40 p-4">
          <div className="mb-3 text-sm text-slate-400">
            {status === 'loading' ? 'Loading services…' : `Total: ${services.length}`}
          </div>
          <div className="space-y-3">
            {orderedServices.map((service) => (
              <div
                key={service.id}
                className="flex items-start justify-between rounded border border-slate-800 px-3 py-3"
              >
                <div>
                  <div className="font-semibold">{service.title}</div>
                  <div className="text-xs text-slate-400">{service.slug}</div>
                  <div className="text-xs text-slate-500">{service.category}</div>
                </div>
                <div className="flex gap-2">
                  <button
                    className="rounded border border-slate-700 px-2 py-1 text-xs hover:border-white"
                    onClick={() => handleEdit(service)}
                  >
                    Edit
                  </button>
                  <button
                    className="rounded border border-rose-500/60 px-2 py-1 text-xs text-rose-200 hover:border-rose-300"
                    onClick={() => handleDelete(service.id)}
                  >
                    Delete
                  </button>
                </div>
              </div>
            ))}
            {!services.length && status !== 'loading' && (
              <p className="text-sm text-slate-500">No services yet.</p>
            )}
          </div>
        </div>

        <form
          className="rounded-lg border border-slate-800 bg-slate-900/40 p-4"
          onSubmit={handleSubmit}
        >
          <div className="mb-4 text-sm text-slate-400">
            {editingId ? 'Edit service' : 'Create service'}
          </div>
          <div className="space-y-3">
            <input
              className="w-full rounded border border-slate-700 bg-slate-900 px-3 py-2 text-sm"
              placeholder="Slug"
              value={form.slug}
              onChange={(event) => setForm({ ...form, slug: event.target.value })}
              required
            />
            <input
              className="w-full rounded border border-slate-700 bg-slate-900 px-3 py-2 text-sm"
              placeholder="Title"
              value={form.title}
              onChange={(event) => setForm({ ...form, title: event.target.value })}
              required
            />
            <select
              className="w-full rounded border border-slate-700 bg-slate-900 px-3 py-2 text-sm"
              value={form.category}
              onChange={(event) => setForm({ ...form, category: event.target.value as ServiceCategoryKey })}
            >
              {SERVICE_CATEGORIES.map((category) => (
                <option key={category.key} value={category.key}>
                  {category.label}
                </option>
              ))}
            </select>
            <textarea
              className="min-h-[80px] w-full rounded border border-slate-700 bg-slate-900 px-3 py-2 text-sm"
              placeholder="Summary"
              value={form.summary}
              onChange={(event) => setForm({ ...form, summary: event.target.value })}
              required
            />
            <textarea
              className="min-h-[120px] w-full rounded border border-slate-700 bg-slate-900 px-3 py-2 text-sm"
              placeholder="Body"
              value={form.body}
              onChange={(event) => setForm({ ...form, body: event.target.value })}
              required
            />
            <textarea
              className="min-h-[100px] w-full rounded border border-slate-700 bg-slate-900 px-3 py-2 text-sm"
              placeholder="Deliverables (one per line)"
              value={form.deliverables}
              onChange={(event) => setForm({ ...form, deliverables: event.target.value })}
              required
            />
            <input
              className="w-full rounded border border-slate-700 bg-slate-900 px-3 py-2 text-sm"
              placeholder="Tags (comma separated)"
              value={form.tags}
              onChange={(event) => setForm({ ...form, tags: event.target.value })}
            />
            <div className="flex items-center gap-3 text-sm">
              <label className="flex items-center gap-2">
                <input
                  type="checkbox"
                  checked={form.is_featured}
                  onChange={(event) => setForm({ ...form, is_featured: event.target.checked })}
                />
                Featured
              </label>
              <input
                className="w-24 rounded border border-slate-700 bg-slate-900 px-2 py-1 text-sm"
                type="number"
                value={form.sort_order}
                onChange={(event) => setForm({ ...form, sort_order: Number(event.target.value) })}
                min={0}
              />
              <span className="text-xs text-slate-400">Sort order</span>
            </div>
            <button
              className="w-full rounded border border-slate-600 px-4 py-2 text-sm hover:border-white"
              type="submit"
            >
              {editingId ? 'Update service' : 'Create service'}
            </button>
            {editingId && (
              <button
                type="button"
                className="w-full rounded border border-slate-700 px-4 py-2 text-sm text-slate-300 hover:text-white"
                onClick={() => {
                  setEditingId(null)
                  setForm(emptyForm())
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

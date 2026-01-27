import { useEffect, useMemo, useState } from 'react'

import {
  createAdminProject,
  createAdminProjectMedia,
  deleteAdminProject,
  deleteAdminProjectMedia,
  fetchAdminProjects,
  updateAdminProject,
  updateAdminProjectMedia
} from '../lib/api'
import type { Project, ProjectMedia } from '../lib/types'

type ProjectFormState = {
  slug: string
  title: string
  summary: string
  body: string
  tags: string
  is_featured: boolean
  sort_order: number
}

type MediaFormState = {
  type: 'image' | 'video'
  url: string
  caption: string
  sort_order: number
}

const emptyProjectForm = (): ProjectFormState => ({
  slug: '',
  title: '',
  summary: '',
  body: '',
  tags: '',
  is_featured: false,
  sort_order: 0
})

const emptyMediaForm = (): MediaFormState => ({
  type: 'image',
  url: '',
  caption: '',
  sort_order: 0
})

const parseTags = (value: string) =>
  value
    .split(',')
    .map((tag) => tag.trim())
    .filter(Boolean)

export const ProjectsAdminPage = () => {
  const [projects, setProjects] = useState<Project[]>([])
  const [selectedProjectId, setSelectedProjectId] = useState<string | null>(null)
  const [form, setForm] = useState<ProjectFormState>(emptyProjectForm())
  const [editingId, setEditingId] = useState<string | null>(null)
  const [mediaForm, setMediaForm] = useState<MediaFormState>(emptyMediaForm())
  const [editingMediaId, setEditingMediaId] = useState<string | null>(null)
  const [error, setError] = useState<string | null>(null)

  const orderedProjects = useMemo(
    () =>
      [...projects].sort((a, b) =>
        a.sort_order === b.sort_order
          ? a.title.localeCompare(b.title)
          : a.sort_order - b.sort_order
      ),
    [projects]
  )

  const selectedProject = projects.find((project) => project.id === selectedProjectId)

  const loadProjects = async () => {
    try {
      const data = await fetchAdminProjects()
      setProjects(data)
      if (data.length && !selectedProjectId) {
        setSelectedProjectId(data[0].id)
      }
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to load projects')
    }
  }

  useEffect(() => {
    loadProjects()
  }, [])

  const handleEdit = (project: Project) => {
    setEditingId(project.id)
    setForm({
      slug: project.slug,
      title: project.title,
      summary: project.summary,
      body: project.body,
      tags: (project.tags ?? []).join(', '),
      is_featured: project.is_featured,
      sort_order: project.sort_order
    })
  }

  const handleDelete = async (id: string) => {
    if (!confirm('Delete this project?')) {
      return
    }
    try {
      await deleteAdminProject(id)
      await loadProjects()
      if (selectedProjectId === id) {
        setSelectedProjectId(null)
      }
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
      summary: form.summary,
      body: form.body,
      tags: parseTags(form.tags),
      is_featured: form.is_featured,
      sort_order: form.sort_order
    }

    try {
      if (editingId) {
        await updateAdminProject(editingId, payload)
      } else {
        await createAdminProject(payload)
      }
      setForm(emptyProjectForm())
      setEditingId(null)
      await loadProjects()
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Save failed')
    }
  }

  const handleMediaEdit = (media: ProjectMedia) => {
    setEditingMediaId(media.id)
    setMediaForm({
      type: media.type,
      url: media.url,
      caption: media.caption ?? '',
      sort_order: media.sort_order
    })
  }

  const handleMediaSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault()
    if (!selectedProject) {
      return
    }

    const payload = {
      type: mediaForm.type,
      url: mediaForm.url,
      caption: mediaForm.caption || undefined,
      sort_order: mediaForm.sort_order
    }

    try {
      if (editingMediaId) {
        await updateAdminProjectMedia(selectedProject.id, editingMediaId, payload)
      } else {
        await createAdminProjectMedia(selectedProject.id, payload)
      }
      setMediaForm(emptyMediaForm())
      setEditingMediaId(null)
      await loadProjects()
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Media save failed')
    }
  }

  const handleMediaDelete = async (mediaId: string) => {
    if (!selectedProject) {
      return
    }
    if (!confirm('Delete this media item?')) {
      return
    }
    try {
      await deleteAdminProjectMedia(selectedProject.id, mediaId)
      await loadProjects()
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Delete failed')
    }
  }

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-semibold">Projects</h1>
        <p className="text-sm text-slate-400">Manage projects and media.</p>
      </div>

      {error && <p className="text-sm text-rose-300">{error}</p>}

      <div className="grid gap-6 lg:grid-cols-[2fr_1fr]">
        <div className="rounded-lg border border-slate-800 bg-slate-900/40 p-4">
          <div className="mb-3 text-sm text-slate-400">Total: {projects.length}</div>
          <div className="space-y-3">
            {orderedProjects.map((project) => (
              <div
                key={project.id}
                className={`flex items-start justify-between rounded border px-3 py-3 ${
                  selectedProjectId === project.id
                    ? 'border-sky-500/60 bg-sky-500/10'
                    : 'border-slate-800'
                }`}
              >
                <button
                  className="text-left"
                  onClick={() => setSelectedProjectId(project.id)}
                >
                  <div className="font-semibold">{project.title}</div>
                  <div className="text-xs text-slate-400">{project.slug}</div>
                </button>
                <div className="flex gap-2">
                  <button
                    className="rounded border border-slate-700 px-2 py-1 text-xs hover:border-white"
                    onClick={() => handleEdit(project)}
                  >
                    Edit
                  </button>
                  <button
                    className="rounded border border-rose-500/60 px-2 py-1 text-xs text-rose-200 hover:border-rose-300"
                    onClick={() => handleDelete(project.id)}
                  >
                    Delete
                  </button>
                </div>
              </div>
            ))}
            {!projects.length && (
              <p className="text-sm text-slate-500">No projects yet.</p>
            )}
          </div>
        </div>

        <form
          className="rounded-lg border border-slate-800 bg-slate-900/40 p-4"
          onSubmit={handleSubmit}
        >
          <div className="mb-4 text-sm text-slate-400">
            {editingId ? 'Edit project' : 'Create project'}
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
              {editingId ? 'Update project' : 'Create project'}
            </button>
            {editingId && (
              <button
                type="button"
                className="w-full rounded border border-slate-700 px-4 py-2 text-sm text-slate-300 hover:text-white"
                onClick={() => {
                  setEditingId(null)
                  setForm(emptyProjectForm())
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
            Media for {selectedProject?.title ?? 'Select a project'}
          </div>
          <div className="space-y-2">
            {selectedProject?.media?.map((media) => (
              <div key={media.id} className="flex items-start justify-between rounded border border-slate-800 px-3 py-2 text-sm">
                <div>
                  <div className="font-semibold">{media.type}</div>
                  <div className="text-xs text-slate-400">{media.caption ?? media.url}</div>
                </div>
                <div className="flex gap-2">
                  <button
                    className="rounded border border-slate-700 px-2 py-1 text-xs hover:border-white"
                    onClick={() => handleMediaEdit(media)}
                  >
                    Edit
                  </button>
                  <button
                    className="rounded border border-rose-500/60 px-2 py-1 text-xs text-rose-200 hover:border-rose-300"
                    onClick={() => handleMediaDelete(media.id)}
                  >
                    Delete
                  </button>
                </div>
              </div>
            ))}
            {!selectedProject?.media?.length && (
              <p className="text-sm text-slate-500">No media yet.</p>
            )}
          </div>
        </div>

        <form
          className="rounded-lg border border-slate-800 bg-slate-900/40 p-4"
          onSubmit={handleMediaSubmit}
        >
          <div className="mb-4 text-sm text-slate-400">
            {editingMediaId ? 'Edit media' : 'Add media'}
          </div>
          <div className="space-y-3">
            <select
              className="w-full rounded border border-slate-700 bg-slate-900 px-3 py-2 text-sm"
              value={mediaForm.type}
              onChange={(event) =>
                setMediaForm({ ...mediaForm, type: event.target.value as MediaFormState['type'] })
              }
            >
              <option value="image">image</option>
              <option value="video">video</option>
            </select>
            <input
              className="w-full rounded border border-slate-700 bg-slate-900 px-3 py-2 text-sm"
              placeholder="URL"
              value={mediaForm.url}
              onChange={(event) => setMediaForm({ ...mediaForm, url: event.target.value })}
              required
            />
            <input
              className="w-full rounded border border-slate-700 bg-slate-900 px-3 py-2 text-sm"
              placeholder="Caption (optional)"
              value={mediaForm.caption}
              onChange={(event) => setMediaForm({ ...mediaForm, caption: event.target.value })}
            />
            <input
              className="w-24 rounded border border-slate-700 bg-slate-900 px-2 py-1 text-sm"
              type="number"
              value={mediaForm.sort_order}
              onChange={(event) => setMediaForm({ ...mediaForm, sort_order: Number(event.target.value) })}
              min={0}
            />
            <button
              className="w-full rounded border border-slate-600 px-4 py-2 text-sm hover:border-white"
              type="submit"
              disabled={!selectedProject}
            >
              {editingMediaId ? 'Update media' : 'Add media'}
            </button>
            {editingMediaId && (
              <button
                type="button"
                className="w-full rounded border border-slate-700 px-4 py-2 text-sm text-slate-300 hover:text-white"
                onClick={() => {
                  setEditingMediaId(null)
                  setMediaForm(emptyMediaForm())
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

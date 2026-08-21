import { useEffect, useMemo, useState, type FormEvent } from 'react'

import { useWorldStore } from '../stores/worldStore'
import type { LeadCreate, Project, Service, ServiceCategoryKey } from '../lib/types'

type PanelStatus = 'idle' | 'loading' | 'success' | 'error'

export const WorldPanel = () => {
  const {
    activePanel,
    closePanel,
    getServicesByCategory,
    getProjects,
    getProject,
    submitLead,
    entryPhase
  } = useWorldStore()

  const [status, setStatus] = useState<PanelStatus>('idle')
  const [error, setError] = useState<string | null>(null)
  const [services, setServices] = useState<Service[]>([])
  const [selectedService, setSelectedService] = useState<Service | null>(null)
  const [projects, setProjects] = useState<Project[]>([])
  const [selectedProject, setSelectedProject] = useState<Project | null>(null)
  const [formData, setFormData] = useState<LeadCreate>({
    name: '',
    email: '',
    message: ''
  })
  const [leadSuccess, setLeadSuccess] = useState(false)

  const panelType = activePanel?.type
  const panelPayload = activePanel?.payload ?? {}

  const panelTitle = useMemo(() => {
    if (panelType === 'service_category') {
      return 'Services'
    }
    if (panelType === 'project') {
      return 'Projects'
    }
    if (panelType === 'contact') {
      return 'Contact'
    }
    return 'Panel'
  }, [panelType])

  useEffect(() => {
    if (!activePanel) {
      return
    }

    let isMounted = true
    setStatus('loading')
    setError(null)
    setLeadSuccess(false)

    const load = async () => {
      try {
        if (panelType === 'service_category') {
          const category = panelPayload.category as ServiceCategoryKey | undefined
          if (!category) {
            throw new Error('Service category missing in payload.')
          }
          const data = await getServicesByCategory(category)
          if (!isMounted) {
            return
          }
          setServices(data)
          setSelectedService(data[0] ?? null)
        }

        if (panelType === 'project') {
          const slug = panelPayload.project_slug as string | undefined
          if (slug) {
            const project = await getProject(slug)
            if (!isMounted) {
              return
            }
            setSelectedProject(project)
          } else {
            const list = await getProjects()
            if (!isMounted) {
              return
            }
            setProjects(list)
            setSelectedProject(list[0] ?? null)
          }
        }

        if (panelType === 'contact') {
          setFormData({ name: '', email: '', message: '' })
        }

        if (isMounted) {
          setStatus('idle')
        }
      } catch (err) {
        if (isMounted) {
          setError(err instanceof Error ? err.message : 'Failed to load panel data')
          setStatus('error')
        }
      }
    }

    load()

    return () => {
      isMounted = false
      setServices([])
      setProjects([])
      setSelectedService(null)
      setSelectedProject(null)
    }
  }, [activePanel, panelPayload.category, panelPayload.project_slug, panelType, getServicesByCategory, getProjects, getProject])

  const handleProjectSelect = async (slug: string) => {
    try {
      setStatus('loading')
      const project = await getProject(slug)
      setSelectedProject(project)
      setStatus('idle')
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to load project')
      setStatus('error')
    }
  }

  const handleLeadSubmit = async (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault()
    setStatus('loading')
    setError(null)
    try {
      await submitLead({
        ...formData,
        source_url: window.location.href
      })
      setLeadSuccess(true)
      setStatus('success')
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to submit lead')
      setStatus('error')
    }
  }

  if (!activePanel || entryPhase !== 'inside') {
    return null
  }

  return (
    <aside className="pointer-events-auto fixed right-0 top-0 z-20 h-full w-full max-w-md overflow-y-auto border-l border-slate-800 bg-slate-950/95 p-6 text-white shadow-xl">
      <div className="flex items-start justify-between gap-4">
        <div>
          <p className="text-xs uppercase tracking-[0.2em] text-slate-400">{panelType}</p>
          <h2 className="text-2xl font-semibold">{panelTitle}</h2>
          {typeof panelPayload.category === 'string' && (
            <p className="mt-1 text-xs text-slate-400">Category: {String(panelPayload.category)}</p>
          )}
        </div>
        <button
          className="rounded-full border border-slate-700 px-3 py-1 text-sm hover:border-white"
          onClick={closePanel}
        >
          Close
        </button>
      </div>

      {status === 'loading' && (
        <p className="mt-6 text-sm text-slate-300">Loading...</p>
      )}
      {status === 'error' && error && (
        <p className="mt-6 text-sm text-rose-300">{error}</p>
      )}

      {panelType === 'service_category' && status !== 'loading' && (
        <div className="mt-6 space-y-6">
          <div className="space-y-2">
            {services.map((service) => (
              <button
                key={service.id}
                className={`w-full rounded-lg border px-4 py-3 text-left text-sm ${
                  selectedService?.id === service.id
                    ? 'border-sky-400 bg-sky-500/10'
                    : 'border-slate-800 hover:border-slate-500'
                }`}
                onClick={() => setSelectedService(service)}
              >
                <div className="font-semibold">{service.title}</div>
                <div className="text-xs text-slate-400">{service.summary}</div>
              </button>
            ))}
          </div>
          {selectedService && (
            <div className="rounded-lg border border-slate-800 bg-slate-900/40 p-4">
              <h3 className="text-lg font-semibold">{selectedService.title}</h3>
              <p className="mt-2 text-sm text-slate-300">{selectedService.summary}</p>
              <p className="mt-3 text-sm text-slate-300">{selectedService.body}</p>
              {selectedService.deliverables?.length ? (
                <ul className="mt-3 list-disc space-y-1 pl-4 text-sm text-slate-300">
                  {selectedService.deliverables.map((item) => (
                    <li key={item}>{item}</li>
                  ))}
                </ul>
              ) : null}
            </div>
          )}
        </div>
      )}

      {panelType === 'project' && status !== 'loading' && (
        <div className="mt-6 space-y-6">
          {!panelPayload.project_slug && (
            <div className="space-y-2">
              {projects.map((project) => (
                <button
                  key={project.id}
                  className={`w-full rounded-lg border px-4 py-3 text-left text-sm ${
                    selectedProject?.id === project.id
                      ? 'border-sky-400 bg-sky-500/10'
                      : 'border-slate-800 hover:border-slate-500'
                  }`}
                  onClick={() => handleProjectSelect(project.slug)}
                >
                  <div className="font-semibold">{project.title}</div>
                  <div className="text-xs text-slate-400">{project.summary}</div>
                </button>
              ))}
            </div>
          )}
          {selectedProject && (
            <div className="rounded-lg border border-slate-800 bg-slate-900/40 p-4">
              <h3 className="text-lg font-semibold">{selectedProject.title}</h3>
              <p className="mt-2 text-sm text-slate-300">{selectedProject.summary}</p>
              <p className="mt-3 text-sm text-slate-300">{selectedProject.body}</p>
              {selectedProject.media?.length ? (
                <div className="mt-4 space-y-2 text-sm text-slate-300">
                  {selectedProject.media.map((media) => (
                    <div key={media.id} className="rounded border border-slate-800 px-3 py-2">
                      <div className="text-xs uppercase text-slate-500">{media.type}</div>
                      <div className="text-sm">{media.caption ?? media.url}</div>
                    </div>
                  ))}
                </div>
              ) : null}
            </div>
          )}
        </div>
      )}

      {panelType === 'contact' && (
        <div className="mt-6">
          {leadSuccess ? (
            <div className="rounded-lg border border-emerald-500/40 bg-emerald-500/10 p-4 text-sm text-emerald-200">
              Thanks! Your message has been sent.
            </div>
          ) : (
            <form className="space-y-4" onSubmit={handleLeadSubmit}>
              <input
                className="w-full rounded border border-slate-700 bg-slate-900 px-3 py-2 text-sm"
                placeholder="Name"
                value={formData.name}
                onChange={(event) => setFormData({ ...formData, name: event.target.value })}
                required
              />
              <input
                className="w-full rounded border border-slate-700 bg-slate-900 px-3 py-2 text-sm"
                placeholder="Email"
                type="email"
                value={formData.email}
                onChange={(event) => setFormData({ ...formData, email: event.target.value })}
                required
              />
              <input
                className="w-full rounded border border-slate-700 bg-slate-900 px-3 py-2 text-sm"
                placeholder="Company (optional)"
                value={formData.company ?? ''}
                onChange={(event) => setFormData({ ...formData, company: event.target.value })}
              />
              <input
                className="w-full rounded border border-slate-700 bg-slate-900 px-3 py-2 text-sm"
                placeholder="Phone (optional)"
                value={formData.phone ?? ''}
                onChange={(event) => setFormData({ ...formData, phone: event.target.value })}
              />
              <input
                className="w-full rounded border border-slate-700 bg-slate-900 px-3 py-2 text-sm"
                placeholder="Subject (optional)"
                value={formData.subject ?? ''}
                onChange={(event) => setFormData({ ...formData, subject: event.target.value })}
              />
              <textarea
                className="min-h-[140px] w-full rounded border border-slate-700 bg-slate-900 px-3 py-2 text-sm"
                placeholder="Message"
                value={formData.message}
                onChange={(event) => setFormData({ ...formData, message: event.target.value })}
                required
              />
              <button
                className="rounded-full border border-slate-600 px-4 py-2 text-sm hover:border-white"
                type="submit"
                disabled={status === 'loading'}
              >
                {status === 'loading' ? 'Sending…' : 'Send message'}
              </button>
            </form>
          )}
        </div>
      )}
    </aside>
  )
}

import { useEffect, useMemo } from 'react'
import { useSearchParams } from 'react-router-dom'

import { WorldCanvas } from '../world/WorldCanvas'
import { WorldHUD } from '../world/WorldHUD'
import { WorldPanel } from '../world/WorldPanel'
import { useWorldStore } from '../stores/worldStore'

export const WorldPage = () => {
  const [searchParams] = useSearchParams()
  const {
    loadWorld,
    error,
    nodes,
    entryPhase,
    setEntryPhase,
    setNode
  } = useWorldStore()

  const entryParam = searchParams.get('entry')

  const lobbyNode = useMemo(
    () => nodes.find((node) => node.key === 'lobby') ?? nodes[0],
    [nodes]
  )

  useEffect(() => {
    let isMounted = true
    const init = async () => {
      await loadWorld()
      if (!isMounted) {
        return
      }
      if (entryParam === '1') {
        setEntryPhase('drone')
      } else {
        setEntryPhase('atDoor')
      }
    }

    init()

    return () => {
      isMounted = false
    }
  }, [entryParam, loadWorld, setEntryPhase])

  if (error) {
    return (
      <div className="flex h-screen items-center justify-center bg-slate-950 p-6 text-white">
        <div className="max-w-md text-center">
          <h1 className="text-2xl font-semibold">World failed to load</h1>
          <p className="mt-2 text-sm text-slate-300">{error}</p>
          <button
            className="mt-4 rounded-full border border-slate-600 px-4 py-2 text-sm hover:border-white"
            onClick={() => loadWorld()}
          >
            Retry
          </button>
        </div>
      </div>
    )
  }

  if (!nodes.length) {
    return (
      <div className="flex h-screen items-center justify-center bg-slate-950 text-white">
        Loading world...
      </div>
    )
  }

  return (
    <div className="relative h-screen w-full bg-slate-950">
      <WorldCanvas />
      {(entryPhase === 'atDoor' || entryPhase === 'idle') && (
        <div className="pointer-events-none absolute inset-x-0 bottom-8 z-20 flex justify-center">
          <div className="pointer-events-auto flex items-center gap-4 rounded-full border border-slate-700 bg-slate-900/80 px-5 py-3 text-white shadow-lg">
            <button
              className="rounded-full border border-slate-500 px-4 py-2 text-sm hover:border-white"
              onClick={() => {
                if (!lobbyNode) {
                  return
                }
                setEntryPhase('inside')
                setNode(lobbyNode.key)
              }}
            >
              Enter Building
            </button>
            <span className="text-xs uppercase tracking-[0.2em] text-slate-400">
              or click the door
            </span>
          </div>
        </div>
      )}
      <WorldHUD />
      <WorldPanel />
    </div>
  )
}

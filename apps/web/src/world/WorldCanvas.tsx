import { Suspense, useEffect, useLayoutEffect, useMemo, useRef, useState } from 'react'
import { Canvas, useFrame, useThree } from '@react-three/fiber'
import { PerspectiveCamera } from '@react-three/drei'
import gsap from 'gsap'
import * as THREE from 'three'

import { useWorldStore, type PanelType } from '../stores/worldStore'
import type { WorldHotspot, WorldNode } from '../lib/types'
import { ExteriorScene } from './ExteriorScene'

type HotspotProps = {
  hotspot: WorldHotspot
  onClick: (hotspot: WorldHotspot) => void
  disabled: boolean
}

const Hotspot = ({ hotspot, onClick, disabled }: HotspotProps) => {
  const [hovered, setHovered] = useState(false)
  const color = hovered ? '#fbbf24' : '#38bdf8'
  const scale = hovered ? 1.2 : 1.0

  return (
    <mesh
      position={hotspot.position}
      scale={scale}
      onPointerOver={() => !disabled && setHovered(true)}
      onPointerOut={() => setHovered(false)}
      onClick={() => !disabled && onClick(hotspot)}
    >
      <sphereGeometry args={[0.12, 24, 24]} />
      <meshStandardMaterial color={color} emissive={color} emissiveIntensity={0.35} />
    </mesh>
  )
}

const Room = ({ node }: { node: WorldNode }) => {
  const size = 8

  return (
    <group>
      <mesh rotation={[-Math.PI / 2, 0, 0]} position={[0, 0, 0]}>
        <planeGeometry args={[size, size]} />
        <meshStandardMaterial color="#0f172a" />
      </mesh>
      <mesh position={[0, 2, -size / 2]}>
        <boxGeometry args={[size, 4, 0.2]} />
        <meshStandardMaterial color="#1e293b" />
      </mesh>
      <mesh position={[-size / 2, 2, 0]} rotation={[0, Math.PI / 2, 0]}>
        <boxGeometry args={[size, 4, 0.2]} />
        <meshStandardMaterial color="#1e293b" />
      </mesh>
      <mesh position={[size / 2, 2, 0]} rotation={[0, Math.PI / 2, 0]}>
        <boxGeometry args={[size, 4, 0.2]} />
        <meshStandardMaterial color="#1e293b" />
      </mesh>
      <mesh position={[0, 4, 0]}>
        <boxGeometry args={[size, 0.2, size]} />
        <meshStandardMaterial color="#0b1220" />
      </mesh>
    </group>
  )
}

const InteriorScene = ({ animateOnMount = false }: { animateOnMount?: boolean }) => {
  const { camera } = useThree()
  const {
    nodes,
    currentNodeKey,
    setNode,
    isTransitioning,
    setTransitioning,
    openPanel
  } = useWorldStore()

  const targetRef = useRef(new THREE.Vector3(0, 1.6, 0))
  const previousNodeKey = useRef<string | null>(null)

  const currentNode = useMemo(
    () => nodes.find((node) => node.key === currentNodeKey) ?? nodes[0],
    [nodes, currentNodeKey]
  )

  useLayoutEffect(() => {
    const direction = new THREE.Vector3()
    camera.getWorldDirection(direction)
    targetRef.current.copy(camera.position).add(direction.multiplyScalar(10))
  }, [camera])

  useFrame(() => {
    camera.lookAt(targetRef.current)
  })

  useEffect(() => {
    if (!currentNode) {
      return
    }

    const [x, y, z] = currentNode.camera_position
    const [tx, ty, tz] = currentNode.camera_target
    const fov = currentNode.camera_fov || 50

    if (!previousNodeKey.current && !animateOnMount) {
      camera.position.set(x, y, z)
      targetRef.current.set(tx, ty, tz)
      camera.fov = fov
      camera.updateProjectionMatrix()
      previousNodeKey.current = currentNode.key
      return
    }

    setTransitioning(true)
    const timeline = gsap.timeline({
      onComplete: () => setTransitioning(false)
    })

    timeline.to(
      camera.position,
      {
        x,
        y,
        z,
        duration: 1.2,
        ease: 'power3.inOut'
      },
      0
    )
    timeline.to(
      targetRef.current,
      {
        x: tx,
        y: ty,
        z: tz,
        duration: 1.2,
        ease: 'power3.inOut'
      },
      0
    )
    timeline.to(
      camera,
      {
        fov,
        duration: 1.2,
        ease: 'power3.inOut',
        onUpdate: () => camera.updateProjectionMatrix()
      },
      0
    )

    previousNodeKey.current = currentNode.key
  }, [animateOnMount, camera, currentNode, setTransitioning])

  const handleHotspotClick = (hotspot: WorldHotspot) => {
    if (isTransitioning || !hotspot.payload) {
      return
    }

    if (hotspot.kind === 'NAVIGATE_NODE') {
      const target = hotspot.payload?.target_node_key as string | undefined
      if (target) {
        setNode(target)
      }
      return
    }

    if (hotspot.kind === 'OPEN_URL') {
      const url = hotspot.payload?.url as string | undefined
      if (url) {
        window.open(url, '_blank', 'noopener,noreferrer')
      }
      return
    }

    if (hotspot.kind === 'OPEN_PANEL') {
      const panel = hotspot.payload?.panel as PanelType | undefined
      if (panel) {
        openPanel({ type: panel, payload: hotspot.payload ?? {} })
      }
    }
  }

  if (!currentNode) {
    return null
  }

  return (
    <>
      <ambientLight intensity={0.45} />
      <directionalLight position={[4, 6, 2]} intensity={1.2} />
      <Room node={currentNode} />
      {currentNode.hotspots.map((hotspot) => (
        <Hotspot
          key={hotspot.id}
          hotspot={hotspot}
          disabled={isTransitioning}
          onClick={handleHotspotClick}
        />
      ))}
    </>
  )
}

export const WorldCanvas = () => {
  const { entryPhase } = useWorldStore()

  return (
    <Canvas className="h-full w-full" shadows>
      <PerspectiveCamera makeDefault fov={50} position={[0, 1.6, 6]} />
      <Suspense fallback={null}>
        {entryPhase === 'inside' ? (
          <InteriorScene animateOnMount />
        ) : (
          <ExteriorScene />
        )}
      </Suspense>
    </Canvas>
  )
}

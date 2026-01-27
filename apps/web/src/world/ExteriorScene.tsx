import { useEffect, useMemo, useRef, useState } from 'react'
import { useFrame, useThree } from '@react-three/fiber'
import { useGLTF } from '@react-three/drei'
import gsap from 'gsap'
import * as THREE from 'three'

import { useWorldStore } from '../stores/worldStore'

const MODEL_URL = '/models/hengshi-hq-atlanta-exterior-web.glb'

type CameraKeyframe = {
  position: [number, number, number]
  target: [number, number, number]
  fov: number
  duration: number
}

type DoorHotspotProps = {
  position: [number, number, number]
  disabled: boolean
  onClick: () => void
}

const DoorHotspot = ({ position, disabled, onClick }: DoorHotspotProps) => {
  const [hovered, setHovered] = useState(false)
  const color = hovered ? '#f59e0b' : '#38bdf8'
  const scale = hovered ? 1.15 : 1

  return (
    <mesh
      position={position}
      scale={scale}
      onPointerOver={() => !disabled && setHovered(true)}
      onPointerOut={() => setHovered(false)}
      onClick={() => !disabled && onClick()}
    >
      <sphereGeometry args={[0.28, 28, 28]} />
      <meshStandardMaterial color={color} emissive={color} emissiveIntensity={0.4} />
    </mesh>
  )
}

export const ExteriorScene = () => {
  const { camera } = useThree()
  const { scene } = useGLTF(MODEL_URL)
  const { entryPhase, setEntryPhase, setNode, nodes } = useWorldStore()

  const targetRef = useRef(new THREE.Vector3(0, 1.6, 0))
  const timelineRef = useRef<gsap.core.Timeline | null>(null)

  const metrics = useMemo(() => {
    const bounds = new THREE.Box3().setFromObject(scene)
    const size = bounds.getSize(new THREE.Vector3())
    const center = bounds.getCenter(new THREE.Vector3())

    const width = Math.max(size.x, 8)
    const depth = Math.max(size.z, 8)
    const height = Math.max(size.y, 6)

    const frontZ = size.z * 0.5
    const doorY = Math.max(1.4, height * 0.25)
    const doorZ = frontZ + 0.2

    const keyframes: CameraKeyframe[] = [
      {
        position: [width * 0.6, height * 0.85, frontZ + depth * 1.8],
        target: [0, height * 0.35, 0],
        fov: 48,
        duration: 2.4
      },
      {
        position: [width * 0.32, height * 0.6, frontZ + depth * 1.1],
        target: [0, height * 0.32, 0],
        fov: 44,
        duration: 1.7
      },
      {
        position: [width * 0.12, doorY + height * 0.08, frontZ + depth * 0.6],
        target: [0, doorY, 0],
        fov: 40,
        duration: 1.3
      }
    ]

    return {
      modelOffset: [-center.x, -bounds.min.y, -center.z] as [number, number, number],
      groundSize: Math.max(width, depth) * 4,
      fogNear: depth * 1.4,
      fogFar: depth * 3.6,
      doorHotspot: [0, doorY, doorZ] as [number, number, number],
      keyframes
    }
  }, [scene])

  const lobbyKey = useMemo(
    () => nodes.find((node) => node.key === 'lobby')?.key ?? nodes[0]?.key,
    [nodes]
  )

  useFrame(() => {
    camera.lookAt(targetRef.current)
  })

  const applyKeyframe = (frame: CameraKeyframe) => {
    camera.position.set(...frame.position)
    targetRef.current.set(...frame.target)
    camera.fov = frame.fov
    camera.updateProjectionMatrix()
  }

  useEffect(() => {
    if (entryPhase === 'drone') {
      timelineRef.current?.kill()
      const [far, mid, door] = metrics.keyframes
      applyKeyframe(far)

      const timeline = gsap.timeline({
        onComplete: () => setEntryPhase('atDoor')
      })

      timeline.to(
        camera.position,
        {
          x: mid.position[0],
          y: mid.position[1],
          z: mid.position[2],
          duration: mid.duration,
          ease: 'power2.inOut'
        },
        0
      )
      timeline.to(
        targetRef.current,
        {
          x: mid.target[0],
          y: mid.target[1],
          z: mid.target[2],
          duration: mid.duration,
          ease: 'power2.inOut'
        },
        0
      )
      timeline.to(
        camera,
        {
          fov: mid.fov,
          duration: mid.duration,
          ease: 'power2.inOut',
          onUpdate: () => camera.updateProjectionMatrix()
        },
        0
      )

      timeline.to(
        camera.position,
        {
          x: door.position[0],
          y: door.position[1],
          z: door.position[2],
          duration: door.duration,
          ease: 'power3.inOut'
        },
        '>'
      )
      timeline.to(
        targetRef.current,
        {
          x: door.target[0],
          y: door.target[1],
          z: door.target[2],
          duration: door.duration,
          ease: 'power3.inOut'
        },
        '<'
      )
      timeline.to(
        camera,
        {
          fov: door.fov,
          duration: door.duration,
          ease: 'power3.inOut',
          onUpdate: () => camera.updateProjectionMatrix()
        },
        '<'
      )

      timelineRef.current = timeline

      return () => {
        timeline.kill()
      }
    }

    if (entryPhase === 'atDoor' || entryPhase === 'idle') {
      timelineRef.current?.kill()
      applyKeyframe(metrics.keyframes[2])
    }

    return undefined
  }, [camera, entryPhase, metrics.keyframes, setEntryPhase])

  return (
    <group>
      <fog attach="fog" args={['#0b1220', metrics.fogNear, metrics.fogFar]} />
      <ambientLight intensity={0.4} />
      <directionalLight position={[6, 10, 8]} intensity={1.2} />
      <directionalLight position={[-8, 6, -4]} intensity={0.4} />

      <mesh rotation={[-Math.PI / 2, 0, 0]} position={[0, 0, 0]} receiveShadow>
        <planeGeometry args={[metrics.groundSize, metrics.groundSize]} />
        <meshStandardMaterial color="#0f172a" />
      </mesh>

      <group position={metrics.modelOffset}>
        <primitive object={scene} />
      </group>

      <DoorHotspot
        position={metrics.doorHotspot}
        disabled={entryPhase === 'drone' || !lobbyKey}
        onClick={() => {
          if (!lobbyKey) {
            return
          }
          setEntryPhase('inside')
          setNode(lobbyKey)
        }}
      />
    </group>
  )
}

useGLTF.preload(MODEL_URL)

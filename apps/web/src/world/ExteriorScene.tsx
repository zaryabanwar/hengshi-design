import { useEffect, useMemo, useRef, useState } from 'react'
import { useFrame, useThree } from '@react-three/fiber'
import { useGLTF } from '@react-three/drei'
import gsap from 'gsap'
import * as THREE from 'three'

import { useWorldStore } from '../stores/worldStore'

const MODEL_URL = '/models/hengshi-hq-atlanta-exterior-web.glb'

const BLENDER_DOOR_POSITION: [number, number, number] = [0, 1.904, 0.058396]
const BLENDER_BUILDING_CENTER: [number, number, number] = [55.613, 46.309, 113.37]
const BLENDER_BUILDING_DIMENSIONS = { width: 60.8, depth: 212, height: 96.9 }
const BLENDER_SCALE = 100
const BLENDER_DOOR_HOTSPOT_OFFSET: [number, number, number] = [0, 0, 0.2]

const blenderToThree = ([x, y, z]: [number, number, number]): [number, number, number] => [
  x * BLENDER_SCALE,
  z * BLENDER_SCALE,
  y * BLENDER_SCALE
]

const { width, depth, height } = BLENDER_BUILDING_DIMENSIONS
const BLENDER_DRONE_POSITIONS: [number, number, number][] = [
  [BLENDER_BUILDING_CENTER[0], BLENDER_BUILDING_CENTER[1] - depth * 1.5, height * 3],
  [BLENDER_BUILDING_CENTER[0] + width * 1.2, BLENDER_BUILDING_CENTER[1] - depth * 1.2, height * 2.6],
  [BLENDER_BUILDING_CENTER[0] + width * 1.2, BLENDER_BUILDING_CENTER[1] + depth * 0.2, height * 2.3],
  [BLENDER_BUILDING_CENTER[0] - width * 1.2, BLENDER_BUILDING_CENTER[1] + depth * 0.2, height * 2.1],
  [BLENDER_DOOR_POSITION[0], BLENDER_DOOR_POSITION[1] - 6, BLENDER_DOOR_POSITION[2] + 2]
]

const DOOR_POSITION = blenderToThree(BLENDER_DOOR_POSITION)
const BUILDING_CENTER = blenderToThree(BLENDER_BUILDING_CENTER)
const DOOR_HOTSPOT = blenderToThree([
  BLENDER_DOOR_POSITION[0] + BLENDER_DOOR_HOTSPOT_OFFSET[0],
  BLENDER_DOOR_POSITION[1] + BLENDER_DOOR_HOTSPOT_OFFSET[1],
  BLENDER_DOOR_POSITION[2] + BLENDER_DOOR_HOTSPOT_OFFSET[2]
])

const DRONE_KEYFRAMES: CameraKeyframe[] = [
  {
    position: blenderToThree(BLENDER_DRONE_POSITIONS[0]),
    target: DOOR_POSITION,
    fov: 58,
    duration: 0
  },
  {
    position: blenderToThree(BLENDER_DRONE_POSITIONS[1]),
    target: DOOR_POSITION,
    fov: 54,
    duration: 2.4
  },
  {
    position: blenderToThree(BLENDER_DRONE_POSITIONS[2]),
    target: DOOR_POSITION,
    fov: 50,
    duration: 1.9
  },
  {
    position: blenderToThree(BLENDER_DRONE_POSITIONS[3]),
    target: DOOR_POSITION,
    fov: 46,
    duration: 1.7
  },
  {
    position: blenderToThree(BLENDER_DRONE_POSITIONS[4]),
    target: DOOR_POSITION,
    fov: 42,
    duration: 1.6
  }
]

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
      <sphereGeometry args={[0.28 * BLENDER_SCALE, 28, 28]} />
      <meshStandardMaterial color={color} emissive={color} emissiveIntensity={0.4} />
    </mesh>
  )
}

export const ExteriorScene = () => {
  const { camera } = useThree()
  const perspectiveCamera = camera as THREE.PerspectiveCamera
  const { scene } = useGLTF(MODEL_URL)
  const { entryPhase, setEntryPhase, transitionTo, nodes } = useWorldStore()

  const targetRef = useRef(new THREE.Vector3(...DOOR_POSITION))
  const timelineRef = useRef<gsap.core.Timeline | null>(null)

  const environment = useMemo(() => {
    const groundSize = Math.max(width, depth) * 4 * BLENDER_SCALE
    const fogNear = depth * 0.9 * BLENDER_SCALE
    const fogFar = depth * 4.2 * BLENDER_SCALE

    return { groundSize, fogNear, fogFar }
  }, [])

  const canEnter = nodes.length > 0

  useFrame(() => {
    camera.lookAt(targetRef.current)
  })

  const applyKeyframe = (frame: CameraKeyframe) => {
    perspectiveCamera.position.set(...frame.position)
    targetRef.current.set(...frame.target)
    perspectiveCamera.fov = frame.fov
    perspectiveCamera.updateProjectionMatrix()
  }

  useEffect(() => {
    if (entryPhase === 'drone') {
      timelineRef.current?.kill()
      applyKeyframe(DRONE_KEYFRAMES[0])

      const timeline = gsap.timeline({
        onComplete: () => setEntryPhase('atDoor')
      })

      for (let i = 1; i < DRONE_KEYFRAMES.length; i += 1) {
        const frame = DRONE_KEYFRAMES[i]
        timeline.to(
          camera.position,
          {
            x: frame.position[0],
            y: frame.position[1],
            z: frame.position[2],
            duration: frame.duration,
            ease: 'power2.inOut'
          },
          '>'
        )
        timeline.to(
          targetRef.current,
          {
            x: frame.target[0],
            y: frame.target[1],
            z: frame.target[2],
            duration: frame.duration,
            ease: 'power2.inOut'
          },
          '<'
        )
        timeline.to(
          perspectiveCamera,
          {
            fov: frame.fov,
            duration: frame.duration,
            ease: 'power2.inOut',
            onUpdate: () => perspectiveCamera.updateProjectionMatrix()
          },
          '<'
        )
      }

      timelineRef.current = timeline

      return () => {
        timeline.kill()
      }
    }

    if (entryPhase === 'atDoor' || entryPhase === 'idle') {
      timelineRef.current?.kill()
      applyKeyframe(DRONE_KEYFRAMES[DRONE_KEYFRAMES.length - 1])
    }

    return undefined
  }, [camera, entryPhase, perspectiveCamera, setEntryPhase])

  return (
    <group>
      <fog attach="fog" args={['#0b1220', environment.fogNear, environment.fogFar]} />
      <ambientLight intensity={0.4} />
      <directionalLight position={[6, 10, 8]} intensity={1.2} />
      <directionalLight position={[-8, 6, -4]} intensity={0.4} />

      <mesh
        rotation={[-Math.PI / 2, 0, 0]}
        position={[BUILDING_CENTER[0], 0, BUILDING_CENTER[2]]}
        receiveShadow
      >
        <planeGeometry args={[environment.groundSize, environment.groundSize]} />
        <meshStandardMaterial color="#0f172a" />
      </mesh>

      <primitive object={scene} />

      <DoorHotspot
        position={DOOR_HOTSPOT}
        disabled={entryPhase === 'drone' || !canEnter}
        onClick={() => {
          if (!canEnter) {
            return
          }
          transitionTo('lobby')
        }}
      />
    </group>
  )
}

useGLTF.preload(MODEL_URL)

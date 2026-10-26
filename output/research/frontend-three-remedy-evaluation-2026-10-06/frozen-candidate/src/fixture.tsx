import { StrictMode, useEffect, useRef, useState } from 'react';
import { createRoot } from 'react-dom/client';
import { Canvas, useThree } from '@react-three/fiber';
import { OrbitControls } from '@react-three/drei';
import { Link, MemoryRouter, Route, Routes } from 'react-router-dom';
import { create } from 'zustand';
import { gsap } from 'gsap';
import './fixture.css';

// Synthetic compatibility fixture, not Hengshi UI, architecture or World controls.
const useFixtureStore = create<{ visits: number; visit: () => void }>((set) => ({
  visits: 0, visit: () => set((state) => ({ visits: state.visits + 1 })),
}));

function SceneEvidence({ report }: { report: (text: string) => void }) {
  const gl = useThree((state) => state.gl);
  useEffect(() => { report(gl.getContext() instanceof WebGL2RenderingContext ? 'WebGL2 renderer created' : 'Unexpected renderer'); }, [gl, report]);
  return null;
}

function Counter({ initial }: { initial: number }) {
  const [count, setCount] = useState(initial);
  const ref = useRef<HTMLButtonElement | null>(null);
  return <button ref={ref} className="rounded bg-emerald-700 px-4 py-2 text-white"
    onClick={(event) => { event.currentTarget.disabled = true; setCount(count + 1); }}>Count {count}</button>;
}

function Fixture() {
  const [scene, setScene] = useState(true);
  const [renderer, setRenderer] = useState('Not created');
  const visits = useFixtureStore((state) => state.visits);
  const visit = useFixtureStore((state) => state.visit);
  const heading = useRef<HTMLHeadingElement | null>(null);
  const [animation, setAnimation] = useState('Not requested');
  useEffect(() => {
    if (animation !== 'Requested' || !heading.current) return;
    const tween = gsap.fromTo(heading.current, { opacity: 0.5 }, { opacity: 1, duration: 0.1,
      onComplete: () => setAnimation('Completed') });
    return () => { tween.kill(); };
  }, [animation]);
  return <main className="mx-auto max-w-4xl space-y-4 p-6 font-sans text-slate-900">
    <h1 ref={heading} className="text-2xl font-bold">Isolated frontend tooling fixture</h1>
    <p>Compatibility evidence only. This is not the Hengshi website or campus.</p>
    <Counter initial={0} />
    <button className="ml-3 border px-3 py-2" onClick={visit}>Store increment</button>
    <p>Store value: {visits}</p>
    <button className="border px-3 py-2" onClick={() => setAnimation('Requested')}>Run fixture animation</button>
    <p>Animation: {animation}</p>
    <nav><Link to="/notes">Open fixture notes</Link> | <Link to="/">Fixture home</Link></nav>
    <Routes><Route path="/" element={<p>Fixture home route</p>} /><Route path="/notes" element={<p>Fixture notes route</p>} /></Routes>
    <button className="border px-3 py-2" onClick={() => setScene((current) => !current)}>{scene ? 'Unmount scene' : 'Mount scene'}</button>
    <p>Renderer: {renderer}</p>
    {scene && <div className="h-64 border" aria-label="Synthetic WebGL scene">
      <Canvas frameloop="demand" camera={{ position: [3, 2, 4] }} fallback={<p>WebGL unavailable</p>}>
        <ambientLight intensity={2} />
        <mesh><boxGeometry /><meshStandardMaterial color="#047857" /></mesh>
        <OrbitControls enableRotate={false} enableZoom={false} enablePan={false} />
        <SceneEvidence report={setRenderer} />
      </Canvas>
    </div>}
  </main>;
}

const container = document.getElementById('root');
if (!container) throw new Error('Missing synthetic fixture root');
createRoot(container).render(<StrictMode><MemoryRouter><Fixture /></MemoryRouter></StrictMode>);

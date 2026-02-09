# 3D Mega Menu Style Guide v2.0

**Version:** 2.0 | **Date:** February 9, 2026 | **Status:** Active
**Supersedes:** 3D Mega Menu Style Guide v1.0 (Angular + Three.js direct)

---

## 1. Overview

This document provides style guidelines for the Hengshi Design Platform's 3D immersive navigation system. The system uses **React Three Fiber (R3F)** with **GSAP** animations and **Zustand** state management to create an interactive building experience where users navigate through 3D rooms corresponding to service categories.

### 1.1 Technology Changes from v1.0

| Aspect | v1.0 (Feb 2025) | v2.0 (Feb 2026) |
|--------|-----------------|-----------------|
| Framework | Angular + Three.js direct | React 18 + React Three Fiber |
| State | Angular Services | Zustand stores |
| Animation | Tween.js + Angular Animations | GSAP timelines |
| 3D Helpers | Manual Three.js setup | @react-three/drei |
| Styling | SCSS + Angular Material | TailwindCSS |
| Build | Angular CLI | Vite |

---

## 2. Design Principles

### 2.1 Core Principles
- **Immersive Experience:** Depth and dimension that extends the platform's 3D environment
- **Performance First:** Visual richness must never compromise performance
- **Intuitive Navigation:** 3D elements enhance, not confuse, the navigation experience
- **Brand Consistency:** All elements reflect the Hengshi design language
- **Progressive Enhancement:** Graceful degradation on limited-capability devices

### 2.2 Animation Philosophy
- **Purpose-Driven:** Every animation communicates meaning and guides users
- **Smooth Transitions:** Natural easing functions via GSAP
- **Restrained Effects:** Subtle over overwhelming
- **Performance Balanced:** Simplified animations on lower-powered devices

---

## 3. Visual Language

### 3.1 Color Palette

| Element | Color | Hex Code | Usage |
|---------|-------|----------|-------|
| Card Base | Dark Gray | `#2D3142` | Primary card surface |
| Card Highlight | Red/Orange | `#E72A00` | Card edges, highlights |
| Card Accents | Orange | `#F44A25` | Interactive elements |
| Text Primary | White | `#F4F5F7` | Card titles, primary text |
| Text Secondary | Light Gray | `rgba(255,255,255,0.7)` | Descriptions, secondary text |
| Hotspot Default | Cyan | `#00BFFF` | Inactive hotspot glow |
| Hotspot Hover | White | `#FFFFFF` | Active hotspot glow |

### 3.2 Typography

| Element | Font | Size | Weight |
|---------|------|------|--------|
| Card Titles | Playfair Display | 1.25rem (20px) | 500 |
| Card Descriptions | Inter | 0.875rem (14px) | 400 |
| Section Headers | Playfair Display | 2rem (32px) | 500 |
| Featured Content | Inter | 1rem (16px) | 400 |
| Panel Headings | Inter | 1.5rem (24px) | 600 |
| Panel Body | Inter | 1rem (16px) | 400 |

### 3.3 Spacing (TailwindCSS)
- Card Padding: `p-6` (1.5rem)
- Grid Gap: `gap-6` (1.5rem)
- Section Margins: `my-10` (2.5rem)
- Content Padding: `p-4` (1rem)

---

## 4. 3D Elements

### 4.1 Hotspot Design

Hotspots are rendered as interactive spheres using `@react-three/drei` components within the R3F canvas.

**Configuration (database-driven):**
- Position: `{x, y, z}` from WorldHotspot.position
- Radius: `WorldHotspot.radius` (default 0.5 units)
- Normal: Surface alignment vector

**States:**

| State | Scale | Color | Emission |
|-------|-------|-------|----------|
| Default | 1.0 | `#00BFFF` | 0.3 |
| Hover | 1.2 | `#FFFFFF` | 0.6 |
| Active/Click | 0.9 → 1.1 | `#F44A25` | 0.8 |
| Disabled | 0.8 | `#666666` | 0.1 |

### 4.2 GLB Model Standards

- **Format:** GLTF Binary (.glb)
- **Source:** Blender export with draco compression (planned)
- **Coordinate system:** Blender defaults (Z-up converted to Y-up by Three.js)
- **Scale factor:** 100x (Blender meters to Three.js units)
- **Materials:** PBR (Physically Based Rendering) via MeshStandardMaterial

### 4.3 Lighting

| Light | Type | Color | Intensity | Position |
|-------|------|-------|-----------|----------|
| Ambient | AmbientLight | `#ffffff` | 0.5 | — |
| Main | DirectionalLight | `#ffffff` | 1.0 | (5, 5, 5) |
| Accent Blue | PointLight | `#0066ff` | 1.0 | Scene-dependent |
| Accent Red | PointLight | `#ff0066` | 1.0 | Scene-dependent |

### 4.4 Camera Settings

| Parameter | Value | Notes |
|-----------|-------|-------|
| FOV | 50° (configurable per node) | WorldNode.camera_fov |
| Near Plane | 0.1 | |
| Far Plane | 1000 | |
| Position | Per-node from database | WorldNode.camera_position |
| Target | Per-node from database | WorldNode.camera_target |

---

## 5. Animations (GSAP)

### 5.1 Timing Guidelines

| Animation | Duration | Easing | GSAP Function |
|-----------|----------|--------|---------------|
| Drone entry (per keyframe) | 2–4s | power3.inOut | `gsap.timeline()` |
| Room transition | 1.5s | power2.inOut | `gsap.to()` |
| Hotspot hover | 300ms | power2.out | `gsap.to()` |
| Hotspot click | 100ms | power1.inOut | `gsap.to()` with yoyo |
| Panel open/close | 400ms | power2.out | CSS transition |
| Loading fade | 500ms | linear | CSS opacity |

### 5.2 Drone Entry Sequence

The entry animation uses a GSAP timeline with 5 keyframes:

```
Keyframe 1: Bird-eye view (high altitude, looking down)
    ↓ 3s power3.inOut
Keyframe 2: Orbit approach (circling building)
    ↓ 3s power3.inOut
Keyframe 3: Front approach (straight-on view)
    ↓ 2s power2.inOut
Keyframe 4: Door-level approach
    ↓ 2s power2.out
Keyframe 5: At door (stopped, CTA visible)
```

### 5.3 Room Transition Pattern

When `NAVIGATE_NODE` hotspot is clicked:
1. Current hotspots fade out (200ms)
2. Camera animates to new node's `camera_position`/`camera_target` (1.5s, power2.inOut)
3. New hotspots fade in (200ms staggered)

---

## 6. Panel Overlay System

Panels are HTML/CSS overlays rendered outside the R3F canvas, triggered by `OPEN_PANEL` hotspots.

### 6.1 Panel Types

| Panel | Trigger | Content |
|-------|---------|---------|
| Services | `{"panel": "services"}` | Service listings filtered by category |
| Projects | `{"panel": "projects"}` | Portfolio items with media |
| Contact | `{"panel": "contact"}` | Lead capture form |

### 6.2 Panel Styling (TailwindCSS)

```
Container: fixed right-0 top-0 h-full w-[480px] bg-gray-900/95 backdrop-blur
Header:    p-6 border-b border-gray-700
Content:   p-6 overflow-y-auto
Close:     absolute top-4 right-4 text-gray-400 hover:text-white
```

---

## 7. Interaction Guidelines

### 7.1 Cursor States

| State | Cursor | Context |
|-------|--------|---------|
| Default (3D canvas) | `default` | Exploring scene |
| Hotspot hover | `pointer` | Over interactive hotspot |
| Panel interaction | `default` | Over HTML panel overlay |
| Dragging (future) | `grab` / `grabbing` | Camera orbit control |

### 7.2 Keyboard Navigation (Planned)

- **Tab:** Cycle through hotspots
- **Enter/Space:** Activate hotspot
- **Escape:** Close panel / go back
- **Arrow keys:** Camera orbit (future)

### 7.3 Accessibility

- `prefers-reduced-motion`: Skip drone animation, use instant transitions
- ARIA labels on hotspot overlays
- Focus indicators for keyboard navigation
- Screen reader descriptions for 3D scene state
- Minimum contrast WCAG AA for all text

---

## 8. Responsive Behavior

### 8.1 Breakpoints

| Breakpoint | Panel Width | 3D Adjustments |
|------------|-------------|----------------|
| Desktop (>1024px) | 480px side panel | Full 3D experience |
| Tablet (768–1024px) | 400px side panel | Simplified lighting |
| Mobile (<768px) | Full-width bottom sheet | Reduced hotspot count, simpler models |

### 8.2 Performance Adaptations

| Device Tier | Adaptations |
|-------------|-------------|
| High (desktop GPU) | Full lighting, shadows, high-res textures |
| Medium (tablet/laptop) | Reduced shadows, medium textures |
| Low (mobile/old devices) | No shadows, low-res textures, fewer hotspots |
| No WebGL | Fallback to static image gallery with navigation |

---

## 9. R3F Component Patterns

### 9.1 Scene Structure

```jsx
<Canvas camera={{ fov: 50, near: 0.1, far: 1000 }}>
  <CameraController />        {/* GSAP animation target */}
  <ambientLight intensity={0.5} />
  <directionalLight position={[5,5,5]} intensity={1} />
  
  {entryPhase !== 'inside' && <ExteriorScene />}
  {entryPhase === 'inside' && <InteriorScene nodeKey={currentNode} />}
  
  <HotspotRenderer hotspots={activeHotspots} />
</Canvas>
```

### 9.2 State Flow

```
User Click Hotspot
    → worldStore.handleHotspotAction(hotspot)
    → switch(hotspot.kind):
        OPEN_PANEL  → setActivePanel(hotspot.payload.panel)
        NAVIGATE_NODE → setCurrentNode(hotspot.payload.target_node)
                        → CameraController animates to new position
        OPEN_URL    → window.open(hotspot.payload.url)
```

---

## 10. Testing Checklist

- [ ] Performance: 60fps on target devices
- [ ] Animation smoothness across entry sequence
- [ ] Hotspot click accuracy (raycasting precision)
- [ ] Panel open/close transitions
- [ ] WebGL fallback rendering
- [ ] Keyboard navigation (when implemented)
- [ ] `prefers-reduced-motion` behavior
- [ ] Cross-browser: Chrome, Firefox, Safari, Edge
- [ ] Mobile touch: iOS Safari, Android Chrome
- [ ] Memory usage during extended navigation
- [ ] GLB model loading time (< 3s on 4G)

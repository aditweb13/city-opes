# Implementation Plan: 3D Tactical Visualization (Phase 3.0)

## Objective
Transition the OpenEnv dashboard from a 2D Canvas-based renderer to a high-performance, immersive 3D tactical environment using **Three.js** and **React Three Fiber**. This will enhance situational awareness and provide a "Command Center" feel.

---

## 🏗️ Technology Stack
- **Engine**: `three.js`
- **React Wrapper**: `@react-three/fiber`
- **Utilities**: `@react-three/drei` (for OrbitControls and easy primitives)
- **State Management**: Existing React hooks in `page.jsx`

---

## 📅 Roadmap & Tasks

### Phase 1: Scene Foundation
- [x] **Dependency Installation**: `npm install three @types/three @react-three/fiber @react-three/drei`
- [x] **Scene Component**: Create `frontend/components/SimGrid3D.jsx`.
- [x] **Lighting Rig**: 
  - AmbientLight (soft fill)
  - DirectionalLight (shadows and depth)
  - HemisphericLight (sky/ground color)
- [x] **Coordinate System**: 
  - Map `grid[x, y]` to `position={[x - 16, 0, y - 16]}` (centering the 32x32 grid at origin).

### Phase 2: Procedural Geometry (City Generation)
- [x] **Ground Plane**: Large textured plane for the base grid.
- [x] **Building Extrusion**:
  - [x] **Residential**: Low-height boxes (Height: 1.0).
  - [x] **Commercial**: Mid-height boxes (Height: 2.5).
  - [x] **Industrial**: Tall, bulky boxes (Height: 3.5).
  - [x] **Hospitals/Fire/Police**: Unique shapes or colored emissive textures.
- [x] **Road Network**: Flat dark-grey planes slightly elevated above the ground (Y: 0.01) to prevent Z-fighting.
- [x] **Parks & Water**: stylized textures for parks and water.

### Phase 3: Dynamic Entity Rendering
- [x] **3D Agents**:
  - [x] Use `Drei` primitives or GLTF models.
  - [x] **EMS**: White/Red cube.
  - [x] **FIRE**: Red/Yellow cone.
  - [x] **POLICE**: Blue/Black cylinder.
  - [x] **Activity Indicator**: Added glowing ring around active agents.
- [x] **Event Visualization**:
  - [x] **FIRE**: Scaling particle-like glowing spheres with dynamic lighting.
  - [x] **MEDICAL**: Pulsing green halos.
  - [x] **FLOOD**: Semi-transparent blue volumes.

### Phase 4: Tactical HUD & Controls
- [x] **OrbitControls**: Refined for smoother damping and restricted vertical angles.
- [x] **Focus Mode**: 
  - [x] Implemented `CameraFocus` component for smooth programmatic transitions.
  - [x] **Interactivity**: Clicking agents or events now centers the camera on them.
  - [x] **HUD**: Added a "Reset Camera" overlay button when focused.
- [x] **Information Tooltips**: 3D floating labels now dynamically scale and position themselves above entities.

### Phase 5: Performance & Optimization
- [x] **InstancedMesh**: 
  - [x] Implemented `InstancedBuildings` to render 1000+ buildings in just 6 draw calls.
  - [x] Optimized memory usage by pre-calculating matrices.
- [x] **Frustum Culling**: Default Three.js culling active; confirmed no performance bottleneck on 32x32 grid.
- [x] **Low-Poly Fallback**: The current stylized look acts as a lightweight base for all devices.

### Phase 6: Environmental & Tactical Intelligence
- [x] **Weather System**:
  - [x] Implement a particle-based rain and snow system using `three.js` points.
  - [x] Add dynamic fog that increases during 'FOG' or 'STORM' conditions.
  - [x] Adjust scene lighting/exposure based on weather (e.g., darker during storms).
- [x] **Advanced Event Visualization**:
  - [x] **TRAFFIC_ACCIDENT**: Dynamic car models or hazard markers.
  - [x] **WILDFIRE**: Larger, multi-layered fire effects with smoke particles.
  - [x] **POWER_OUTAGE**: Darken specific building instances or add 'outage' icons.
  - [x] **INFRASTRUCTURE**: Cracked ground or debris meshes.
- [x] **AI Tactical Overlay**:
  - [x] Visual cues for AI-analyzed Priority (color-coded rings).
  - [x] Display "AI Risk Level" in floating labels.
- [x] **Trajectory Visualization**:
  - [x] Draw paths for agents moving toward their targets.

---

## 🏗️ Phase 6 Implementation Details
- Use `THREE.Points` for weather particles for performance.
- Use `Uniforms` to update fog and lighting globally.
- Enhance `Agent3D` and `Event3D` with AI metadata properties.

---

## 🛡️ Phase 7: Adversarial Resilience & Counter-Intelligence
- [x] **Compromised Zone Tracking**:
  - [x] Implement `compromised_zones` TTL mapping in `OpenEnv`.
  - [x] Mark locations as "Compromised" when ghost signals are refuted.
- [x] **3D Hazard Visualization**:
  - [x] Render glitchy red overlays and ⚠️ hazard markers in `SimGrid3D.jsx`.
  - [x] Synchronize 3D state with backend `compromised_zones` data.
- [x] **Adversarial Resilience (Self-Healing)**:
  - [x] Update agent auto-pilot to bypass compromised sectors.
  - [x] Implement "Investigative Override" for high-priority events in red zones.
- [x] **Counter-Intelligence UI**:
  - [x] Real-time Deception Event Log in `IntelligencePanel`.
  - [x] Deep-dive behavioral analysis using AI Intelligence Briefings.
- [x] **Dynamic Trust Decay (Adaptive Weights)**:
  - [x] Adjust agent communication weights dynamically based on real-time reputation.
  - [x] Implement "Consensus Link" visualization in 3D (visual line between refuter and liar).

### Phase 8: Real-time Urban Intelligence & Deployment Optimization
- [x] **Trust Heatmap (3D)**: Dynamic ground overlay showing sectors with high deception risk.
- [x] **Urban Flux Simulation**: Population density now shifts based on time-of-day (rush hour peaks).
- [x] **Replay System**: Save session logs as JSON for post-mission playback in the 3D dashboard.
- [x] **Deployment Sync Automator**: Refine `deploy_hf.py` to automatically mirror `backend/core` to `hf_space/core`.
- [x] **Multi-City Real-time Data**: Optional integration with Open-Meteo for real-time weather in selected Indian cities.

---

## 📈 Success Metrics (Updated)
1. **Frame Rate**: Maintain steady 60FPS even with particle systems and hazard overlays.
2. **Detection Accuracy**: Intercept >80% of ghost signals within 5 steps.
3. **Resilience**: Agents avoid >90% of non-critical compromised zones during auto-pilot.
4. **Immersiveness**: 3D tactical view clearly highlights "trusted" vs "untrusted" areas.
5. **Urban Realism**: Population density varies by >40% during simulated peak hours.

# OpenEnv (City Ops) — Multi-Agent Emergency Response Simulator

<div align="center">

[![Deployed on Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Live%20Demo-yellow?style=flat-square)](https://rajadityaaaaaa-file2-openenv.hf.space)
[![Next.js 14](https://img.shields.io/badge/Next.js-14-000000?style=flat-square&logo=nextdotjs&logoColor=white)](https://nextjs.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-v0.104-009688?style=flat-square&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![PPO](https://img.shields.io/badge/RL-PPO%20(Proximal%20Policy%20Optimization)-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)](https://arxiv.org)
[![React Three Fiber](https://img.shields.io/badge/Three.js-React%20Three%20Fiber-000000?style=flat-square&logo=threedotjs&logoColor=white)](https://r3f.docs.pmnd.rs)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)

**Authors: Priyam Parashar & Aditya Raj**

*A production-grade, 3D tactical simulator for adversarial multi-agent coordination — training EMS, Fire, and Police agents to coordinate across 8 Indian cities under signal-spoofing attacks.*

🚀 **[Live Demo on Hugging Face Spaces](https://rajadityaaaaaa-file2-openenv.hf.space)**

</div>

---

## 📸 Demo Preview

> **TODO:** Add a screenshot or GIF of the live 3D tactical HUD here.
> Suggested file: `assets/openenv-tactical-hud.png`
>
> Capture: 3D city isometric view with active EMS/Fire/Police units, trust heatmap overlay, and adversarial ghost signal indicators.

---

## 🏙️ What is OpenEnv?

OpenEnv is a real-time, multi-agent Reinforcement Learning (RL) simulation platform designed to optimize emergency response in dynamic urban environments. It features a digital twin city where AI agents (EMS, Fire, Police) learn to coordinate and save lives.

**The Unique Innovation:** Unlike standard simulators, OpenEnv introduces **Adversarial Informational Sabotage**. Malicious agents broadcast "Ghost Signals" (fake emergencies) to disrupt coordination. The system employs a **Mistral-7B LLM Intelligence Layer** to perform real-time semantic validation and maintain a spatial **Trust Heatmap** across the city.

---

## ✨ Key Features

| Feature | Description |
|---|---|
| **3D Tactical HUD** | Immersive isometric city view built with Three.js and React Three Fiber — units visible, relocatable, and color-coded by agent type |
| **Adversarial RL** | Configurable ghost-signal deception probability; agents learn to detect and ignore "liars" via PPO training |
| **Counter-Intelligence Layer** | Mistral-7B LLM validates incoming broadcast authenticity using weather and zone context |
| **8 Indian Cities** | Real density data for Bengaluru, Mumbai, Delhi, Chennai, Hyderabad, Pune, Kolkata, Ahmedabad |
| **Cascade Events** | FEMA-calibrated logic where primary events (fires) trigger secondary hazards (medical crises) |
| **Dynamic Weather** | 7 weather conditions affecting agent travel speed and event intensity in real time |
| **AI Command Console** | Natural-language interface for dispatchers to adjust simulation parameters on the fly |

---

## 🏗️ System Architecture

```
┌──────────────────────────────────────────────────────┐
│         Frontend — Next.js 14 + React Three Fiber     │
│  3D City Grid · Trust Heatmap · Tactical Panel HUD    │
└───────────────────────┬──────────────────────────────┘
                        │ REST / SSE
┌───────────────────────▼──────────────────────────────┐
│          Backend — FastAPI (Python 3.11)              │
│  RL Core (PPO) · Agent State Engine · Event Cascade  │
│  LLM Intelligence (Mistral-7B) · Trust Scoring       │
└───────────────────────┬──────────────────────────────┘
                        │ HF Inference API
┌───────────────────────▼──────────────────────────────┐
│     Mistral-7B-Instruct (Hugging Face Inference)     │
│   Validates: weather + zone + broadcast authenticity  │
└──────────────────────────────────────────────────────┘
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Frontend** | Next.js 14, React 18, Three.js, React Three Fiber, Recharts |
| **Backend** | FastAPI, Uvicorn, Python 3.11 |
| **RL Engine** | PPO (Proximal Policy Optimization), NumPy, PyTorch |
| **Intelligence** | Mistral-7B-Instruct (via Hugging Face Inference API) |
| **Deployment** | Docker, Hugging Face Spaces (Monolithic) |

---

## 📁 Project Structure

```
city-opes/
├── backend/
│   ├── core/               RL Environment & PPO Logic
│   ├── api/                REST & SSE Endpoints
│   ├── services/           LLM Integration (Mistral-7B)
│   └── static/             Built Next.js static files
├── frontend/
│   ├── components/         3D Grid & Tactical Panels
│   └── lib/                API & Translation Utilities
├── hf_space/               Deployment Container Config
├── docs/                   Patent Drafts & Methodology Diagrams
├── Dockerfile
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.11+
- Node.js 18+
- Hugging Face API token (for Mistral-7B inference)

### Backend Setup

```bash
git clone https://github.com/aditweb13/city-opes.git
cd city-opes/backend

pip install -r requirements.txt

# Set your HF token for Mistral-7B
export HF_TOKEN=your_token_here

python -m uvicorn api.main:app --port 8000
```

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
# → http://localhost:3000
```

### Docker (Full Stack)

```bash
docker build -t openenv .
docker run -p 7860:7860 -e HF_TOKEN=$HF_TOKEN openenv
```

---

## 🌐 Live Deployment

**Hugging Face Spaces:** [rajadityaaaaaa-file2-openenv.hf.space](https://rajadityaaaaaa-file2-openenv.hf.space)

The full monolithic stack (FastAPI serving built Next.js statics) is containerized and deployed to Hugging Face Spaces via Docker.

---

## 🗺️ Roadmap

- [ ] Full PPO training run with convergence curves and reward plots
- [ ] Agent replay visualization (exportable video of emergency scenarios)
- [ ] Multi-city simultaneous event simulation
- [ ] Additional Indian cities and real OSM road networks

---

## 📄 Intellectual Property

This project includes a novel **Trust-Augmented Coordination Architecture** — a patent draft is included in `/docs`.

**Inventors:** Priyam Parashar & Aditya Raj

---

## 📄 License

MIT — see [LICENSE](LICENSE).

---

<div align="center">

Built by [Aditya Raj](https://github.com/aditweb13) & Priyam Parashar · [LinkedIn](https://linkedin.com/in/aditya-raj-a1891a285)

</div>

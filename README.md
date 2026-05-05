# OpenEnv — Multi-Agent Emergency Response Simulator
### **Authors:** Priyam Parashar & Aditya Raj
> **A production-grade, 3D tactical simulator for adversarial multi-agent coordination.**

[![Deployed on Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-yellow)](https://huggingface.co/spaces/rajadityaaaaaa/file2-openenv)
[![Next.js 14](https://img.shields.io/badge/Next.js-14-black)](https://nextjs.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-v0.104-green)](https://fastapi.tiangolo.com/)

---

## 🏙️ What is OpenEnv?
OpenEnv is a real-time, multi-agent Reinforcement Learning (RL) simulation platform designed to optimize emergency response in dynamic urban environments. It features a digital twin city where AI agents (EMS, Fire, Police) learn to coordinate and save lives.

**The Unique Innovation:** Unlike standard simulators, OpenEnv introduces **Adversarial Informational Sabotage**. Malicious agents broadcast "Ghost Signals" (fake emergencies) to disrupt coordination. The system employs a **Mistral-7B LLM Intelligence Layer** to perform real-time semantic validation and maintain a spatial **Trust Heatmap**.

---

## ✨ Key Features
*   **3D Tactical HUD**: Immersive isometric city view built with **Three.js** and **React Three Fiber**.
*   **Adversarial RL**: Configurable deception probability where agents must learn to ignore "liars."
*   **Counter-Intelligence Pipeline**: Mistral-7B LLM validates broadcasts based on weather and zone context.
*   **Real Indian Cities**: Supports 8 cities including Bangalore, Mumbai, and Delhi with real density data.
*   **Cascade Engine**: FEMA-calibrated logic where primary events (Fires) trigger secondary hazards (Medical crises).
*   **Dynamic Weather**: 7 weather conditions that affect agent speed and event intensity.
*   **AI Command Console**: Natural language interface to adjust simulation parameters on the fly.

---

## 🛠️ Tech Stack
| Layer | Technology |
|---|---|
| **Frontend** | Next.js 14, React 18, Three.js, Recharts |
| **Backend** | FastAPI, Uvicorn, Python 3.11 |
| **RL Engine** | PPO (Proximal Policy Optimization), NumPy, PyTorch |
| **Intelligence** | Mistral-7B-Instruct (via Hugging Face API) |
| **Deployment** | Docker, Hugging Face Spaces (Monolithic) |

---

## 🚀 Deployment
**Live Link:** [https://rajadityaaaaaa-file2-openenv.hf.space](https://rajadityaaaaaa-file2-openenv.hf.space)

---

## 📂 Project Structure
```bash
FILE2/
├── backend/            # FastAPI Simulation Engine
│   ├── core/           # RL Environment & PPO Logic
│   ├── api/            # REST & SSE Endpoints
│   ├── services/       # LLM Integration (Mistral-7B)
│   └── static/         # Built Next.js static files
├── frontend/           # Next.js 14 Dashboard
│   ├── components/     # 3D Grid & Tactical Panels
│   └── lib/            # API & Translation Utilities
├── hf_space/           # Deployment Container Config
└── docs/               # Patent Drafts & Methodology Diagrams
```

---

## 📜 Intellectual Property
This project includes a novel **Trust-Augmented Coordination Architecture** (Patent Draft included in `/docs`).
**Inventors:** Priyam Parashar & Aditya Raj

---

## 🛠️ Local Setup

1. **Clone the repo**
2. **Backend Setup:**
   ```bash
   cd backend
   pip install -r requirements.txt
   python -m uvicorn api.main:app --port 8000
   ```
3. **Frontend Setup:**
   ```bash
   cd frontend
   npm install
   npm run dev
   ```

---
**License:** MIT

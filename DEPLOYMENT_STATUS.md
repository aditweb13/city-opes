# OpenEnv Deployment Status

## ✅ Deployments

### 1. Hugging Face Space (Primary)
- **URL**: https://huggingface.co/spaces/rajadityaaaaaa/file2-openenv
- **API**: https://rajadityaaaaaa-file2-openenv.hf.space
- **Status**: Operational
- **Architecture**: Monolithic Docker (FastAPI + Next.js Static)

### 2. Vercel Frontend (Mirror)
- **URL**: https://emergency-response-simulator-fronte-one.vercel.app/
- **Backend**: https://emergency-response-simulator-backend.onrender.com (Render)
- **Fix**: Trailing slash issue in `NEXT_PUBLIC_API_URL` has been resolved.

## 🚀 Key Features Active
- **MARL Simulation**: Multi-agent PPO coordination in Indian cities.
- **AI Intelligence Layer**: Mistral-7B powered event analysis and tactical reports.
- **Adversarial Resilience**: Agents automatically ignore deceptive signals from compromised zones.
- **Natural Language Control**: Simulation parameters can be adjusted via the AI Command Console.

## 🛠️ Maintenance & Development
- To update the HF Space:
  1. Ensure `hf_space/` folder has the latest `core/`, `api/`, and `static/` files.
  2. Run `python deploy_hf.py`.
- To rebuild frontend:
  1. `cd frontend`
  2. `npm run build`
  3. Copy `out/` to `hf_space/static/`.

---
*OpenEnv v1.0 — Emergency Response RL System*

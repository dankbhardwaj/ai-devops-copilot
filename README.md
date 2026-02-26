🚀 AI DevOps Copilot

An end-to-end AI-powered DevOps assistant built using FastAPI, Ollama, RAG (ChromaDB), Docker, Kubernetes, and GitHub Actions CI/CD.

This project demonstrates a production-style DevOps workflow integrating AI with containerization and automated deployment.

🧠 Project Overview

AI DevOps Copilot answers DevOps and Kubernetes-related questions using Retrieval-Augmented Generation (RAG).

Instead of directly querying an LLM, the system:

Retrieves relevant documentation

Passes it as context to the LLM

Generates grounded, accurate answers

This reduces hallucination and improves reliability.

🏗 Architecture
User Question
     ↓
FastAPI (/ask endpoint)
     ↓
Chroma Vector DB (Retrieve relevant docs)
     ↓
Ollama LLM
     ↓
Generated Answer

CI/CD Flow:

Git Push
   ↓
GitHub Actions (Self-hosted runner)
   ↓
Docker Build
   ↓
Push to Docker Hub
   ↓
kubectl set image
   ↓
Rolling Update in Kubernetes
🛠 Tech Stack

Backend: FastAPI

LLM: Ollama (TinyLlama / Phi3 / Llama3)

Embeddings: nomic-embed-text

Vector DB: ChromaDB

Containerization: Docker

Orchestration: Kubernetes (kind)

CI/CD: GitHub Actions

Image Registry: Docker Hub

📂 Project Structure
ai-devops-copilot/
│
├── app/
│   ├── main.py
│   ├── routes/
│   ├── services/
│   ├── rag/
│   └── agents/
│
├── docs/
├── k8s/
│   ├── deployment.yaml
│   ├── service.yaml
│
├── Dockerfile
├── requirements.txt
└── .github/workflows/
⚙️ Local Setup
1️⃣ Clone Repo
git clone https://github.com/dankbhardwaj/ai-devops-copilot.git
cd ai-devops-copilot
2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
3️⃣ Start Ollama
ollama run tinyllama

Ensure Ollama runs on:

http://localhost:11434
4️⃣ Create Embeddings
python create_embeddings.py
5️⃣ Run FastAPI
uvicorn app.main:app --reload

Open:

http://localhost:8000/docs
🐳 Docker

Build image:

docker build -t dankbhardwaj/ai-devops-copilot:latest .

Run container:

docker run -p 8000:8000 \
  --add-host=host.docker.internal:host-gateway \
  dankbhardwaj/ai-devops-copilot
☸ Kubernetes Deployment

Create kind cluster:

kind create cluster --name dev

Load image:

kind load docker-image dankbhardwaj/ai-devops-copilot:latest --name dev

Deploy:

kubectl apply -f k8s/

Access via port-forward:

kubectl port-forward service/ai-devops-service 8000:8000

Open:

http://localhost:8000/docs
🔄 CI/CD Pipeline

On every push to main:

Build Docker image

Tag with commit SHA

Push to Docker Hub

Update Kubernetes deployment

Trigger rolling update

Deployment strategy:

StrategyType: RollingUpdate
maxUnavailable: 25%
maxSurge: 25%
📦 Features

✔ RAG-based grounded responses
✔ Local LLM integration
✔ Dockerized application
✔ Kubernetes deployment
✔ Rolling updates
✔ Automated CI/CD
✔ Self-hosted GitHub runner

🎯 Future Improvements

Liveness & Readiness Probes

Persistent Volume for ChromaDB

Horizontal Pod Autoscaler (HPA)

Helm packaging

Security scanning (Trivy)

Cloud deployment (EKS)

🏆 Resume Highlight

Built an end-to-end AI DevOps Copilot using FastAPI, Ollama (LLM), RAG (ChromaDB), Docker, Kubernetes (kind), and GitHub Actions with full CI/CD and rolling deployments.

👨‍💻 Author

Bhaskar Sharma
GitHub: https://github.com/dankbhardwaj

🚀 Status

Project Version: v1.0
Deployment: Automated CI/CD Enabled
Cluster: Local Kubernetes (kind)

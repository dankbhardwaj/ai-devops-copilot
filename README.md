<div align="center">

# 🤖 AI DevOps Copilot

[![CI/CD](https://img.shields.io/github/actions/workflow/status/dankbhardwaj/ai-devops-copilot/deploy.yml?branch=main&label=CI%2FCD&logo=github-actions&logoColor=white)](https://github.com/dankbhardwaj/ai-devops-copilot/actions)
[![Docker](https://img.shields.io/docker/pulls/dankbhardwaj/ai-devops-copilot?logo=docker&logoColor=white&color=2496ED)](https://hub.docker.com/r/dankbhardwaj/ai-devops-copilot)
[![Kubernetes](https://img.shields.io/badge/Kubernetes-Enabled-326CE5?logo=kubernetes&logoColor=white)](https://kubernetes.io/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)](https://www.python.org/)

**A production-grade LLMOps system integrating RAG, LLM inference, containerization, Kubernetes orchestration, and automated CI/CD pipelines.**

[📖 Documentation](#-architecture) • [🚀 Quick Start](#-quick-start) • [🛠 API Reference](#-api-reference) • [🤝 Contributing](#-contributing)

---

</div>

## 📌 Table of Contents

- [Overview](#-overview)
- [Architecture](#-architecture)
- [Tech Stack](#-tech-stack)
- [System Flow Diagrams](#-system-flow-diagrams)
- [CI/CD Pipeline](#-cicd-pipeline)
- [Kubernetes Deployment Strategy](#-kubernetes-deployment-strategy)
- [Quick Start](#-quick-start)
- [Docker Usage](#-docker-usage)
- [Kubernetes Setup](#-kubernetes-setup)
- [API Reference](#-api-reference)
- [Project Structure](#-project-structure)
- [DevOps Capabilities](#-devops-capabilities)
- [Screenshots](#-screenshots)
- [Resume Summary](#-resume-summary)
- [Author](#-author)

---

## 🧠 Overview

**AI DevOps Copilot** is a **Retrieval-Augmented Generation (RAG)** assistant specialized in answering DevOps, Kubernetes, and cloud infrastructure questions. It combines semantic search with large language model inference to deliver accurate, context-aware responses.

This project is a complete **end-to-end LLMOps demonstration** covering:

- 🔍 **Intelligent retrieval** from a vector database (ChromaDB)
- 🧠 **Local LLM inference** via Ollama (no cloud API costs)
- ⚡ **High-performance REST API** using FastAPI
- 🐳 **Containerized** with Docker for portability
- ☸️ **Orchestrated** on Kubernetes with zero-downtime deployments
- 🔁 **Fully automated CI/CD** with GitHub Actions

---

## 🏗 Architecture

### High-Level System Architecture

```mermaid
graph TB
    subgraph CLIENT["🖥️ Client Layer"]
        A[Web Browser / cURL / SDK]
    end

    subgraph API["⚡ API Layer"]
        B[FastAPI Server<br/>POST /ask<br/>GET /health]
    end

    subgraph RAG["🔍 RAG Pipeline"]
        C[Query Encoder<br/>Embedding Model]
        D[(ChromaDB<br/>Vector Store)]
        E[Context Retriever<br/>Top-K Results]
    end

    subgraph LLM["🧠 LLM Inference"]
        F[Ollama Runtime]
        G[TinyLlama / Phi3 / Llama3]
    end

    subgraph OUTPUT["📤 Response"]
        H[AI-Generated Answer<br/>with Context]
    end

    A -->|HTTP POST /ask| B
    B --> C
    C -->|Embed Query| D
    D -->|Semantic Search| E
    E -->|Retrieved Context| F
    F --> G
    G -->|Generated Response| H
    H -->|JSON Response| A

    style CLIENT fill:#1a1a2e,stroke:#e94560,color:#fff
    style API fill:#16213e,stroke:#0f3460,color:#fff
    style RAG fill:#0f3460,stroke:#533483,color:#fff
    style LLM fill:#533483,stroke:#e94560,color:#fff
    style OUTPUT fill:#1a1a2e,stroke:#e94560,color:#fff
```

---

## 🛠 Tech Stack

| Category | Technology | Purpose |
|---|---|---|
| **API Framework** | ![FastAPI](https://img.shields.io/badge/-FastAPI-009688?logo=fastapi&logoColor=white) | REST API server & Swagger UI |
| **LLM Runtime** | ![Ollama](https://img.shields.io/badge/-Ollama-black?logo=llama&logoColor=white) | Local LLM inference engine |
| **LLM Models** | TinyLlama / Phi3 / Llama3 | Language model backends |
| **Vector DB** | ChromaDB | Semantic context retrieval |
| **Containerization** | ![Docker](https://img.shields.io/badge/-Docker-2496ED?logo=docker&logoColor=white) | Application packaging |
| **Orchestration** | ![Kubernetes](https://img.shields.io/badge/-Kubernetes-326CE5?logo=kubernetes&logoColor=white) | Container orchestration |
| **Local K8s** | kind (K8s in Docker) | Local cluster for development |
| **CI/CD** | ![GitHub Actions](https://img.shields.io/badge/-GitHub_Actions-2088FF?logo=github-actions&logoColor=white) | Automated pipelines |
| **Runner** | Self-hosted GitHub Runner | Pipeline execution agent |
| **Registry** | ![Docker Hub](https://img.shields.io/badge/-Docker_Hub-2496ED?logo=docker&logoColor=white) | Container image registry |
| **Language** | ![Python](https://img.shields.io/badge/-Python_3.11+-3776AB?logo=python&logoColor=white) | Application language |

---

## 🔄 System Flow Diagrams

### RAG Query Processing Pipeline

```mermaid
sequenceDiagram
    autonumber
    actor User
    participant API as FastAPI<br/>/ask endpoint
    participant Embed as Embedding<br/>Model
    participant VDB as ChromaDB<br/>Vector Store
    participant LLM as Ollama<br/>LLM Runtime
    participant Model as TinyLlama /<br/>Phi3 / Llama3

    User->>+API: POST /ask {"question": "How to scale pods in K8s?"}
    API->>+Embed: Encode query to vector
    Embed-->>-API: Query embedding [0.23, -0.41, ...]
    API->>+VDB: Similarity search (top-k=3)
    VDB-->>-API: Relevant context chunks
    Note over API: Build augmented prompt:<br/>Context + Question
    API->>+LLM: Send augmented prompt
    LLM->>+Model: Forward pass inference
    Model-->>-LLM: Generated tokens
    LLM-->>-API: Decoded response text
    API-->>-User: {"answer": "To scale pods, use kubectl scale..."}
```

---

### Component Interaction Map

```mermaid
graph LR
    subgraph INGESTION["📥 Data Ingestion (Offline)"]
        D1[Raw DevOps Docs]
        D2[K8s Docs]
        D3[Custom Knowledge Base]
        D4[Text Chunker & Embedder]
        D5[(ChromaDB)]
        D1 & D2 & D3 --> D4 --> D5
    end

    subgraph INFERENCE["⚡ Inference (Online)"]
        I1[User Query]
        I2[FastAPI]
        I3[Embed Query]
        I4[Vector Search]
        I5[Prompt Builder]
        I6[Ollama]
        I7[Response]
        I1 --> I2 --> I3 --> I4 --> I5 --> I6 --> I7
    end

    D5 -->|Retrieve Context| I4

    style INGESTION fill:#1e3a5f,stroke:#4fc3f7,color:#fff
    style INFERENCE fill:#1b5e20,stroke:#81c784,color:#fff
```

---

## 🔁 CI/CD Pipeline

### GitHub Actions Workflow

```mermaid
flowchart TD
    A([👨‍💻 Developer\nPushes Code]) -->|git push origin main| B

    subgraph GHA["🔧 GitHub Actions Cloud"]
        B[Trigger Workflow\ngithub.event: push]
        B --> C{Branch Check\nbranch == 'main'?}
        C -->|❌ No| Z([Skip Deployment])
        C -->|✅ Yes| D[Checkout Repository\nactions/checkout@v3]
        D --> E[Set up Docker Buildx\ndocker/setup-buildx-action]
        E --> F[Login to Docker Hub\ndocker/login-action]
    end

    subgraph RUNNER["🖥️ Self-Hosted Runner"]
        F --> G[Build Docker Image\ndocker build -t app:SHA]
        G --> H{Build\nSuccess?}
        H -->|❌ Fail| FAIL([🚨 Notify Failure\nPipeline Aborted])
        H -->|✅ Pass| I[Tag with Commit SHA\n& 'latest']
        I --> J[Push to Docker Hub\ndocker push]
        J --> K[Update K8s Deployment\nkubectl set image]
        K --> L[Rolling Update Triggered\nKubernetes Scheduler]
    end

    subgraph K8S["☸️ Kubernetes Cluster"]
        L --> M[Old Pod: Terminating]
        L --> N[New Pod: Pulling Image]
        N --> O{Health Check\nReadiness Probe}
        O -->|❌ Fail| P[Rollback Initiated\nPrevious Version Restored]
        O -->|✅ Pass| Q([🟢 Deployment Live\nZero Downtime])
    end

    style GHA fill:#1a1a2e,stroke:#4fc3f7,color:#fff
    style RUNNER fill:#0d1b2a,stroke:#e94560,color:#fff
    style K8S fill:#1b2838,stroke:#326CE5,color:#fff
```

---

## ☸️ Kubernetes Deployment Strategy

### Rolling Update Architecture

```mermaid
graph TB
    subgraph CLUSTER["☸️ Kubernetes Cluster (kind)"]

        subgraph CTRL["Control Plane"]
            API_SRV[kube-apiserver]
            SCHED[kube-scheduler]
            CM[controller-manager]
        end

        subgraph NS["Namespace: default"]
            SVC[Service\nai-devops-service\nport: 8000]

            subgraph DEPLOY["Deployment: ai-devops-copilot\nstrategy: RollingUpdate"]
                subgraph RS_NEW["ReplicaSet v2 (New)"]
                    P3[🟢 Pod v2\nRunning]
                    P4[🟡 Pod v2\nStarting]
                end
                subgraph RS_OLD["ReplicaSet v1 (Old)"]
                    P1[🔴 Pod v1\nTerminating]
                    P2[🟢 Pod v1\nRunning]
                end
            end
        end

        SVC --> P2
        SVC --> P3
        API_SRV --> DEPLOY
        SCHED --> P4
        CM --> RS_NEW
    end

    subgraph POLICY["🔄 Rolling Update Policy"]
        direction LR
        RU1["maxUnavailable: 25%\n(min 1 pod always serving)"]
        RU2["maxSurge: 25%\n(max 1 extra pod during update)"]
        RU3["Zero Downtime ✅"]
        RU1 --- RU2 --- RU3
    end

    style CLUSTER fill:#0d1b35,stroke:#326CE5,color:#fff
    style CTRL fill:#0f2044,stroke:#4fc3f7,color:#fff
    style NS fill:#112244,stroke:#326CE5,color:#fff
    style DEPLOY fill:#0a1a33,stroke:#81c784,color:#fff
    style POLICY fill:#1b2838,stroke:#e94560,color:#fff
```

---

### Kubernetes Resource Topology

```mermaid
graph LR
    subgraph K8S_RES["Kubernetes Resources"]
        direction TB
        CM2[ConfigMap\napp-config]
        SEC[Secret\nregistry-credentials]
        DEP[Deployment\nai-devops-copilot\nreplicas: 2]
        SVC2[Service\nClusterIP / NodePort\n:8000]
        ING[Ingress\n/ask → svc:8000]
        HPA[HorizontalPodAutoscaler\nmin:2 max:10\nCPU: 70%]

        CM2 --> DEP
        SEC --> DEP
        DEP --> SVC2
        SVC2 --> ING
        HPA --> DEP
    end

    style K8S_RES fill:#0d1b35,stroke:#326CE5,color:#fff
```

---

## 🚀 Quick Start

### Prerequisites

```bash
# Required tools
docker --version       # Docker 24+
kubectl version        # Kubernetes CLI
kind version           # Kind 0.20+
ollama --version       # Ollama runtime
```

### 1️⃣ Clone Repository

```bash
git clone https://github.com/dankbhardwaj/ai-devops-copilot.git
cd ai-devops-copilot
```

### 2️⃣ Start Ollama & Pull Model

```bash
# Start Ollama service
ollama serve &

# Pull a lightweight model
ollama pull tinyllama
# OR for better quality:
ollama pull phi3
```

### 3️⃣ Run Locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

Open: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🐳 Docker Usage

### Build Image

```bash
docker build -t dankbhardwaj/ai-devops-copilot:latest .
```

### Run Container

```bash
docker run -d \
  --name ai-devops-copilot \
  -p 8000:8000 \
  --add-host=host.docker.internal:host-gateway \
  dankbhardwaj/ai-devops-copilot:latest
```

### Docker Compose (Recommended)

```bash
docker compose up -d
```

---

## ☸️ Kubernetes Setup

### Step 1 — Create Kind Cluster

```bash
kind create cluster --name dev
kubectl cluster-info --context kind-dev
```

### Step 2 — Load Image into Kind

```bash
kind load docker-image dankbhardwaj/ai-devops-copilot:latest --name dev
```

### Step 3 — Deploy to Kubernetes

```bash
kubectl apply -f k8s/
```

### Step 4 — Verify Deployment

```bash
# Check pods are running
kubectl get pods -l app=ai-devops-copilot

# Check deployment rollout
kubectl rollout status deployment/ai-devops-copilot

# Describe deployment
kubectl describe deployment ai-devops-copilot
```

### Step 5 — Access the Application

```bash
kubectl port-forward service/ai-devops-service 8000:8000
```

Open: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🌐 API Reference

### `POST /ask`

Submit a question to the AI DevOps Copilot.

**Request:**
```json
{
  "question": "How do I perform a rolling update in Kubernetes?"
}
```

**Response:**
```json
{
  "answer": "To perform a rolling update in Kubernetes, you can update the image of your deployment using: kubectl set image deployment/<name> <container>=<new-image>. Kubernetes will then gradually replace old pods with new ones, ensuring zero downtime based on your maxUnavailable and maxSurge settings.",
  "context_used": true,
  "model": "tinyllama",
  "latency_ms": 842
}
```

### `GET /health`

Health check endpoint.

```json
{
  "status": "healthy",
  "vector_db": "connected",
  "ollama": "connected"
}
```

---

## 📁 Project Structure

```
ai-devops-copilot/
├── 📂 app/
│   ├── main.py              # FastAPI application entry point
│   ├── routes/
│   │   └── ask.py           # /ask endpoint handler
│   ├── rag/
│   │   ├── retriever.py     # ChromaDB vector search
│   │   ├── embedder.py      # Embedding model wrapper
│   │   └── prompt.py        # Prompt template builder
│   └── llm/
│       └── ollama_client.py # Ollama API client
├── 📂 data/
│   └── knowledge_base/      # DevOps & K8s documentation
├── 📂 k8s/
│   ├── deployment.yaml      # Kubernetes Deployment manifest
│   ├── service.yaml         # Kubernetes Service manifest
│   └── hpa.yaml             # HorizontalPodAutoscaler
├── 📂 .github/
│   └── workflows/
│       └── deploy.yml       # GitHub Actions CI/CD pipeline
├── Dockerfile               # Multi-stage Docker build
├── docker-compose.yml       # Local development stack
├── requirements.txt         # Python dependencies
└── README.md
```

---

## 🎯 DevOps Capabilities Demonstrated

```mermaid
mindmap
  root((AI DevOps\nCopilot))
    LLMOps
      RAG Pipeline
      Local LLM Inference
      Vector Embeddings
      ChromaDB Integration
    Containerization
      Multi-stage Dockerfile
      Docker Compose
      Image Versioning with SHA
      Docker Hub Registry
    Kubernetes
      Kind Local Cluster
      Deployment Manifests
      Rolling Update Strategy
      Zero-Downtime Deploys
      HPA Autoscaling
    CI/CD Automation
      GitHub Actions Workflow
      Self-hosted Runner
      Automated Image Build
      kubectl Rolling Update
      Commit SHA Tagging
    API Design
      FastAPI REST API
      Swagger UI
      Health Checks
      JSON Responses
```

---

## 📸 Screenshots

<details>
<summary>☸️ Kubernetes Pod Running</summary>

> Demonstrates successful deployment and running container in Kubernetes with `kubectl get pods`.

![K8s Pods](docs/screenshots/k8s-pods.png)

</details>

<details>
<summary>🔄 Rolling Update in Progress</summary>

> Live rolling update with old pods terminating and new pods initializing — zero downtime maintained.

![Rolling Update](docs/screenshots/rolling-update.png)

</details>

<details>
<summary>🔁 GitHub Actions CI/CD Pipeline</summary>

> Automated workflow: build → tag → push → deploy. Triggered on every push to `main`.

![CI/CD Pipeline](docs/screenshots/github-actions.png)

</details>

<details>
<summary>🌐 FastAPI Swagger UI</summary>

> Interactive API documentation at `/docs` with live `POST /ask` endpoint.

![Swagger UI](docs/screenshots/swagger-ui.png)

</details>

---

## 🏆 Resume Summary

> Built a **production-style LLMOps system** integrating Retrieval-Augmented Generation (RAG), FastAPI, Docker, Kubernetes, and fully automated CI/CD with rolling deployments. Demonstrated end-to-end ownership from LLM inference to zero-downtime production delivery using self-hosted GitHub Actions runners, ChromaDB vector search, and Ollama for local model inference.

**Key achievements:**
- ✅ End-to-end RAG pipeline with ChromaDB and local LLM (Ollama)
- ✅ Dockerized AI application with multi-stage builds and SHA-tagged versioning
- ✅ Kubernetes orchestration on Kind with zero-downtime rolling updates
- ✅ Fully automated CI/CD pipeline with self-hosted GitHub Actions runner
- ✅ Production-ready API with health checks and Swagger documentation

---

## 📌 Repository

🔗 [https://github.com/dankbhardwaj/ai-devops-copilot](https://github.com/dankbhardwaj/ai-devops-copilot)

---

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'feat: add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

## 👨‍💻 Author

**Bhaskar Sharma**

*DevOps | LLMOps | Kubernetes | CI/CD | AI Infrastructure*

[![GitHub](https://img.shields.io/badge/GitHub-dankbhardwaj-181717?logo=github)](https://github.com/dankbhardwaj)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?logo=linkedin)](https://linkedin.com/in/dankbhardwaj)

---

⭐ **Star this repo** if you found it useful!

*Built with ❤️ for the DevOps & AI community*

</div>

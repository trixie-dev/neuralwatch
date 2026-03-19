# NeuralWatch

A live dashboard shows real-time model status, CPU load, latency, and request traffic.

---

## What it does

You can register AI models (like TensorFlow or PyTorch deployments), check their health status, send mock inference requests, and manage them through a secured REST API. A standalone HTML dashboard visualises everything live.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, FastAPI |
| Auth | JWT (OAuth2 + Bearer tokens) |
| Database | SQLite via SQLAlchemy |
| Containerisation | Docker + Docker Compose |
| Frontend | Vanilla HTML/CSS/JS |

---

## API Endpoints

| Method | Endpoint | Auth | Description |
|---|---|---|---|
| POST | `/api/auth/register` | ❌ | Create a user account |
| POST | `/api/auth/token` | ❌ | Login and get JWT token |
| GET | `/api/models` | ✅ | List all registered models |
| POST | `/api/models/register` | ✅ | Register a new model |
| GET | `/api/models/{id}/status` | ✅ | Get one model's status |
| POST | `/api/models/{id}/predict` | ✅ | Send a mock inference request |
| DELETE | `/api/models/{id}` | ✅ | Remove a model |

---

## Getting Started

```bash
git clone https://github.com/YOUR_USERNAME/neuralwatch.git
cd neuralwatch
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Then visit `http://127.0.0.1:8000/docs`
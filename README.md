# Mini Workflow Engine

A mini n8n-style workflow automation backend built using:

- FastAPI
- PostgreSQL
- MongoDB
- Redis
- Celery
- Docker
- JWT Authentication
- Async Programming
- Webhooks
- CI/CD

---

# Features

- User Registration/Login
- JWT Authentication
- Create Workflows
- Dynamic Webhook URLs
- Async Webhook Processing
- Background Task Queue using Celery
- PostgreSQL for relational data
- MongoDB for event logs
- Dockerized setup
- GitHub Actions CI/CD

---

# Architecture

```text
Client
   ↓
FastAPI APIs
   ↓
Webhook Endpoint
   ↓
MongoDB Stores Logs
   ↓
Celery Queue (Redis)
   ↓
Background Worker
   ↓
PostgreSQL Updates Status
```

---

# Project Structure

```text
mini-workflow-engine/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── mongodb.py
│   ├── models.py
│   ├── schemas.py
│   ├── auth.py
│   ├── tasks.py
│   ├── celery_worker.py
│   └── routers/
│       ├── user_router.py
│       ├── workflow_router.py
│       └── webhook_router.py
│
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

# Prerequisites

Install:

- Docker Desktop
- Python 3.11+

Verify Docker:

```bash
docker ps
```

---

# Running Project Locally

## Step 1 — Clone Repository

```bash
git clone <your_repo_url>

cd mini-workflow-engine
```

---

## Step 2 — Start Docker Desktop

Open Docker Desktop and ensure it is running.

Verify:

```bash
docker ps
```

---

## Step 3 — Start All Services

Run:

```bash
docker compose up --build
```

This starts:

- FastAPI
- PostgreSQL
- MongoDB
- Redis
- Celery Worker

---

# Services Running

| Service | Port |
|---|---|
| FastAPI | 8000 |
| PostgreSQL | 5432 |
| MongoDB | 27017 |
| Redis | 6379 |

---

# Open Swagger Docs

Open:

```text
http://localhost:8000/docs
```

You can test APIs directly from Swagger UI.

---

# API Endpoints

## Register User

```http
POST /users/register
```

Body:

```json
{
  "email": "test@gmail.com",
  "password": "123456"
}
```

---

## Login User

```http
POST /users/login
```

Body:

```json
{
  "email": "test@gmail.com",
  "password": "123456"
}
```

---

## Create Workflow

```http
POST /workflow/create
```

Body:

```json
{
  "name": "GitHub Workflow"
}
```

Response:

```json
{
  "webhook_url": "/webhook/abc123"
}
```

---

## Trigger Webhook

```http
POST /webhook/{workflow_id}
```

Example:

```http
POST /webhook/abc123
```

Body:

```json
{
  "event": "push",
  "repo": "workflow-engine"
}
```

---

# How Webhook Flow Works

```text
External System Sends Webhook
            ↓
FastAPI Receives Event
            ↓
Payload Stored in MongoDB
            ↓
Task Sent to Redis Queue
            ↓
Celery Worker Processes Task
            ↓
Status Stored in PostgreSQL
```

---

# View PostgreSQL Data

Open PostgreSQL shell:

```bash
docker exec -it mini-workflow-engine-db-1 psql -U postgres
```

Connect database:

```sql
\c workflow_db
```

Show tables:

```sql
\dt
```

View data:

```sql
SELECT * FROM users;
```

Exit:

```sql
\q
```

---

# View MongoDB Data

Open Mongo shell:

```bash
docker exec -it mini-workflow-engine-mongo-1 mongosh
```

Show databases:

```javascript
show dbs
```

Switch database:

```javascript
use workflow_logs
```

Show collections:

```javascript
show collections
```

View documents:

```javascript
db.workflow_logs.find().pretty()
```

---

# Stop Containers

```bash
docker compose down
```

---

# Remove Containers + Data

```bash
docker compose down -v
```

WARNING:

This deletes:
- PostgreSQL data
- MongoDB data
- Docker volumes

---

# Rebuild Containers

```bash
docker compose up --build
```

---

# Common Docker Commands

## See Running Containers

```bash
docker ps
```

---

## See All Containers

```bash
docker ps -a
```

---

## See Volumes

```bash
docker volume ls
```

---

## See Logs

```bash
docker compose logs
```

---

## See API Logs Only

```bash
docker compose logs api
```

---

## See Celery Logs

```bash
docker compose logs celery
```

---

# Future Improvements

- JWT Protected Routes
- Role Based Access
- Workflow Nodes
- Retry Dashboard
- WebSocket Notifications
- Slack Integration
- GitHub Integration
- Rate Limiting
- Redis Caching
- LangGraph Integration
- AI Agent Workflows
- RAG Pipeline

---

# Tech Concepts Learned

- Async APIs
- Webhooks
- Background Processing
- Celery Workers
- Redis Queues
- Docker Containers
- PostgreSQL
- MongoDB
- JWT Authentication
- REST APIs
- CI/CD
- Event Driven Architecture

---
# Flask Monitoring App 🚀

A multi-container application built with **Flask + Redis + Prometheus + Grafana** using Docker Compose.

## 📌 Project Overview

This project demonstrates container orchestration and application monitoring using Docker Compose. Four containers work together on a shared network — no manual networking required.

| Container | Role | Port |
|-----------|------|------|
| Flask | Web app with visit counter | 5001 |
| Redis | In-memory store for visit count | 6379 |
| Prometheus | Scrapes metrics from Flask | 9090 |
| Grafana | Visualizes Prometheus metrics | 3000 |

## 🏗️ Project Structureflask-monitoring-app/

├── app.py               # Flask app with Redis counter and /metrics endpoint

├── Dockerfile           # Containerizes the Flask app

├── docker-compose.yml   # Defines and orchestrates all 4 containers

├── prometheus.yml       # Prometheus scrape configuration

├── requirements.txt     # Python dependencies

└── README.md## ⚙️ How It Works

- Flask serves a webpage that increments a **Redis visit counter** on every request
- Flask exposes a `/metrics` endpoint using `prometheus_client`
- Prometheus scrapes `/metrics` every 5 seconds
- Grafana connects to Prometheus to visualize metrics in real time
- All containers communicate via a Docker bridge network called `monitor-net`

## 🚀 Run Locally

### Prerequisites
- Docker
- Docker Compose

### Steps

```bash
git clone https://github.com/jeevansaibotla/flask-monitoring-app.git
cd flask-monitoring-app
docker-compose up -d --build
```

### Access the Services

| Service | URL |
|---------|-----|
| Flask App | http://localhost:5001 |
| Flask Metrics | http://localhost:5001/metrics |
| Prometheus | http://localhost:9090 |
| Grafana | http://localhost:3000 |

### Grafana Setup
1. Login at `http://localhost:3000` with `admin / admin`
2. Go to **Connections → Data Sources → Add → Prometheus**
3. Set URL to `http://prometheus:9090`
4. Click **Save & Test**
5. Create a panel with query: `flask_request_count_total`

## 🛑 Stop the App

```bash
docker-compose down
```

## 🧠 Key Concepts Demonstrated

- **Docker Compose** — multi-container orchestration with a single command
- **Container Networking** — service discovery using container names instead of IPs
- **Application Monitoring** — metrics collection with Prometheus
- **Data Visualization** — real-time dashboards with Grafana
- **Redis** — in-memory data store for fast read/write operations

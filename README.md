#  Order Processing System

An Event-Driven Microservices Order Processing System built with **FastAPI**, **RabbitMQ**, **PostgreSQL**, **SQLAlchemy**, **Docker**, and **Docker Compose**.

The system demonstrates asynchronous communication between microservices using the Publish/Subscribe (Pub/Sub) pattern with RabbitMQ.

---

#  Architecture

```
                    +----------------+
                    |     Client     |
                    +--------+-------+
                             |
                             v
                   +-------------------+
                   |   Order Service   |
                   +-------------------+
                             |
                    Publish Event
                    order.created
                             |
                             v
                     +---------------+
                     |   RabbitMQ    |
                     +---------------+
                       |           |
             Consume   |           | Consume
                       |           |
                       v           v
        +-------------------+   +------------------------+
        | Inventory Service |   | Notification Service   |
        +-------------------+   +------------------------+
```

---

#  Features

- Event-Driven Microservices Architecture
- FastAPI REST APIs
- RabbitMQ Pub/Sub Messaging
- PostgreSQL Database
- SQLAlchemy ORM
- Dockerized Services
- Docker Compose Orchestration
- Idempotent Event Processing
- Asynchronous Communication
- Independent Microservices

---

#  Tech Stack

| Technology | Purpose |
|------------|----------|
| Python 3.13 | Programming Language |
| FastAPI | REST API Framework |
| SQLAlchemy | ORM |
| PostgreSQL | Database |
| RabbitMQ | Message Broker |
| AsyncPG | PostgreSQL Driver |
| Docker | Containerization |
| Docker Compose | Multi-container Orchestration |
| Pydantic | Data Validation |

---

#  Project Structure

```
order-processing-system/

├── docker-compose.yml
│
├── order_service/
│   ├── app/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── .env
│
├── inventory_service/
│   ├── app/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── .env
│
└── notification_service/
    ├── app/
    ├── Dockerfile
    ├── requirements.txt
    └── .env
```

---

#  Running the Project

## Clone Repository

```bash
git clone https://github.com/your-username/order-processing-system.git

cd order-processing-system
```

---

## Start All Services

```bash
docker compose up --build
```

---

## Stop All Services

```bash
docker compose down
```

---

#  Services

| Service | URL / Port |
|----------|------------|
| Order Service | http://localhost:8000 |
| Notification Service | http://localhost:8001 |
| Inventory Service | http://localhost:8002 |
| RabbitMQ UI | http://localhost:15672 |
| RabbitMQ AMQP | 5672 |
| Order Database | 5433 |
| Inventory Database | 5434 |

---

#  API Endpoints

## Create Order

```
POST /orders
```

Example Request

```json
{
    "customer_name": "Ajit",
    "product_name": "Laptop",
    "quantity": 2
}
```

---

## Get Order

```
GET /orders/{id}
```

---

#  Event Flow

```
Client
   │
   ▼
Order Service
   │
Save Order
   │
Publish order.created
   │
   ▼
RabbitMQ
   │
   ├──────────────► Inventory Service
   │                   │
   │                   ▼
   │           Update Inventory
   │
   └──────────────► Notification Service
                       │
                       ▼
               Send Notification
```

---

#  Docker

Build Images

```bash
docker compose build
```

Start Containers

```bash
docker compose up
```

Stop Containers

```bash
docker compose down
```

View Logs

```bash
docker compose logs -f
```

---

# Future Improvements

- API Gateway
- JWT Authentication
- Redis Caching
- Kubernetes Deployment
- Prometheus Monitoring
- Grafana Dashboard
- CI/CD Pipeline
- Distributed Tracing
- Service Discovery

---

# Author

**Ajit Tiwari**

Backend Developer

**Tech Stack:** Python • FastAPI • RabbitMQ • PostgreSQL • SQLAlchemy • Docker • Docker Compose

GitHub: https://github.com/AjitTiwari85

LinkedIn: https://www.linkedin.com/in/ajittiwari85/

---

## ⭐ If you found this project useful, don't forget to star the repository.

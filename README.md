cat <<EOF > README.md
# Distributed Payment Validator

A microservice-based system designed to demonstrate distributed transaction processing using **FastAPI** and **Docker**. This project is a part of a portfolio for SDET/Backend roles, focusing on reliability, containerization, and inter-service communication.

## Architecture
The system consists of two main services:
1.  **Payment Service (Port 8000):** Handles incoming payment requests and orchestrates the flow.
2.  **Accounting Service (Port 8001):** Records transactions and generates unique transaction IDs (UUIDs).

## 🛠 Tech Stack
* **Language:** Python 3.12
* **Framework:** FastAPI
* **Containerization:** Docker & Docker Compose
* **Communication:** Synchronous REST API (Requests)

## How to Run
Ensure you have Docker and Docker Compose installed, then run:

\`\`\`bash
docker-compose up --build
\`\`\`

Once the services are up, you can test the flow using cURL:

\`\`\`bash
curl -X POST http://localhost:8000/process
\`\`\`

## Challenges Overcome
* **macOS Path Mapping:** Resolved Docker volume mounting issues on macOS by optimizing directory structures and permissions.
* **Service Discovery:** Implemented internal Docker networking to allow seamless communication between containers using service names.

##  Future Roadmap
* [ ] Add Automated Integration Tests (Pytest).
* [ ] Implement Asynchronous processing with RabbitMQ/Kafka.
* [ ] Add Database persistence (PostgreSQL).
EOF
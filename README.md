Cloud-Native Telecom Data Platform Monitoring Architecture
 Project Overview
 <details>
  <summary><b>Click to view detailed Architecture Diagram</b></summary>
  <br>
  <img src="drawio.pncloud native telecom data platform monitoring architecture.drawio.png" width="100%">
</details>

This project demonstrates a robust, scalable, and automated Data Monitoring Pipeline tailored for the Telecommunications industry. It simulates real-time network traffic and user activities, processes this data through a cloud-native environment, and provides deep visual insights into network health.

The core objective is to shift from reactive to proactive monitoring, allowing engineers to detect anomalies in network loads before they impact the end-user experience.

 Architecture
The architecture follows a modern DevOps & Data Engineering flow:

Data Generation: A custom Python script simulating high-frequency telecom metrics (e.g., active users, latency, traffic volume).

Containerization: The application is packaged using Docker to ensure consistency across environments.

Orchestration: Managed by a Kubernetes Cluster, ensuring high availability and automated scaling of the simulator.

Data Collection: Prometheus scrapes real-time metrics from the Python exporter every 5 seconds.

Visualization: Grafana transforms raw time-series data into intuitive, actionable dashboards (Real-time Green Graph).

Cloud Storage: Integrated with AWS S3 for log archiving and AWS DynamoDB for fast metadata storage.

 Tech Stack
Cloud: AWS (S3, DynamoDB)

IaC: Terraform (Infrastructure Provisioning)

Orchestration: Kubernetes (K8s)

Containerization: Docker

Monitoring: Prometheus

Visualization: Grafana

Language: Python

 Key Features
Real-time Monitoring: Instant visibility into network performance via Grafana.

Automated Infrastructure: Full environment setup using Terraform.

Self-Healing: Kubernetes ensures the data simulator is always running.

Scalability: Designed to handle increasing data loads by scaling pods within the cluster.

📈 Dashboard Preview
The platform features a Real-time Green Time-Series Graph that tracks cumulative network requests, providing a clear visual of traffic growth and system stability.

#  Task Tracker DevOps Project

##  Project Overview

This project demonstrates end-to-end deployment of a containerized web application using Docker and Terraform on AWS.

##  Key Concepts Used

* Docker (Containerization)
* Terraform (Infrastructure as Code)
* AWS EC2 (Cloud Deployment)
* Security Groups (Networking)

---

##  Architecture

User → AWS EC2 → Docker Container → Flask Application

---

##  Tech Stack

* Python (Flask)
* Docker
* Terraform
* AWS EC2

---

##  Features

* Task management dashboard
* Add, delete, and track tasks
* Deployed on cloud infrastructure

---

## Docker Setup

```bash
docker build -t task-tracker .
docker run -p 5000:5000 task-tracker
```

---

##  Terraform Deployment

```bash
terraform init
terraform apply
```

---

##  Security

* Configured custom AWS Security Groups
* Enabled HTTP (80) and SSH (22)

---

##  Deployment Flow

1. Build Docker image
2. Push to Docker Hub
3. Provision EC2 using Terraform
4. Deploy container on EC2

---

##  Cleanup

```bash
terraform destroy
```

---

##  Outcome

Successfully deployed a containerized application on AWS using Infrastructure as Code principles.

---

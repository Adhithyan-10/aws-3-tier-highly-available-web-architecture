# 📘 Project Documentation

This folder contains the complete documentation for the project:

**Production-Style 3-Tier Web Architecture on AWS**

The documentation is provided as a structured presentation that explains the full architecture, implementation, and key learnings from the project.

---

## 📄 Documentation File

👉 [View Full Documentation](./aws-3tier-architecture-v2-main.pdf)

---

## 🧠 What This Documentation Covers

### 🔹 1. Architecture Understanding

* Complete 3-tier AWS architecture
* Public vs Private subnet isolation
* Role of Application Load Balancer (ALB)

---

### 🔹 2. Core Concept (Critical Learning)

* Why browser cannot access private backend directly
* How ALB enables secure communication
* Correct request flow:

  * ❌ Web → App
  * ✅ Browser → ALB → App

---

### 🔹 3. Frontend (Web Tier)

* Static website hosted on Apache EC2
* JavaScript `fetch()` used for API calls
* Interaction between UI and backend

---

### 🔹 4. Backend (App Tier)

* Flask-based API (`/data`)
* Runs inside private subnet
* Connects securely to RDS MySQL

---

### 🔹 5. Database (RDS)

* Amazon RDS MySQL deployment
* Multi-AZ configuration for high availability
* Accessible only from App Tier

---

### 🔹 6. Networking & Security

* Custom VPC design
* Public and Private subnet separation
* Bastion host for secure SSH access
* Security group chaining (least privilege model)

---

### 🔹 7. Load Balancer & Routing

* ALB as a single entry point
* Path-based routing:

  * `/` → Web Tier
  * `/data` → App Tier

---

### 🔹 8. High Availability & Scaling

* Auto Scaling Group for App Tier
* Multi-AZ deployment
* Health checks using ALB

---

### 🔹 9. Problems Faced & Debugging

* Backend not reachable initially
* Misunderstanding of request flow
* Target group port mismatch
* Flask accessibility issues

---

### 🔹 10. Interview Preparation

* Common interview questions
* Real-world explanations
* Important traps and concepts

---

## 🎯 Purpose of This Documentation

This documentation demonstrates:

* Strong understanding of cloud architecture
* Ability to design secure and scalable systems
* Hands-on experience with AWS services
* Real debugging and problem-solving skills

---

## 🏁 Summary

This project is not just about deploying services —
it reflects a clear understanding of how real-world cloud systems are built, secured, and scaled.

---

🚀 This documentation serves as both a learning reference and an interview preparation guide.

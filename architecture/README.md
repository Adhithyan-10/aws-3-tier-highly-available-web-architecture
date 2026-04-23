# 🏗️ Architecture Overview

This folder contains the architecture diagram for the project:

**Production-Style 3-Tier Highly Available Web Architecture on AWS**

---

## 📌 Architecture Diagram

![Architecture Diagram](ARCHH.png)

---

## 🚀 System Overview

This project implements a **3-tier web architecture** on AWS with a strong focus on:

* High Availability
* Scalability
* Security
* Real-world production design

The system is divided into three layers:

---

## 🌐 1. Web Tier (Public Subnet)

* Hosted on an EC2 instance (Apache)
* Serves static frontend (HTML, CSS, JavaScript)
* Accessible via the Application Load Balancer (ALB)
* Acts as the entry point for user interface

---

## ⚙️ 2. Application Tier (Private Subnet)

* EC2 instances running Flask (Python)
* Deployed inside a private subnet (no direct internet access)
* Managed using an Auto Scaling Group (ASG)
* Handles API requests (`/data` endpoint)

---

## 🗄️ 3. Database Tier (Private - Multi-AZ)

* Amazon RDS MySQL (Multi-AZ)
* Primary database in one Availability Zone
* Standby database in another Availability Zone
* Automatic failover ensures high availability

---

## 🔀 Request Flow (Core Concept)

This architecture follows a **controlled routing model using ALB**:

1. User accesses the application via browser

2. Request goes to **Application Load Balancer (ALB)**

3. ALB routes traffic based on path:

   * `/` → Web Tier (Frontend)
   * `/data` → Application Tier (Backend API)

4. Backend connects to RDS for data

5. Response is returned back to the user

---

## 💡 Key Architectural Insight

> The frontend (browser) directly calls backend APIs through the ALB.
> The web server does NOT communicate with the backend server directly.

This ensures:

* Clear separation of concerns
* Better scalability
* Secure backend isolation

---

## 🔐 Security Design

* Only ALB is exposed to the internet

* Application and Database tiers are in private subnets

* Security Groups enforce least privilege access:

  * ALB → Web Tier
  * ALB → App Tier
  * App Tier → Database

* Database has **no public access**

---

## 📈 High Availability & Scalability

* Application tier uses **Auto Scaling Group**
* Database uses **Multi-AZ deployment**
* ALB distributes traffic across components

---

## 🧠 Why This Architecture Matters

This project demonstrates:

* Real-world AWS system design
* Understanding of request flow (Frontend → ALB → Backend)
* Secure and scalable infrastructure practices
* Production-style deployment thinking

---

## 📂 File Included

* `ARCHH.png` → Complete architecture diagram

---

💥 This architecture reflects a **practical, production-ready design**, not just a theoretical setup.

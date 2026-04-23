# 📸 Project Execution Proof (Step-by-Step Screenshots)

This folder contains real execution screenshots captured during the implementation of the **3-Tier Highly Available Web Architecture on AWS**.

Each screenshot represents a critical stage in building and validating the architecture — from secure access to full end-to-end connectivity.

---

## 🔐 1. Bastion Host Access (Entry Point)

👉 ![View Screenshot](./1️⃣-bastion-ssh-success.png)

* SSH connection established from local machine to Bastion Host
* Demonstrates secure entry into the private infrastructure
* Public access is restricted to Bastion only

💡 **Key Concept:**
Private resources are never accessed directly from the internet

---

## 🔄 2. Bastion → Web Server (Private Access)

👉 ![View Screenshot](./2️⃣-bastion-to-web-ssh.png)

* SSH from Bastion Host to Web Server (Private EC2)
* Shows internal connectivity within VPC

💡 **Key Concept:**
Web server is not publicly accessible — only reachable via Bastion

---

## 🔄 3. Bastion → App Server (Private Access)

👉 ![View Screenshot](./3️⃣-bastion-to-app-ssh.png)

* SSH from Bastion Host to App Server (Private EC2)
* Validates secure access to backend tier

💡 **Key Concept:**
App tier is completely isolated from the internet

---

## 🌐 4. Web → App Communication (Internal API Call)

👉 ![View Screenshot](./4️⃣-web-to-app-success.png)

* Web server successfully communicates with App server using private IP
* Backend API is reachable inside private network

💡 **Key Concept:**
Internal communication happens via private networking (VPC)

---

## 🗄️ 5. App → Database Connection

👉 ![View Screenshot](./5️⃣-app-to-db-success.png)

* Flask backend successfully connects to RDS MySQL
* Database connectivity validated

💡 **Key Concept:**
Database is only accessible from App tier (not from internet)

---

## ⚖️ 6. ALB Target Group Health Check

👉 ![View Screenshot](./6️⃣-alb-healthy-targets.png)

* Application Load Balancer target group showing **healthy instances**
* Confirms backend is correctly registered and reachable

💡 **Key Concept:**
Target group port must match application port (e.g., 8000)

---

## 🌍 7. ALB DNS → Web Tier Working

👉 ![View Screenshot](./7️⃣-alb-dns-working.png)

* Accessing ALB DNS loads Web Tier successfully
* Static frontend is served via Apache

💡 **Key Concept:**
ALB acts as the **single entry point** for users

---

## 🚀 8. End-to-End Flow (Frontend → Backend → DB)

👉 ![View Screenshot](./8️⃣-final-end-to-end-success.png)

* Button click triggers API call (`/data`)
* Backend processes request and connects to database
* Response displayed in browser

💡 **Key Concept (VERY IMPORTANT):**
Browser → ALB → App (**NOT Web → App**)

---

## 📈 9. Auto Scaling Group (App Tier)

👉 ![View Screenshot](./9️⃣-asg-instances-running.png)

* Multiple EC2 instances running in Auto Scaling Group
* Demonstrates scalability of App tier

💡 **Key Concept:**
App layer scales dynamically based on load

---

## 🌐 10. Multi-AZ Deployment Proof

👉 ![View Screenshot](./🔟-multi-az-proof(circle-the-az-table).png)

* Instances distributed across multiple Availability Zones
* Confirms high availability setup

💡 **Key Concept:**
Fault tolerance achieved using Multi-AZ architecture

---

# 🧠 Final Takeaways

* Only ALB is exposed to the internet
* Backend and Database are fully private
* Path-based routing separates Web and App traffic
* Secure access is enforced via Bastion Host
* System is scalable and highly available

---

# 🚀 Why This Matters

These screenshots prove that the architecture is not just theoretical —
it is **fully implemented, tested, and validated in AWS**.

👉 This demonstrates:

* Real cloud hands-on experience
* Strong understanding of networking & security
* Ability to design production-ready systems

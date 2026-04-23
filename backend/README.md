# ⚙️ Backend (Application Tier)

This folder contains the backend application of the 3-tier architecture.

The backend is responsible for:

* Handling API requests
* Connecting to the database
* Returning responses to the frontend

---

## 📄 File Included

* `app.py` → Flask-based backend application

---

## 🧠 Backend Design

The backend is built using:

* **Python Flask** → Lightweight web framework
* **MySQL Connector** → Database connectivity

It is deployed on EC2 instances inside a **private subnet**, ensuring:

* No direct internet access
* Secure communication via ALB

---

## 🔌 API Endpoint

The backend exposes a single API:

```text
/data
```

---

## 🔁 Functionality

When a request is sent to `/data`:

1. Flask receives the request
2. A connection to the RDS MySQL database is attempted
3. If successful, response is returned:

```text
DB connection successful!
```

---

## 🌐 Request Flow (Important)

```text
Browser → ALB → App Tier → RDS → Response → Browser
```

---

## 🚨 CRITICAL CONCEPT (VERY IMPORTANT)

> The backend is NOT directly accessible from the browser.

Why?

* It is deployed in a **private subnet**
* Security groups block public access
* Only the **Application Load Balancer (ALB)** can route requests to it

---

## ❌ Issue Faced During Implementation

Initially:

* API calls were failing
* No response from `/data`

---

## 🔍 Root Cause

* ALB was routing all traffic to the **Web Tier**
* No rule existed for `/data`
* Backend was never receiving requests

---

## ✅ Solution

Configured **ALB Path-Based Routing**:

```text
/ → Web Tier  
/data* → App Tier
```

This ensured:

* API requests reach backend
* Proper separation of frontend and backend

---

## ⚙️ Application Configuration

### 🔹 Flask Binding

```python
app.run(host='0.0.0.0', port=8000)
```

---

### 💡 Why `0.0.0.0`?

* Allows the app to listen on all network interfaces
* Required for ALB to connect to the instance

👉 Important:

> This does NOT make the server public — security groups control access.

---

## 🔐 Security Design

* Backend is in **private subnet**

* Only accepts traffic from:

  * ALB Security Group
  * Bastion (for SSH)

* No public access allowed

---

## 🗄️ Database Connection

The backend connects to:

* Amazon RDS MySQL
* Using credentials configured in the application

👉 This proves:

* End-to-end connectivity
* Real database interaction

---

## ⚠️ Note (Production Consideration)

This setup uses Flask’s development server.

In production:

* Use **Gunicorn** or similar WSGI server
* Add reverse proxy (e.g., Nginx)

---

## 🏁 Summary

The backend layer demonstrates:

* API design using Flask
* Secure database connectivity
* Private subnet deployment
* Proper integration with ALB

---

💥 This layer is the core logic of the system, connecting frontend interactions to the database securely and efficiently.


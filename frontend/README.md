# 🌐 Frontend (Web Tier)

This folder contains the frontend component of the 3-tier architecture.

The frontend is responsible for:

* Serving the user interface
* Triggering backend API calls
* Demonstrating real client → backend interaction

---

## 📄 File Included

* `index.html` → Static web page served using Apache

---

## 🧠 Frontend Design

The frontend is a simple HTML page hosted on an EC2 instance in the **public subnet**.

It contains:

* A heading indicating the web tier is working
* A button to trigger backend communication
* JavaScript logic to call the backend API

---

## 🔁 How It Works

1. User opens the application in browser
2. Request goes to **Application Load Balancer (ALB)**
3. ALB routes `/` to the **Web Tier**
4. The `index.html` page is loaded

---

## 🔥 Core Functionality

The frontend includes a button:

```html id="f1"
<button onclick="loadData()">Test Backend</button>
```

When clicked:

* JavaScript runs inside the browser
* It sends a request to:

```id="f2"
/data
```

---

## 🚨 IMPORTANT CONCEPT (KEY LEARNING)

> The frontend server does NOT directly communicate with the backend server.

Instead:

* The **browser** makes the API call
* The request is sent to the **ALB**
* ALB routes it to the backend

---

## 🔄 Actual Request Flow

```id="f3"
Browser → ALB → App Tier → RDS → Response → Browser
```

---

## ❌ Common Misunderstanding (Faced During Project)

Initially, it was assumed that:

```id="f4"
Web Server → Backend Server
```

But this is incorrect.

---

## ✅ Correct Understanding

```id="f5"
Browser (JavaScript) → ALB → Backend
```

This is why:

* Backend remains in **private subnet**
* It is not directly accessible
* ALB acts as a controlled entry point

---

## 🌐 API Call Implementation

Inside `index.html`, JavaScript uses:

```javascript id="f6"
fetch("http://<ALB-DNS>/data")
```

This ensures:

* Request goes through ALB
* Correct routing happens
* Backend is accessed securely

---

## ⚠️ Issue Faced & Fix

### ❌ Problem

* API call initially failed
* No response from backend

### 🔍 Root Cause

* ALB routing was not configured for `/data`
* Requests were going to Web Tier instead

### ✅ Solution

* Configured **path-based routing in ALB**:

```id="f7"
/ → Web Tier  
/data* → App Tier
```

---

## 💡 Key Takeaway

> In modern architectures, the frontend (browser) communicates with backend services through a load balancer, not through direct server-to-server communication.

---

## 🏁 Summary

The frontend layer demonstrates:

* Client-side API calls using JavaScript
* Proper use of ALB for backend routing
* Clear separation between UI and backend logic
* Real-world request flow understanding

---

💥 This is a critical part of the architecture that proves understanding of how real web systems operate.

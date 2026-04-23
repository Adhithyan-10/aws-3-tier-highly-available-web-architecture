# 🗄️ Database (RDS Layer)

This folder explains the database layer of the 3-tier architecture.

The database is designed with a focus on:

* High availability
* Fault tolerance
* Secure access

---

## 🧠 Database Design

The database is implemented using:

* **Amazon RDS (MySQL)**
* **Multi-AZ Deployment**

It is deployed inside a **private subnet**, ensuring that it is not directly accessible from the internet.

---

## 📌 Key Features

### 🔹 1. Managed Database Service (RDS)

* No manual database installation required
* Automated backups
* Patch management handled by AWS
* Simplified operations

---

### 🔹 2. Multi-AZ Deployment (High Availability)

The database is deployed across **two Availability Zones**:

* **Primary DB Instance (AZ1)** → Handles all traffic
* **Standby DB Instance (AZ2)** → Passive replica

---

### 🔁 How Failover Works

1. Primary database becomes unavailable
2. AWS automatically promotes the standby instance
3. Same endpoint is used
4. Application reconnects without changes

---

## 🌐 DB Subnet Group

The RDS instance is associated with a **DB Subnet Group**:

* Subnet in AZ1 → `10.0.5.0/24`
* Subnet in AZ2 → `10.0.6.0/24`

This ensures:

* Multi-AZ capability
* Isolation from public access

---

## 🔐 Security Design

The database is highly secured:

* ❌ No public access
* Only accessible from **Application Tier**

### Security Group Rules:

* Allow inbound:

  * Port **3306 (MySQL)** from App Tier Security Group

* Deny all other traffic

---

## 🚨 CRITICAL CONCEPT

> The database is never exposed to the internet.

Why?

* Prevent unauthorized access
* Protect sensitive data
* Enforce layered security

---

## 🔁 Request Flow

```text id="dbflow1"
Browser → ALB → App Tier → RDS → Response → Browser
```

---

## 🔌 Backend Integration

The backend connects to the database using:

* MySQL connection from Flask (`app.py`)
* Credentials configured in application

When `/data` API is triggered:

* Backend attempts DB connection
* If successful, response is returned

---

## ⚠️ Issue Awareness

While building the system:

* Database was working correctly
* But backend was not receiving requests initially

👉 Root cause was NOT database-related
👉 It was ALB routing misconfiguration

This highlights:

> In distributed systems, failures may occur due to routing, not just database issues.

---

## 💡 Key Takeaways

* Multi-AZ ensures **high availability without manual intervention**
* Database must always be placed in a **private subnet**
* Security groups enforce **strict access control**
* Backend acts as the only bridge to the database

---

## 🏁 Summary

The database layer demonstrates:

* Highly available architecture using Multi-AZ
* Secure deployment in private subnets
* Proper integration with application tier
* Real-world cloud database design practices

---

💥 This layer ensures the system remains reliable even during infrastructure failures.

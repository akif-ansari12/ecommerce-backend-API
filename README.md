# 🧠 Core E-Commerce Backend System (Django REST Framework)

A **modular backend system** built using Django REST Framework that simulates a real-world e-commerce architecture with authentication, role-based access, product management, cart, order processing, and payment integration.

---

## ⚙️ Project Architecture

This project follows a **modular backend design**, where each feature is separated into independent Django apps:

- 🔐 **accounts** → Authentication & Role Management
- 📦 **products** → Product Catalog (Seller module)
- 🛒 **cart** → Shopping Cart System
- 🧾 **orders** → Order Processing System
- 💳 **payments** → Payment Gateway Integration

Each module is independently responsible for its business logic and communicates through Django ORM relationships.

---

## 🚀 Key Features

### 🔐 Authentication System
- JWT-based authentication
- Secure login & registration
- Role-based access control (Buyer / Seller)

---

### 👥 Role Management
- **Seller**
  - Create, update, delete products
- **Buyer**
  - Browse products
  - Add to cart
  - Place orders

---

### 📦 Product System
- Full CRUD operations
- Seller-specific ownership
- Public product listing API

---

### 🛒 Cart System
- Add / update / remove items
- User-specific cart isolation
- Quantity management

---

### 🧾 Order System
- Cart → Order conversion
- Automatic total calculation
- Order history per user

---

### 💳 Payment System
- Razorpay integration
- Payment order creation
- Payment verification flow

---

## 🔁 System Flow


---

## 📡 API Endpoints

### Authentication
- POST `/api/auth/register/`
- POST `/api/auth/login/`

### Products
- GET `/api/products/`
- POST `/api/products/`

### Cart
- POST `/api/cart/add/`
- GET `/api/cart/view/`

### Orders
- POST `/api/orders/place/`
- GET `/api/orders/history/`

### Payments
- POST `/api/payments/create/`
- POST `/api/payments/verify/`

---

## 🛠️ Tech Stack

- Python 3.x
- Django
- Django REST Framework
- JWT Authentication
- Razorpay API
- SQLite / PostgreSQL

---

## 🧠 Architecture Highlights

- Modular Django app structure
- RESTful API design
- Secure authentication layer
- Role-based authorization system
- Real-world e-commerce workflow
- Scalable backend architecture

---

## 🔐 Security Features

- JWT authentication
- Role-based permissions (Seller / Buyer)
- User-specific data isolation
- Secure payment verification

---

## 👨‍💻 Developer

**Akif Ansari**  
Backend Developer | Django | REST API | Python

---

## 🎯 Project Objective

This project demonstrates a **production-style backend system design**, focusing on:

- API development best practices
- Authentication & authorization
- Database modeling & relationships
- Payment gateway integration
- Scalable backend architecture

---

## ⭐ Outcome

✔ Built a complete e-commerce backend system  
✔ Implemented real-world business workflow  
✔ Designed modular and scalable architecture  
✔ Production-ready API structure

# PhiMart e-Commerce backend project

A fully-featured **E-commerce REST API** built with **Django Rest Framework (DRF)**. This project provides core e-commerce functionalities including product management, categories, cart system, JWT authentication, and interactive API documentation using **Swagger (drf-yasg)**.

---

## 🚀 Features

* 🔐 **JWT Authentication** (Login, Register, Token Refresh)
* 👤 User-based access control
* 🛍️ Product management (Create, Read, Update, Delete)
* 🗂️ Product Categories
* 🛒 Shopping Cart system
* 📦 Order-ready structure
* 📄 API Documentation with **Swagger UI**
* 🔍 Optimized queries with `select_related` & `prefetch_related`

---

## 🛠️ Tech Stack

* **Backend**: Django, Django REST Framework
* **Authentication**: Simple JWT
* **Database**: PostgreSQL
* **API Docs**: drf-yasg (Swagger & ReDoc)
* **Language**: Python

---


## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/sheikh-riyadh/django-rest-framework
cd django-rest-framework
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Environment Variables

Create a `.env` file if needed:

```env
user=
password=
host=
port=
dbname=


cloud_name=
api_key=
api_secret=
```

### 5️⃣ Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6️⃣ Create Superuser

```bash
python manage.py createsuperuser
```

### 7️⃣ Run Server

```bash
python manage.py runserver
```

---




## 📘 API Documentation

Swagger UI is available at:

* **Swagger**: `http://127.0.0.1:8000/swagger/`
* **ReDoc**: `http://127.0.0.1:8000/redoc/`

Powered by **drf-yasg**.

---



## 🚀 Future Improvements

* Order checkout system
* Product reviews & ratings

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 👨‍💻 Author

**Sheikh Riyadh**
Backend Developer | Django & DRF

---

⭐ If you like this project, give it a star!

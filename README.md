
# Lunch Voting Service

A Django + DRF application for internal company use that allows employees to vote for daily restaurant menus.  
Supports backward compatibility for older mobile app versions via custom middleware.

---

## 🚀 Tech Stack

- Django / Django REST Framework
- PostgreSQL
- JWT Authentication
- Docker + Docker Compose
- Pytest
- flake8 / black
- drf-spectacular (Swagger UI)

---

## 📦 Installation & Running (Docker)

### 1. Clone repository
```bash
git clone https://github.com/PavelSemenikhin/Inforce-tesk-task.git
cd inforce-test-task
```

### 2. Create `.env` file in project root:
```
SECRET_KEY=your_secret
DEBUG=True
POSTGRES_DB=lunch_db
POSTGRES_USER=lunch_user
POSTGRES_PASSWORD=lunch_pass
POSTGRES_HOST=db
POSTGRES_PORT=5432
```

### 3. Build and start containers
```bash
docker compose up --build
```



### 4. Open API docs:
```
http://localhost:8000/api/docs/
```

---

## 🧪 Running Tests

### Run full test suite:
```bash
docker compose exec app pytest -v
```



---

## ✅ Linting & Code Style

### flake8:
```bash
docker compose exec app flake8 .
```

### black (dry-run check):
```bash
docker compose exec app black --check .
```

### black (auto-format):
```bash
docker compose exec app black .
```

---

## 📡 API Structure

### Accounts  
- POST `/api/accounts/register/`  
- POST `/api/accounts/token/`  
- POST `/api/accounts/token/refresh/`  

### Employees  
- GET `/api/accounts/employees/`  
- POST `/api/accounts/employees/`  

### Restaurants  
- GET `/api/restaurants/`  
- POST `/api/restaurants/`  

### Menus  
- GET `/api/menus/`  
- POST `/api/menus/`  

### Votes  
- POST `/api/votes/`  
- GET `/api/votes/results/`  
- GET `/api/votes/todays_winner/`

---

## 🔧 App Version Middleware

Older versions of the mobile app are supported via build-version header parsing:

```
Build-Version: 1.0
```

The middleware attaches value as:
```
request.app_version
```

---

## 🎯 Summary

This project provides:
- Clean architecture  
- Proper separation of logic into services  
- Dockerized production-ready setup  
- Full REST API  
- Pytest test suite  
- Swagger documentation  
- Linting and formatting tools  

Perfect foundation for a production microservice. 

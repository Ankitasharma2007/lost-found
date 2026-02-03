
# 🧾 Lost & Found Management API

A Django REST Framework–based backend for managing lost and found items with JWT authentication and admin moderation.

---

## 🚀 Features
- Custom user model (roll number, phone number)
- JWT authentication
- Report lost & found items
- Admin moderation endpoints
- UUID-based records

---

## 🔐 Authentication

### Register
**POST** `/users/register/`

```json
{
  "username": "john",
  "email": "john@example.com",
  "password": "password123",
  "phonenumber": "9876543210",
  "rollnumber": 101
}
```

**Response**
```json
{
  "message": "User registered"
}
```

---

### Login
**POST** `/users/login/`

```json
{
  "username": "john",
  "password": "password123"
}
```

**Response**
```json
{
  "access": "<jwt_access_token>",
  "refresh": "<jwt_refresh_token>"
}
```

---

### Refresh Token
**POST** `/users/token/refresh/`

```json
{
  "refresh": "<jwt_refresh_token>"
}
```

---

## 📦 Lost & Found APIs

### Report Lost Item
**POST** `/users/lost/`  
🔒 Auth required

```json
{
  "nameofarticle": "Wallet",
  "description": "Black leather wallet",
  "location": "Library"
}
```

---

### Report Found Item
**POST** `/users/found/`  
🔒 Auth required

```json
{
  "nameofarticle": "Phone",
  "description": "Samsung phone",
  "location": "Cafeteria"
}
```

---

## 🛡️ Admin APIs

### Unresolved Lost Items
**GET** `/users/lostlist/`  
👑 Admin only

**Response**
```json
[
  {
    "id": "uuid",
    "rollnumber": 101,
    "nameofarticle": "Wallet",
    "description": "Black leather wallet",
    "location": "Library",
    "resolved": false,
    "found_item": null
  }
]
```

---

### Unmatched Found Items
**GET** `/users/Foundlist/`  
👑 Admin only

```json
[
  {
    "id": "uuid",
    "rollnumber": 102,
    "nameofarticle": "Phone",
    "description": "Samsung phone",
    "location": "Cafeteria",
    "lost_item": null
  }
]
```

---

## 🔑 Authorization Header

```
Authorization: Bearer <access_token>
```

---

## ⚙️ Setup

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

---

## 📌 Future Improvements
- Auto match Lost & Found items
- Resolve workflow
- Notifications
- Pagination & filters

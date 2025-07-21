# Backend Task:
# 🛒 E-commerce API
A simple, asynchronous E-commerce backend built with **FastAPI**, **Motor** (MongoDB), and **Python** — created as an internship backend assignment.

---

## ✅ API Endpoints
### 🔹 POST: `/products`
**Create Product API**

**Request Body:**
```json
{
  "name": "string",
  "price": 100.0,
  "sizes": [
    {
      "size": "string",
      "quantity": 0
    }
  ]
}
```

**Response Body:**
```json
{
  "id": "1234567890"
}
```

* Status Code: **201 CREATED**

---

### 🔹 GET: `/products`
**List Products API**
**Query Parameters:** *(all optional)*
* `name` → Regex/partial search
* `size` → e.g., `size=large` → Filters products having `size=large`
* `limit` → Number of documents to return
* `offset` → Number of documents to skip while paginating (sorted by `_id`)

**Response Body:**
```json
{
  "data": [
    {
      "id": "12345",
      "name": "sample",
      "price": 100.0
      // No sizes in output
    },
    {
      "id": "12348",
      "name": "sample2",
      "price": 10.0
    }
    // ...
  ],
  "page": {
    "next": "10",     // next page starting index
    "limit": 0,       // number of records in current page
    "previous": -10   // previous page starting index
  }
}
```

* Status Code: **200 OK**

---

### 🔹 POST: `/orders`
**Create Order API**

**Request Body:**
```json
{
  "userId": "user1", // can be hardcoded
  "items": [
    {
      "productId": "123441", // id of prod in str format
      "qty": 3
    },
    {
      "productId": "2332321",
      "qty": 3
    }
  ]
}
```

**Response Body:**
```json
{
  "id": "1234567890"
}
```

* Status Code: **201 CREATED**

---

### 🔹 GET: `/orders/{user_id}`
**Get List of Orders by User**

**URL Parameter:**
* `{user_id}`

**Query Parameters:** *(all optional)*
* `limit` → Number of documents to return
* `offset` → Number of documents to skip while paginating (sorted by `_id`)

**Response Body:**
```json
{
  "data": [
    {
      "id": "12345",
      "items": [
        {
          "productDetails": { // we need to join/lookup the product details at query time.
            "name": "Sample Product",
            "id": "123456"
          },
          "qty": 3
        },
        {
          "productDetails": {
            "name": "Sample Product",
            "id": "123456"
          },
          "qty": 3
        }
      ],
      "total": 250.0
    }
    // ... more records
  ],
  "page": {
    "next": "10",     // next page starting index
    "limit": 0,       // number of records in current page
    "previous": -10   // previous page starting index
  }
}
```

* Status Code: **200 OK**

---

## 🚀 Deployment
Deployed on **Render**
👉 [View it here](https://fastapi-ecom-api.onrender.com/docs)

---

## ⚙️ Tech Stack
* **FastAPI**
* **Python**
* **MongoDB** (PyMongo or Motor)

---

## 🛠️ Installation & Setup
1. **Clone the repository**
   ```bash
   git clone https://github.com/aayushmaan-54/hrone-fastapi-ecommerce-api.git
   cd hrone-fastapi-ecommerce-api
   ```

2. **Create and activate virtual environment**
   ```bash
   # Create virtual environment
   python -m venv venv

   # Activate virtual environment
   ## Windows (Command Prompt)
   venv\Scripts\activate

   ## Windows (PowerShell)
   venv\Scripts\Activate.ps1

   ## Windows (Git Bash)
   source venv/Scripts/activate

   ## Linux/macOS
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment configuration**
   ```bash
   # Copy the sample environment file
   cp .env.sample .env

   # Edit .env file with your configuration
   # Update database URLs, API keys, and other settings as needed
   ```

5. **Database setup**
   ```bash
   # Initialize and seed the database (optional)
   python -m seed
   ```

6. **Run the application**
   ```bash
   # Option 1: Using run.py
   python run.py

   # Option 2: Using uvicorn directly
   uvicorn app.main:app --reload
   ```

7. **Access the application**
   - API: http://localhost:8000
   - Interactive API docs: http://localhost:8000/docs for Swagger UI
   - Alternative docs: http://localhost:8000/redoc for ReDoc

---

> Built with ❤️ for internship evaluation.

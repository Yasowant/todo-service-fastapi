---

# ⚡ FastAPI Todo API — PostgreSQL + AI 🤖

A production-ready **Todo REST API** built with **FastAPI** and **PostgreSQL**, enhanced with **AI-powered task generation, chat, and priority prediction**.

---

# 🚀 Live API

🌐 [https://todo-service-fastapi.onrender.com](https://todo-service-fastapi.onrender.com)

📄 Swagger Docs:
[https://todo-service-fastapi.onrender.com/docs](https://todo-service-fastapi.onrender.com/docs)

---

# ⚙️ Tech Stack

## 🧠 Backend

* ⚡ FastAPI
* 🗄 PostgreSQL
* 🧱 SQLAlchemy
* 📦 Pydantic
* 🚀 Uvicorn

## 🤖 AI Layer

* AI Chat Service
* AI Todo Generator
* AI Priority Prediction
* OpenRouter / LLM API integration

---

# 📂 Project Structure

```bash
fastapi-postgresql-todo-api
│
├── app
│   ├── main.py
│   │
│   ├── database
│   │   └── database.py
│   │
│   ├── models
│   │   └── todo_model.py
│   │
│   ├── schemas
│   │   └── todo_schema.py
│   │
│   ├── services
│   │   ├── todo_service.py
│   │   ├── ai_service.py        # 🤖 AI logic
│   │   └── chat_service.py      # 💬 Chat logic
│   │
│   ├── routes
│   │   ├── todo_routes.py
│   │   └── ai_routes.py         # 🚀 AI endpoints
│   │
│   └── utils
│       └── dependencies.py
│
├── requirements.txt
└── README.md
```

---

# ✨ Features

## ✅ Core Features

* Create, update, delete todos
* PostgreSQL database integration
* Clean service-based architecture
* Dependency injection (FastAPI)

## 🤖 AI Features (🔥 Highlight)

### 💬 AI Chat

* Chat with AI (ChatGPT-like experience)
* Context-aware responses

### 📝 AI Todo Generator

* Convert natural language → structured todo
* Extract title, description automatically

### 📊 AI Priority Prediction

* Predicts task priority:

  * Low
  * Medium
  * High

---

# 🔌 API Endpoints

## 📌 Todo APIs

| Method | Endpoint    | Description |
| ------ | ----------- | ----------- |
| POST   | /todos      | Create Todo |
| GET    | /todos      | Get Todos   |
| PUT    | /todos/{id} | Update Todo |
| DELETE | /todos/{id} | Delete Todo |

---

## 🤖 AI APIs

### 💬 Chat

```http
POST /ai/chat
```

```json
{
  "message": "How can I be productive?"
}
```

---

### ✨ Generate Todo

```http
POST /ai/generate-todo
```

```json
{
  "text": "Buy groceries tomorrow evening"
}
```

---

### 📊 Predict Priority

```http
POST /ai/predict-priority
```

```json
{
  "title": "Finish project urgently"
}
```

---

# 🧠 AI Route Example

```python
@router.post("/chat")
def chat(data: dict, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return {"reply": handle_chat(user.id, data["message"], db)}


@router.post("/generate-todo")
def ai_generate(data: dict):
    return generate_todo(data["text"])


@router.post("/predict-priority")
def ai_priority(data: dict):
    return {"priority": predict_priority(data["title"])}
```

---

# 🛠 Installation

## 1️⃣ Clone repo

```bash
git clone https://github.com/Yasowant/todo-service-fastapi.git
cd todo-service-fastapi
```

---

## 2️⃣ Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

---

## 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🗄 Database Setup

Create PostgreSQL DB:

```sql
CREATE DATABASE studydatabase;
```

Update:

```python
DATABASE_URL = "postgresql://postgres:password@localhost:5432/studydatabase"
```

---

# 🔐 Environment Variables

Create `.env`:

```env
DATABASE_URL=postgresql://postgres:password@localhost:5432/studydatabase
OPENROUTER_API_KEY=your_api_key_here
```

⚠️ **Important:**
Never commit your API key to GitHub.

---

# ▶️ Run Server

```bash
uvicorn app.main:app --reload
```

---

# 📄 API Docs

* Swagger UI → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* ReDoc → [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

# 🔮 Future Improvements

* 🔐 JWT Authentication (partially implemented)
* 🐳 Docker support
* 📄 Pagination
* 🧪 Unit testing
* 🔄 CI/CD pipeline
* ⚡ Caching AI responses
* 🧠 Fine-tuned AI model

---

# ⭐ Why This Project is Strong

✅ Clean architecture (routes + services)
✅ AI + CRUD integration
✅ Real-world backend design
✅ Scalable & production-ready
✅ Resume-level project

---

# 👨‍💻 Author

**Yasowant**
Full Stack Developer (MERN + FastAPI + AI)

---

## 🔥 Important Fix (Security)

You exposed your API key:

```env
OPENROUTER_API_KEY=sk-or-v1-xxxxx
```

👉 **Immediately do this:**

1. Revoke the key from OpenRouter
2. Generate a new one
3. Store only in `.env`
4. Add `.env` to `.gitignore`

---


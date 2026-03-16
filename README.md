# FastAPI PostgreSQL Todo API

A simple **Todo REST API** built with **FastAPI** and **PostgreSQL** using a clean project structure.
This project demonstrates how to build a production-style backend API with Python.

---

## Tech Stack

* FastAPI
* PostgreSQL
* SQLAlchemy
* Pydantic
* Uvicorn

---

## Project Structure

```
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
│   │   └── todo_service.py
│   │
│   └── routes
│       └── todo_routes.py
│
├── requirements.txt
└── README.md
```

---

## Installation

### Clone the repository

```
git clone https://github.com/Yasowant/todo-service-fastapi.git
```

### Navigate to project

```
cd todo-service-fastapi
```

### Create virtual environment

```
python3 -m venv venv
```

### Activate environment

Mac/Linux

```
source venv/bin/activate
```

Windows

```
venv\Scripts\activate
```

---

## Install Dependencies

```
pip install -r requirements.txt
```

---

## Setup PostgreSQL

Create a database:

```
CREATE DATABASE studydatabase;
```

Update your database connection inside:

```
app/database/database.py
```

Example:

```
DATABASE_URL = "postgresql://postgres:password@localhost:5432/studydatabase"
```

---

## Run the Server

```
uvicorn app.main:app --reload
```

Server will start at:

```
http://127.0.0.1:8000
```

---

## API Documentation

FastAPI automatically generates API documentation.

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## API Endpoints

| Method | Endpoint    | Description   |
| ------ | ----------- | ------------- |
| POST   | /todos      | Create Todo   |
| GET    | /todos      | Get All Todos |
| PUT    | /todos/{id} | Update Todo   |
| DELETE | /todos/{id} | Delete Todo   |

---

## Example Request

Create Todo

```
POST /todos
```

Request Body:

```
{
  "title": "Learn FastAPI",
  "description": "Build Todo API project"
}
```

---

## Future Improvements

* Authentication (JWT)
* Docker support
* Pagination
* Unit testing
* CI/CD pipeline

---

## Author

Yasowant

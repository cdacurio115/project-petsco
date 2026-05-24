# Petscop 🐾

Petscop is a web application for a pet adoption foundation. It allows users to explore posts of pets available for adoption, register, log in, create posts, and mark pets for adoption.

## Features

- User registration and login
- Create, edit, and delete pet posts
- Upload images to posts
- View individual posts
- Search pets by title or content
- Post pagination
- Check system to mark pets in the adoption process
- Adoptions in progress section (registered users only)
- Health check endpoint (`GET /health`)
- Responsive UI for mobile and desktop

## Technologies Used

- Python 3.11
- Flask
- SQLAlchemy
- MySQL Server 8.0
- PyMySQL
- Werkzeug
- python-dotenv

## Prerequisites

- Python 3.11
- MySQL Server 8.0 (and optionally MySQL Workbench to visualize the database)

## Local Setup

1. Clone the repository:
git clone https://github.com/cdacurio115/project-petsco.git
cd project-petsco

2. Create and activate the virtual environment:
python -m venv .venv
.venv\Scripts\activate

3. Install dependencies:
pip install -r requirements.txt

4. Create the database. From MySQL Workbench or the MySQL console run:
```sql
CREATE DATABASE blog_db;
```

5. Create a `.env` file in the root of the project with the following variables:
DATABASE_URL=mysql+pymysql://root:root@localhost:3306/blog_db
SECRET_KEY=dev

6. Default MySQL credentials:
- User: `root`
- Password: `root`
- Port: `3306`

7. Run the application:
py main.py

The app will be available at http://127.0.0.1:5000

## Demo Credentials

- User: `lexons` / Password: `12345`
- User: `luis` / Password: `12345`
- User: `adriana` / Password: `123`

## Running the Tests

pytest tests/

## Project Structure
```
petscop/
├── myblog/
│   ├── models/
│   │   ├── user.py
│   │   ├── post.py
│   │   └── adopcion.py
│   ├── views/
│   │   ├── user.py
│   │   └── blog.py
│   ├── templates/
│   │   ├── autentic/
│   │   └── blog/
│   └── static/
│       ├── css/
│       ├── img/
│       └── uploads/
├── tests/
│   └── test_app.py
├── config.py
├── main.py
├── requirements.txt
└── .env
```
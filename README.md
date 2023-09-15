# FastAPI ML
The project is an API implementation using the FastAPI framework. Allows you to work with machine learning models, download data from the server, perform training and test models on your own test data.

# Motivation
Often, in the course of some services, a large amount of well-structured data arises. They can be used to form machine learning models, which, if applied correctly, can significantly improve real performance indicators.

***


# Installation and launch

Install all dependencies in a virtual environment:
```commandLine
git clone https://github.com/RolfAdolf/final_project.git
cd final_project

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```

### .env-файл
The environment file should be located in the root folder of the project `final_project/` and have the form as below
```bash
HOST= 
PORT=

DB_HOST=
DB_PORT=
DB_NAME=
DB_USER=
DB_PASS=

POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=

JWT_SECRET=
JWT_ALGORITHM=
JWT_EXPIRES_SECONDS=

ADMIN_USERNAME=
ADMIN_PASSWORD=

MODEL_EXPIRE_SECONDS=
```

### Alembic 
```bash
cd src
alembic upgrade head
```

### Launch
```bash
gunicorn src.app:app --workers 1 --daemon --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:11000

gunicorn dsh.app:server --bind=0.0.0.0:8000
```

## Docker
To start, you can use docker-compose:
```bash
git clone https://github.com/RolfAdolf/final_project.git
cd final_project

docker compose build

docker compose up
```

***

For all questions and suggestions, please contact:


`Telegram`: @Nadir_Devrishev


`Email`: nadir.dewrishew@gmail.com

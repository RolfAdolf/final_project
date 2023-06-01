# FastAPI ML
Проект является реализацией API с использованием фреймворка FastAPI. Позволяет работать с моделями машинного обучения, скачивать данные с сервера, совершать обучение и проверять модели на собственных тестовых данных.

# Мотивация
Часто в процессе работы некоторых сервисов возникает большое количество хорошо структурированных данных. 
Они могут быть использованы для формирования моделей машинного обучения, которые при правильном применении
способны значительно улучшить реальные показатели производительности.

***


# Установка и запуск

Уставите все зависимости в виртуальной среде:
```commandLine
git clone https://github.com/RolfAdolf/final_project.git
cd final_project

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```

### .env-файл
Файл окружения должен находиться в корневой папке проекта `final_project/` и иметь вид
```bash
# Параметры развёртывания API
HOST= 
PORT=
# Параметры подключения к базе данных
DB_HOST=
DB_PORT=
DB_NAME=
DB_USER=
DB_PASS=
# Параметры создания базы данных (только для docker-compose)
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
# Параметры атворизации
JWT_SECRET=
JWT_ALGORITHM=
JWT_EXPIRES_SECONDS=
# Супер пользователь
ADMIN_USERNAME=
ADMIN_PASSWORD=
# Время жизни модели
MODEL_EXPIRE_SECONDS=
```

### Alembic 
```bash
cd src
alembic upgrade head
```

### Запуск
```bash
gunicorn src.app:app --workers 1 --daemon --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:11000

gunicorn dsh.app:server --bind=0.0.0.0:8000
```

## Docker
Для запуска можно воспользовать docker-compose:
```bash
git clone https://github.com/RolfAdolf/final_project.
cp $PATH_TO_ENV/.env ./final_project
cd final_project
docker compose build
docker compose up
```
***
По всем вопросам обращаться:


`Telegram`: @Nadir_Devrishev


`Mail`: n.devrishev@gmail.com

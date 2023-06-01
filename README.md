# FastApi ML
Проект является реализацией API с использованием фреймворка FastAPI. Позволяет работать с моделями машинного обучения, скачивать данные с сервера, совершать обучение и проверять модели на собственных тестовых данных.
***
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
#Пользователь создаваемый по умолчанию
ADMIN_USERNAME=
ADMIN_PASSWORD=
# Время жизни модели
MODEL_EXPIRE_SECONDS=
```
### Запуск
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

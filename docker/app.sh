#!/bin/bash

cd src
echo "UPGRADING ALEMBIC"
alembic upgrade head
cd ../
echo "UPGRADING has been finished"

echo "STARTING SERVER"
gunicorn src.app:app --workers 1 --daemon --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:11000
echo "SERVER HAS BEEN LAUNCHED"

echo "STARTING CLIENT"
gunicorn dsh.app:server --bind=0.0.0.0:8000
echo "CLIENT HAS BEEN LAUNCHED"

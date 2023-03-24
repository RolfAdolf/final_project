#!/bin/bash

cd src
echo "UPGRADING ALEMBIC"
pwd
ls
alembic upgrade head
cd ../
echo "UPGRADING has been finished"
pwd ls

echo "STARTING CLIENT"
gunicorn dsh.app:server --bind=0.0.0.0:8050 --daemon
echo "CLIENT HAS BEEN LAUNCHED"

echo "STARTING SERVER"
gunicorn src.app:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000
echo "SERVER HAS BEEN LAUNCHED"

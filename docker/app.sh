#!/bin/bash

cd src
echo "UPGRADING ALEMBIC"
pwd
ls
alembic upgrade head
cd ../
echo "UPGRADING has been finished"
pwd ls

echo "STARTING SERVER"
gunicorn src.app:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000
echo "SERVER HAS BEEN LAUNCHED"

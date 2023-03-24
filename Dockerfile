FROM python:3.10

RUN mkdir /final_app

WORKDIR /final_app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod a+x docker/*.sh

FROM python:3.11.2

RUN apt update && apt install -y cron

RUN pip install --upgrade pip

WORKDIR /nothilfe_tracker

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY crontab /etc/cron.d/crontab

ADD . /nothilfe_tracker

RUN crontab /etc/cron.d/crontab

CMD ["cron", "-f"]
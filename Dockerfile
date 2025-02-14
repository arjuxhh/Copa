FROM python:3.11-slim-buster
RUN apt update && apt upgrade -y
RUN apt install git -y
COPY requirements.txt /requirements.txt
grep -r "class Instance" .
grep -r "def from_db" .
RUN cd /
RUN pip install -U pip && pip install -U -r requirements.txt
WORKDIR /app

COPY . .
CMD ["python", "bot.py"]

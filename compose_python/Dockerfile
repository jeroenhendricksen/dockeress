# https://hub.docker.com/_/python?tab=tags&page=1&name=3.1
FROM python:3.11-alpine

RUN apk --no-cache add bash tini

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY *.py ./

ENTRYPOINT ["python3", "-u", "/usr/src/app/app.py"]

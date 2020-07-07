FROM python:3

WORKDIR /usr/src/app

COPY ./README.md ./

COPY ./flask/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./flask ./

CMD ["uwsgi", "app.ini"]

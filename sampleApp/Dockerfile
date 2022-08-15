FROM python:slim-buster

WORKDIR /sampleApp

COPY app app
COPY requirements requirements
COPY manage.py manage.py

RUN python -m manage --install docker

EXPOSE 8000

CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8000","--no-access-log", "--factory", "app:create_app"]
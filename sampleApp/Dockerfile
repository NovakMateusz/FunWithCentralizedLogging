FROM python:slim-buster

WORKDIR /sampleApp

COPY app app
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT [ "python" ]
CMD [ "run_app.py" ]

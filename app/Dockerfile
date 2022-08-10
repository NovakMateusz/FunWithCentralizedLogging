FROM python:slim-buster

WORKDIR /app
RUN mkdir logs

COPY main.py main.py
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT [ "python" ]
CMD [ "main.py" ]

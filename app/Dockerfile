FROM python:3.10.4-alpine3.15

COPY src/requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 5000

COPY ./src/ /app/

ENTRYPOINT ["python"]

CMD ["run.py"]
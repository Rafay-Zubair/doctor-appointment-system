FROM python:alpine3.19

RUN mkdir app

WORKDIR /app

COPY ./requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

EXPOSE 9090

ENV HOST_URL="mongodb"
ENV DB_PORT="27017"

COPY ./app.py ./

CMD ["python", "app.py"]


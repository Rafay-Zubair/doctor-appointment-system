FROM node:20.8.0-alpine3.18

RUN mkdir app

WORKDIR /app

COPY package*.json ./

RUN npm install

EXPOSE 3000

ENV DOCTORS_SERVICE_URL="doc-cont:9090"
ENV APPOINTMENTS_SERVICE_URL="app-cont:7070"

COPY ./app.js ./
COPY ./public/* ./public/

CMD ["npm", "start"]


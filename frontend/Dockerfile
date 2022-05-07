FROM node:13.12.0-alpine

WORKDIR /apps


COPY . /apps

RUN npm install --silent


EXPOSE 8080

CMD ["npm","run","serve"]


# https://hub.docker.com/_/node?tab=tags
FROM node:19-alpine
WORKDIR /usr/src/app
COPY package*.json ./
RUN npm install
COPY --chown=node:node . .

USER node
EXPOSE 8080
CMD [ "node", "server.js" ]

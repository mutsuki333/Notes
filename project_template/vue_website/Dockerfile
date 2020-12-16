FROM node as build
WORKDIR /source
COPY package*.json /source/
RUN npm install
RUN npm run build

FROM nginx
COPY --from=build /source/dist /usr/share/nginx/html
COPY ./nginx.cong /etc/nginx/nginx.conf
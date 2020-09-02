# Nginx SPA

> An dockerized server to serve local docs and spa

## Config

### docker-compose.yml

```yml
version: "3"

services:

  nginx:
    image: "nginx:latest"
    restart: "always"
    volumes:
      - ../../docs:/usr/share/nginx/html/docs
      - PATH_TO_DIR:/usr/share/nginx/html/NAME
      - ./nginx.conf:/etc/nginx/nginx.conf
    ports:
      - "PORT:80"
```

The volumes can be added to serve.

|Property|Description                         |Default|
|--------|------------------------------------|--------------------|
|Volume  |set for the folder you want to serve|docs of this project|
|PORT    |The port server on local host       |`1234`              |

### nginx.conf

```conf
server {
    listen 80;
    location /PATH {
        alias   /usr/share/nginx/html/PATH/;
        expires -1;
        add_header Pragma "no-cache";
        add_header Cache-Control "no-store, no-cache, must-revalidate, post-check=0, pre-check=0";
        try_files $uri$args $uri$args/ $uri /PATH/index.html ;
    }
}
```

|Property|Description                 |Default |
|--------|----------------------------|--------|
|PATH    |The url path for the folder |`'docs'`|


## Usage

```bash
docker-compose up
```

url: 
http://localhost:1234/docs/

(Replace `1234` to your port)

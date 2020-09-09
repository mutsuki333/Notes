# Comprehensive Backend

> A backend powered by flask, peewee  
> Including role management and access logs

## Dependency

* flask
* flask-login
* flask-restful
* flask_cors
* passlib
* peewee
* requests
* uwsgi

## Install

```bash
python -m venv ENV
source ./ENV/bin/activate
pip install -r requirements.txt
```

## Config

```conf
# server.conf
[App]
debug=true
testing=false
secret_key = \xc3c\x9c!|kN\xc5G\xc1\xcal\xdc\xefo\x91\xf8\x1c\xe41\x9d\xb1_\x93

[Database]
location=./data/server.db
```

```ini
# uwsgi.ini
[uwsgi]
socket = 0.0.0.0:8000
wsgi-file = start.py
callable = app
processes = 4
threads = 2
buffer-size = 32768
stats = 0.0.0.0:9191
```

## Usage

## Customize

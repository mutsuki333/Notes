FROM python:3.8-alpine3.12
WORKDIR /app
COPY ./requirements.lock .
RUN set -e; \
	apk add --no-cache --virtual .build-deps \
		gcc \
        python3-dev \
        jpeg-dev \
        zlib-dev \
		libc-dev \
		linux-headers \
	; \
	pip install -r requirements_lock.txt; \
	apk del .build-deps;
RUN apk add libjpeg

COPY . .
CMD ["uwsgi","uwsgi.ini"]
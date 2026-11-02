FROM nginx:stable-alpine3.24-perl

RUN apk add python3 py3-pip

COPY --chmod=755 ./start.sh /start.sh

CMD ["/bin/sh", "/start.sh"]

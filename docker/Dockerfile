FROM nginx:stable-alpine3.24-perl

#Install packages dependencies
COPY ./src/app/alpine-packages.txt /tmp/alpine-packages.txt
RUN apk add python3 ruff py3-pip git $(tr '\n' ' ' < /tmp/alpine-packages.txt)

#Install python requirements
COPY ./src/app/requirements.txt /tmp/requirements.txt
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install -r /tmp/requirements.txt

WORKDIR  /app

CMD ["/bin/sh", "/app/docker/start.sh"]

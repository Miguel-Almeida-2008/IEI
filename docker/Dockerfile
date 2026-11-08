FROM nginx:stable-alpine3.24-perl

#Install packages dependencies
RUN apk add python3 py3-pip ruff git

#Install python requirements
COPY ./src/app/requirements.txt /tmp/requirements.txt
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install -r /tmp/requirements.txt

WORKDIR  /app

CMD ["/bin/sh", "/app/docker/start.sh"]

#!/bin/sh

python3 -m venv /docker/volume/.venv
. /docker/volume/.venv/bin/activate
pip install -r /docker/volume/app/requirements.txt
python3 /docker/volume/app/main.py
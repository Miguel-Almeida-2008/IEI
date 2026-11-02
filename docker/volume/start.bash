#!/bin/sh

sudo apt install python3-full

python3 -m venv docker/volume/venv
source docker/volume/.venv/bin/activate
pipx install requirements.txt
python main.py
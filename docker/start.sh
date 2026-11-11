#!/bin/sh

sh /app/runTests.sh
/opt/venv/bin/python3 /app/src/app/main.py
#python3 -m venv .venv && . /app/.venv/bin/activate && pip install -r /app/src/app/requirements.txt && python3 /app/src/app/main.py
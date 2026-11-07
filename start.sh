#!/bin/sh

ruff check --fix /app/src/app/
ruff format /app/src/app/

python3 /app/src/app/main.py

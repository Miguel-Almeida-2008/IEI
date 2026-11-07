# IEI
Files for IEI project

## Requirements
Have docker installed and set-up
Run this to grant premissions for devcontainer: ``sudo apt update && sudo apt install docker-compose-plugin``

## How to run  
go to ``/IEI/docker/`` folder


run:


``docker compose up -d --build runtime && docker attach python-tester``

## when finished:
run:


``docker compose down``


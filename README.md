# IEI
Files for IEI project

## Requirements
On Linux:
- Have docker installed and set-up
- Add the VSCode plugin ``Dev Containers``

On Windows:
- Have docker and WSL installed and set-up
- Have Docker Desktop working with WLS
- Add the VSCode plugin ``Dev Containers``.

## How to run  
Go to ``/IEI/docker/`` folder

run:
- ``docker compose up -d --build`` to start the container and run the tests.
- Inside the container: ``./runTests.sh`` to run the testes

The linting reports will be in ``lintingReports.txt`` file.


## when finished:
run:
 - ``docker compose down``


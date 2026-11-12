# IEI
Files for IEI project

## Requirements
**On Linux:**
- Have docker installed and set-up
- Add the VSCode plugin **Dev Containers**

**On Windows:**
- Have **docker and WSLVcXsrv** installed and set-up
- Have Docker Desktop working with WLS
- Add the VSCode plugin **Dev Containers**

- If you want to run a app with GUI you will need to install VcXsrv:
    - After you install VcXsrv run it for the first time
        - Click next on every window and finish on the last one
        - When a Windows Defender window pops up, click **Allow**

## How to use
- Put the python app you want to run in ``/pythonTester/src/app/`` with the name ``main.py`` and the python app to run the tests in ```/pythonTester/src/app/`` with the name ``tests.py``
- Write the name of the packages you need to import in ``/IEI/src/app/requirements.txt``, one in each line
- Write the name of the packages that need to be installed on the os in ``/IEI/src/app/alpine-packages.txt``, with the name to install the package on **Alpine OS**, one in each line

## How to run
**If your app needs display access**
- In the file ``/IEI/docker/.env`` chose the OS you are using
**On Linux**
- run ``xhost +local:`` to allow the container to connect to your X11 server.
**On windows**
- Start **XLaunch** and select next on every window and finish in the last one


Go to ``/IEI/docker/`` folder

**On Linux:**
- run ``docker compose up -d --build`` to start the container, run the tests and if everything is working start the program.
- run ``docker exec -it python-tester sh`` to enter into the container

**On Windows:**
- Start **docker desktop** and wait for it to initialize
- run ``docker compose -d --build`` to start the container, run the tests and if everything is working start the program.
- run ``docker exec -it python-tester sh`` to enter into the container

On the container run ``sh runTests.sh`` to run the ``tests.py`` file and to use ruff automaticly

The linting reports and any errors that the ``tests.py`` app encounter will be in ``/IEI/lintingReports.txt`` file on your computer or in ``/app/lintingReports.txt`` inside the docker.


## when finished:
run:
 - ``docker compose down``


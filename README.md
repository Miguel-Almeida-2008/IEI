# IEI
Files for IEI project

## Requirements
**On Linux:**
- Have docker installed and set-up
- Add the VSCode plugin ``Dev Containers``

**On Windows:**
- Have **docker and WSLVcXsrv** installed and set-up
- Have Docker Desktop working with WLS
- Add the VSCode plugin ``Dev Containers``

- If you want to run a app with GUI you will need to install VcXsrv:
    - After you install VcXsrv run it for the first time
        - Click next on every window and finish on the last one
        - When a Windows Defender window pops up, click **Allow**

## How to use
- Put the python app you want to run in ``/pythonTester/src/app/`` with the name ``main.py``
- Write the name of the packages you need to import in ``/IEI/src/app/requirements.txt``, one in each line
- Write the name of the packages that need to be installed on the os in ``/IEI/src/app/alpine-packages.txt``, with the name to install the package on ``Alpine OS``, one in each line

## How to run
In the file ``/IEI/docker/.env`` chose the OS you are using 

Go to ``/IEI/docker/`` folder

**On Linux:**
- run ``xhost +local:`` to allow the container to connect to your X11 server.
- run ``docker compose up -d --build`` to start the container, run the tests and if everything is working start the program.
- run ``docker attach python-tester`` if you need to interact with the program console

**On Windows:**
- Start **docker desktop** and wait for it to initialize
- Start **XLaunch** and select next on every window and finish in the last one
- run ``docker compose -d --build`` to start the container, run the tests and if everything is working start the program.
- run ``docker attach python-tester`` if you need to interact with the program console

If the app doesn't execute and if any errors were found they will be listed in ``lintingReports.txt``.

The linting reports will be in ``/IEI/lintingReports.txt`` file.


## when finished:
run:
 - ``docker compose down``


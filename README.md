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
        - Select Multiple windows and set the Display number to 0. Click Next
        - Select Start no client. Click Next
        - Check the box for **Disable access control**
        - Click Next, then Finish.
        - When a Windows Defender window pops up, click **Allow**

## How to run
Go to ``/IEI/docker/`` folder

**On Linux:**
- run ``xhost +local:`` to allow the container to connect to your X11 server.
- run ``docker compose up -d --build`` to start the container, run the tests and if everything is working start the program.
- run ``docker attach python-tester`` if you need to interact with the program console

**On Windows:**
- Start docker desktop and wait for it to initialize
- run ``docker compose -d --build`` to start the container, run the tests and if everything is working start the program.
- run ``docker attach python-tester`` if you need to interact with the program console

If any errors were found they will be listed in ``lintingReports.txt``.

The linting reports will be in ``/IEI/lintingReports.txt`` file.


## when finished:
run:
 - ``docker compose down``


# IEI
Files for IEI project

## Requirements
On Linux:
- Have docker installed and set-up
- Add the VSCode plugin ``Dev Containers``

On Windows:
- Have **docker, WSL and VcXsrv** installed and set-up
    - The first time you run XLaunch a Windows Defender Firewall window will pop up. You must check both "Private networks" and "Public networks" and click Allow.
    - Open the XLaunch shortcut that VcXsrv installed. You must configure it with these specific settings:

        - Select Multiple windows and set the Display number to 0. Click Next

        - Select Start no client. Click Next

        - Check the box for **Disable access control**

        - Click Next, then Finish.
- Have Docker Desktop working with WLS
- Add the VSCode plugin ``Dev Containers``

## How to run  
Go to ``/IEI/docker/`` folder

On Linux:
- ``xhost +local:`` to allow the container to connect to your X11 server.
- ``docker compose up -d --build`` to start the container, run the tests and if everything is working start the program.
- ``docker attach python-tester`` if you need to interact with the program console

On Windows:
- 

If any errors were found they will be listed in ``lintingReports.txt``.

The linting reports will be in ``/IEI/lintingReports.txt`` file.


## when finished:
run:
 - ``docker compose down``


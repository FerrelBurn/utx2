#!/bin/bash

# Generates text to terminal  
echo "******************************************************************"
echo "getting ready to get some containers"
echo "this script will pull the docker images needed and start them"
echo "don't re-download if you don't need to  blah3"

# (U)(G) can read, write, and execute. (O) can read, can't write, can execute.
chmod 775 notebooks

# Defines and runs multi-container applications.
docker-compose -f /opt/zapataai/docker-compose.yaml up -d

# Which Python 3 TODO CG
/usr/bin/python3 --version
/usr/bin/pip3 install -r /opt/zapataai/requirements.txt

# makes file executable
chmod +x /opt/zapataai/heartbeat.py

# Which python 3 TODO CG
/usr/bin/python3 /opt/zapataai/heartbeat.py 

# Generates text to terminal
echo "setup-containers script completed"

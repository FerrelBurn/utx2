#!/bin/bash
echo "******************************************************************"
echo "getting ready to get some containers"
echo "this script will pull the docker images needed and start them"
echo "don't re-download if you don't need to  blah3"

docker-compose -f /opt/zapataai/docker-compose.yaml up -d
/usr/bin/python3 --version
which python3
which pip3
/usr/local/bin/pip3 install -r /opt/zapataai/requirements.txt
/usr/bin/python3 /opt/zapataai/heartbeat.py
echo "setup-containers script completed"
exit 0

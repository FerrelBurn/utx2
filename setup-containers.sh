#!/bin/bash
echo "******************************************************************"
echo "getting ready to get some containers"
echo "this script will pull the docker images needed and start them"
echo "don't re-download if you don't need to  blah3"

docker-compose -f /opt/zapataai/docker-compose.yaml up -d
pip3 install -r /opt/zapataai/requirements.txt
python3 /opt/zapataai/heartbeat.py &
exit 0

#!/bin/bash
echo "Welcome"
echo "checking to see if this script has ran before"
FILE=/etc/.startup
if test -f "$FILE"; then
  echo "$FILE exists which means it has ran before... exiting..."
  exit
  else
  apt get install python3-pip
  apt get install docker-compose
  sed -i '/ExecStart=/usr/bin/dockerd/c\ExecStart=/usr/bin/dockerd -H fd:// -H=tcp://0.0.0.0:5555 --containerd=/run/containerd/containerd.sock' /lib/systemd/system/docker.service
  systemctl daemon-reload
  service docker restart
  chown -R nvidia:nvidia /home/nvidia/.cache/
  usermod -aG docker $USER

  touch $FILE
fi
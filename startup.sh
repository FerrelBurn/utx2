#!/bin/bash
echo "Welcome"
apt get install python3-pip
apt get install docker-compose
sed -i '/ExecStart=/usr/bin/dockerd/c\ExecStart=/usr/bin/dockerd -H fd:// -H=tcp://0.0.0.0:5555 --containerd=/run/containerd/containerd.sock' /lib/systemd/system/docker.service
systemctl daemon-reload
service docker restart
chown -R nvidia:nvidia /home/nvidia/.cache/
usermod -aG docker $USER



create first run file
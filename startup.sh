#!/bin/bash
echo "Welcome"
sudo apt get install python3-pip
sudo apt get install docker-compose
sed -i '/ExecStart=/usr/bin/dockerd/c\ExecStart=/usr/bin/dockerd -H fd:// -H=tcp://0.0.0.0:5555 --containerd=/run/containerd/containerd.sock' /lib/systemd/system/docker.service
ls
echo "this is a directory list"

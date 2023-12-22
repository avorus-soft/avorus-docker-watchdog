#!/bin/sh

##
# Install dependencies
# #
sudo apt-get update
sudo apt-get install -qq python3-docker
sudo apt-get install -qq python3-sdnotify

##
# Install service
# #
chmod +x ./docker-watchdog.py
sudo cp ./docker-watchdog.py /usr/local/bin/
sudo cp ./docker-watchdog.service /usr/lib/systemd/system/

##
# Reload systemd & start service
##
sudo systemctl daemon-reload
sudo systemctl enable docker-watchdog.service
sudo systemctl start docker-watchdog.service

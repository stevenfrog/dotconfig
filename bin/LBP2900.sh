#!/bin/bash

sudo /usr/sbin/ccpdadmin -p LBP2900 -o /dev/usb/lp0
sudo systemctl restart ccpd

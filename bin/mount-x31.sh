#!/bin/bash

#The uid and gid should find in "User and Group"
echo "Please add X31's ip address as parameter"
sudo mount -t cifs -o uid=1000,gid=100,username="administrator",password="" //$1/Temp /home/stevenfrog/x31/Temp
sudo mount -t cifs -o uid=1000,gid=100,username="administrator",password="" //$1/Emule_Down /home/stevenfrog/x31/Emule_Down

#!/bin/bash

# No protocol specified
#xhost local:db2inst1
xhost +

# profile for db2 jdbc type2
if [ -f /home/db2inst1/sqllib/db2profile ]; then
   . /home/db2inst1/sqllib/db2profile
fi
 
# start db2admin
sudo /opt/ibm/db2/V9.7/das/bin/db2admin start
 
# open the db2cc with user db2inst1
#su - db2inst1 # can not use - here, it will make display can not open
su - db2inst1
# next command need type in
#db2start

# Please type two times of db2start
# Because the linux kernel version is too new
#https://www.ibm.com/developerworks/community/forums/html/topic?id=77777777-0000-0000-0000-000014632773

#db2cc

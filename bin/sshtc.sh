#!/bin/sh

if [ $# = 1 ]; then
    ssh -i ~/.ssh/id_rsa tc@$1 -L 5901:localhost:5901
elif [ $# = 2 ]; then
    ssh -i ~/.ssh/id_rsa $2@$1 -L 5901:localhost:5901
fi

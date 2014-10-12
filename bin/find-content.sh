#!/bin/bash

#echo "The funcation is to find the content in file"
name="zzz"${1}

if [[ $name = "zzz*" ]]; then
    find . | xargs grep -d skip -n -i --color $2
else
    find . -iname "$1" | xargs grep -d skip -n -i --color $2
fi

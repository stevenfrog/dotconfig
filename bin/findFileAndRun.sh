#!/bin/sh

# This script accecpt two param like this:
# findFileAndRun.sh package.json "npm start"
#
# It will find specify file and then input command

FILE=$1
COMMAND=$2

FLAG=false

for I in 1 2 3 4 5 6 7 8 9
do
    if [ "$(pwd)" = "/" ] ; then
        break
    fi

    filePath="$(pwd)/"$FILE

    if [ -f $filePath ] ; then
        FLAG=true
        break
    fi

    echo $filePath" : Not Exist"

    cd ..
done

if $FLAG ;
then
    echo "=== Got it in:$filePath ==="
    echo $COMMAND
    $($COMMAND)
else
    echo "=== Not found ==="
fi

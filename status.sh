#!/bin/bash

count=$(finger -l | grep ':0\b' | wc -l)
board=$(lshal | grep -i 'altera' | wc -l)
if [ $count -gt 0 ]
then
    echo "machine is in use."
    exit 1
else
    echo "MACHINE IS FREE."
    if [ $board -gt 0 ]
    then
        echo "BOARD AVAILABLE"
        exit 0
    else
        echo "...but no board plugged in."
        exit 2
    fi
fi

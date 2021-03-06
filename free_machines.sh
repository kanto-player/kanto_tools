#!/bin/bash

echo "EMBEDDED SYSTEM LAB POLLING"

machine_statuses=(0 0 0 0 0 0 0 0 0 0 0 0 0 0 0)
fr=0
bu=0
fne=0
user=$1

for i in {1..15}
do
    echo "machine $i=========================="
    ssh "$user@micro${i}.ilab.columbia.edu" 'bash -s' < ./status.sh
    machine_statuses[$((i-1))]=$?;
done
echo "**************************************************"
echo ""

echo "FR = Free and Ready"
echo "Bu = Busy"
echo "FNE = Free Not Equipped"
echo "**************************************************"
echo -e "\tFR\tBu\tFNE"
echo "**************************************************"
for i in {1..15}
do
    echo -n "$i"
    if [ ${machine_statuses[$((i-1))]} -eq 0 ]
    then
        fr=$(($fr+1))
        echo -e "\tX"
    elif [ ${machine_statuses[$((i-1))]} -eq 1 ]
    then
        echo -e "\t\tX"
        bu=$(($bu+1))
    else
        echo -e "\t\t\tX"
        fne=$(($fne+1))
    fi
done
echo "**************************************************"
echo "Total FR: $fr"
echo "Total Bu: $bu"
echo "Total FNE: $fne"

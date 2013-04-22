#!/bin/bash

length=$(($#-1))
inputs=${@:1:$length}
output=$(eval echo \$$#)

for file in $inputs
do
	sox "$file" -b 16 -e signed-integer -B -c 1 -t raw -
done > $output

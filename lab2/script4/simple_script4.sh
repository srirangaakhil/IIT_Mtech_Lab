#!/bin/bash

line=$(head -n 1 $1)
array=($line)

max=${array[0]}
second_max=${array[0]}

for i in ${array[@]} ; do
	if (( i > max )); then
		second_max=$max
		max=$i
	fi
done

echo $max
echo $second_max
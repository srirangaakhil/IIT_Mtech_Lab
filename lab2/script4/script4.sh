#!/bin/bash

line=$(head -n 1 $1)
array=($line)


max=${array[0]}
for n in "${array[@]}" ; do
    ((n > max)) && max=$n
done

secondGreatest=$(printf '%s\n' "${array[@]}" | sort -nu | tail -2 | head -1)

echo $(($max+$secondGreatest))
echo $(($max*$secondGreatest))
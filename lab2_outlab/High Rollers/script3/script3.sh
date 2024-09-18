#! /bin/bash

cdir=$(pwd)
cd $1
files="$(ls -p | grep -v /)"
IFS=$'\n'
total_lines=0
for x in $files; do   
    blank_lines=$(grep "^\s*$" $x | wc -l)
    all_lines=$(wc -l < $x)
    total_lines=$(($total_lines + $all_lines - $blank_lines))
done
cd $cdir

echo $total_lines

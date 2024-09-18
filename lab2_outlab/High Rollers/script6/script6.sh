#!/bin/bash

cp $1 output
array=()
while IFS= read -r line
do
   array+=(${line})
done < "$2"


for word in "${array[@]}"
do
   sed -i "s/ ${word}/ bleep/Ig" output
   sed -i "s/^${word}/bleep/Ig" output
done

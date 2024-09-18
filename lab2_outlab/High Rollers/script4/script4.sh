#!/bin/bash

while IFS= read -r line
do
   IFS=',' read -r -a array <<< "$line"
      for ((i=1; i<${#array[*]}; i++));
      do
         echo "${array[0]},${array[i]},${array[++i]}" >> output
      done

sort -o output output
done < "$1"




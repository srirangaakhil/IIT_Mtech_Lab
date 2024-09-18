#!/bin/bash

while IFS= read -r line
do
  if [ -d "$line" ]; then
      echo could not create test1
  else
      mkdir $line
      echo created $line
  fi
done < "$1"

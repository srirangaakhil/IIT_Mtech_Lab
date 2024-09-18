#!/bin/bash
sed -E "s/[[:space:]]+/ /g" $1 |sed -e "s/^[[:space:]]//g" | grep -v "^ $" |grep -v "^$"

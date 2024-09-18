#!/bin/bash

sed -nr 's/( )?$/\tPoints/; 1,1 p' $1 
sed -n '2,$ p' $1 |  awk '{ printf("%s	%d\n", $0, $3*4+$4*2) }'

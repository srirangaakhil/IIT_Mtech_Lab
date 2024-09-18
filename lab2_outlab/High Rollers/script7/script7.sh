#!/bin/bash

cp $1 output
word="mighty"
rep="dumb"
sed -i "s/ ${word}/ ${rep}/Ig" output
sed -i "s/(${word}/(${rep}/Ig" output
sed -i "s/{${word}/{${rep}/Ig" output
sed -i "s/[[]${word}/[${rep}/Ig" output
cat output
rm output



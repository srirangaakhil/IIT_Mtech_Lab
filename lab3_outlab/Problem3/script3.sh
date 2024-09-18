#! /bin/bash

char_count=0
word_count=0
line_count=0
para_count=0
para_flag=0

while IFS= read -r line; do
	line_count=$(( $line_count + 1 ))
	for word in $line; do
		word_count=$(( $word_count + 1 ))
	done
	while read -n 1 char;do
		char_count=$(( $char_count + 1 ))
	done <<< "$line"	

	#Para count
	if [[ $(echo "$line" | egrep -v -a '^[[:space:]]*$') ]]; then
		if [[ para_flag -eq 0 ]]; then
			para_count=$(( $para_count + 1 ))
			para_flag=1
		fi
	else
		para_flag=0
	fi
done < "$1"

if [[ $# -eq 1 ]]; then
	echo "${char_count} characters, ${word_count} words, ${line_count} lines, ${para_count} paragraphs"

elif [[ "$2" = "-chars" ]]; then
	echo "${char_count}"

elif [[ "$2" = "-words" ]]; then
	echo "${word_count}"

elif [[ "$2" = "-lines" ]]; then
	echo "${line_count}"

elif [[ "$2" = "-paras" ]]; then
	echo "${para_count}"
fi
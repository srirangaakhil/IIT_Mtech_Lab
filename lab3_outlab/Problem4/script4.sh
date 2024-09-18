#! /bin/bash

sed -e "s/\r/\n/" -e "s///" $1 | egrep -v -a '^[[:space:]]*$' > out
echo "Name||Address||EmailID"

while IFS= read line; do
	echo -n $line
	echo -n "||"
	flag=0
	while IFS= read address; do
		result=$(echo $address | egrep '^Email.*$')
		if [[ $result ]]; then
			echo -n "||"
			echo ${result:10}
			break
		else
			if [[ flag -eq 0 ]]; then
				echo -n -e "$address"
				flag=1
			elif [[ flag -eq 1 ]]; then
				echo -n -e " $address"
			fi
		fi
	done
done < $"out"
rm out

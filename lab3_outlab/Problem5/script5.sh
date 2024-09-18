#! /bin/bash
awk 'BEGIN{FS=","}

{a[$2]+=$3}

END{
for(i in a)
	{
	printf("%s,%d\n",i,a[i])
	}

}
' $1 | sort -t, -k1 
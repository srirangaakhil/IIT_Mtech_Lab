#!/bin/bash


#input 1
sed -r 's/[[:space:]]/\n/g' < $1 \
| egrep -v '^( )*$' \
| sed -r "s/^[?!,;:_(){}'\"]//" \
| sed -r "s/^-//" \
| sed -r "s/^\[//" \
| sed -r "s/^\]//" \
| sed -r "s/^\.\.\.//" \
| sed -r "s/^\.//" \
| sed -r "s/[?!,;:_(){}'\"]$//" \
| sed -r "s/-$//" \
| sed -r "s/\[$//" \
| sed -r "s/\]$//" \
| sed -r "s/\.\.\.$//" \
| sed -r "s/\.$//" \
| tr '[:upper:]' '[:lower:]' > wordsInFile1


wordCount1=$(grep -c '' wordsInFile1)

awk -v wordCount="$wordCount1" '
{ 
	a[$1]+=1
}
END{
	for(i in a) 
	{
		printf("%s	%d	%f	1\n", i, a[i], a[i]/wordCount);
	}
}' wordsInFile1 \
| sort -k1 > combinedFile

#echo ------------------------------------------------------------

#input 2
sed -r 's/[[:space:]]/\n/g' < $2 \
| egrep -v '^( )*$' \
| sed -r "s/^[?!,;:_(){}'\"]//" \
| sed -r "s/^-//" \
| sed -r "s/^\[//" \
| sed -r "s/^\]//" \
| sed -r "s/^\.\.\.//" \
| sed -r "s/^\.//" \
| sed -r "s/[?!,;:_(){}'\"]$//" \
| sed -r "s/-$//" \
| sed -r "s/\[$//" \
| sed -r "s/\]$//" \
| sed -r "s/\.\.\.$//" \
| sed -r "s/\.$//" \
| tr '[:upper:]' '[:lower:]' > wordsInFile2


wordCount2=$(grep -c '' wordsInFile2)

awk -v wordCount="$wordCount2" '
{ 
	a[$1]+=1
}
END{
	for(i in a) 
	{
		printf("%s	%d	%f	2\n", i, a[i], a[i]/wordCount);
	}
}' wordsInFile2 \
| sort -k1 >> combinedFile

#echo ------------------------------------------------------------

#input 3
sed -r 's/[[:space:]]/\n/g' < $3 \
| egrep -v '^( )*$' \
| sed -r "s/^[?!,;:_(){}'\"]//" \
| sed -r "s/^-//" \
| sed -r "s/^\[//" \
| sed -r "s/^\]//" \
| sed -r "s/^\.\.\.//" \
| sed -r "s/^\.//" \
| sed -r "s/[?!,;:_(){}'\"]$//" \
| sed -r "s/-$//" \
| sed -r "s/\[$//" \
| sed -r "s/\]$//" \
| sed -r "s/\.\.\.$//" \
| sed -r "s/\.$//" \
| tr '[:upper:]' '[:lower:]' > wordsInFile3


wordCount3=$(grep -c '' wordsInFile3)

awk -v wordCount="$wordCount3" '
{ 
	a[$1]+=1
}
END{
	for(i in a) 
	{
		printf("%s	%d	%f	3\n", i, a[i], a[i]/wordCount);
	}
}' wordsInFile3 \
| sort -k1 >> combinedFile

#sort -k1 combinedFile \
#| awk -v wordCount1=$wordCount1 -v wordCount2=$wordCount2 -v wordCount3=$wordCount3 '
#{
#	if($4==1)
#	{
#		a[$1]+=$3*wordCount1/(wordCount1+wordCount2+wordCount3);
#	}
#	else if($4==2)
#	{
#		a[$1]+=$3*wordCount2/(wordCount1+wordCount2+wordCount3);
#	}
#	if($4==1)
#	{
#		a[$1]+=$3*wordCount3/(wordCount1+wordCount2+wordCount3);
#	}
#}
#END{
#	for(i in a)
#	{
#		printf("%s, %f\n", i, a[i]/3);
#	}
#}' \
#| sort -k1

sort -k1 combinedFile \
| awk -v wordCount1=$wordCount1 -v wordCount2=$wordCount2 -v wordCount3=$wordCount3 '
{
	a[$1]+=$2;
}
END{
	for(i in a)
	{
		printf("%s, %.8f\n", i, a[i]/(wordCount1 + wordCount2 + wordCount3));
	}
}
' \
| sort -k1



#echo $wordCount1 $wordCount2 $wordCount3

rm wordsInFile1
rm wordsInFile2
rm wordsInFile3
rm combinedFile


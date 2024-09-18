sed -f script3.sed testcase/input3 > out

diff -Z out testcase/output3 > result

if [[ -s result ]];
then
	echo failed
else
	echo passed
fi
rm out result

./script2.sh testcase/input2 > out

diff -Z testcase/output2 out > result

if [[ -s result ]];
then
	echo failed
else
	echo passed
fi
rm out result

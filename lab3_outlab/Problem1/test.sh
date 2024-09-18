./script1.sh testcase/input1 > out

diff testcase/output1 out > result

if [[ -s result ]];
then
	echo failed
else
	echo passed
fi
rm out result

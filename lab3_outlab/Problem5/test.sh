./script5.sh testcase/input5 > tmpout1
diff -Z tmpout1 testcase/output5 > result1
if [ -s result1 ]
then 
     echo "failed"
else
     echo "passed"
fi



rm tmpout1 result1





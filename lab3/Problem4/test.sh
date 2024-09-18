awk -f script4.awk testcase/input41 > tmpout1
diff -Z tmpout1 testcase/output41 > result1
if [ -s result1 ]
then 
     echo "Test case-1 failed"
else
     echo "Test case-1 passed"
fi


awk -f script4.awk testcase/input42 > tmpout2
diff tmpout2 testcase/output42 > result2

if [ -s result2 ]
then 
     echo "Test case-2 failed"
else
     echo "Test case-2 passed"
fi

rm tmpout1 tmpout2 result1 result2





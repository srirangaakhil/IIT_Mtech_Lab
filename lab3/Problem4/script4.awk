BEGIN{OFS="\t";
RS="!";
FS=",";
ORS="\n";
printf "Value\tSensorNumber\n";
}
{print $1"\t"$2}

set xrange [-10:10] noreverse writeback
set yrange [-10:10] noreverse writeback

set style line 1 lt 1 lw 2
set style line 2 lt 2 lw 2
set style line 3 lt 3 lw 2
set style line 4 linetype 0 dt 2 lw 2
f0(x)=0
f(x)=x**2-2*x
f1(x)=x**2-4*x
f2(x)=x**2-6*x
set term png size 600, 400 font ""
set output "5.png"
set key reverse
plot f0(x) title 'poly(x)' with lines linestyle 4, f(x) title 'poly1(x)' with lines linestyle 1, f1(x) title 'poly2(x)' with lines linestyle 2, f2(x) title 'poly3(x)' with lines linestyle 3


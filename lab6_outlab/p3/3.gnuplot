set xlabel "Roll No -->"
set ylabel "Gradepoint -->"
set xtics 0,1,22 rotate by 0+45#45angle45#45
set ytics 0,1,10
set style textbox opaque
set bmargin 3
set xtics offset 0,-1,0
set xrange [0:22] noreverse writeback 
set yrange [3:11] noreverse writeback
set grid ytics lc rgb "#bbbbbb" lw 1 lt 0
set grid xtics lc rgb "#bbbbbb" lw 1 lt 0
set term png size 600, 400
set output "3.png"
set key autotitle columnhead
set datafile separator ","
plot "Plot3Data.csv" using 1:(($2<40)?4:($2<45)?5:($2<50)?6:($2<55)?7:($2<60)?8:($2<70)?9:10) title "Grade Chart" w lp ls 1 lw 3 ,\
'' using 1:((($2<40)?4:($2<45)?5:($2<50)?6:($2<55)?7:($2<60)?8:($2<70)?9:10)):(sprintf("%d",int($2))) w labels center boxed notitle

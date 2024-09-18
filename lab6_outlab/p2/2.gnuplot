set t pngcairo size 640,400
set o "2.png"
set xrange [-4:4]
set yrange [-4:4]
set zrange [0:1000]
set cbrange[0:1000]

set ytics 2
set xtics 2
set ztics 200

set pm3d
set ticslevel 0

set border 95

func(x,y) = 2*(x+y)*(x+y)*(x+y)

splot func(x,y) lc rgb "orange" lw 1



set t pngcairo
set o "4.png"

set title "Ackermann function"
set xrange [0:3]
set yrange [0:3]
set zrange [0:70]
ack(x, y) = (x == 0) ? y + 1 : (y == 0) ? ack(x - 1, 1) : ack(x - 1, ack(x, y-1))
set samples 4,4 # how many samples should you give
set isosamples 4,4 # for the number of lines you see , def: 10
splot ack(x,y) lc rgb "forest-green" lw 2

# Ignore the following
#$points << EOD
#0 0 1
#0 1 2
#1 0 2
#1 1 3
#0 2 3
#1 2 4
#2 0 3
#2 1 5
#2 2 7
#3 0 5
#3 1 13
#3 2 29
#0 3 4
#1 3 5
#2 3 9
#3 3 61
#EOD
#splot '$points' matrix with lines notitle
set t pngcairo
set o "4.png"
set ytics 0.2
set xtics 0.2
f(x) = sqrt(1 - x * x)
g(x) = -1 * f(x)
plot [-1:1] f(x) title 'f(t),g(t)' with lines linestyle 1 lc 2, \
			g(x) notitle with lines linestyle 1 lc 2

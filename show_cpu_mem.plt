set term png small size 800,600
set output "logs/cpu_mem_graph_150.png"

set ylabel "%Consumo"
set xlabel "%Tempo"

set ytics nomirror
set xtics nomirror

set yrange [0:*]
set xrange [0:*]

plot "logs/log_cpu_150.dat" with linespoints title "%CPU", \
     "logs/log_mem_150.dat" with linespoints title "%MEM"
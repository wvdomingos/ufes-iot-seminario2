#!/bin/bash

delay=1; # customize it
while true; do
#ps -C <ProgramName> -o pid=,%mem=,vsz= >> /tmp/mem.log
     ps -C mosquitto -o %cpu=,%mem= >> logs/log_$1.dat
     #gnuplot show_mem.plt
     sleep $delay
done 

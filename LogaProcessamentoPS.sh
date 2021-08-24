#!/bin/bash

delay=1;
while true; do
     ps -C python -o %cpu= >> logs/log_cpu_$1.dat
     ps -C python -o %mem= >> logs/log_mem_$1.dat
     sleep $delay
done 

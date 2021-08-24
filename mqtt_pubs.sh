#!/bin/bash
numPublishers=$1;
qtdIoT=$2
simTime=60; # customize it
for i in $(seq 1 $numPublishers);
 do
    nohup python mqtt_mininet.py $qtdIoT > pub_$i.log &
    nohup bash LogaProcessamentoPS.sh $numPublishers &
done 
sleep "$simTime"
gnuplot show_cpu_mem.plt
killall python
killall bash

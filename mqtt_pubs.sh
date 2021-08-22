#!/bin/bash
numPublishers=1;
qtdIoT=20
simTime=60; # customize it
for i in $(seq 1 $numPublishers);
 do
    nohup python mqtt_mininet.py $qtdIoT > pub_$i.log &
    nohup bash LogaProcessamentoPS.sh $qtdIoT &
done 
sleep "$simTime"
killall python
killall bash

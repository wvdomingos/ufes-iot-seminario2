#!/usr/bin/python

# Link: https://gist.github.com/ramonfontes/651c591141a66280f6433bae28217919

'Setting the position of Nodes and providing mobility using mobility models'
import os
from random import randrange, uniform, randint
from time import sleep
from sys import argv
from mininet.log import setLogLevel, info
from mn_wifi.cli import CLI
from mn_wifi.net import Mininet_wifi


def topology():
    "Create a network."
    net = Mininet_wifi()

    info('*** Adding stations\n')

    iot = int(argv[1])
    for x in range(1, iot+1):
        min_xy = randint(1, 249)
        max_xy = randint(250, 500)
        min_v = randint(1, 10)
        max_v = randint(11, 20)
        net.addStation(f'iot{str(x).zfill(3)}', mac=f'00:00:00:00:00:{str(x).zfill(2)}', ip=f'10.0.0.{str(x)}/8',
                      min_x=min_xy, max_x=max_xy, min_y=min_xy, max_y=max_xy, min_v=min_v, max_v=max_v)

    info('*** Adding APs\n')
    ap1 = net.addAccessPoint('ap1', ssid='new-ssid', mode='g', channel='1',
                             failMode="standalone", position='250,250,0')

    info("*** Configuring wifi nodes\n")
    net.configureWifiNodes()

    net.plotGraph(max_x=100, max_y=100)

    net.setMobilityModel(time=0, model='RandomDirection', max_x=500, max_y=500,seed=20)

    info("*** Starting network\n")
    net.build()
    ap1.start([])

    info("*** Starting Mosquitto Publisher\n")
    i = 0
    while True:
        i+=1
        if i == 4000000: 
            for sta in net.stations:
                x = sta.pos[0]
                y = sta.pos[1]
                z = sta.pos[2]
                temperatura = uniform(19.0, 22.0)
                os.system('mosquitto_pub -t \"%s\" -P user -u user -m \"device=%s x=%s,y=%s,z=%s,temp=%s\"' % (sta.name,sta.name,x,y,z,temperatura))
            i=0

    info("*** Stopping network\n")
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    topology()

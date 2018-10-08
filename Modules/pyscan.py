#!/usr/bin/env python
# *-* coding: iso-8859-1 *-*
import socket

print """
 ___      _   _               ___                            
 | _ \_  _| |_| |_  ___ _ _   / __| __ __ _ _ _  _ _  ___ _ _ 
 |  _/ || |  _| ' \/ _ \ ' \  \__ \/ _/ _` | ' \| ' \/ -_) '_|
 |_|  \_, |\__|_||_\___/_||_| |___/\__\__,_|_||_|_||_\___|_|  
      |__/                                                          
C0d3d by Whoamii

[INFO]Will take some time, depending on your internet speed!

This tool will be scan all ports you set to scan so just wait to finish!

"""

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

url = raw_input("Enter the url you want to scan: ")
port1 = int(raw_input("Where to start scanning the gates: "))
port2 = int(raw_input("And where to finish scanning the gates: "))
porting = range(port1,port2)

def pscan(port):
    try:
       s.connect((url, port))
       return True
    except:
       return False

for x in porting:
    if pscan(x):
       print "Port",x,"is open"
    else:
       print "Port",x,"is closed"

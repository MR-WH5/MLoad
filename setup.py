# Create python3 
# Author B3avers
# 
import urllib.request  as urllib2 
import re
import sys,os
import subprocess
import random

os.system("xdg-open https://www.youtube.com/channel/UCmiZfr9dgRCkwHa_GXSa97A/")

H = '\033[95m'
B = '\033[94m'
G = '\033[92m'
W = '\033[93m'
F = '\033[91m'
E = '\033[0m'
U = '\033[4m'
O = '\033[33m'
BR = "\033[41m"

def heads():
	global head
	head = E+H+"""
╔══════════════════════════════════════╗
║	                               ║
║ ███╗   ███╗███████╗████████╗ █████╗  ║
║ ████╗ ████║██╔════╝╚══██╔══╝██╔══██╗ ║
║ ██╔████╔██║█████╗     ██║   ███████║ ║
║ ██║╚██╔╝██║██╔══╝     ██║   ██╔══██║ ║
║ ██║ ╚═╝ ██║███████╗   ██║   ██║  ██║ ║
║ ╚═╝     ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ║
║      __    ____     ___     ____     ║
║     / /   / __ \   /   |   / __ \    ║
║    / /   / / / /  / /| |  / / / /    ║
║   / /___/ /_/ /  / ___ | / /_/ /     ║
║  /_____/\____/  /_/  |_|/_____/      ║
║                                      ║
║        """+G+'🄰🅄🅃🄷🄾🅁 : 🅂🄰🄳🄴🅆🄰 🄳🄴🅆🄰'+H+"""          ║
║           """+E+'🅈🄾🅄🅃🅄🄱🄴 : 🄼🅁 🅆🄷5'+O+H+"""           ║
║       """+U+B+'🄵🄰🄲🄴🄱🄾🄾🄺 : 🅂🄰🄳🄴🅆🄰 🄳🄴🅆🄰'+U+H+"""         ║
║                                      ║
╚════ .:: For Android 5.0 + ::. ═══════╝
	"""+E
def a():
        os.system(H+'''pkg update -y && pkg upgrade -y && pkg install unstable-repo -y'''+H)
def b():
	os.system('clear')
	soal = input("The Metasploit-Framework installation will begin, continued [y/n] ?")
	if soal == 'y':
	    os.system(H+'''curl -LO https://github.com/termux/termux-packages/files/3995119/metasploit_5.0.65-1_all.deb.gz && gunzip metasploit_5.0.65-1_all.deb.gz && dpkg -i metasploit_5.0.65-1_all.deb && apt -f install'''+H)
	else :
	    os.system('clear')
def c():
	os.system('clear')
	soal = input("The Metasploit-Framework installation will begin, continued [y/n] ?")
	if soal == 'y':
	    os.system(H+'''pkg update && pkg upgrade && pkg install git curl wget nmap -y && curl -LO raw.githubusercontent.com/Hax4us/Metasploit_termux/master/metasploit.sh && chmod 777 metasploit.sh && ./metasploit.sh'''+H)
	else :
	    os.system('clear')	
def d():
	os.system('clear')
	soal = input("The Metasploit-Framework installation will begin, continued [y/n] ?")
	if soal == 'y':
	    os.system(H+'''pkg update -y && pkg upgrade -y && pkg install curl wget git -y && git clone github.com/verluchie/termux-metasploit && chmod 777 termux-metasploit/install.sh && sh termux-metasploit/install.sh'''+H)
	else :
	    os.system('clear')
def e():
	os.system('clear')
	soal = input("The Metasploit-Framework installation will begin, continued [y/n] ?")
	if soal == 'y':
	    os.system(H+'''apt update -y && apt upgrade -y && apt install curl -y && curl -LO raw.githubusercontent.com/1Tech-X/Metasploit-4.16.12/master/metasploit.sh && chmod 777 metasploit.sh && sh metasploit.sh'''+H)
	else :
	    os.system('clear')
def f():
    os.system("xdg-open https://www.youtube.com/channel/UCmiZfr9dgRCkwHa_GXSa97A/")
	
def z():
    os.system('clear')
    os.system('exit')
def solution():
    os.system("xdg-open https://www.youtube.com/")
	
def Main_Menu():
	print(head)
	print('\n')
	print(B+'''
 Before installing, make sure that:
 1). Android 5.0 + (For older Androids, click enter for a solution.)
 2). TermuX (Downloaded from Google Play or Play Store)
 3). About 500MB of internal storage (for properly installing Metasploit)

 '''+F+'''Download Metasploit Dari :
 '''+G+'''1]'''+W+''' Original Termux For Android 7.0+
 '''+G+'''2]'''+W+''' Original Termux For Android 5.0 - 6.0
 '''+G+'''3]'''+W+''' Gitub :
       '''+G+'''31'''+W+''' : Hax4Us
       '''+G+'''32'''+W+''' : V3rluchies
       '''+G+'''33'''+W+''' : Tech-X3s
	   
 '''+G+'''4]'''+W+''' For android 5.0- :
	  
 0] EXIT
  	'''+W+'''-------------------\n'''+E)
	try:
		v = input('Type according to number ⫸ ')
	except:
		print(' Good by Bro ')
		exit()
	
	if v == '':
		solution()
	elif int(v) == 0:
		z()
	elif int(v) == 1:
		a()
	elif int(v) == 2:
		b()
	elif int(v) == 31:
		c()
	elif int(v) == 32:
		d()
	elif int(v) == 33:
		e()
	elif int(v) == 4:
		f()
	else:
		print(F+'[!]'+' Sorry Bro, Invalid input '+E)
		os.system('clear')
		os.system('python setup.py')
heads()
Main_Menu()

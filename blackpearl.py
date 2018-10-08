import os
import sys
from termcolor import cprint
import getpass
import time
import builtwith
import shodan
import socket



def clear():
    try:
        os.system("clear")
    except:
        os.system("cls")

def scanfile():
    try:
        clear()
        print "If output is (1,'Example mal') it means its a virus, if is 0 its not!"
        askfile = str(raw_input("Enter the file which you want to scan?: "))
        import pyclamav
        print pyclamav.scanfile(askfile)
        raw_input("Press Enter")
        mains()
    except:
        print ValueError
        mains()


def dirbrute():
    try:
        clear()
        import Modules.dir_brute
        print " "
        raw_input("Press Enter")
        mains()
    except:
        mains()


def shodan_scan():
    try:
        clear()
        import Modules.shodans
        print " "
        raw_input("Press Enter")

        mains()
    except:
        mains()

def ftp_brute():
    try:
        clear()
        import Modules.ftps
        print " "
        raw_input("Press Enter")
        mains()
    except:
        mains()

def bs64encode():
    try:
        clear()
        import Modules.encode_decode
        print Modules.encode_decode.encrypt()
        raw_input("Press Enter")

        mains()
    except:
        mains()

def bs64decode():
    try:
        clear()
        import Modules.encode_decode
        print Modules.encode_decode.decrypt()
        raw_input("Press Enter")

        mains()
    except:

        mains()

def whtcode():
    try:
        clear()
        url = str(raw_input("Enter url (DO NOT TYPE HTTP://) : "))
        print builtwith.parse("http://" + url)
        raw_input("Press Enter")
        mains()
    except:
        print ValueError
        mains()


def ipsolv():
   try:
       clear()
       # op = termcolor.cprint("Enter IP/DOMAIN: ", "red")
       ip = str(raw_input("Enter IP/DOMAIN: "))
       print socket.gethostbyaddr(ip)
       print socket.gethostbyname(ip)
       raw_input("Press Enter")
       mains()
   except:
       print ValueError
       mains()

def portscan():
    try:
        clear()
        import Modules.pyscan
        raw_input("Press Enter to Exit")
        mains()
    except:
        print "[-]Error Importing Module"

def gmailb():
    try:
        clear()
        import  Modules.gm41l
        raw_input("Press Enter to exit")
        mains()
    except:
        mains()

def yahoo():
    try:
        clear()
        import Modules.y4h00
        raw_input("Press Enter")
        mains()
    except:
        mains()

def zipcrack():
    try:
        clear()
        import Modules.z1pcrack
        raw_input("Press Enter")
        mains()
    except:
        mains()



def mains():
    main_banner = """
    ____  __           __   ____                  __
   / __ )/ /___ ______/ /__/ __ \___  ____ ______/ /
  / __  / / __ `/ ___/ //_/ /_/ / _ \/ __ `/ ___/ / 
 / /_/ / / /_/ / /__/ ,< / ____/  __/ /_/ / /  / /  
/_____/_/\__,_/\___/_/|_/_/    \___/\__,_/_/  /_/   

Coded by Whoami - BCS
Version: 2.0"""

    cprint(main_banner, 'blue')
    number_list = """
    1] Web Directory Bruteforce
    2] Check Website CMS and Technologies
    3] Shodan Scan
    4] FTP Bruteforce
    5] IP/DOMAIN Resolver
    6] Base64 Text Encoder
    7] Base64 Text Decoder
    8] Scan File with ClamAV
    9] Python Port Scanner
    10] Gmail SMTP BruteForce
    11] Yahoo SMTP BruteForce
    12] Zip Cracker
    99] Exit
        """
    cprint(number_list, 'blue')
    snm = raw_input("black@pearl:~$ ")

    if snm == "1":
        dirbrute()
    elif snm == "2":
        whtcode()
    elif snm == "3":
        shodan_scan()
    elif snm == "4":
        ftp_brute()
    elif snm == "5":
        ipsolv()
    elif snm == "6":
        bs64encode()
    elif snm == "7":
        bs64decode()
    elif snm == "8":
        scanfile()
    elif snm == "99":
        sys.exit()
    elif snm == "exit":
        sys.exit()
    elif snm == "9":
        portscan()
    elif snm == "10":
        gmailb()
    elif snm == "11":
        yahoo()
    elif snm == "12":
        zipcrack()
    else:
        mains()






mains()



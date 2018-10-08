import zipfile
import time
print """
################################
##    CoDeD By Whoamii        ##
##    Zip Password cracker    ##
##    Version: 1.0            ##
##    Hack the World          ##
##    Bruteforce tool         ##
################################
"""
print time.sleep(1)
ask = str(raw_input("Enter the tha name of 'zip' file (the zip file need to be in same folder where zipcrack.py is!): "))
print time.sleep(1)
zipFile = zipfile.ZipFile(ask)
enter = raw_input("Enter the password list: ")
passFile = open(enter, 'r')
for line in passFile.readlines():
    password = line.strip('\n')
    try:
        zipFile.extractall(pwd=password)
        print "[+]Password = " + password + '\n'
        exit(0)
    except Exception, e:
        print "[-]Password",password,'is wrong!'

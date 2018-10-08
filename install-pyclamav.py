import os
import termcolor

print termcolor.cprint("MUST BE ROOT TO RUN THIS SCRIPT!", "red")


os.system("apt-get install python-pyclamav")

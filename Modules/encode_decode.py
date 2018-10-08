import base64
import sys
import os



def encrypt():
    code = raw_input("Enter: ")

    answ = code.encode('base64', 'strict')
    print answ


def decrypt():
    smp = raw_input("Enter: ")
    ans = smp.decode('base64','strict')
    print ans


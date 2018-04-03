#!/usr/bin/env python

__copyright__ = "Copyright 2015, Moscow Exchange"
__author__ =    "Nikolay Viskov"
__email__ =     "help@moex.com"


import sys
import os
try:
    import configparser
except ImportError:
    import ConfigParser as configparser
        

sys.path.append('./cfg')


from client import Client
from schema import *

import time
import datetime


def settings():
    global ip_main
    global port_main
    global login
    global securityid
    global price
    global account_1
                    
    path = "settings.ini"
    config = configparser.ConfigParser()
    config.read(path)
    ip_main = config.get("Settings", "ip_main")
    port_main = config.get("Settings", "port_main")
    login = config.get("Settings", "login")
    securityid = config.get("Settings", "securityid")
    price = config.get("Settings", "price")
    account_1 = config.get("Settings", "account_1")
                                                    
                                                    
settings()
                                                    

print ("{0:^100}".format("EstablishmentReject_1") + "\n")


c = Client()

c.connect(str(ip_main),int(port_main))

e = Establish()

e.populate("Timestamp", 1454056522056416880)
e.populate("KeepaliveInterval", 6000)
e.populate("Credentials", str(login))

#print datetime.datetime.now()

#print time.strftime("%d.%m.%Y %H:%M:%S")
print str(datetime.datetime.now()) +" OUT: "+ str(e.deserialize(e.serialize()))

c.send(e)

time.sleep(1)

def on(message):
    print str(datetime.datetime.now()) +" IN: "+ str(message)
    if ("EstablishmentAck(blockLength=20, templateId=5001, schemaId=19781, version=1" in str(message)):
        print("\n" + "TEST 1 OK")
    else:
        print("\n" + "TEST 1 FAIL")
                            
                            
c.check(on)

print("\n")


c2 = Client()

c2.connect(str(ip_main),int(port_main))

e2 = Establish()

e2.populate("Timestamp", 1454056522056416880)
e2.populate("KeepaliveInterval", 6000)
e2.populate("Credentials", str(login))

#print datetime.datetime.now()

#print time.strftime("%d.%m.%Y %H:%M:%S")
print str(datetime.datetime.now()) +" OUT: "+ str(e2.deserialize(e2.serialize()))

c2.send(e2)

time.sleep(1)

def on(message):
    print str(datetime.datetime.now()) +" IN: "+ str(message)
    if ("EstablishmentReject(blockLength=9, templateId=5002, schemaId=19781, version=1, RequestTimestamp=1454056522056416880, EstablishmentRejectCode=1)" == str(message)):
        print("\n" + "TEST 2 OK")
    else:
        print("\n" + "TEST 2 FAIL")

c2.check(on)
print("\n")
                                                        
                            
                            
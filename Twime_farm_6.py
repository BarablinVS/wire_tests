#!/usr/bin/env python

__copyright__ = "Copyright 2015, Moscow Exchange"
__author__ =    "Nikolay Viskov"
__email__ =     "help@moex.com"


import sys

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
    global ip_reserve
    global port_main
    global port_reserve 
    global login
    global account_2
    global securityid
    global multileg_securityid
    global multileg_price
    global multileg_sec1
    global multileg_sec2
    global price
    global account_1

    path = "settings.ini"
    config = configparser.ConfigParser()
    config.read(path)
    ip_main = config.get("Settings", "ip_main")
    port_main = config.get("Settings", "port_main")
    ip_reserve = config.get("Settings", "ip_reserve")
    port_reserve = config.get("Settings", "port_reserve")    
    login = config.get("Settings", "login")
    multileg_securityid = config.get("Settings", "multileg_securityid")
    multileg_sec1 = config.get("Settings", "multileg_sec1")
    multileg_sec2 = config.get("Settings", "multileg_sec2")
    multileg_price = config.get("Settings", "multileg_price")
    securityid = config.get("Settings", "securityid")
    price = config.get("Settings", "price")
    account_1 = config.get("Settings", "account_1")
    account_2 = config.get("Settings", "account_2")

settings()



print ("{0:^100}".format("EstablishmentReject_1") + "\n")


c = Client()
c2 = Client()



c.connect(str(ip_main),int(port_main))
c2.connect(str(ip_reserve),int(port_reserve))


e = Establish()
e2 = Establish()



e.populate("Timestamp", 1454056522056416880)
e2.populate("Timestamp", 1454056522056416880)

e.populate("KeepaliveInterval", 6000)
e2.populate("KeepaliveInterval", 6000)
e.populate("Credentials", str(login))
e2.populate("Credentials",str(login))


term = Terminate()
term.populate("TerminationCode",0)


print("\n" + str(ip_main) +":" + port_main)
print str(datetime.datetime.now()) +" OUT: "+ str(e.deserialize(e.serialize()))

c.send(e)

time.sleep(1)


print("\n" + str(ip_reserve) +":" + port_reserve)
print str(datetime.datetime.now()) +" OUT: "+ str(e2.deserialize(e2.serialize()))

c2.send(e2)

print("\n" + str(ip_main) +":" + port_main)
print str(datetime.datetime.now()) +" OUT: "+ str(term.deserialize(term.serialize()))
c.send(term)


time.sleep(1)

def on(message):
    print("\n" + str(ip_main) +":" + port_main)
    print str(datetime.datetime.now()) +" IN: "+ str(message)
    if ("EstablishmentAck(blockLength=20, templateId=5001, schemaId=19781, version=1" in str(message)):
        print("\n" + "TEST 1 OK")
    elif ("Terminate(blockLength=1, templateId=5003, schemaId=19781, version=1, TerminationCode=0)" in str(message)):
        print("\n" + "TEST 2 OK")
    else:    
        print("\n" + "TEST FAIL")
        
                            
                            
c.check(on)

print("\n")



def on(message):
    print("\n" + str(ip_reserve) +":" + port_reserve)
    print str(datetime.datetime.now()) +" IN: "+ str(message)
    if ("EstablishmentReject(blockLength=9, templateId=5002, schemaId=19781, version=1, RequestTimestamp=1454056522056416880, EstablishmentRejectCode=1)" == str(message)):
        print("\n" + "TEST 3 OK")
    else:
        print("\n" + "TEST 3 FAIL")

c2.check(on)
print("\n")
                                                        
                            
                            

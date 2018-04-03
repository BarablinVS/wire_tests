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
import socket
import subprocess

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
                                                            

print ("{0:^100}".format("FloodReject") + "\n")


c = Client()

c.connect(str(ip_main),int(port_main))

e = Establish()

e.populate("Timestamp", 1454056522056416880)
e.populate("KeepaliveInterval", 60000)
e.populate("Credentials", str(login))


print str(datetime.datetime.now()) +" OUT: "+ str(e.deserialize(e.serialize()))

c.send(e)

#time.sleep(0.01)

def on(message):
    print str(datetime.datetime.now()) +" IN: "+ str(message)
    if ("EstablishmentAck(blockLength=20, templateId=5001, schemaId=19781, version=1, RequestTimestamp=1454056522056416880, KeepaliveInterval=60000" in str(message)):
        print("\n" + "TEST 1 OK")
    else:
        print("\n" + "TEST 1 FAIL")
c.check(on)


def send(i=1,n=0):


    while i < 22:
        nos = NewOrderSingle()
        nos.populate("ClOrdID", i)
        nos.populate("Account", account_1)
        nos.populate("Price",int(price + "00000"))
        nos.populate("OrderQty", i)
        nos.populate("Side",1)
        nos.populate("TimeInForce",3)
        nos.populate("SecurityID", int(securityid))
        nos.populate("ExpireDate",18446744073709551615)
        nos.populate("CheckLimit",1)
        nos.populate("ClOrdLinkID", i)
        i += 1
                                                                                                    
                                                                                                    
        print str(datetime.datetime.now()) +" OUT: "+ str(nos.deserialize(nos.serialize()))
                                                                                                            
        c.send(nos)
        time.sleep(0.02)
        n += 1
        
        def on(message):
            print str(datetime.datetime.now()) +" IN: "+ str(message)
            if (n == 21) and ("FloodReject(blockLength=16, templateId=5007, schemaId=19781, version=1, ClOrdID=21, QueueSize=21, PenaltyRemain=" in str(message)):
                print("\n" + "TEST 2 OK")
            elif (n != 21):
                pass
            else:
                print("\n" + "TEST 2 FAIL")
        c.check(on)           
                        
send()
print("\n")


#def on(message):
    
    
#    print str(datetime.datetime.now()) +" IN: "+ str(message)
#    if ("FloodReject(blockLength=16, templateId=5007, schemaId=19781, version=1, ClOrdID=21, QueueSize=21, PenaltyRemain=" in str(message)):
#        print("\n" + "TEST 2 OK")
#    elif (n != 21):
#        pass    
#    else:
#        print("\n" + "TEST 2 FAIL")                
#c.check(on)
        
#print("\n")
                   
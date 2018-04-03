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
    global port_main
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


print ("{0:^100}".format("SessionReject_5_TimeInForce") + "\n")


c = Client()

c.connect(str(ip_main),int(port_main))

e = Establish()

e.populate("Timestamp", 1454056522056416880)
e.populate("KeepaliveInterval", 60000)
e.populate("Credentials", str(login))


print str(datetime.datetime.now()) +" OUT: "+ str(e.deserialize(e.serialize()))

c.send(e)

time.sleep(1)

def on(message):
    print str(datetime.datetime.now()) +" IN: "+ str(message)
    if ("EstablishmentAck(blockLength=20, templateId=5001, schemaId=19781, version=1, RequestTimestamp=1454056522056416880, KeepaliveInterval=60000" in str(message)):
        print("\n" + "TEST 1 OK")
    else:
        print("\n" + "TEST 1 FAIL")
                          
c.check(on)
                           
def send(i=1):

    while i < 2:
        nos = NewOrderSingle()
        nos.populate("ClOrdID", i)
        nos.populate("Account", account_2)
        nos.populate("Price", int(price + "00000"))
        nos.populate("OrderQty", i)
        nos.populate("Side",1)
        nos.populate("TimeInForce",9)
        nos.populate("SecurityID", int(securityid))
        nos.populate("ExpireDate",18446744073709551615)
        nos.populate("CheckLimit",1)
        nos.populate("ClOrdLinkID", i)
        i += 1
                                                                
        print str(datetime.datetime.now()) +" OUT: "+ str(nos.deserialize(nos.serialize()))
                                                                                                        
        c.send(nos)
        time.sleep(0.02)


        def on(message):
            print str(datetime.datetime.now()) +" IN: "+ str(message)
            if ("SessionReject(blockLength=13, templateId=5008, schemaId=19781, version=1, ClOrdID=1, RefTagID=59, SessionRejectReason=5)" == str(message)):
                print("\n" + "TEST 2 OK")
            else:
                print("\n" + "TEST 2 FAIL")
                    
    
        c.check(on)
                                                                                                                                                                                          
send()

print("\n")                          

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


print ("{0:^100}".format("MassCancelRequest") + "\n")


c = Client()

c.connect(str(ip_main),int(port_main))

e = Establish()

e.populate("Timestamp", 1454056522056416880)
e.populate("KeepaliveInterval", 60000)
e.populate("Credentials", str(login))

#print datetime.datetime.now()

#print time.strftime("%d.%m.%Y %H:%M:%S")
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



omc = OrderMassCancelRequest()

omc.populate("ClOrdID", 105)
omc.populate("Side", 89)
omc.populate("ClOrdLinkID", 0)
omc.populate("Account", 'FU01%%%')
omc.populate("SecurityGroup", '')
omc.populate("SecurityType", 0)
omc.populate("SecurityID", 2147483647)



print str(datetime.datetime.now()) +" OUT: "+ str(omc.deserialize(omc.serialize()))

c.send(omc)

time.sleep(1)

def on(message):
    print str(datetime.datetime.now()) +" IN: "+ str(message)

c.check(on)
    

                            

def send(i=1,n=0):
                            

    while i < 6:
        nos = NewOrderSingle()
        nos.populate("ClOrdID", i)
        nos.populate("Account", account_1)
        nos.populate("Price",int(price + "00000"))
        nos.populate("OrderQty", i)
        nos.populate("Side",2)
        nos.populate("TimeInForce",0)
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
            if (n == 1) and ("NewOrderSingleResponse(blockLength=65, templateId=7000, schemaId=19781, version=1, ClOrdID=1" in  str(message)) and ("ClOrdLinkID=1, Side=2" in str(message)):
                print("\n" + "TEST 2 OK")
            elif (n == 2) and ("NewOrderSingleResponse(blockLength=65, templateId=7000, schemaId=19781, version=1, ClOrdID=2" in  str(message)) and ("ClOrdLinkID=2, Side=2" in str(message)):
                print("\n" + "TEST 3 OK")
            elif (n == 3) and ("NewOrderSingleResponse(blockLength=65, templateId=7000, schemaId=19781, version=1, ClOrdID=3" in  str(message)) and ("ClOrdLinkID=3, Side=2" in str(message)):
                print("\n" + "TEST 4 OK")
            elif (n == 4) and ("NewOrderSingleResponse(blockLength=65, templateId=7000, schemaId=19781, version=1, ClOrdID=4" in  str(message)) and ("ClOrdLinkID=4, Side=2" in str(message)):
                print("\n" + "TEST 5 OK")
            elif (n == 5) and ("NewOrderSingleResponse(blockLength=65, templateId=7000, schemaId=19781, version=1, ClOrdID=5" in  str(message)) and ("ClOrdLinkID=5, Side=2" in str(message)):
                print("\n" + "TEST 6 OK")
            else:
                print("\n" + "TEST FAIL")
                         
                                      
                        
        c.check(on)

send()




omc = OrderMassCancelRequest()
    
omc.populate("ClOrdID", 105)
omc.populate("Side", 89)
omc.populate("Account", 'FU01%%%')
omc.populate("SecurityGroup", '')
omc.populate("SecurityType", 0)
omc.populate("SecurityID", 2147483647)
    
    
    
print str(datetime.datetime.now()) +" OUT: "+ str(omc.deserialize(omc.serialize()))
    
c.send(omc)
    
time.sleep(1)

n = 0    
def on(message):
    global n
    n = n + 1
    print str(datetime.datetime.now()) +" IN: "+ str(message)
    if (n == 1) and ("OrderCancelResponse(blockLength=44, templateId=7003, schemaId=19781, version=1, ClOrdID=1" in  str(message)) and ("ClOrdLinkID=1" in str(message)) and ("OrderQty=1"in str(message)):
        print("\n" + "TEST 7 OK")
    elif (n == 2) and ("OrderCancelResponse(blockLength=44, templateId=7003, schemaId=19781, version=1, ClOrdID=2" in  str(message)) and ("ClOrdLinkID=2" in str(message)) and ("OrderQty=2"in str(message)):
        print("\n" + "TEST 8 OK")
        
    elif (n == 3) and ("OrderCancelResponse(blockLength=44, templateId=7003, schemaId=19781, version=1, ClOrdID=3" in  str(message)) and ("ClOrdLinkID=3" in str(message)) and ("OrderQty=3"in str(message)):
        print("\n" + "TEST 9 OK")
    elif (n == 4) and ("OrderCancelResponse(blockLength=44, templateId=7003, schemaId=19781, version=1, ClOrdID=4" in  str(message)) and ("ClOrdLinkID=4" in str(message)) and ("OrderQty=4"in str(message)):
        print("\n" + "TEST 10 OK")
    elif (n == 5) and ("OrderCancelResponse(blockLength=44, templateId=7003, schemaId=19781, version=1, ClOrdID=5" in  str(message)) and ("ClOrdLinkID=5" in str(message)) and ("OrderQty=5"in str(message)):
        print("\n" + "TEST 11 OK")
    elif (n == 6) and ("OrderMassCancelResponse(blockLength=24, templateId=7007, schemaId=19781, version=1, ClOrdID=105" in str(message)) and (" TotalAffectedOrders=5, OrdRejReason=0" in str(message)):
        print("\n" + "TEST 12 OK")
    else:
        print("\n" + "TEST FAIL")
                 
        
            
        
c.check(on)
        
print("\n")                                                                                                                            
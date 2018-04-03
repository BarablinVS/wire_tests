#!/usr/bin/env python

__copyright__ = "Copyright 2015, Moscow Exchange"
__author__ =    "Nikolay Viskov"
__email__ =     "help@moex.com"

import sys
import string


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


print ("{0:^100}".format("Terminate_9") + "\n")


c = Client()
c.connect(str(ip_main),int(port_main))

e = Establish()

e.populate("Timestamp", 1454056522056416880)
e.populate("KeepaliveInterval", 5000)
e.populate("Credentials", str(login))


print str(datetime.datetime.now()) +" OUT: "+ str(e.deserialize(e.serialize()))

c.send(e)

time.sleep(1)

def on(message):
    print str(datetime.datetime.now()) +" IN: "+ str(message)
    if ("EstablishmentAck(blockLength=20, templateId=5001, schemaId=19781, version=1, RequestTimestamp=1454056522056416880, KeepaliveInterval=5000, NextSeqNo=" in str(message)):
        print ("\n" + "TEST 1 OK")
        
    else:
        print("\n" + "TEST 1 FAIL")
        
                            
                            
c.check(on)



seq = Sequence()
seq.populate("NextSeqNo",2)

print str(datetime.datetime.now()) +" OUT: "+ str(seq.deserialize(seq.serialize()))
c.send(seq)


#def on(message):
#    print str(datetime.datetime.now()) +" IN: "+ str(message)
#    if ("Sequence(blockLength=8, templateId=5006, schemaId=19781, version=1, NextSeqNo=" in str(message)):
#        print("TEST 2 OK")
            
#    else:
#        print("TEST 2 FAIL")
        
#c.check(on)

def on(message):
    print str(datetime.datetime.now()) +" IN: "+ str(message)
    if ("Terminate(blockLength=1, templateId=5003, schemaId=19781, version=1, TerminationCode=9)" == str(message)):
        print("\n" + "TEST 2 OK")
    else:
        print("\n" + "TEST 2 FAIL")
c.check(on)
                            



#seq2 = Sequence()
#seq2.populate("NextSeqNo",1)

#print str(datetime.datetime.now()) +" OUT: "+ str(seq2.deserialize(seq2.serialize()))
#c.send(seq2)


#def on(message):
#    print str(datetime.datetime.now()) +" IN: "+ str(message)
#    if ("Terminate(blockLength=1, templateId=5003, schemaId=19781, version=1, TerminationCode=9)" == str(message)):
#        print("\n" + "TEST 3 OK")
#    else:
#        print("\n" + "TEST 3 FAIL")
        
                    
#c.check(on)


print ("\n")
                            
                            
                            
                            

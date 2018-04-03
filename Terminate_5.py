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
import socket
import subprocess

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



print ("{0:^100}".format("Terminate_5") + "\n")




#cmd = "cd /app/fusion/wire_gate/scripts;./EOD.sh;./start_new.sh"
#process = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
#temp = process.communicate()[0]

#time.sleep(10)




c = Client()

c.connect("127.0.0.1",2222)

e = Establish()

e.populate("Timestamp", 1454056522056416880)
e.populate("KeepaliveInterval", 60000)
e.populate("Credentials", 'FIXADAPTER_BF')


print str(datetime.datetime.now()) +" OUT: "+ str(e.deserialize(e.serialize()))

c.send(e)

time.sleep(1)

#def on(message):
#    print str(datetime.datetime.now()) +" IN: "+ str(message)
#    if ("EstablishmentAck(blockLength=20, templateId=5001, schemaId=19781, version=1, RequestTimestamp=1454056522056416880, KeepaliveInterval=60000" in str(message)):
#        print("TEST OK")
#    else:
#        print("TEST FAIL")
#c.check(on)


def send(i=1):

    try:
        while i < 150:
            nos = NewOrderSingle()
            nos.populate("ClOrdID", i)
            nos.populate("Account", '6001005')
            nos.populate("Price",98000000)
            nos.populate("OrderQty", i)
            nos.populate("Side",1)
            nos.populate("TimeInForce",3)
            nos.populate("SecurityID", 230323)
            nos.populate("ExpireDate",18446744073709551615)
            nos.populate("CheckLimit",1)
            nos.populate("ClOrdLinkID", i)
            i += 1
                                                                                                    
                                                                                                    
            print str(datetime.datetime.now()) +" OUT: "+ str(nos.deserialize(nos.serialize()))
                                                                                                            
            c.send(nos)
            time.sleep(1)
    except IOError:
        cmd = "grep 'Terminate user \[FIXADAPTER_BF\] with code \[5\]' /app/fusion/wire_gate/log/wire_log*"
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        temp = process.communicate()[0]
        
        if temp is not None:
            print("\n" + "TEST 1 OK")
            print(temp)
        else:
            print("\n" + "TEST 1 FAIL")
            
#        cmd = "cd /app/fusion/wire_gate/scripts;./EOD.sh;./start.sh"
#        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
#        temp = process.communicate()[0]
                    
        time.sleep(10)
            
send()
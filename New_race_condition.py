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



print ("{0:^100}".format("New_race_condition") + "\n")


#cmd = "cd /app/fusion/wire_gate/scripts;./SOD.sh"
#process = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
#temp = process.communicate()[0]




c = Client()

e = Establish()

e.populate("KeepaliveInterval", 10000)
e.populate("Credentials", str(login))
t = Terminate()

n=0
while n<21:
    try:
        c.connect(str(ip_main),int(port_main))
        c.send(e)
        c.send(t)
        time.sleep(1)
        n=n+1
    except:
        pass
        
k=0
while k<6:
    c.connect(str(ip_main),int(port_main))
    c.send(e)
    print str(datetime.datetime.now()) +" OUT: "+ str(e.deserialize(e.serialize()))     
    time.sleep(1)
    def on(message):
        print str(datetime.datetime.now()) +" IN: "+ str(message)
    c.check(on)
                 

    nos = NewOrderSingle()
    nos.populate("ClOrdID", k)
    nos.populate("Account", account_2)
    nos.populate("Price", int(price + "00000"))
    nos.populate("OrderQty", 1)
    nos.populate("Side",1)
    nos.populate("TimeInForce",3)
    nos.populate("SecurityID", int(securityid))
    nos.populate("ExpireDate",18446744073709551615)
    nos.populate("CheckLimit",1)
    nos.populate("ClOrdLinkID", 1)
    
    print str(datetime.datetime.now()) +" OUT: "+ str(nos.deserialize(nos.serialize()))
    
    c.send(nos)

    time.sleep(1)
                                                                                                                            
                                                                                                                            
    def on(message):
        print str(datetime.datetime.now()) +" IN: "+ str(message)
    c.check(on)
    time.sleep(1)

    c.send(t)
    print str(datetime.datetime.now()) +" OUT: "+ str(t.deserialize(t.serialize()))
    
    
    def on(message):
        print str(datetime.datetime.now()) +" IN: "+ str(message)
    c.check(on)
    
    k=k+1
    
    print ('\n')
                                                                                                                                                        
 
time.sleep(10)         
        
        
#cmd = "cd /app/fusion/wire_gate/scripts;./EOD.sh"
#process = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
#temp = process.communicate()[0]                           

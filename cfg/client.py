#!/usr/bin/env python

__copyright__ = "Copyright 2015, Moscow Exchange"
__author__ =    "Nikolay Viskov"
__email__ =     "help@moex.com"

import socket
import struct

from serializer import Serializer

class Client(object):

    def __init__(self):
        pass

    def connect(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket()
        self.sock.connect((host, port))
#        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 1024)
        self.sock.setblocking(1)

    def send(self, message):
        self.sock.send(message.serialize())

    def close(self):
        self.sock.close()

    def check(self,callback):
#callback
        counter = 0
        
#        message = ''
#        MSGLEN = 20480
#        while len(message) < MSGLEN:
#            chunk = self.sock.recv(MSGLEN-len(message))
#            if chunk == '':
#                raise RuntimeError("socket connection broken")
#            message = message + chunk
#        return message
         
#        message = self.sock.recv(20480)
        message = self.sock.recv(20240)
        while callback and message and len(message) > counter + 4:
            tag = struct.unpack('<HH', message[counter:counter + 4])[1]
            for subclass in Serializer.__subclasses__():
                if tag == subclass().tag:
                    callback(subclass().deserialize(message[counter:counter + subclass().size]))
                    counter += subclass().size
#        return message


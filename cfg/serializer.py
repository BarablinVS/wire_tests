#!/usr/bin/env python

__copyright__ = "Copyright 2015, Moscow Exchange"
__author__ =    "Nikolay Viskov"
__email__ =     "help@moex.com"

from struct         import Struct
from collections    import namedtuple
from functools      import partial

class Serializer(Struct):

    def __init__(self, tag, fields):
        self.tag    = tag
        self.fields = fields
#        print (tag)
#        print (fields)

        fmt = '<'
        for f in self.fields : fmt += f['fmt']
#        print(fmt)  
        Struct.__init__(self, fmt)

        self.clean()
        self.header()
#        print(self.header())

    def header(self):
        self.populate('blockLength',    (self.size - 8))
        self.populate('templateId',  self.tag)
        self.populate('schemaId', 19781)
        self.populate('version', 1)
        
        
        self.populate('schemaId',       19781)
#        self.populate('schemaId',       1)
        self.populate('version',        1)

    def clean(self):
        self.values = {}
        for f in self.fields:
            if 's' in f['fmt'] :
                self.values[f['name']] = ''
            else :
                self.values[f['name']] = 0
                
    def deserialize(self, data) :
        fields = ''
        for f in self.fields : fields += f['name'] + ' '
        Class = namedtuple(self.__class__.__name__, fields)
        return Class._make(self.unpack(data))

    def serialize(self) :
        handler = self.pack
        for f in self.fields :
            handler = partial(handler, self.values[f['name']])

        return handler()

    def populate(self, name, value):
        field = {}
        for f in self.fields:
            if f['name'] == name:
                field = f

#        if not field:
#            raise Exception("Invalid field [" + name + "]")

        self.values[name] = value

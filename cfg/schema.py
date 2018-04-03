#!/usr/bin/env python

__copyright__ = "Copyright 2015, Moscow Exchange"
__author__ =    "Nikolay Viskov"
__email__ =     "help@moex.com"

from serializer import Serializer

#    <message name="Establish" id="5000">
#            <type name="blockLength"    primitiveType="uint16" />
#            <type name="templateId"     primitiveType="uint16" />
#            <type name="schemaId"       primitiveType="uint16" />
#            <type name="version"        primitiveType="uint16" />
#        <field name="Timestamp"         id="20204" type="TimeStamp" />
#        <field name="KeepaliveInterval" id="20205" type="DeltaMillisecs" />
#        <field name="Credentials"       id="20206" type="String20" />
#    </message>

class Establish(Serializer):

    def __init__(self):
        tag = 5000

        fields = [
            {'name':'blockLength',          'fmt':'H'},
            {'name':'templateId',           'fmt':'H'},
            {'name':'schemaId',             'fmt':'H'},
            {'name':'version',              'fmt':'H'},

            {'name':'Timestamp',            'fmt':'Q'},
            {'name':'KeepaliveInterval',    'fmt':'L'},
            {'name':'Credentials',          'fmt':'20s'}
        ]

        Serializer.__init__(self, tag, fields)

#    <message name="EstablishmentAck" id="5001">
#        <field name="RequestTimestamp"  id="20207" type="TimeStamp" />
#        <field name="KeepaliveInterval" id="20205" type="DeltaMillisecs" />
#        <field name="NextSeqNo"         id="20208" type="UInt64" />
#    </message>

class EstablishmentAck(Serializer):

    def __init__(self):
        tag = 5001

        fields = [
            {'name':'blockLength',          'fmt':'H'},
            {'name':'templateId',           'fmt':'H'},
            {'name':'schemaId',             'fmt':'H'},
            {'name':'version',              'fmt':'H'},

            {'name':'RequestTimestamp',     'fmt':'Q'},
            {'name':'KeepaliveInterval',    'fmt':'L'},
            {'name':'NextSeqNo',            'fmt':'Q'}
        ]

        Serializer.__init__(self, tag, fields)
        
class SystemEvent(Serializer):
    def __init__(self):
        tag = 7011
        
        fields = [
            {'name':'blockLength',          'fmt':'H'},
            {'name':'templateId',           'fmt':'H'},
            {'name':'schemaId',             'fmt':'H'},
            {'name':'version',              'fmt':'H'},
        
            {'name':'Timestamp',            'fmt':'Q'},
            {'name':'TradingSessionID',     'fmt':'i'},
            {'name':'TradSesEvent',         'fmt':'B'}
        
        ]
        
        
        Serializer.__init__(self, tag, fields)
        
        
                                                         


#    <message name="EstablishmentReject" id="5002">
#        <field name="RequestTimestamp"      id="20207" type="TimeStamp" />
#        <field name="EstablishmentRejectCode"   id="20209" type="EstablishmentRejectCodeEnum" />
#    </message>

class EstablishmentReject(Serializer):

    def __init__(self):
        tag = 5002

        fields = [
            {'name':'blockLength',          'fmt':'H'},
            {'name':'templateId',           'fmt':'H'},
            {'name':'schemaId',             'fmt':'H'},
            {'name':'version',              'fmt':'H'},

            {'name':'RequestTimestamp',         'fmt':'Q'},
            {'name':'EstablishmentRejectCode',  'fmt':'B'}
        ]

        Serializer.__init__(self, tag, fields)


#    <message name="Terminate" id="5003">
#        <field name="TerminationCode"   id="20210" type="TerminationCodeEnum" />
#    </message>

class Terminate(Serializer):

    def __init__(self):
        tag = 5003

        fields = [
            {'name':'blockLength',          'fmt':'H'},
            {'name':'templateId',           'fmt':'H'},
            {'name':'schemaId',             'fmt':'H'},
            {'name':'version',              'fmt':'H'},

            {'name':'TerminationCode',      'fmt':'B'}
        ]

        Serializer.__init__(self, tag, fields)

#    <message name="RetransmitRequest" id="5004">
#        <field name="Timestamp"         id="20204"    type="TimeStamp" />
#        <field name="FromSeqNo"         id="20211"    type="UInt64" />
#        <field name="Count"             id="20212"    type="UInt32" />
#    </message> 

class RetransmitRequest(Serializer):

    def __init__(self):
        tag = 5004

        fields = [
            {'name':'blockLength',          'fmt':'H'},
            {'name':'templateId',           'fmt':'H'},
            {'name':'schemaId',             'fmt':'H'},
            {'name':'version',              'fmt':'H'},

            {'name':'Timestamp',            'fmt':'Q'},
            {'name':'FromSeqNo',            'fmt':'Q'},
            {'name':'Count',                'fmt':'I'}
        ]

        Serializer.__init__(self, tag, fields)

#    <message name="Retransmission" id="5005">
#        <field name="NextSeqNo"         id="20208"    type="UInt64" />
#        <field name="RequestTimestamp"  id="20207"    type="TimeStamp" />
#        <field name="Count"             id="20212"    type="UInt32" />
#    </message>

class Retransmission(Serializer):

    def __init__(self):
        tag = 5005

        fields = [
            {'name':'blockLength',          'fmt':'H'},
            {'name':'templateId',           'fmt':'H'},
            {'name':'schemaId',             'fmt':'H'},
            {'name':'version',              'fmt':'H'},

            {'name':'NextSeqNo',            'fmt':'Q'},
            {'name':'RequestTimestamp',     'fmt':'Q'},
            {'name':'Count',                'fmt':'I'}
        ]

        Serializer.__init__(self, tag, fields)

#    <message name="Sequence" id="5006">
#        <field name="NextSeqNo" id="20208"  type="UInt64" />
#    </message>

class Sequence(Serializer):

    def __init__(self):
        tag = 5006

        fields = [
            {'name':'blockLength',          'fmt':'H'},
            {'name':'templateId',           'fmt':'H'},
            {'name':'schemaId',             'fmt':'H'},
            {'name':'version',              'fmt':'H'},

            {'name':'NextSeqNo',            'fmt':'Q'}
        ]

        Serializer.__init__(self, tag, fields)
	
#    <message name="FloodReject" id="5007">
#        <field name="ClOrdID"             id="11"    type="UInt64"/>
#        <field name="QueueSize"           id="20213" type="UInt32"/>
#        <field name="PenaltyRemain"       id="20214" type="UInt32"/>
#    </message>

class FloodReject(Serializer):

    def __init__(self):
        tag = 5007

        fields = [
            {'name':'blockLength',          'fmt':'H'},
            {'name':'templateId',           'fmt':'H'},
            {'name':'schemaId',             'fmt':'H'},
            {'name':'version',              'fmt':'H'},

            {'name':'ClOrdID',              'fmt':'Q'},
            {'name':'QueueSize',            'fmt':'I'},
            {'name':'PenaltyRemain',        'fmt':'I'}
        ]

        Serializer.__init__(self, tag, fields)


#    <message name="SessionReject" id="5008">
#        <field name="ClOrdID"             id="11"     type="UInt64"/>
#        <field name="RefTagID"            id="371"    type="UInt32"/>
#        <field name="SessionRejectReason" id="373"    type="SessionRejectReasonEnum"/>
#    </message>

class SessionReject(Serializer):

    def __init__(self):
        tag = 5008

        fields = [
            {'name':'blockLength',          'fmt':'H'},
            {'name':'templateId',           'fmt':'H'},
            {'name':'schemaId',             'fmt':'H'},
            {'name':'version',              'fmt':'H'},

            {'name':'ClOrdID',              'fmt':'Q'},
            {'name':'RefTagID',             'fmt':'I'},
            {'name':'SessionRejectReason',  'fmt':'B'}
        ]

        Serializer.__init__(self, tag, fields)

#    <message name="NewOrderSingle" id="6000" spectra_name="AddOrderLegacy">
#        <field name="ClOrdID"             id="11"    type="UInt64"           spectra_name="fix_client_operation_id"/>
#        <field name="ExpireDate"          id="432"   type="TimeStamp"        spectra_name="StrDateExp"/>
#        <field name="Price"               id="44"    type="Decimal5"         spectra_name="StrPrice"/>
#        <field name="SecurityID"          id="48"    type="Int32"            spectra_name=""/>
#        <field name="OrderQty"            id="38"    type="UInt32"           spectra_name="Amount"/>
#        <field name="TimeInForce"         id="59"  [M 8  type="TimeInForceEnum"  spectra_name="CotirContr"/>
#        <field name="Side"                id="54"    type="SideEnum"         spectra_name="OrderType"/>
#        <field name="CheckLimit"          id="20217" type="CheckLimitEnum"   spectra_name="is_check_limit"/>
#        <field name="Account"             id="1"     type="String7"          spectra_name="BrokerCode,ClientCode"/>
#    </message>



class NewOrderSingle(Serializer):

    def __init__(self):
        tag = 6000

        fields = [
            {'name':'blockLength',          'fmt':'H'},
            {'name':'templateId',           'fmt':'H'},
            {'name':'schemaId',             'fmt':'H'},
            {'name':'version',              'fmt':'H'},

            {'name':'ClOrdID',              'fmt':'Q'},
            {'name':'ExpireDate',           'fmt':'Q'},
            {'name':'Price',                'fmt':'q'},
            {'name':'SecurityID',           'fmt':'i'},
            {'name':'ClOrdLinkID',          'fmt':'i'},
            {'name':'OrderQty',             'fmt':'I'},
            {'name':'TimeInForce',          'fmt':'B'},
            {'name':'Side',                 'fmt':'B'},
#            {'name':'Side1',                 'fmt':'B'},
            {'name':'CheckLimit',           'fmt':'B'},
            {'name':'Account',              'fmt':'7s'}
        ]

        Serializer.__init__(self, tag, fields)


#    <message name="NewOrderSingleResponse" id="7000" spectra_name="AddOrderSingleSuper">
#        <field name="ClOrdID"             id="11"    type="UInt64"           spectra_name="fix_client_operation_id"/>
#        <field name="Timestamp"           id="20204" type="TimeStamp"        spectra_name="server_time"/>
#        <field name="ExpireDate"          id="432"   type="TimeStamp"        spectra_name="date_exp"/>
#        <field name="OrderID"             id="37"    type="Int64"            spectra_name="order_id"/>
#        <field name="Flags"               id="20215" type="Int64"            spectra_name="flags"/>
#        <field name="Price"               id="44"    type="Decimal5"         spectra_name="price"/>
#        <field name="SecurityID"          id="48"    type="Int32"            spectra_name="legacy_isin_id"/>
#        <field name="OrderQty"            id="38"    type="UInt32"           spectra_name="abs(amount)"/>
#        <field name="TradingSessionID"    id="336"   type="Int32"            spectra_name="sess_id"/>
#        <field name="Side"                id="54"    type="SideEnum"         spectra_name="amount"/>
#    </message>

class NewOrderSingleResponse(Serializer):

    def __init__(self):
        tag = 7000

        fields = [
            {'name':'blockLength',          'fmt':'H'},
            {'name':'templateId',           'fmt':'H'},
            {'name':'schemaId',             'fmt':'H'},
            {'name':'version',              'fmt':'H'},

            {'name':'ClOrdID',              'fmt':'Q'},
            {'name':'Timestamp',            'fmt':'Q'},
            {'name':'ExpireDate',           'fmt':'Q'},
            {'name':'OrderID',              'fmt':'q'},
            {'name':'Flags',                'fmt':'q'},
            {'name':'Price',                'fmt':'q'},
            {'name':'SecurityID',           'fmt':'i'},
            {'name':'OrderQty',             'fmt':'I'},
            {'name':'TradingSessionID',     'fmt':'i'},
            {'name':'ClOrdLinkID',          'fmt':'i'},
            {'name':'Side',                 'fmt':'B'}
        ]

        Serializer.__init__(self, tag, fields)

#    <message name="NewOrderReject" id="7002" spectra_name="P2ReportAddSuper">
#        <field name="ClOrdID"             id="11"    type="UInt64"           spectra_name="fix_client_operation_id"/>
#        <field name="Timestamp"           id="20204" type="TimeStamp"        spectra_name="server_time"/>
#        <field name="OrdRejReason"        id="103"   type="Int32"            spectra_name="reply_code"/>
#    </message>

class NewOrderReject(Serializer):

    def __init__(self):
        tag = 7002

        fields = [
            {'name':'blockLength',          'fmt':'H'},
            {'name':'templateId',           'fmt':'H'},
            {'name':'schemaId',             'fmt':'H'},
            {'name':'version',              'fmt':'H'},

            {'name':'ClOrdID',              'fmt':'Q'},
            {'name':'Timestamp',            'fmt':'Q'},
            {'name':'OrdRejReason',         'fmt':'i'}
        ]

        Serializer.__init__(self, tag, fields)


#    <message name="OrderCancelResponse" id="7003" spectra_name="CancelOrderSuper">
#        <field name="ClOrdID"             id="11"    type="UInt64"           spectra_name="fix_client_operation_id"/>
#        <field name="Timestamp"           id="20204" type="TimeStamp"        spectra_name="server_time"/>
#        <field name="OrderID"             id="37"    type="Int64"            spectra_name="order_id"/>
#        <field name="Flags"               id="20215" type="Int64"            spectra_name="flags"/>
#        <field name="OrderQty"            id="38"    type="UInt32"           spectra_name="abs(amount)"/>
#        <field name="TradingSessionID"    id="336"   type="Int32"            spectra_name="sess_id"/>
#    </message>


class NewOrderMultileg(Serializer):

    def __init__(self):
        tag = 6001
        
        fields = [
            {'name':'blockLength',          'fmt':'H'},
            {'name':'templateId',           'fmt':'H'},
            {'name':'schemaId',             'fmt':'H'},
            {'name':'version',              'fmt':'H'},
                                                                    
            {'name':'ClOrdID',              'fmt':'Q'},
            {'name':'ExpireDate',           'fmt':'Q'},
            {'name':'Price',                'fmt':'q'},
            {'name':'SecurityID',           'fmt':'i'},
            {'name':'ClOrdLinkID',          'fmt':'i'},
            {'name':'OrderQty',             'fmt':'I'},
            {'name':'TimeInForce',          'fmt':'B'},
            {'name':'Side',                 'fmt':'B'},
            {'name':'Account',              'fmt':'7s'}
        ]
                                                                                                                                                                                        
        Serializer.__init__(self, tag, fields)
        
class NewOrderMultilegResponse(Serializer):

    def __init__(self):
        tag = 7001
            
        fields = [
            {'name':'blockLength',          'fmt':'H'},
            {'name':'templateId',           'fmt':'H'},
            {'name':'schemaId',             'fmt':'H'},
            {'name':'version',              'fmt':'H'},
                                                                    
            {'name':'ClOrdID',              'fmt':'Q'},
            {'name':'Timestamp',            'fmt':'Q'},
            {'name':'ExpireDate',           'fmt':'Q'},
            {'name':'OrderID',              'fmt':'q'},
            {'name':'Flags',                'fmt':'q'},
            {'name':'Price',                'fmt':'q'},
            {'name':'SecurityID',           'fmt':'i'},
            {'name':'OrderQty',             'fmt':'I'},
            {'name':'TradingSessionID',     'fmt':'i'},
            {'name':'ClOrdLinkID',          'fmt':'i'},
            {'name':'Side',                 'fmt':'B'}
        ]
            
        Serializer.__init__(self, tag, fields)
                                                                                                                                                                                                            
class OrderCancelRequest(Serializer):

    def __init__(self):
            tag = 6002
            
            fields = [
                {'name':'blockLength',          'fmt':'H'},
                {'name':'templateId',           'fmt':'H'},
                {'name':'schemaId',             'fmt':'H'},
                {'name':'version',              'fmt':'H'},
                                                                    
                {'name':'ClOrdID',              'fmt':'Q'},
                {'name':'OrderID',              'fmt':'q'},
                {'name':'Account',              'fmt':'7s'}
            ]
                                                                                                                                                    
            Serializer.__init__(self, tag, fields)
            

class OrderCancelResponse(Serializer):

    def __init__(self):
        tag = 7003

        fields = [
            {'name':'blockLength',          'fmt':'H'},
            {'name':'templateId',           'fmt':'H'},
            {'name':'schemaId',             'fmt':'H'},
            {'name':'version',              'fmt':'H'},

            {'name':'ClOrdID',              'fmt':'Q'},
            {'name':'Timestamp',            'fmt':'Q'},
            {'name':'OrderID',              'fmt':'q'},
            {'name':'Flags',                'fmt':'q'}, 
            {'name':'OrderQty',             'fmt':'I'},
            {'name':'TradingSessionID',     'fmt':'i'},
            {'name':'ClOrdLinkID',          'fmt':'i'}
             
        ]

        Serializer.__init__(self, tag, fields)
        
class OrderCancelReject(Serializer):

    def __init__(self):
        tag = 7004
            
        fields = [
            {'name':'blockLength',          'fmt':'H'},
            {'name':'templateId',           'fmt':'H'},
            {'name':'schemaId',             'fmt':'H'},
            {'name':'version',              'fmt':'H'},
                                                                    
            {'name':'ClOrdID',              'fmt':'Q'},
            {'name':'Timestamp',            'fmt':'Q'},
            {'name':'OrdRejReason',         'fmt':'i'}
        ]
                                                                                                                                                    
        Serializer.__init__(self, tag, fields)
        

class OrderReplaceRequest(Serializer):
    def __init__(self):
        tag = 6003
        fields = [
            {'name':'blockLength',          'fmt':'H'},
            {'name':'templateId',           'fmt':'H'},
            {'name':'schemaId',             'fmt':'H'},
            {'name':'version',              'fmt':'H'},
            
            {'name':'ClOrdID',              'fmt':'Q'},
            {'name':'OrderID',              'fmt':'q'},
            {'name':'Price',                'fmt':'q'},
            {'name':'OrderQty',             'fmt':'I'},
            {'name':'ClOrdLinkID',          'fmt':'i'},
            {'name':'Mode',                 'fmt':'B'},
            {'name':'CheckLimit',           'fmt':'B'},
            {'name':'Account',              'fmt':'7s'}
         
        ]
         
        Serializer.__init__(self, tag, fields)
            

class OrderReplaceResponse(Serializer):
    def __init__(self):
        tag = 7005
        fields = [
            {'name':'blockLength',          'fmt':'H'},
            {'name':'templateId',           'fmt':'H'},
            {'name':'schemaId',             'fmt':'H'},
            {'name':'version',              'fmt':'H'},
            
            {'name':'ClOrdID',              'fmt':'Q'},
            {'name':'Timestamp',            'fmt':'Q'},
            {'name':'OrderID',              'fmt':'q'},
            {'name':'PrevOrderID',          'fmt':'q'},
            {'name':'Flags',                'fmt':'q'},
            {'name':'Price',                'fmt':'q'},
            {'name':'OrderQty',             'fmt':'I'},
            {'name':'TradingSessionID',     'fmt':'i'},
            {'name':'ClOrdLinkID',          'fmt':'i'}
             
        ]
        
        Serializer.__init__(self, tag, fields)
        
class OrderReplaceReject(Serializer):
    def __init__(self):
        tag = 7006
        fields = [
            {'name':'blockLength',          'fmt':'H'},
            {'name':'templateId',           'fmt':'H'},
            {'name':'schemaId',             'fmt':'H'},
            {'name':'version',              'fmt':'H'},
             
            {'name':'ClOrdID',              'fmt':'Q'},
            {'name':'Timestamp',            'fmt':'Q'},
            {'name':'OrdRejReason',         'fmt':'i'}
        ]
        
        Serializer.__init__(self, tag, fields)
        
class ExecutionSingleReport(Serializer):
    def __init__(self):
        tag = 7008
        fields = [
            {'name':'blockLength',          'fmt':'H'},
            {'name':'templateId',           'fmt':'H'},
            {'name':'schemaId',             'fmt':'H'},
            {'name':'version',              'fmt':'H'},
                                                                                
            {'name':'ClOrdID',              'fmt':'Q'},
            {'name':'Timestamp',            'fmt':'Q'},
            {'name':'OrderID',              'fmt':'q'},
            {'name':'TrdMatchID',           'fmt':'q'},
            {'name':'Flags',                'fmt':'q'},
            {'name':'LastPx',               'fmt':'q'},
            {'name':'LastQty',              'fmt':'I'},
            {'name':'OrderQty',             'fmt':'I'},
            {'name':'TradingSessionID',     'fmt':'i'},
            {'name':'ClOrdLinkID',          'fmt':'i'},
            {'name':'SecurityID',           'fmt':'i'},
            {'name':'Side',                 'fmt':'B'}
                                   
        ]
                                                                                                
        Serializer.__init__(self, tag, fields)
        
class ExecutionMultilegReport(Serializer):
    def __init__(self):
        tag = 7009
        fields = [
            {'name':'blockLength',          'fmt':'H'},
            {'name':'templateId',           'fmt':'H'},
            {'name':'schemaId',             'fmt':'H'},
            {'name':'version',              'fmt':'H'},
            
            {'name':'ClOrdID',              'fmt':'Q'},
            {'name':'Timestamp',            'fmt':'Q'},
            {'name':'OrderID',              'fmt':'q'},
            {'name':'TrdMatchID',           'fmt':'q'},
            {'name':'Flags',                'fmt':'q'},
            {'name':'LastPx',               'fmt':'q'},
            {'name':'LegPrice',             'fmt':'q'},
            {'name':'LastQty',              'fmt':'I'},
            {'name':'OrderQty',             'fmt':'I'},
            {'name':'TradingSessionID',     'fmt':'i'},
            {'name':'ClOrdLinkID',          'fmt':'i'},
            {'name':'SecurityID',           'fmt':'i'},
            {'name':'Side',                 'fmt':'B'},
            
            
        ]
        
        Serializer.__init__(self, tag, fields)                


class OrderMassCancelRequest(Serializer):
    def __init__(self):
        tag = 6004
        fields = [
            {'name':'blockLength',          'fmt':'H'},
            {'name':'templateId',           'fmt':'H'},
            {'name':'schemaId',             'fmt':'H'},
            {'name':'version',              'fmt':'H'},
                                                                    
            {'name':'ClOrdID',              'fmt':'Q'},
            {'name':'ClOrdLinkID',          'fmt':'i'},
            {'name':'SecurityID',           'fmt':'i'},
            {'name':'SecurityType',         'fmt':'B'},
            {'name':'Side',                 'fmt':'B'},
            {'name':'Account',              'fmt':'7s'},
            {'name':'SecurityGroup',        'fmt':'25s'}
             
        ]
        
        Serializer.__init__(self, tag, fields)
                                                                                                                                                                                                        

class OrderMassCancelResponse(Serializer):
    def __init__(self):
        tag = 7007
        fields = [
            {'name':'blockLength',          'fmt':'H'},
            {'name':'templateId',           'fmt':'H'},
            {'name':'schemaId',             'fmt':'H'},
            {'name':'version',              'fmt':'H'},
                                                                                
            {'name':'ClOrdID',              'fmt':'Q'},
            {'name':'Timestamp',            'fmt':'Q'},
            {'name':'TotalAffectedOrders',  'fmt':'i'},
            {'name':'OrdRejReason',         'fmt':'i'}
        ]
        Serializer.__init__(self, tag, fields)
        
class EmptyBook(Serializer):
    def __init__(self):
        tag = 7010
        fields = [
            {'name':'blockLength',          'fmt':'H'},
            {'name':'templateId',           'fmt':'H'},
            {'name':'schemaId',             'fmt':'H'},
            {'name':'version',              'fmt':'H'},
            
            {'name':'Timestamp',          'fmt':'Q'},
            {'name':'TradingSessionID',   'fmt':'i'},
        ]
        Serializer.__init__(self, tag, fields)
              
                                                                    
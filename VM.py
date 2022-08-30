import urllib
import urllib.parse
import urllib.request
import hashlib
import hmac
import base64
import sys
# sys.path.append('./ServiceOffering')
import urls as key
# from .ServiceOffering import listServiceOfferings as service
import Zone.getZone1ID as zone
import Template.getCentosID as centos
import ServiceOffering.listServiceOfferings as listOffer
# import Zone.listZone

class VM():

    def deployVM(self):
        baseurl=key.baseurl
        apiKey=key.apiKey
        secretkey=key.secretKey
        # serviceofferingId = "6906780f-3625-46ea-86f0-5ed272dc2f73"
        serviceofferingId = listOffer.listServiceOfferings()
        # baseurl='http://10.125.70.28:8080/client/api?'
        request={
            "apiKey": "oCFMurQjw4EX-T7fRQXBCmkbDv5F1Hn2O-y-Jf_xZe2WtqGhIx6zgGvmXCOOv8XWsBHbEe4xnWR94H6HWyWt9A",
            "response" : "json",
            "command" : "deployVirtualMachine",
            "serviceofferingId": "1",
            "response":"json",
            "hostid":"db1f8fad-efa5-4cdb-92e6-19ff286a2253",
            "networkids":"d4e11e5f-def3-4d32-876f-636c5606f6f5"
        }
        request["apiKey"]=apiKey
        request['serviceofferingId']=serviceofferingId
        request['templateId']=centos.getCentosID()
        # request['zoneId']=zone.getZone1ID()
        request['zoneId']="aee60d64-ae63-4319-85f1-92687f1875ff"
        request_str='&'.join(['='.join([k,urllib.parse.quote_plus(request[k])]) for k in request.keys()])
        sig_str='&'.join(['='.join([k.lower(),urllib.parse.quote_plus(request[k].lower().replace('+','%20'))])for k in sorted(request)])
        sig=hmac.new(secretkey.encode('utf-8'),sig_str.encode('utf-8'),hashlib.sha1)
        sig=hmac.new(secretkey.encode('utf-8'),sig_str.encode('utf-8'),hashlib.sha1).digest()
        sig=base64.encodebytes(hmac.new(secretkey.encode('utf-8'),sig_str.encode('utf-8'),hashlib.sha1).digest())
        sig=base64.encodebytes(hmac.new(secretkey.encode('utf-8'),sig_str.encode('utf-8'),hashlib.sha1).digest()).strip()
        sig=urllib.parse.quote_plus(base64.encodebytes(hmac.new(secretkey.encode('utf-8'),sig_str.encode('utf-8'),hashlib.sha1).digest()).strip())
        req=baseurl+request_str+'&signature='+sig
        req
        res=urllib.request.urlopen(req)
        response=res.read()

        print(response)


import urllib
import urllib.parse
import urllib.request
import hashlib
import hmac
import base64
import sys
# sys.path.append('./ServiceOffering')
import signature
import urls as key
# from .ServiceOffering import listServiceOfferings as service
import Zone.getZone1ID as zone
import Template.getCentosID as centos
import ServiceOffering.listServiceOfferings as listOffer
# import Zone.listZone
import zone
import network
import host
class VM():

    def deployVM(self,templateID,vmname="test"):
        baseurl=key.baseurl
        apiKey=key.apiKey
        secretkey=key.secretKey
        z=zone.zone()
        n=network.net()
        h=host.host()
        # serviceofferingId = "6906780f-3625-46ea-86f0-5ed272dc2f73"
        serviceofferingId = listOffer.listServiceOfferings()
        # baseurl='http://10.125.70.28:8080/client/api?'
        request= {"apiKey": apiKey, "response": "json", "command": "deployVirtualMachine",
                  "hostid": h.gethostid(),
                  "networkids": n.getnetid(), 'serviceofferingId': serviceofferingId,
                  'templateId': templateID, 'zoneId': z.getZoneID(), "startvm": "false","displayname":vmname,"name":vmname}
        # request['zoneId']=zone.getZone1ID()
        # request_str='&'.join(['='.join([k,urllib.parse.quote_plus(request[k])]) for k in request.keys()])
        # sig_str='&'.join(['='.join([k.lower(),urllib.parse.quote_plus(request[k].lower().replace('+','%20'))])for k in sorted(request)])
        # sig=hmac.new(secretkey.encode('utf-8'),sig_str.encode('utf-8'),hashlib.sha1)
        # sig=hmac.new(secretkey.encode('utf-8'),sig_str.encode('utf-8'),hashlib.sha1).digest()
        # sig=base64.encodebytes(hmac.new(secretkey.encode('utf-8'),sig_str.encode('utf-8'),hashlib.sha1).digest())
        # sig=base64.encodebytes(hmac.new(secretkey.encode('utf-8'),sig_str.encode('utf-8'),hashlib.sha1).digest()).strip()
        # sig=urllib.parse.quote_plus(base64.encodebytes(hmac.new(secretkey.encode('utf-8'),sig_str.encode('utf-8'),hashlib.sha1).digest()).strip())
        # req=baseurl+request_str+'&signature='+sig
        # req
        # res=urllib.request.urlopen(req)
        # response=res.read()
        response= signature.requestsig(baseurl,secretkey,request)
        # print(response)
        return response

    def getVMid(self,vmname):
        request = {"apiKey": apiKey, "response": "json", "command": "listVirtualMachines",
                   "name": vmname}
        response = signature.requestsig(key.baseurl, key.secretKey, request)
        return response

    def startVM(self,vmid):
        request = {"apiKey": apiKey, "response": "json", "command": "startVirtualMachine",
                   "id": vmid}
        response = signature.requestsig(key.baseurl, key.secretKey, request)
        return response


    def stopVM(self,vmid):
        request = {"apiKey": apiKey, "response": "json", "command": "stopVirtualMachine",
                   "id": vmid}
        response = signature.requestsig(key.baseurl, key.secretKey, request)
        return response
# f=VM()
# f.deployVM("2b8ea85e-8695-4b8e-81f0-57b9463f7336")
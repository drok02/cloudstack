import urllib2
import urllib
import hashlib
import hmac
import base64
import sys
# sys.path.append('./ServiceOffering')
import urls as key
# from .ServiceOffering import listServiceOfferings as service
# import Zone.getZone1ID as zone
# import Template.getCentosID as centos
def deployVM():
    baseurl=key.baseurl
    apiKey=key.apiKey
    secretkey=key.secretKey
    serviceofferingId = "e82173f4-6bf4-4717-a9be-a8675e36e4d2"
    # baseurl='http://10.125.70.28:8080/client/api?'
    request={
        "apiKey": "oCFMurQjw4EX-T7fRQXBCmkbDv5F1Hn2O-y-Jf_xZe2WtqGhIx6zgGvmXCOOv8XWsBHbEe4xnWR94H6HWyWt9A",
        "response" : "json",
        "command" : "deployVirtualMachine",
        "serviceofferingId": "1",
        "response":"json",
        "hostid":"7f725a8f-92d3-4994-992c-c7e9a7535202"
        
    }
    request["apiKey"]=apiKey
    request['serviceofferingId']=serviceofferingId
    request['templateId']="82220e2d-fdb8-11ec-9953-daa9733e8288"
    request['zoneId']="b2f29b5b-9cb1-4223-9e8e-75d9d6bec7b0"
    request_str='&'.join(['='.join([k,urllib.quote_plus(request[k])]) for k in request.keys()])
    sig_str='&'.join(['='.join([k.lower(),urllib.quote_plus(request[k].lower().replace('+','%20'))])for k in sorted(request.iterkeys())])
    sig=hmac.new(secretkey,sig_str,hashlib.sha1)
    sig=hmac.new(secretkey,sig_str,hashlib.sha1).digest()
    sig=base64.encodestring(hmac.new(secretkey,sig_str,hashlib.sha1).digest())
    sig=base64.encodestring(hmac.new(secretkey,sig_str,hashlib.sha1).digest()).strip()
    sig=urllib.quote_plus(base64.encodestring(hmac.new(secretkey,sig_str,hashlib.sha1).digest()).strip())
    print("signature is \n",sig)
    req=baseurl+request_str+'&signature='+sig
    req
    res=urllib2.urlopen(req)
    response=res.read()

    print(response)
# print(req)

deployVM()

# apikey=mivr6x7u6bn_sdahobpjnejpgest35exq-jb8cg20yi3yaxxcgpyuairmfi_ejtvwz0nukkjbpmy3y2bcikwfq
# &command=deployvirtualmachine
# &diskofferingid=1
# &serviceofferingid=1
# &templateid=2
# &zoneid=4
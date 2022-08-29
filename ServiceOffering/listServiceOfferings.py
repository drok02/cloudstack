import urllib2
import urllib
import hashlib
import hmac
import base64
import json
import sys
sys.path.append("C:/Users/PC/bong/Cloudstack/cloudstack")
import urls as key

def listServiceOfferings():
    baseurl=key.baseurl
    apiKey=key.apiKey
    secretkey=key.secretKey

    # baseurl='http://10.125.70.28:8080/client/api?'
    request={
        "apiKey": "oCFMurQjw4EX-T7fRQXBCmkbDv5F1Hn2O-y-Jf_xZe2WtqGhIx6zgGvmXCOOv8XWsBHbEe4xnWR94H6HWyWt9A",
        "response" : "json",
        "command" : "listServiceOfferings"
    }
    request["apiKey"]=apiKey
    # secretKey="2yLo8pQRIpwBW4jOwgPd6WVKBmi3q3gosi2llVa5h3JOVZKBHvbbLdc_mbaYEtKIGP5N_mmfnJeNW1maP4AKew"
    request_str='&'.join(['='.join([k,urllib.quote_plus(request[k])]) for k in request.keys()])
    sig_str='&'.join(['='.join([k.lower(),urllib.quote_plus(request[k].lower().replace('+','%20'))])for k in sorted(request.iterkeys())])
    sig=hmac.new(secretkey,sig_str,hashlib.sha1)
    sig=hmac.new(secretkey,sig_str,hashlib.sha1).digest()
    sig=base64.encodestring(hmac.new(secretkey,sig_str,hashlib.sha1).digest())
    sig=base64.encodestring(hmac.new(secretkey,sig_str,hashlib.sha1).digest()).strip()
    sig=urllib.quote_plus(base64.encodestring(hmac.new(secretkey,sig_str,hashlib.sha1).digest()).strip())
    # print("signature is \n",sig)
    req=baseurl+request_str+'&signature='+sig
    print("request URL is \n1",json.dumps(req,indent="\t"))
    print()
    res=urllib2.urlopen(req)
    response=res.read()
    print(type(response))
    # print(response)
    # print(json.dumps(res,indent=2))
    # print(req)
    jsonData=json.loads(response)
    print(jsonData["listserviceofferingsresponse"]["serviceoffering"][0]["id"])
    return jsonData["listserviceofferingsresponse"]["serviceoffering"][0]["id"]
    
listServiceOfferings()
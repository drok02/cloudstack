# import urllib2
import urllib
import urllib.parse
import urllib.request
import hashlib
import hmac
import base64
import json
import sys,os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
# sys.path.append("/Users/ibonghun/Developer/cloudstack")
import urls as key

def listzone():
    baseurl=key.baseurl
    apiKey=key.apiKey
    secretkey=key.secretKey

    # baseurl='http://10.125.70.28:8080/client/api?'
    request={
        "apiKey": "oCFMurQjw4EX-T7fRQXBCmkbDv5F1Hn2O-y-Jf_xZe2WtqGhIx6zgGvmXCOOv8XWsBHbEe4xnWR94H6HWyWt9A",
        "response" : "json",
        "command" : "listZones"
    }
    request["apiKey"]=apiKey
    
    request_str='&'.join(['='.join([k,urllib.parse.quote_plus(request[k])]) for k in request.keys()])
    sig_str='&'.join(['='.join([k.lower(),urllib.parse.quote_plus(request[k].lower().replace('+','%20'))])for k in sorted(request)])
    sig=hmac.new(secretkey.encode('utf-8'),sig_str.encode('utf-8'),hashlib.sha1)
    sig=hmac.new(secretkey.encode('utf-8'),sig_str.encode('utf-8'),hashlib.sha1).digest()
    sig=base64.encodebytes(hmac.new(secretkey.encode('utf-8'),sig_str.encode('utf-8'),hashlib.sha1).digest())
    sig=base64.encodebytes(hmac.new(secretkey.encode('utf-8'),sig_str.encode('utf-8'),hashlib.sha1).digest()).strip()
    sig=urllib.parse.quote_plus(base64.encodebytes(hmac.new(secretkey.encode('utf-8'),sig_str.encode('utf-8'),hashlib.sha1).digest()).strip())
    req=baseurl+request_str+'&signature='+sig
    print("request URL is \n1",json.dumps(req,indent="\t"))
    print()
    res=urllib.request.urlopen(req)
    response=res.read()
    print(type(response))

    jsonData=json.loads(response)
    print(jsonData)
    return jsonData
    

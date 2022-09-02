import urllib
import urllib.parse
import urllib.request
import hashlib
import hmac
import base64
import json
import sys,os

import signature

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import urls as key

class zone():

    def listzone(self):
        baseurl=key.baseurl
        apiKey=key.apiKey
        secretkey=key.secretKey

        request= {"apiKey": apiKey, "response": "json", "command": "listZones"}

        # request_str='&'.join(['='.join([k,urllib.parse.quote_plus(request[k])]) for k in request.keys()])
        # sig_str='&'.join(['='.join([k.lower(),urllib.parse.quote_plus(request[k].lower().replace('+','%20'))])for k in sorted(request)])
        # sig=hmac.new(secretkey.encode('utf-8'),sig_str.encode('utf-8'),hashlib.sha1)
        # sig=hmac.new(secretkey.encode('utf-8'),sig_str.encode('utf-8'),hashlib.sha1).digest()
        # sig=base64.encodebytes(hmac.new(secretkey.encode('utf-8'),sig_str.encode('utf-8'),hashlib.sha1).digest())
        # sig=base64.encodebytes(hmac.new(secretkey.encode('utf-8'),sig_str.encode('utf-8'),hashlib.sha1).digest()).strip()
        # sig=urllib.parse.quote_plus(base64.encodebytes(hmac.new(secretkey.encode('utf-8'),sig_str.encode('utf-8'),hashlib.sha1).digest()).strip())
        # req=baseurl+request_str+'&signature='+sig
        # print("request URL is \n1",json.dumps(req,indent="\t"))
        # print()
        # res=urllib.request.urlopen(req)
        # response=res.read()
        # print(type(response))
        response=signature.requestsig(baseurl,secretkey,request)
        jsonData=json.loads(response)
        # print(jsonData)
        return jsonData
    
    def getZone1ID(self):
        zone=self.listzone()
        id=zone["listzonesresponse"]["zone"][0]["id"]
        print("zone1 id is "+id)
        return id

# f=zone()
# f.getZone1ID()

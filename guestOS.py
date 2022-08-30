import urllib.parse,urllib.request
import hashlib
import hmac
import base64
import json
import sys,os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import urls as key

class OS():

    def listostype(self):
        baseurl=key.baseurl
        secretkey=key.secretKey
        request={
            "apiKey": "Pr3IZM1ArGIQsKy8i04AVSjkiF_CgOEdGA4wdYwj52ZxA6oUIxzC7iX2lbzouAU8ZEf_pfUEJfpXl_YyA-kCFg",
            "response" : "json",
            "command" : "listOsTypes",
            "keyword":"ubuntu"
        }
        request['apikey']=key.apiKey
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
        print()
        res=urllib.request.urlopen(req)
        response=res.read()
        print(response)
        return response


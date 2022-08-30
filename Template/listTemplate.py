import urllib.parse
import urllib.request
import urllib
import hashlib
import hmac
import base64
import sys,os
import json
sys.path.append("/Users/ibonghun/Developer/cloudstack")
import urls as key


def listTemplate():
    baseurl=key.baseurl
    apiKey=key.apiKey
    secretKey=key.secretKey

    # baseurl='http://10.125.70.28:8080/client/api?'
    request={}
    request['command']='listTemplates'
    request['templatefilter']='featured'
    request['response']='json'
    # request['apikey']='RUwHTWN6y-czxVkr2u0AJvM-sNucusoWc3lw1dqMUSvjJt3rhjPgA7hReEZMqSlSTVl_BfYzQf7Myf7kGqzHHQ'
    request['apikey']=apiKey
    secretkey=secretKey
    # secretkey='FGZAE9Pk5jWqlGPOdCGsdO7mkdkbc8azmTBOQzQnKrnbaiuUsnF2klsJ_FDfKlrs-s2ZTiYDIUiwmHw7aZ7B4Q'
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
    jsonData=json.loads(response)
    return jsonData
# print(req)

listTemplate()

# apikey=mivr6x7u6bn_sdahobpjnejpgest35exq-jb8cg20yi3yaxxcgpyuairmfi_ejtvwz0nukkjbpmy3y2bcikwfq
# &command=deployvirtualmachine
# &diskofferingid=1
# &serviceofferingid=1
# &templateid=2
# &zoneid=4
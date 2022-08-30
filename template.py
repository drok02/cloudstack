import urllib
import hashlib
import hmac
import base64
import sys,os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import urllib.parse
import urllib.request
import urls as key
import Zone.getZone1ID as zone
import Template.getCentosID as centos
import ServiceOffering.listServiceOfferings as listOffer
import GuestOS.listOSTypes as ostype
import json

class Template():


    def regiTemplate(self):
        baseurl=key.baseurl
        apikey=key.apiKey
        secretkey=key.secretKey
        request={
            "apiKey": "oCFMurQjw4EX-T7fRQXBCmkbDv5F1Hn2O-y-Jf_xZe2WtqGhIx6zgGvmXCOOv8XWsBHbEe4xnWR94H6HWyWt9A",
            "response" : "json",
            "command" : "registerTemplate",
            "displaytext": "e5934522-fe91-11ec-ae65-525400c8d027",
            "format":"qcow2",
            "hypervisor":"kvm",
            "name":"bong",
            "url":"https://cloud-images.ubuntu.com/bionic/current/bionic-server-cloudimg-amd64.img",
            "ostypeid":"a20b6938-286a-11ed-bfb3-0800277c0f4b",
            "zoneid":"aee60d64-ae63-4319-85f1-92687f1875ff"
        }
        request["zoneid"]=zone.getZone1ID()
        request["apiKey"]=apikey


        request_str='&'.join(['='.join([k,urllib.parse.quote_plus(request[k])]) for k in request.keys()])
        sig_str='&'.join(['='.join([k.lower(),urllib.parse.quote_plus(request[k].lower().replace('+','%20'))])for k in sorted(request)])
        sig=hmac.new(secretkey.encode('utf-8'),sig_str.encode('utf-8'),hashlib.sha1)
        sig=hmac.new(secretkey.encode('utf-8'),sig_str.encode('utf-8'),hashlib.sha1).digest()
        sig=base64.encodebytes(hmac.new(secretkey.encode('utf-8'),sig_str.encode('utf-8'),hashlib.sha1).digest())
        sig=base64.encodebytes(hmac.new(secretkey.encode('utf-8'),sig_str.encode('utf-8'),hashlib.sha1).digest()).strip()
        sig=urllib.parse.quote_plus(base64.encodebytes(hmac.new(secretkey.encode('utf-8'),sig_str.encode('utf-8'),hashlib.sha1).digest()).strip())
        req=baseurl+request_str+'&signature='+sig
        print(req)
        # res=urllib.request.urlopen(req)
        # response=res.read()

        # print(response)
        
    def listTemplate(self):
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


    def copyTemplate(self):
        baseurl=key.baseurl
        secretkey=key.secretKey
        request={}
        request['command']='copyTemplate'
        request['id']='585e06bb-fbb5-11ec-8775-08002702dd0b'
        request['destzoneid']='8c7c81c5-4379-4fd2-9153-64f17243aa9c'
        request['response']='json'
        request['apikey']=key.apiKey
        request_str='&'.join(['='.join([k,urllib.quote_plus(request[k])]) for k in request.keys()])
        sig_str='&'.join(['='.join([k.lower(),urllib.quote_plus(request[k].lower().replace('+','%20'))])for k in sorted(request.iterkeys())])
        sig=hmac.new(secretkey,sig_str,hashlib.sha1)
        sig=hmac.new(secretkey,sig_str,hashlib.sha1).digest()
        sig=base64.encodestring(hmac.new(secretkey,sig_str,hashlib.sha1).digest())
        sig=base64.encodestring(hmac.new(secretkey,sig_str,hashlib.sha1).digest()).strip()
        sig=urllib.quote_plus(base64.encodestring(hmac.new(secretkey,sig_str,hashlib.sha1).digest()).strip())
        req=baseurl+request_str+'&signature='+sig
        # req
        # res=urllib2.urlopen(req)
        # response=res.read()

        # print(response)
        print(req)


    def getCentosID(self):
        id=self.listTemplate()["listtemplatesresponse"]["template"][0]["id"]
        print(id)
        return id
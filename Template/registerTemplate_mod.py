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

def regiTemplate():
    baseurl=key.baseurl
    apikey=key.apiKey
    secretkey=key.secretKey
    request= {"apiKey": apikey, "response": "json", "command": "registerTemplate",
              "displaytext": "e5934522-fe91-11ec-ae65-525400c8d027", "format": "qcow2", "hypervisor": "kvm",
              "name": "bong", "url": "https://cloud-images.ubuntu.com/bionic/current/bionic-server-cloudimg-amd64.img",
              "ostypeid": "a20b6938-286a-11ed-bfb3-0800277c0f4b", "zoneid": zone.getZone1ID()}

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
    

regiTemplate()
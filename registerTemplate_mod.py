import urllib2
import urllib
import hashlib
import hmac
import base64

baseurl='http://10.125.70.28:8080/client/api?'
request={
    "apiKey": "oCFMurQjw4EX-T7fRQXBCmkbDv5F1Hn2O-y-Jf_xZe2WtqGhIx6zgGvmXCOOv8XWsBHbEe4xnWR94H6HWyWt9A",
    "response" : "json",
    "command" : "registerTemplate",
    "displaytext": "e5934522-fe91-11ec-ae65-525400c8d027",
    "format":"qcow2",
    "hypervisor":"kvm",
    "name":"bong",
    "url":"https://cloud-images.ubuntu.com/bionic/current/bionic-server-cloudimg-amd64.img",
    "ostypeid":"1679086f-fe92-11ec-ae65-525400c8d027",
    "zoneid":"aee60d64-ae63-4319-85f1-92687f1875ff"
}
secretkey='2yLo8pQRIpwBW4jOwgPd6WVKBmi3q3gosi2llVa5h3JOVZKBHvbbLdc_mbaYEtKIGP5N_mmfnJeNW1maP4AKew'


request_url='&'.join(['='.join([k,urllib.quote_plus(request[k])]) for k in request.keys()])

sig_url='&'.join(['='.join([k.lower(),urllib.quote_plus(request[k].lower().replace('+','%20'))])for k in sorted(request.iterkeys())])
sig=hmac.new(secretkey,sig_url,hashlib.sha1)
sig=hmac.new(secretkey,sig_url,hashlib.sha1).digest()
sig=base64.encodestring(hmac.new(secretkey,sig_url,hashlib.sha1).digest())
sig=base64.encodestring(hmac.new(secretkey,sig_url,hashlib.sha1).digest()).strip()
sig=urllib.quote_plus(base64.encodestring(hmac.new(secretkey,sig_url,hashlib.sha1).digest()).strip())

# print(sig)
req=baseurl+request_url+'&signature='+sig
res=urllib2.urlopen(req)
response=res.read()

print(response)
# print(req)
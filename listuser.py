import urllib2
import urllib
import hashlib
import hmac
import base64

# baseurl='http://10.125.70.28:8080/client/api?'
# request={}
# request['command']='listUsers'
# request['response']='json'
# request['apikey']='-Tnv-ixvYb8P0TLxKdWFAVv_TpcCxFlVhzWMqNrv9qJoZdi-C20PulTKQp_P9Fiiw7IdefJHbBTVUPHeu6vIgQ'
# secretkey='49ns46v5CsDd461z4I6C0RMZtNnvhYpwLk9yIm7MUqXRAk-KfbNxyWvDperFeB5uIb3yL28B48HWRa3a0o7F-Q'
# request_str='&'.join(['='.join([k,urllib.quote_plus(request[k])]) for k in request.keys()])
# sig_str='&'.join(['='.join([k.lower(),urllib.quote_plus(request[k].lower().replace('+','%20'))])for k in sorted(request.iterkeys())])
# sig=hmac.new(secretkey,sig_str,hashlib.sha1)
# sig=hmac.new(secretkey,sig_str,hashlib.sha1).digest()
# sig=base64.encodestring(hmac.new(secretkey,sig_str,hashlib.sha1).digest())
# sig=base64.encodestring(hmac.new(secretkey,sig_str,hashlib.sha1).digest()).strip()
# sig=urllib.quote_plus(base64.encodestring(hmac.new(secretkey,sig_str,hashlib.sha1).digest()).strip())
# print("signature is \n",sig)
# req=baseurl+request_str+'&signature='+sig
# req
# res=urllib2.urlopen(req)
# response=res.read()

# print(response)
# # print(req)



# apikey=mivr6x7u6bn_sdahobpjnejpgest35exq-jb8cg20yi3yaxxcgpyuairmfi_ejtvwz0nukkjbpmy3y2bcikwfq
# &command=deployvirtualmachine
# &diskofferingid=1
# &serviceofferingid=1
# &templateid=2
# &zoneid=4

baseurl='http://10.125.70.28:8080/client/api?'
request={
    "apiKey": "oCFMurQjw4EX-T7fRQXBCmkbDv5F1Hn2O-y-Jf_xZe2WtqGhIx6zgGvmXCOOv8XWsBHbEe4xnWR94H6HWyWt9A",
    "response" : "json",
    "command" : "listUsers"
}
secretkey="2yLo8pQRIpwBW4jOwgPd6WVKBmi3q3gosi2llVa5h3JOVZKBHvbbLdc_mbaYEtKIGP5N_mmfnJeNW1maP4AKew"
request_str='&'.join(['='.join([k,urllib.quote_plus(request[k])]) for k in request.keys()])
sig_str='&'.join(['='.join([k.lower(),urllib.quote_plus(request[k].lower().replace('+','%20'))])for k in sorted(request.iterkeys())])
sig=hmac.new(secretkey,sig_str,hashlib.sha1)
sig=hmac.new(secretkey,sig_str,hashlib.sha1).digest()
sig=base64.encodestring(hmac.new(secretkey,sig_str,hashlib.sha1).digest())
sig=base64.encodestring(hmac.new(secretkey,sig_str,hashlib.sha1).digest()).strip()
sig=urllib.quote_plus(base64.encodestring(hmac.new(secretkey,sig_str,hashlib.sha1).digest()).strip())
print("signature is \n",sig)
req=baseurl+request_str+'&signature='+sig
print("request URL is \n1",req)
res=urllib2.urlopen(req)
response=res.read()

print(response)
# print(req)

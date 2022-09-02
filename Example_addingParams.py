import urllib
import urllib.parse, urllib.request
import hashlib
import hmac
import base64
import signature
import urls as key


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

baseurl=key.baseurl
request={
    "apiKey": key.apiKey,
    "response" : "json",
    "command" : "listUsers"
}
secretkey=key.secretKey

# request_str='&'.join(['='.join([k,urllib.quote_plus(request[k])]) for k in request.keys()])
# sig_str='&'.join(['='.join([k.lower(),urllib.quote_plus(request[k].lower().replace('+','%20'))])for k in sorted(request.iterkeys())])
# sig=hmac.new(secretkey,sig_str,hashlib.sha1)
# sig=hmac.new(secretkey,sig_str,hashlib.sha1).digest()
# sig=base64.encodestring(hmac.new(secretkey,sig_str,hashlib.sha1).digest())
# sig=base64.encodestring(hmac.new(secretkey,sig_str,hashlib.sha1).digest()).strip()
# sig=urllib.quote_plus(base64.encodestring(hmac.new(secretkey,sig_str,hashlib.sha1).digest()).strip())
# # print("signature is \n",sig)
# req=baseurl+request_str+'&signature='+sig
# print("request URL is \n1",req)
# print()
# print()
# res=urllib.request.urlopen(req)
# response=res.read()
#
# print(response)
# print(req)

signature.requestsig(baseurl,secretkey,request)
import urllib2
import urllib
import hashlib
import hmac
import base64

baseurl='http://192.168.0.110:8080/client/api?'
request={}
request['command']='listOsTypes'
request['response']='json'
request['apikey']='Qrqan7gk2AVKp7Wb1MP_7GogHiIRAR0guEWQFDYOtbTtx6ijz_6O8hw4g_fJi_0Gh16oEDSjESiMZEJi466aHg'
secretkey='XNoFZwzY6Sq6F7mQVXDo3TBX7P2v0yustaVgNGyIsauJ20eYSBxnkWWlRIkPvsw5EH_xy4GwJLJ2F9MtBobCgA'
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
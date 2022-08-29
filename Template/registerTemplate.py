import urllib2
import urllib
import hashlib
import hmac
import base64

baseurl='http://10.125.70.28:8080/client/api?'
request={}
request['command']='registerTemplate'
request['displaytext']='register_Template_api'
request['format']='QCOW2'
request['hypervisor']='KVM'
request['name']='api_test_template'
request['url']='https://cloud-images.ubuntu.com/bionic/current/bionic-server-cloudimg-amd64.img'
# request['ostypeid']='66209051-fbb5-11ec-8775-08002702dd0b'
request['response']='json'
request['apikey']='-Tnv-ixvYb8P0TLxKdWFAVv_TpcCxFlVhzWMqNrv9qJoZdi-C20PulTKQp_P9Fiiw7IdefJHbBTVUPHeu6vIgQ'
secretkey='49ns46v5CsDd461z4I6C0RMZtNnvhYpwLk9yIm7MUqXRAk-KfbNxyWvDperFeB5uIb3yL28B48HWRa3a0o7F-Q'


request_url='&'.join(['='.join([k,urllib.quote_plus(request[k])]) for k in request.keys()])

sig_url='&'.join(['='.join([k.lower(),urllib.quote_plus(request[k].lower().replace('+','%20'))])for k in sorted(request.iterkeys())])
sig=hmac.new(secretkey,sig_url,hashlib.sha1)
sig=hmac.new(secretkey,sig_url,hashlib.sha1).digest()
sig=base64.encodestring(hmac.new(secretkey,sig_url,hashlib.sha1).digest())
sig=base64.encodestring(hmac.new(secretkey,sig_url,hashlib.sha1).digest()).strip()
sig=urllib.quote_plus(base64.encodestring(hmac.new(secretkey,sig_url,hashlib.sha1).digest()).strip())

print(sig)
# req=baseurl+request_url+'&signature='+sig
# res=urllib2.urlopen(req)
# response=res.read()

# print(response)
# print(req)
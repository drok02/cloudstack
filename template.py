import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import urls as key
import Zone.getZone1ID as zone
import json
import signature

class Template():

    def regiTemplate(self, name, url, osTypeid):
        baseurl = key.baseurl
        apikey = key.apiKey
        secretkey = key.secretKey

        request = {"apiKey": apikey, "response": "json", "command": "registerTemplate",
                   "displaytext": "e5934522-fe91-11ec-ae65-525400c8d027", "format": "qcow2", "hypervisor": "kvm",
                   "name": name, "url": url, "ostypeid": osTypeid, "zoneid": zone.getZone1ID()}

        signature.requestsig(baseurl, secretkey, request)



    def listTemplate(self):
        baseurl = key.baseurl
        apiKey = key.apiKey
        secretKey = key.secretKey

        # baseurl='http://10.125.70.28:8080/client/api?'
        request = {}
        request['command'] = 'listTemplates'
        request['templatefilter'] = 'featured'
        request['response'] = 'json'
        # request['apikey']='RUwHTWN6y-czxVkr2u0AJvM-sNucusoWc3lw1dqMUSvjJt3rhjPgA7hReEZMqSlSTVl_BfYzQf7Myf7kGqzHHQ'
        request['apikey'] = apiKey
        secretkey = secretKey
        # secretkey='FGZAE9Pk5jWqlGPOdCGsdO7mkdkbc8azmTBOQzQnKrnbaiuUsnF2klsJ_FDfKlrs-s2ZTiYDIUiwmHw7aZ7B4Q'
        # request_str = '&'.join(['='.join([k, urllib.parse.quote_plus(request[k])]) for k in request.keys()])
        # sig_str = '&'.join(
        #     ['='.join([k.lower(), urllib.parse.quote_plus(request[k].lower().replace('+', '%20'))]) for k in
        #      sorted(request)])
        # sig = hmac.new(secretkey.encode('utf-8'), sig_str.encode('utf-8'), hashlib.sha1)
        # sig = hmac.new(secretkey.encode('utf-8'), sig_str.encode('utf-8'), hashlib.sha1).digest()
        # sig = base64.encodebytes(hmac.new(secretkey.encode('utf-8'), sig_str.encode('utf-8'), hashlib.sha1).digest())
        # sig = base64.encodebytes(
        #     hmac.new(secretkey.encode('utf-8'), sig_str.encode('utf-8'), hashlib.sha1).digest()).strip()
        # sig = urllib.parse.quote_plus(base64.encodebytes(
        #     hmac.new(secretkey.encode('utf-8'), sig_str.encode('utf-8'), hashlib.sha1).digest()).strip())
        # req = baseurl + request_str + '&signature=' + sig
        # res = urllib.request.urlopen(req)
        response = signature.requestsig(baseurl,secretkey,request)
        jsonData = json.loads(response)
        return jsonData

    def copyTemplate(self):
        baseurl = key.baseurl
        secretkey = key.secretKey
        request = {}
        request['command'] = 'copyTemplate'
        request['id'] = '585e06bb-fbb5-11ec-8775-08002702dd0b'
        request['destzoneid'] = '8c7c81c5-4379-4fd2-9153-64f17243aa9c'
        request['response'] = 'json'
        request['apikey'] = key.apiKey
        # request_str = '&'.join(['='.join([k, urllib.parse.quote_plus(request[k])]) for k in request.keys()])
        # sig_str = '&'.join(['='.join([k.lower(), urllib.parse.quote_plus(request[k].lower().replace('+', '%20'))]) for k in
        #                     sorted(request.iterkeys())])
        # sig = hmac.new(secretkey, sig_str, hashlib.sha1)
        # sig = hmac.new(secretkey, sig_str, hashlib.sha1).digest()
        # sig = base64.encodestring(hmac.new(secretkey, sig_str, hashlib.sha1).digest())
        # sig = base64.encodestring(hmac.new(secretkey, sig_str, hashlib.sha1).digest()).strip()
        # sig = urllib.parse.quote_plus(base64.encodestring(hmac.new(secretkey, sig_str, hashlib.sha1).digest()).strip())
        # req = baseurl + request_str + '&signature=' + sig
        # req
        # res=urllib2.urlopen(req)
        # response=res.read()
        req=signature.requestsig(baseurl,secretkey,request)
        # print(response)
        print(req)

    def getCentosID(self):
        id = self.listTemplate()["listtemplatesresponse"]["template"][0]["id"]
        print(id)
        return id

# f=Template()
# f.listTemplate()
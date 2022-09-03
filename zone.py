import urllib
import urllib.parse
import urllib.request
import hashlib
import hmac
import base64
import json
import sys,os

import signature

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import urls as key

class zone():

    def listzone(self):
        baseurl=key.baseurl
        apiKey=key.apiKey
        secretkey=key.secretKey

        request= {"apiKey": apiKey, "response": "json", "command": "listZones"}
        response=signature.requestsig(baseurl,secretkey,request)
        jsonData=json.loads(response)
        # print(jsonData)
        return jsonData
    
    def getZone1ID(self):
        zone=self.listzone()
        id=zone["listzonesresponse"]["zone"][0]["id"]
        print("zone1 id is "+id)
        return id

# f=zone()
# f.getZone1ID()

import http
from pickle import NONE
import urllib
import hmac
import hashlib
import base64

def make_request(requests, secretKey):
    # request = zip(requests.keys(), requests.values())
    # request.sort(key=lambda x: str.lower(x[0]))

    # requestUrl = "&".join(["=".join([r[0], urllib.quote_plus(str(r[1]))]) for r in request])
    # hashStr = "&".join(["=".join([str.lower(r[0]), str.lower(urllib.quote_plus(str(r[1]))).replace("+","%20")]) for r in request])
    # sig = urllib.quote_plus(base64.encodestring(hmac.new(secretKey, hashStr, hashlib.sha1).digest()).strip())
    # print("Signature:", sig)
    # requestUrl += "&signature="
    # requestUrl += sig
    # print(requestUrl)
    # return requestUrl
    request = zip(requests.keys(), requests.values())
    request.sort(key=lambda x: str.lower(x[0]))

    requestUrl = "&".join(["=".join([r[0], urllib.quote_plus(str(r[1]))]) for r in request])
    hashStr = "&".join(["=".join([str.lower(r[0]), str.lower(urllib.quote_plus(str(r[1]))).replace("+","%20")]) for r in request])
    sig = urllib.quote_plus(base64.encodestring(hmac.new(secretKey, hashStr, hashlib.sha1).digest()).strip())
    print("Signature:", sig)
    requestUrl += "&signature="
    requestUrl += sig
    # print(requestUrl)
    return requestUrl
if __name__ == '__main__':
    # requests = {
    #     "apiKey": "-Tnv-ixvYb8P0TLxKdWFAVv_TpcCxFlVhzWMqNrv9qJoZdi-C20PulTKQp_P9Fiiw7IdefJHbBTVUPHeu6vIgQ",
    #     "response" : "json",
    #     "command" : "registerIso",
    #     "displaytext":"create_ISO",
    #     "name":"api_test_ISO",
    #     "url":"https://releases.ubuntu.com/18.04/ubuntu-18.04.6-live-server-amd64.iso",
    #     "zoneid":"aee60d64-ae63-4319-85f1-92687f1875ff"
    # }
    requests2={
        "apiKey": "-Tnv-ixvYb8P0TLxKdWFAVv_TpcCxFlVhzWMqNrv9qJoZdi-C20PulTKQp_P9Fiiw7IdefJHbBTVUPHeu6vIgQ",
        "response" : "json",
        "command" : "registerTemplate",
        "displaytext":"register_Template_api",
        "format":"QCOW2",
        "hypervisor":"KVM",
        "name":"api_test_template0826",
        "url":"https://cloud-images.ubuntu.com/bionic/current/bionic-server-cloudimg-amd64.img",
        "zoneid":"aee60d64-ae63-4319-85f1-92687f1875ff"
    }
    # requests3={
    #         "apiKey": "oCFMurQjw4EX-T7fRQXBCmkbDv5F1Hn2O-y-Jf_xZe2WtqGhIx6zgGvmXCOOv8XWsBHbEe4xnWR94H6HWyWt9A",
    #         "response" : "json",
    #         "command" : "listUsers"
    #     }
    secretKey = "2yLo8pQRIpwBW4jOwgPd6WVKBmi3q3gosi2llVa5h3JOVZKBHvbbLdc_mbaYEtKIGP5N_mmfnJeNW1maP4AKew"
    url=make_request(requests2, secretKey)
    # print(url)
    print("10.125.70.28:8080/client/api?"+url)
    # url="http://10.125.70.28:8080/client/api"
    # user_res=requests.post(url, )

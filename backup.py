import sys,os
import sys
import signature
import template
import zone

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import urls as key


class bacup():
    baseurl=key.baseurl
    apiKey=key.apiKey
    secretkey=key.secretKey

    def createBackupVM(self,url):
        z = zone.zone()
        zone1id=z.getZoneID()
        print(zone1id)
        #사용자에게서 백업 VM 고르기

        

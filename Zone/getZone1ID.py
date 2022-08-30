import sys,os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import Zone.listZone 


def getZone1ID():
    zone=Zone.listZone.listzone()
    id=zone["listzonesresponse"]["zone"][0]["id"]
    print("zone1 id is "+id)
    return id



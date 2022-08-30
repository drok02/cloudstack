import Zone.listZone 


def getZone1ID():
    zone=Zone.listZone.listzone()
    id=zone["listzonesresponse"]["zone"][0]["id"]
    print("zone1 id is "+id)
    return id


id=getZone1ID()
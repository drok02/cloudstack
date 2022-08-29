import listTemplate as list

def getCentosID():
    id=list.listTemplate()["listtemplatesresponse"]["template"][0]["id"]
    print(id)
    return id

getCentosID()
import Template.listTemplate 

def getCentosID():
    id=Template.listTemplate.listTemplate()["listtemplatesresponse"]["template"][0]["id"]
    print(id)
    return id

getCentosID()
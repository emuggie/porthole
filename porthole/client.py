import requests, json

def get(url) :
    if not url.startswith("http") :
        url = "http://" + url
    if not url.endswith("/json") :
        url = url+"/json"
    response =  requests.get(url)
    if response.status_code != 200 :
        raise Exception("Fail to connect URI : "+ url)
    try :
        return json.loads(response.text)
    except Exception as err :
        raise Exception("Fail to Decode : "+ response.text)
    

## eval data.cpu.io > 0 and all(disk.used > 90 for disk in data.disks)
def test(uri, exp) : 
    try :
        data = get(uri)
        result = eval(exp, globals(), data)
        if not result : 
            return (False, "Expression returned false.\n" +"Expression : " + exp + "\n" + json.dumps(data,indent=4))
        return (True,None)
    except Exception as err :
        return (False, err)
    
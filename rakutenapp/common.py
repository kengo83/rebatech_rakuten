import requests

def execute_api(url:str,params:dict):
    res = requests.get(url,params)
    if not 300 > res.status_code >= 200:
        return None

    return res

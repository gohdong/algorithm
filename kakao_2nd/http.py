from typing import Dict
import requests
import json


# r = requests.get(API_HOST+"v2/local/search/address.json?query=용곡동",headers=headers)
# print(json.dumps(r.json(),indent=2,ensure_ascii=False))


class ApiRequest:

    def __init__(self) -> None:
        pass
        # print("init")

    def getRequest(self, host_url: str, path: str, header: Dict, params: Dict, print_log=False) -> json:
        param = '?'+'&'.join([f'{p}={params[p]}' for p in params])
        req = requests.get(host_url+path+param, headers=header)
        if print_log:
            print(f"Response Status Code : {req.status_code}")
            print(f"Response Header : {req.headers}")
            print(f"Response Body : {req.text}")

        if req.status_code == 200:
            return req.json()
        else:
            return "ERROR"

    def postRequest(self, host_url: str, path: str, header: Dict, params: Dict, print_log=False) -> json:
        req = requests.post(host_url+path, headers=header, params=params)
        if print_log:
            print(f"Response Status Code : {req.status_code}")
            print(f"Response Header : {req.headers}")
            print(f"Response Body : {req.text}")
        if req.status_code == 200:
            return req.json()
        else:
            return "ERROR"

    def printJson(self, json_data: json) -> None:
        if json_data:
            print(json.dumps(json_data, indent=2, ensure_ascii=False))
        else:
            print("No Requests")


API_HOST = "https://kox947ka1a.execute-api.ap-northeast-2.amazonaws.com/prod/users"
headers = {
    # "Authorization": "KakaoAK 22edf950ab1ef2c7a7aa4c5afbdfa9b8"
    'X-Auth-Token': '096e2b22d9c2b8a10febf9ce2d0c8ef5',
    'Content-Type': 'application/json'
}
parameter = {
    "problem": 1
}

a = ApiRequest()

response_data = a.postRequest(
    path="/start",host_url=API_HOST,header=headers ,params=parameter,print_log=True)
# print(a.printJson(response_data))

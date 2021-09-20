from typing import Dict
import requests
import json


# r = requests.get(API_HOST+"v2/local/search/address.json?query=용곡동",headers=headers)
# print(json.dumps(r.json(),indent=2,ensure_ascii=False))


class ApiRequest:

    def __init__(self) -> None:
        pass
        # print("init")

    def getRequest(self, host_url: str, path: str, header: Dict, params={}, print_log=False) -> json:
        param = '?'+'&'.join([f'{p}={params[p]}' for p in params])
        res = requests.get(host_url+path+param, headers=header)
        if print_log:
            print(f"Response Status Code : {res.status_code}")
            print(f"Response Header : {res.headers}")
            print(f"Response Body : {res.text}")

        if res.status_code == 200:
            return res.json()
        else:
            return "ERROR"

    def postRequest(self, host_url: str, path: str, header: Dict, params={}, print_log=False) -> json:
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
api_request = ApiRequest()

def start(problem_num: int):
    headers = {
        # "Authorization": "KakaoAK 22edf950ab1ef2c7a7aa4c5afbdfa9b8"
        'X-Auth-Token': '096e2b22d9c2b8a10febf9ce2d0c8ef5',
        'Content-Type': 'application/json'
    }
    parameter = {
        "problem": problem_num
    }

    return api_request.postRequest(API_HOST, '/start', header=headers, params=parameter)


start_response = start(1)


def getLocation(auth_key: str):
    headers = {
        'Authorization': auth_key
    }

    return api_request.getRequest(API_HOST, '/locations', header=headers)

def getTrucks(auth_key: str):
    headers = {
        'Authorization': auth_key
    }

    return api_request.getRequest(API_HOST, '/trucks', header=headers)    

def printLocation(locations: list, n_row: int, n_col: int):
    temp1 = [[] for _ in range(n_row)]
    row_index = 0
    for loc in locations:
        temp1[row_index].append(loc['located_bikes_count'])
        if loc['id'] % n_col == (n_col - 1):
            row_index+=1

    for t in temp1[::-1]:
        print(t)
    
auth_key = start_response['auth_key']

locations = getLocation(auth_key=auth_key)
print(getTrucks(auth_key))
# print(locations)
print(printLocation(locations['locations'],5,5))

        

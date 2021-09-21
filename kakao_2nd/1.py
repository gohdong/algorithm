from typing import Dict
from collections import Counter
import requests
import json

from requests import api


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
        'X-Auth-Token': 'd1bcdf5ca64a3ab154733e17da7590b6',
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
    for loc in locations:
        temp1[loc['id'] // 5].append([loc['id'], loc['located_bikes_count']])
        # temp1[loc['id'] // 5].append(loc['located_bikes_count'])

    return temp1


auth_key = start_response['auth_key']

locations = getLocation(auth_key=auth_key)


# print(locations)

init_truck_command = json.dumps({"commands": [{"truck_id": 0, "command": [0]}, {"truck_id": 1, "command": [2]}, {
                                "truck_id": 2, "command": [2, 2]}, {"truck_id": 3, "command": [2, 2, 2]}, {"truck_id": 4, "command": [2, 2, 2, 2]}]})
res = requests.put(API_HOST+'/simulate',
                   headers={
                       'Content-Type': 'application/json',
                       'Authorization': auth_key,
                   },
                   data=init_truck_command
                   ).json()
print(res)
truck_at_bottom = True
while True:
    locations = getLocation(auth_key=auth_key)
    command = {"commands": [{"truck_id": 0, "command": []}, {"truck_id": 1, "command": []}, {
        "truck_id": 2, "command": []}, {"truck_id": 3, "command": []}, {"truck_id": 4, "command": []}]}

    col_sum = [0 for _ in range(5)]
    col_max = [[0, 0] for _ in range(5)]
    col_min = [[0, 101] for _ in range(5)]
    for loc in locations['locations']:
        col_sum[loc['id']//5] += loc['located_bikes_count']
        if col_max[loc['id']//5][1] < loc['located_bikes_count']:
            col_max[loc['id']//5] = [loc['id'], loc['located_bikes_count']]

        if col_min[loc['id']//5][1] >= loc['located_bikes_count']:
            col_min[loc['id']//5] = [loc['id'], loc['located_bikes_count']]

    # print(col_sum)
    # print(col_max,col_min)

    # api_request.printJson(getTrucks(auth_key))
    for i, col in enumerate(printLocation(locations['locations'], 5, 5)):
        # col_counter = Counter(col)
        zero_count = 0
        for c in col:
            if c[1] == 0:
                zero_count += 1

        for c in col:
            if c == col_max[i]:
                command['commands'][i]['command'].append(5)
                if zero_count > 0:
                    for _ in range(zero_count-1):
                        command['commands'][i]['command'].append(5)
            elif c == col_min[i] or c[1] == 0:
                command['commands'][i]['command'].append(6)
            if truck_at_bottom:
                command['commands'][i]['command'].append(1)
            else:
                command['commands'][i]['command'].append(3)

        

    #     print(col)
    # print(col_sum)
    truck_at_bottom = not truck_at_bottom

    command_json = json.dumps(command)
    res = requests.put(API_HOST+'/simulate',
                       headers={
                           'Content-Type': 'application/json',
                           'Authorization': auth_key,
                       },
                       data=command_json
                       ).json()

    print(res)

    if res['status'] == "finished":
        score = requests.get(
            API_HOST+'/score', headers={"Authorization": auth_key}).json()
        print(score)
        break

from typing import Dict
from collections import Counter
import requests
import json
import random

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


API_HOST = "https://huqeyhi95c.execute-api.ap-northeast-2.amazonaws.com/prod"
api_request = ApiRequest()


def start(problem_num: int):
    headers = {
        'X-Auth-Token': '6890904aeaf753b7a5229841781d1df3',
        'Content-Type': 'application/json'
    }
    parameter = {
        "problem": problem_num
    }

    return api_request.postRequest(API_HOST, '/start', header=headers, params=parameter)


def getWaitingLine(auth_key: str):
    headers = {
        'Authorization': auth_key,
        'Content-Type': 'application/json'
    }

    return api_request.getRequest(API_HOST, '/waiting_line', header=headers)


def getGameResult(auth_key: str):
    headers = {
        'Authorization': auth_key,
        'Content-Type': 'application/json'
    }

    return api_request.getRequest(API_HOST, '/game_result', header=headers)


def getUserInfo(auth_key: str):
    headers = {
        'Authorization': auth_key,
        'Content-Type': 'application/json'
    }

    return api_request.getRequest(API_HOST, '/user_info', header=headers)


def putMatch(auth_key: str, pairs):
    headers = {
        'Authorization': auth_key,
        'Content-Type': 'application/json'
    }

    data = json.dumps(pairs)

    res = requests.put(API_HOST+'/match',
                       headers=headers,
                       data=data
                       ).json()

    return res


def changeGrade(auth_key: str, commands):
    headers = {
        'Authorization': auth_key,
        'Content-Type': 'application/json'
    }
    data = json.dumps(commands)

    res = requests.put(API_HOST+'/change_grade',
                       headers=headers,
                       data=data
                       ).json()

    return res

start_response = start(1)
auth_key = start_response['auth_key']


## Initial
putMatch(auth_key, {'pairs': []})



user = getUserInfo(auth_key)['user_info']
random_grade = [5000 for i in range(5000,5030)]
random.shuffle(random_grade)

for i,u in enumerate(user):
    u['grade'] = random_grade[i]


print(changeGrade(auth_key,commands={'commands':user}))

# print()
count = 0
while count < 595:
    game_result = getGameResult(auth_key)['game_result']
    user_info = getUserInfo(auth_key)['user_info']

    commands = []
    for result in game_result:
        loser = {
            'id' : result['lose'],
            'grade' : user_info[result['lose']-1]['grade'] - result['taken'] if user_info[result['lose']-1]['grade'] - result['taken'] >0 else 0
        }
        winner = {
            'id' : result['win'],
            'grade' : user_info[result['win']-1]['grade'] + result['taken'] if user_info[result['win']-1]['grade'] + result['taken'] < 10000 else 9999
        }
        commands.append(loser)
        commands.append(winner)

    if commands:
        print(changeGrade(auth_key,commands={'commands':commands}))
        user_info = getUserInfo(auth_key)['user_info']

    queue = getWaitingLine(auth_key)['waiting_line']

    ranking = {u['id']: i for i,u in enumerate(sorted(user_info,key= lambda x : x['grade'],reverse=True))}


    if queue:
        for q in queue:
            q['grade'] = user_info[q['id']-1]['grade']


    queue.sort(key=lambda x : (x['grade'],x['from']))

    pairs = []
    q_index = 0

    while q_index<len(queue)-1:
        waiting_time = count - queue[q_index]['from']
        if waiting_time <=5:
            if ranking[queue[q_index+1]['id']] - ranking[queue[q_index]['id']] <= 5:
                pairs.append([queue[q_index]['id'],queue[q_index+1]['id']])
                q_index+=2
            else:
                q_index+=1
        elif waiting_time <=10:
            if ranking[queue[q_index+1]['id']] - ranking[queue[q_index]['id']] <= 10:
                pairs.append([queue[q_index]['id'],queue[q_index+1]['id']])
                q_index+=2
            else:
                q_index+=1
        else:
            pairs.append([queue[q_index]['id'],queue[q_index+1]['id']])
            q_index+=1




    # for q in range(0,len(queue),2):
    #     if q+1 < len(queue):
    #         pairs.append([queue[q]['id'],queue[q+1]['id']])


    res = putMatch(auth_key=auth_key,pairs={'pairs': pairs})
    print(res)
    count +=1


score = requests.get(
            API_HOST+'/score', headers={"Authorization": auth_key}).json()
print(score)

# print(getWaitingLine(auth_key))
# putMatch(auth_key, {'pairs': []})
# print(getWaitingLine(auth_key))
# putMatch(auth_key, {'pairs': []})
# print(getWaitingLine(auth_key))

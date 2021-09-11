from collections import deque
from math import ceil

def solution(fees, records):
    answer = []
    max_time = time_to_min("23:59")
    car_history = {}


    for record in records:
        temp = record.split(' ')
        if temp[1] not in car_history:
            car_history[temp[1]] = [deque(),deque()] # IN,OUT

        if temp[2] == "IN":
            car_history[temp[1]][0].append(time_to_min(temp[0]))
        elif temp[2] == "OUT":
            car_history[temp[1]][1].append(time_to_min(temp[0]))

    for car in sorted(car_history,key = lambda x : int(x)):
        total_time = 0
        while car_history[car][0]:
            in_time = car_history[car][0].popleft()
            out_time = car_history[car][1].popleft() if car_history[car][1] else max_time
            total_time += out_time - in_time

        if total_time <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + ceil((total_time - fees[0])/fees[2])*fees[3])

    return answer    

def time_to_min(s):
    temp = s.split(':')
    return int(temp[0])*60 + int(temp[1])

    
print(solution([180, 5000, 10, 600],["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
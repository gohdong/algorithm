from collections import deque

def solution(priorities, location):
    priorities = deque([(index,priority) for index,priority in enumerate(priorities)])
    answer = 0
    printed = []

    
    
    while len(priorities) > 0:
        if(priorities[0][1] < max(priorities,key = lambda y : y[1])[1]):
           priorities.append(priorities.popleft())
        else:
            printed.append(priorities.popleft())
            
    
    for i in range(0,len(printed)):
        if(printed[i][0] == location):
            answer = i+1
            break
    
    return answer
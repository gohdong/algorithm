import math
from collections import deque

def solution(progresses, speeds):
    progresses = deque(progresses)
    speeds = deque(speeds)
    answer = []
    while list(progresses) != []:
        for x in range(0,len(speeds)):
            progresses[x] += speeds[x]
        
        count = 0
        while progresses[0]>=100:
            count+=1
            progresses.popleft()
            speeds.popleft()
            if(len(progresses) == 0):
                break
            
                
        if(count >0):
            answer.append(count)
    

    return answer
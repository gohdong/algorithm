from collections import deque

def solution(operations):
    answer = []
    operations = deque(operations)
    dd = []
    
    while len(operations) != 0:
        temp = operations.popleft()
        if(temp[0] == 'I'):
            dd.append(int(temp.split(' ')[1]))
            dd.sort()
        
        if(temp == 'D 1' and dd != []):
            dd.pop()
            
        if(temp == 'D -1' and dd != []):
            dd.pop(0)
        
    if(dd == []):
        return [0,0]
    return [max(dd),min(dd)]
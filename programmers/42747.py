import collections
from typing import List


def solution(citations: List):
    answer = 0	
    citations.sort()
    for i,c in enumerate(citations):
        print(len(citations)-i,c)
        if len(citations)-i <= c:
            return len(citations)-i

    return 0



print(solution([0,1,1]))

# [0,0,2,2,3,4,4,5,6,7,9,10]

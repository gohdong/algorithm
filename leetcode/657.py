from collections import defaultdict
from typing import Counter, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        temp = defaultdict(int) 
        for m in moves:
            temp[m] += 1
        x = temp['L']-temp['R'] 
        y = temp['U']-temp['D']
        return x == 0 and y == 0


solution = Solution()
print(solution.judgeCircle('UD'))

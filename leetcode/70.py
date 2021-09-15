from typing import List
import math

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def climbStairs(self, n: int) -> int:
        # answer = 0

        # for i in range(0,n//2+1):
        #     temp = 
        #     answer += 


        return sum([math.comb(n - 2*i + i,i) for i in range(0,n//2+1)])


solution = Solution()
print(solution.climbStairs(2))
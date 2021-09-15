from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mySqrt(self, x: int) -> int:
        i = 0
        while True:
            if i*i <= x <= (i+1)*(i+1):
                return x


solution = Solution()
print(solution.problem())

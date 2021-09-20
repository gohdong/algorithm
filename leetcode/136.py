from typing import List
from collections import Counter


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        temp = Counter(nums)
        for a in temp:
            if temp[a] == 1:
                return a


solution = Solution()
print(solution.problem())
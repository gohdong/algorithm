from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            temp = str(num)
            num = sum([int(x) for x in temp])

        return num


solution = Solution()
print(solution.problem())
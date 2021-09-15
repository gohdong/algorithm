from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return list(map(int,list(str(int(''.join(str(x) for x in digits))+1))))


solution = Solution()
print(solution.plusOne([1,2,3]))
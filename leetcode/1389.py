from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        answer = []

        for i,n in enumerate(index):
            answer.insert(n,nums[i])

        return answer


solution = Solution()
print(solution.problem())
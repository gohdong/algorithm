from typing import List


class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[a] for a in nums]


solution = Solution()
print(solution.buildArray([0,2,1,5,3,4]))
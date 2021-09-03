from typing import List


class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()


solution = Solution()
print(solution.toLowerCase("adaF"))
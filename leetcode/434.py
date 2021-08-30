from typing import List


class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())


solution = Solution()
print(solution.countSegments(s = "Hello, my name is John"))
from typing import List


class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:
	def titleToNumber(self, columnTitle: str) -> int:
		answer = 0
		count = len(columnTitle) - 1 

		for i,c in enumerate(columnTitle):
			answer += (ord(c)-64) * 26**(count-i)

		return answer




solution = Solution()
print(solution.titleToNumber("FXSHRXW"))

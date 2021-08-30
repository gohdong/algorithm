from typing import List


class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

class Solution:
	def repeatedSubstringPattern(self, s: str) -> bool:
		for i in range(1,len(s)):
			if len(s) % i == 0 and not s.replace(s[:i],""):
				return True
				
		return False
        



solution = Solution()
print(solution.repeatedSubstringPattern(s = "abab"))
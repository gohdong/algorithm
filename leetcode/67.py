from typing import List
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next
class Solution:
	def problem(self, a: str, b: str) -> int:
		return bin(int('0b'+a,2)+int('0b'+b,2))[2:]

solution = Solution()
print(solution.problem("11","1"))
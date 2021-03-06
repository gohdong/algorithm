from typing import List


class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:
	def reverseWords(self, s: str) -> str:
		return ' '.join([word[::-1] for word in s.split()])


solution = Solution()
print(solution.reverseWords(s = "Let's take LeetCode contest"))
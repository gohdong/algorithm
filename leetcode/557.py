from typing import List


class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:
	def reverseWords(self, s: str) -> str:
		answer = []
		for word in s.split():
			answer.append(word[::-1])

		return ' '.join(answer)


solution = Solution()
print(solution.reverseWords(s = "Let's take LeetCode contest"))
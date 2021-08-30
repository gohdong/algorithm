from typing import List


class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:
	def licenseKeyFormatting(self, s: str, k: int) -> str:
		answer = ""
		s = s.upper().replace('-','')[::-1]
		for i,c in enumerate(s):
			if i % k == 0:
				answer += '-'
			answer += c


		return answer[1:][::-1]

solution = Solution()
print(solution.licenseKeyFormatting(s = "5F3Z-2e-9-w", k = 4))
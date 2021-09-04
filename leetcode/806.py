from typing import List


class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:
	def numberOfLines(self, widths: List[int], s: str) -> List[int]:
		answer = 0
		line = 1

		for c in s:
			# answer += 
			temp = widths[ord(c)-97]
			if answer+temp > 100:
				line +=1
				answer = 0

			answer += temp
				
		return [line,answer]

solution = Solution()
print(solution.numberOfLines(widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], s = "abcdefghijklmnopqrstuvwxyz"))
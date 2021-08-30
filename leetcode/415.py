from typing import List


class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:
	def addStrings(self, num1: str, num2: str) -> str:
		# No use int()
		answer = 0
		for i,n in enumerate(num1):
			answer += (ord(n)-48)*10**(len(num1)-1-i)

		for i,n in enumerate(num2):
			answer += (ord(n)-48)*10**(len(num2)-1-i)	

		return str(answer)

		# return str(int(num1)+int(num2))

solution = Solution()
print(solution.addStrings(num1 = "11", num2 = "123"))
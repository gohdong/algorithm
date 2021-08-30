from typing import Counter, List


class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:
	def findWords(self, words: List[str]) -> List[str]:
		answer = []
		first_row = set("qwertyuiop")
		second_row = set("asdfghjkl")
		third_row = set("zxcvbnm")

		for w in words:
			a = set(Counter(w.lower()).keys())
			if first_row == a.union(first_row) or second_row == a.union(second_row) or third_row == a.union(third_row):
				answer.append(w)

		return answer


solution = Solution()
print(solution.findWords(words = ["Hello","Alaska","Dad","Peace"]))
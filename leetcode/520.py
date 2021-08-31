from typing import List


class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

class Solution:
	def detectCapitalUse(self, word: str) -> bool:
		return word == word.upper() or word == word.lower() or word == word[0].upper()+word[1:].lower()
        



solution = Solution()
print(solution.detectCapitalUse(word = "usa"))
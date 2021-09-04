from typing import List


class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:
	def uniqueMorseRepresentations(self, words: List[str]) -> int:
		morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
		answer = set()
		for w in words:
			temp = ""
			for c in w:
				temp += morse[ord(c)-97]
			answer.add(temp)

		return len(answer)
		
solution = Solution()
print(solution.uniqueMorseRepresentations(words = ["gin","zen","gig","msg"]))
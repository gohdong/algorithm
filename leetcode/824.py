from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
	def toGoatLatin(self, sentence: str) -> str:
		answer = ""
		vowel = {
            'a': "",
            'e': "",
            'i': "",
            'o': "",
            'u': "",
            'A': "",
            'E': "",
            'I': "",
            'O': "",
            'U': "",
        }

		for i,word in enumerate(sentence.split()):
			if i != 0:
				answer += " "
			if word[0] in vowel:
				answer += word+"ma"+"a"*(i+1)
			else:
				answer += word[1:]+word[0]+"ma"+"a"*(i+1)
			

		return answer


solution = Solution()
print(solution.toGoatLatin(sentence = "I speak Goat Latin"))

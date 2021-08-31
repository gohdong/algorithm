from typing import List


class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a == b:
            return -1
        
        return max(len(a),len(b))


from typing import Counter, List


class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:
	def isAnagram(self, s: str, t: str) -> bool:
		# 아래 솔루션이 더 빠름
		# 왜냐햐면 Counter 만들때 O(n) Sorted 는 O(nlogn)
		# return sorted(s) == sorted(t)

		return Counter(s) == Counter(t)


solution = Solution()
print(solution.isAnagram("anagram","nagaram"))
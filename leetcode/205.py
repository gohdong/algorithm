from typing import List


class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:
	def isIsomorphic(self, s: str, t: str) -> bool:
		# a = {s[0]: 0}
		# b = {t[0]: 0}

		# count_a = 0
		# count_b = 0
		# pattern_a = []
		# pattern_b = []
		# for i in range(len(s)):

		# 	if s[i] not in a:
		# 		count_a += 1
		# 		a[s[i]] = count_a
		# 	if t[i] not in b:
		# 		count_b += 1
		# 		b[t[i]] = count_b

		# 	pattern_a.append(a[s[i]])
		# 	pattern_b.append(b[t[i]])

		# 	if pattern_a != pattern_b:
		# 		return False

		# return True


		return len(set(s)) == len(set(t)) == len(set(zip(s, t)))


solution = Solution()
print(solution.isIsomorphic("paper", "title"))
print(solution.isIsomorphic("foo", "bar"))

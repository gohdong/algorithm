from collections import defaultdict
from typing import DefaultDict, List


class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:
	def findJudge(self, n: int, trust: List[List[int]]) -> int:
		v_people = defaultdict(set)
		not_judge = set()
		for x in trust:
			not_judge.add(x[0])
			v_people[x[1]].add(x[0])


		may_judge = set(x for x in range(1,n+1))-not_judge

		if may_judge:
			for i in may_judge:
				if v_people[i] == set(x for x in range(1,n+1)) - set([i]):
					return i

		return -1
		


solution = Solution()
print(solution.findJudge(n = 2, trust = []))
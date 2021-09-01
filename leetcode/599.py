from typing import List


class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:
	def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
		answer = []
		same_set = set(list1).intersection(set(list2))
		same_dict = {x:i+list2.index(x) for i,x in enumerate(list1) if x in same_set}
		temp = sorted(same_dict,key= lambda x : same_dict[x])
		for s in temp:
			if same_dict[s] == same_dict[temp[0]]:
				answer.append(s)
			else:
				break

		return answer


solution = Solution()
print(solution.findRestaurant(list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Shogun","Burger King"]))
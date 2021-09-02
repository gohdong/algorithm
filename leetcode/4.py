from typing import List


class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:
	def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
		temp = sorted(nums1+nums2)
		return temp[len(temp)//2]/1 if len(temp)%2 else (temp[len(temp)//2]+temp[len(temp)//2-1])/2



solution = Solution()
print(solution.findMedianSortedArrays(nums1 = [1,3], nums2 = [2]))
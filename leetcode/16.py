from typing import List
from itertools import combinations

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        pivot = (abs(nums[-1]+nums[-2]+nums[-3] - target),nums[-1]+nums[-2]+nums[-3])
        # print(nums,pivot)
        for i,x in enumerate(nums):
            for j,y in enumerate(nums[i+1:]):
                for k,z in enumerate(nums[i+1:][j+1:]):
                    temp = x+y+z
                    if temp == target:
                        return temp
                    if abs(temp-target) < pivot[0]:
                        pivot = (abs(temp-target),temp)
        return pivot[1]

        # while left<right:

        #     for i in nums[left+1:right]:
        #         temp = nums[left] + nums[right] + i
        #         print(pivot)
        #         if temp - target == 0:
        #             return temp
        #         if abs(temp - target) < pivot[0]:
        #             pivot = (abs(temp - target),temp)

        #     if pivot[1] > target:
        #         right -= 1
        #     else:
        #         left +=1

        # return pivot[1]


solution = Solution()
print(solution.threeSumClosest([-1,2,1,-4],1))
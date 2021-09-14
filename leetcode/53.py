from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        current_sum = 0
        for n in nums:
            if current_sum < 0:
                current_sum = 0
            current_sum += n

            maxSum = max(maxSum,current_sum)

        return maxSum


solution = Solution()
print(solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
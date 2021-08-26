class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort()
        sub_sq = [nums.pop()]
        while sum(sub_sq) <= sum(nums):
            sub_sq.append(nums.pop())
            
        return sub_sq
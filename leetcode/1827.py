class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0;
        for i in range(0,len(nums)):
            if(i==0):
                continue
            if(nums[i-1] >= nums[i]):
                a = (nums[i-1]-nums[i]+1)
                nums[i] += a
                count += a
        return count
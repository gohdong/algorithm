class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        answer = ""
        i = 0

        while i < len(nums):
            j = i + 1

            while j < len(nums):
                if str(nums[i]) + str(nums[j]) < str(nums[j]) + str(nums[i]):
                    nums[i], nums[j] = nums[j], nums[i]
                j += 1

            i += 1

        return str(int(''.join(str(n) for n in nums)))
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        answer = -1
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return right + 1

        while left <= right:
            answer = (left + right) // 2
            if nums[answer] == target:
                break
            elif nums[answer-1] < target < nums[answer]:
                break
            elif target > nums[answer]:
                left = answer + 1
            else:
                right = answer - 1

        return answer

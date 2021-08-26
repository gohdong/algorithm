class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] > target:
                right = mid - 1

            if nums[mid] < target:
                left = mid + 1

            if nums[mid] == target:
                return mid

        return -1

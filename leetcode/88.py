class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for x in range(m,len(nums1)):
            nums1[x] = nums2[x-m]
        
        nums1.sort()
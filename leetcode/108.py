# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def recursion(n):
            mid = len(n) // 2

            if not n:
                return

            return TreeNode(val=n[mid], left=recursion(n[:mid]), right=recursion(n[mid + 1:]))

        return recursion(nums)
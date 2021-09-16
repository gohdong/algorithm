from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        sums = []
        def recursion(node:TreeNode,cal_sum):
            temp = cal_sum + node.val
            if node.left:
                recursion(node.left,temp)

            if node.right:
                recursion(node.right,temp)

            if not (node.left or node.right):
                sums.append(temp)

        recursion(root,0)
        return targetSum in sums

        


solution = Solution()
print(solution.problem())
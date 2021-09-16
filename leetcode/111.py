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
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        min_depth = 9999999
        def recursion(node:TreeNode,depth):
            nonlocal min_depth
            if depth >= min_depth:
                return
            if node.left:
                recursion(node.left,depth+1)
            if node.right:
                recursion(node.right,depth+1)

            if not (node.left or node.right):
                min_depth = min(min_depth,depth)
        
        recursion(root,1)
        return min_depth
        
solution = Solution()
print(solution.problem())
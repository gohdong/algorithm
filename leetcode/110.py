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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def recursion(node:TreeNode,depth):
            left_depth = depth
            right_depth = depth
            if node.left:
                left_depth = recursion(node.left,depth+1)
            if node.right:
                right_depth = recursion(node.right,depth+1)


            if left_depth == -1 or right_depth == -1:
                return -1

            elif abs(left_depth-right_depth) <2:
                return max(depth,left_depth,right_depth)
            
            else:
                return -1
        
        return recursion(root,0) != -1

solution = Solution()
print(solution.problem())
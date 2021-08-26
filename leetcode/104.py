# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        vals = []
        max_depth = 1
        
        def dfs_left(node : TreeNode,depth):
            nonlocal max_depth
            vals.append(node.val)
            max_depth = max(depth,max_depth)
            if node.left:
                dfs_left(node.left,depth+1)
                
            if node.right:
                dfs_left(node.right,depth+1)
                
        if root:        
            dfs_left(root,max_depth)
        else:
            return 0
        

        
        return max_depth
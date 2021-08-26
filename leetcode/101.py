# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        left = []
        right = []
        
        def dfs_left(node : TreeNode):

            left.append(node.val)
            
            if node.left:
                dfs_left(node.left)
            else:
                left.append(None)
                
            if node.right:
                dfs_left(node.right)
            else:
                left.append(None)
                
        def dfs_right(node : TreeNode):

            right.append(node.val)
            if node.right:
                dfs_right(node.right)
            else:
                right.append(None)
                
            
            if node.left:
                dfs_right(node.left)
            else:
                right.append(None)
                
            
        if root.left:
            dfs_left(root.left)
            
        if root.right:
            dfs_right(root.right)
        
        return left==right
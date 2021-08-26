# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        answer = []
        
        def dfs(node,grand_parent,parent):
            if grand_parent and grand_parent%2 == 0:
                answer.append(node.val)
                
            if node.right:
                dfs(node.right,parent,node.val)
                
            if node.left:
                dfs(node.left,parent,node.val)
            
        if root.left:
            dfs(root.left, None, root.val)
            
        if root.right:
            dfs(root.right,None, root.val)
            
        
        
        
        return sum(answer)
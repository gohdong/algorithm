# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        p_val = []
        q_val = []
        
        def dfs(storage : list ,node : TreeNode):

            storage.append(node.val)
            
            if node.left:
                dfs(storage,node.left)
            else:
                storage.append(None)
                
            if node.right:
                dfs(storage,node.right)
            else:
                storage.append(None)
                
        if p:
            dfs(p_val,p)
        if q:
            dfs(q_val,q)
        
        return p_val==q_val
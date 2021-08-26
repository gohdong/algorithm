# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
#         print(original)
#         print(cloned)
        # print()
        answer = TreeNode()
        def dfs(node):
            if node.val == target.val:
                nonlocal answer
                answer = node
                return
            
            if node.right:
                dfs(node.right)
            
            if node.left:
                dfs(node.left)
                
        
        dfs(cloned)
        
        
        
    
        # a = target.val
        
        return answer
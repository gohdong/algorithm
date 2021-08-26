# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        vals = []
        answer = 0        
        
        def dfs(node : TreeNode):
            nonlocal answer
            if(low<=node.val<=high):
                answer += node.val

            if node.left:
                dfs(node.left)
                
            if node.right:
                dfs(node.right)
                
        
        dfs(root)        
        

        
        return answer
            
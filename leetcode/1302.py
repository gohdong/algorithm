from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        
        max_depth = 0
        depth_dict = defaultdict(list)
        
        def dfs(dep, node):
            nonlocal max_depth
            max_depth = max(dep,max_depth)
            depth_dict[dep].append(node.val)
            
            if node.left:
                dfs(dep+1,node.left)
            if node.right:
                dfs(dep+1,node.right)
            
        
        dfs(0,root)
        return sum(depth_dict[max_depth])
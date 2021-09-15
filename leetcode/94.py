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
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        if not root:
            return answer
        def recursion(node):
            if node.left:
                recursion(node.left)
            answer.append(node.val)
            if node.right:
                recursion(node.right)
        recursion(root)
        return answer


solution = Solution()
print(solution.problem())
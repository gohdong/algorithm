# Definition for a binary tree node.

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        temp = []
        def dfs(node: TreeNode, tempList: List):
            tempList.append(node.val)
            if not(node.left or node.right):
                temp.append(tempList)

            if node.left:
                dfs(node.left, tempList[:])

            if node.right:
                dfs(node.right, tempList[:])

        dfs(root, [])
        answer = []
        for t in temp:
            answer.append('->'.join(str(x) for x in t))

        return answer




solution = Solution()
print(solution.binaryTreePaths(
    TreeNode(val=1, left=TreeNode(2, right=TreeNode(val=5)), right=TreeNode(val=3))))

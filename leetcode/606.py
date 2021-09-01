from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:


        def dfs(node: TreeNode):
            if node.val == None:
                return

            temp_left = ""
            temp_right = ""

            if node.left:
                temp_left =  dfs(node.left)
            
            if node.right:
                temp_right =  dfs(node.right)

            temp = ""
            if not (temp_left or temp_right):
                temp = ""
            elif not temp_left and temp_right:
                temp = f"()({temp_right})"
            elif temp_left and not temp_right:
                temp = f"({temp_left})"
            else:
                temp = f"({temp_left})({temp_right})"
            

            return f"{node.val}{temp}"


        return dfs(root)


solution = Solution()
print(solution.tree2str(TreeNode(val=0)))

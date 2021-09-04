from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for x in range(0,len(s)):
            if s == goal:
                return True
            s = s[1:] + s[0]

        return False

solution = Solution()
print(solution.rotateString("gcmbf","fgcmb"))
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        temp_s = []
        temp_t = []

        for x in s:
            if x != "#":
                temp_s.append(x)
            elif temp_s:
                temp_s.pop()

        for x in t:
            if x != "#":
                temp_t.append(x)
            elif temp_s:
                temp_t.pop()

        return temp_s == temp_t

solution = Solution()
print(solution.backspaceCompare(s = "ab#c", t = "ad#c"))
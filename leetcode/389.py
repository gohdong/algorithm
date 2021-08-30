from typing import Counter, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_counter = Counter(s)
        t_counter = Counter(t)
        for tc in t_counter:
            if tc not in s_counter or s_counter[tc] != t_counter[tc]:
                return tc
        return 0

solution = Solution()
print(solution.problem())
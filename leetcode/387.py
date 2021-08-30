from typing import Counter, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_counter = Counter(s)
        if 1 not in s_counter.values():
            return -1
        temp = [x for x in s_counter if s_counter[x]==1]
        
        for i,x in enumerate(s):
            if x in temp:
                return i

        # print(s_counter.values())


solution = Solution()
print(solution.firstUniqChar(s = "leetcode"))
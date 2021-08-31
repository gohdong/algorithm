from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def checkRecord(self, s: str) -> bool:
        late_count = 0
        if s.count("A") > 1:
            return False
        for c in s:
            if c == "L":
                late_count +=1
            else:
                late_count = 0
            if late_count >2:
                return False
        return True
        


solution = Solution()
print(solution.checkRecord(s = "LLAL"))
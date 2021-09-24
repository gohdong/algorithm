from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def numberOfMatches(self, n: int) -> int:
        answer = 0
        
        while n != 1:
            answer += n//2
            n -= n//2

        return answer
        


solution = Solution()
print(solution.numberOfMatches(14))
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getLucky(self, s: str, k: int) -> int:
        temp = ""
        for a in s:
            temp += str(ord(a)-96)

        for _ in range(k): 
            temp = str(sum([int(a) for a in temp]))
            
        
        return int(temp)




solution = Solution()
print(solution.getLucky('leetcode',6))
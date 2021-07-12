from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def problem(self, s: str) -> int:
        answer = 0
        temp = ""
        for x in s:
            if x in temp:
                temp = temp.split(x)[1]
            temp += x
            answer = max(answer,len(temp))
        return answer

print(Solution().problem("abcabcbb"))
print(Solution().problem("dvdf"))

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
        i = 0
        pivot = 0

        while i < len(s):
            if i == len(s)-1:
                answer = max(answer,len(temp))
                
            if s[i] in temp:
                answer = max(answer,len(temp))
                i -= (len(temp)-1)
                temp = ""
            
            # print(i)
            # print(temp,s[i])
            temp += s[i]    


            i+=1
        

        return answer

print(Solution().problem("abcabcbb"))
print(Solution().problem("dvdf"))

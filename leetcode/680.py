from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        while left<right:

            if s[left] != s[right]:
                return s[left+1:right+1] == s[left+1:right+1][::-1] or s[left:right] == s[left:right][::-1]

            left+=1
            right-=1

        return True


solution = Solution()
print(solution.validPalindrome("aefbcddcbfa"))
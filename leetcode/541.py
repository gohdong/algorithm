from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        answer = ""
        flag = True
        
        for i in range(0,len(s),k):
            if flag:
                answer += s[i:i+k][::-1]
            else:
                answer += s[i:i+k]

            flag = not flag
        
        return answer


solution = Solution()
print(solution.reverseStr(s = "abcdefg", k = 2))
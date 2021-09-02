from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        s_pointer = 0
        i = 0
        while i < len(p):
            if s_pointer >= len(s):
                break

            if p[i] == '.':

                i+=1
                s_pointer+=1

            elif p[i] == '*':

                if i+1<len(p) and p[i-1] == p[i+1]:
                    i+=1
                    s_pointer+=1
                elif p[i-1] == s[s_pointer] or p[i-1] == '.':
                    s_pointer += 1
                elif i+1 < len(p) and (p[i+1] == s[s_pointer] or p[i+1] == '.'):
                    i += 1
                else:
                    return False
            else:

                if p[i] != s[s_pointer]:
                    if i+1 < len(p) and p[i+1]=='*':
                        i +=1
                    else:
                        return False
                else:
                    i+=1
                    s_pointer+=1
        

        # print(i)
        # return s_pointer == len(s)




solution = Solution()
print(solution.isMatch("aaa","ab*a*c*a"))

"aa"
"a"
"aa"
"a*"
"ab"
".*"
"mississippi"
"mis*is*ip*."
"aab"
"c*a*b"
"mississippi"
"mis*is*p*."
"aaa"
"a.a"
"aaa"
"a*a"
"ab"
".*c"
"aaa"
"ab*a*c*a"
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        answer = []
        stack = []

        for i,c in enumerate(s):
            if not stack:
                stack.append(c)

            elif c == stack[0]:
                stack.append(c)
                if i == len(s) -1 and len(stack) >= 3:
                    answer.append([i - len(stack)+1,i])

            else:
                if len(stack) >= 3:
                    answer.append([i -len(stack),i-1])
                stack.clear()
                stack.append(c)

        return answer

solution = Solution()
print(solution.largeGroupPositions(s = "abcdddeeeeaabbbcd"))
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        for op in ops:
            print(stack)

            if op == 'C':
                stack.pop()

            elif op == 'D':
                stack.append(stack[-1]*2)

            elif op == '+':
                stack.append(stack[-1]+stack[-2])
            else:
                stack.append(int(op))

        return sum(stack)

solution = Solution()
print(solution.calPoints(ops = ["5","-2","4","C","D","9","+","+"]))
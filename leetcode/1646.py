from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        answer = []
        for i in range(0,n+1):
            if i == 0:
                answer.append(0)
            elif i == 1:
                answer.append(1)
            elif i%2:
                answer.append(answer[i//2]+answer[i//2 + 1])
            else:
                answer.append(answer[i//2])

        return max(answer)

solution = Solution()
print(solution.getMaximumGenerated(7))
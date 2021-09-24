from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        answer = 0
        for op in operations:
            if '-' in op:
                answer -= 1
            else:
                answer +=1

        return answer
    


solution = Solution()
print(solution.finalValueAfterOperations(["--X","X++","X++"]))
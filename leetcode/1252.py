from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        answer = 0
        row_dict = {i:0 for i in range(m)}
        col_dict = {i:0 for i in range(n)}

        for ind in indices:
            row_dict[ind[0]] += 1
            col_dict[ind[1]] += 1

        for i in range(m*n):
            if (row_dict[i//n] + col_dict[i%n])%2:
                answer+=1

        return answer


solution = Solution()
print(solution.oddCells(m=2, n=3, indices=[[0, 1], [1, 1]]))

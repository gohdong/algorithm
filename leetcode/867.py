from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        answer = [[] for _ in matrix[0]]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                answer[j].append(matrix[i][j])

        return answer


solution = Solution()
print(solution.transpose([[1,2,3],[4,5,6]]))
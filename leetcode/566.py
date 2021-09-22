from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat)*len(mat[0]) != r*c:
            return mat
        temp = []
        # flatten
        for m in mat:
            temp += m

        answer = [[] for _ in range(r)]
        r_index = 0
        for i,t in enumerate(temp):
            answer[r_index].append(t)

            if i % c == c-1:
                r_index +=1

        return answer

solution = Solution()
print(solution.matrixReshape(mat = [[1,2],[3,4]], r = 1, c = 4))
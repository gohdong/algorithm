from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        r_num = len(grid)
        c_num = len(grid[0])
        answer = [[] for _ in range(r_num)]
        flatten = [i for j in grid for i in j]

        flatten = flatten[len(flatten)-(k%(r_num*c_num)):] + flatten[:len(flatten)-(k%(r_num*c_num))]

        for i,f in enumerate(flatten):
            answer[i//c_num].append(f)

        return answer

solution = Solution()
print(solution.shiftGrid( grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4))
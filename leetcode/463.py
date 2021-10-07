from typing import List


class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        answer = 0
        for y,g in enumerate(grid):
            for x,i in enumerate(g):
                if i == 1:
                    temp = 4
                    if x - 1 >=0:
                        temp -= grid[y][x-1]
                    if y -1 >=0:
                        temp -= grid[y-1][x]
                    if x + 1 < len(g):
                        temp -= grid[y][x+1]
                    if y + 1 < len(grid):
                        temp -= grid[y+1][x]
                    answer += temp
                    
        return answer


solution = Solution()
print(solution.problem())
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def floodFill2(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        start_color = image[sr][sc]
        if start_color == newColor:
            return image
        stack = [(sr,sc)]

        while stack:
            temp = stack.pop()
            image[temp[0]][temp[1]] = newColor
            if temp[0] - 1 >= 0 and image[temp[0]-1][temp[1]] == start_color:
                stack.append((temp[0]-1,temp[1]))
            if temp[1] - 1 >= 0 and image[temp[0]][temp[1]-1] == start_color:
                stack.append((temp[0],temp[1]-1))
            if temp[0] + 1 < len(image) and image[temp[0]+1][temp[1]] == start_color:
                stack.append((temp[0]+1,temp[1]))
            if temp[1] + 1 < len(image[0]) and image[temp[0]][temp[1]+1] == start_color:
                stack.append((temp[0],temp[1]+1))
        return image

    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        start_color = image[sr][sc]
        if start_color == newColor:
            return image
        def dfs(y,x):
            image[y][x] = newColor
            if y - 1 >= 0 and image[y-1][x] == start_color:
                dfs(y-1,x)
            if x - 1 >= 0 and image[y][x-1] == start_color:
                dfs(y,x-1)
            if y + 1 < len(image) and image[y+1][x] == start_color:
                dfs(y+1,x)
            if x + 1 < len(image[0]) and image[y][x+1] == start_color:
                dfs(y,x+1)
        dfs(sr,sc)
        return image


solution = Solution()
print(solution.floodFill([[0, 0, 0], [0, 1, 1]],
                         1,
                         1,
                         1))

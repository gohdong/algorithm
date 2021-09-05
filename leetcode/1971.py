from collections import defaultdict
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        path_dict = defaultdict(list)
        for e in edges:
            path_dict[e[0]].append(e[1])
            path_dict[e[1]].append(e[0])


        q = [start]
        visited = []

        while q:
            for node in path_dict[q[0]]:
                if node == end:
                    return True
                elif node not in visited:
                    q.append(node)
            visited.append(q.pop(0))

        return False

solution = Solution()
print(solution.validPath(1,[],0,0))

from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in image:
            i.reverse()
            for a in range(len(i)):
                i[a] = int(not i[a])
        return image
                 


solution = Solution()
print(solution.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))
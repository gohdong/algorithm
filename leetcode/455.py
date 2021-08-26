from collections import deque
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count = 0
        g.sort(reverse=True)
        cookies = deque(sorted(s, reverse=True))
        for a in g:
            if(len(cookies) != 0 and cookies[0] >= a):
                cookies.popleft()
                count+=1
                
        return count
            
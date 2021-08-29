from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        for i,c in enumerate(citations):
            if len(citations)-i <=c:
                return len(citations)-i
            
        return 0
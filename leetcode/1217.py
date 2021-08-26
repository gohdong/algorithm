class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        left = 0 
        right = 0
        
        for chip in position:
            if(chip%2==1):
                left += 1
            else:
                right += 1

        return min(left,right)
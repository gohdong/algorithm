class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        
        while len(stones)>1:
            temp = abs(stones.pop() - stones.pop())
            if(temp != 0):
                stones.append(temp)
                stones.sort()
                
        return sum(stones)
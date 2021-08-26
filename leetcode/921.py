class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        left = 0
        count = 0
        
        for s in S:
            if s =='(':
                left+=1
            else:
                if(left > 0):
                    left -=1
                else:
                    count +=1
                
        
        return count + left
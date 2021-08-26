class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        if(len(s)==1):
            return True
        
        zero_exist = False
        
        for x in s:
            if(x =='0'):
                zero_exist = True
            if(zero_exist and x == '1'):
                return False
            
        return True

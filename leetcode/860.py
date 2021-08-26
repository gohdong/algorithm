class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        if(bills[0] != 5):
            return False
        
        a = [0,0]
        
        for x in bills:
            if(x == 5):
                a[0]+=1
                
            if(x == 10):
                if(a[0] == 0 ):
                    return False
                a[0] -=1
                a[1] +=1
            
            if(x == 20):
                if(a[1]>=1 and a[0]>=1):
                        a[0] -=1
                        a[1] -=1
                elif(a[0]>=3):
                    a[0] -= 3
                    
                else:
                    return False
            
                
                
                        
                
                
        return True
        
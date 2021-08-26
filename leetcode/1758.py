class Solution:
    def minOperations(self, s: str) -> int:
        a = [1,0]
        s = [int(x) for x in s]
        
        rs_a = [a[x%2] for x in range(len(s))]
        rs_b = [int(not a[x%2]) for x in range(len(s))]
        
        count_a = 0
        count_b = 0
        
        for x in range(len(s)):
            if(s[x] != rs_a[x]):
                count_a +=1
                
            if(s[x] != rs_b[x]):
                count_b +=1
            
        
#         a = ['1','0']
#         b = ['0','1']
        
#         result_a = ''
#         result_b = ''
        
        
        
        return min(count_a,count_b)
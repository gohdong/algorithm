class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        a = [[0,0]]
        for i,c in enumerate(s):
            if(c == 'R'):
                a[count][1]+=1
            else:
                a[count][0]+=1
            
            if(a[count][1] == a[count][0]):
                a.append([0,0])
                count+=1

            
            
        return count
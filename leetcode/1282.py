class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        # groupSizes.sort()
        answ = []
        a = {}
        for i,x in enumerate(groupSizes):
            if(not x in a):
                a[x] = []
            
            a[x].append(i)
            
        for x in a:
            
            while a[x] != []:
                answ.append(a[x][:x])
                a[x] = a[x][x:]
                
        
        return answ
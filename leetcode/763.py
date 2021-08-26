class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last = {x : i for i,x in enumerate(S)}
        
        answer = []
        
        temp = set([])
        count = 0
        
        for i,x in enumerate(S):
            count +=1
            if(len(temp) == 0):
                temp.add(last[x])
            
            if i < max(temp) :
                temp.add(last[x])
                
            if i == max(temp) :
                temp = set()
                answer.append(count)
                count = 0
                
                
        return answer
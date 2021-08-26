class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        answer = 0
        boxTypes.sort(key = lambda x : x[1], reverse=True)
        
        
        for x in boxTypes:
            if(truckSize >= x[0]):
                answer += x[0]*x[1]
                truckSize -= x[0]
                
            else:
                answer += truckSize*x[1]
                truckSize = 0
                
                break
        
        return answer
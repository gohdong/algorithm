class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        asw = []
        ball_dict = {}
        for i,x in enumerate(boxes):
            if x == '1':
                ball_dict[i] = '1'
        
        for i in range(len(boxes)):
            temp = 0
            
            for k in ball_dict:
                if(k!=i):
                    temp += abs(i-k)
            
            asw.append(temp)
            
        
        
        
        return asw
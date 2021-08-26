class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        coor = [0,0]
        o_set = set(map(tuple, obstacles))
        
        now_dir = 0
        result = 0
        direction = [
            [0,1],
            [1,0],
            [0,-1],
            [-1,0]
        ]
        
        for c in commands:
            if(c == -1):
                now_dir +=1
            
            elif(c == -2):
                now_dir -=1
                
            else:
                for _ in range(c):
                    if((coor[0]+direction[now_dir%4][0],coor[1]+direction[now_dir%4][1]) in o_set):
                        break
                    coor[0] += direction[now_dir%4][0]
                    coor[1] += direction[now_dir%4][1]
            
                    result = max(result, coor[0]**2 + coor[1]**2)
            
        return result
                
            
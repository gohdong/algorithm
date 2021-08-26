class Solution:
    def maximumTime(self, time: str) -> str:
        
        for i in range(len(time)):
            
            if(i == 0 and time[i] =='?'):
                if(time[1]=='?' or int(time[1])<4):
                    time = '2'+time[1:]
                else:
                    time = '1'+time[1:]
                
            if(i == 1 and time[i] == '?'):
                if(time[0] == '2'):
                    time = '23' + time[2:]
                else:
                    time = time[0]+'9' + time[2:]
                    
                    
            if(i == 3 and time[i] == '?'):
                time = time[0:3]+'5'+time[-1]
                
            if(i == 4 and time[i] == '?'):
                time = time[:-1] + '9'
                
                
        
        return time
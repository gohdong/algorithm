class Solution:
    
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit_logs = []
        letter_logs = []
        for each_log in logs:
            if(each_log.split(' ')[1].isdigit()):
                digit_logs.append(each_log)
            else:
                letter_logs.append(each_log)
        
        letter_logs.sort(key= lambda x: (x.split(' ')[1:],x.split(' ')[0]))
        
        return letter_logs+digit_logs

        
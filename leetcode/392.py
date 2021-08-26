class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        temp = ''
        for x in s:
            flag = False
            for y in range(len(t)):
                if(t[y] == x):
                    t = t[y+1:]
                    flag = True
                    break
            if(not flag):
                return False
            
        return True
                
        # for x in t:
        #     if(x in s):
        #         temp += x
        # print(temp)
        # return s in temp
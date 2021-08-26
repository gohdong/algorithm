class Solution:
    def myAtoi(self, s: str) -> int:
        answer = ''
        for x in s:
            if(x.isdigit()):
                answer += x
            elif(x == ' '):
                if answer:
                    break
            elif(x == '-' or x=='+'):
                if answer:
                    break
                answer += x
            else:
                break
        try:
            answer = int(answer)
        except:
            answer = 0

        if(answer < -2**31):
            answer = -2**31
        if(answer > 2**31 -1):
            answer = 2**31 -1

        return answer
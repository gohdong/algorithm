class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if(numRows==1):
            return s
        answer = ''
        for x in range(0, numRows):
            temp = x
            center = 2*(numRows - x - 1)
            while temp < len(s):

                answer += s[temp]
                if (center != 0 and center != 2*numRows-2) and temp+center<len(s):
                    answer += s[temp+center]
                temp += 2*numRows-2
        return answer

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 0
        temp = ""

        for x in s:
            
            if x in temp:
                temp = temp.split(x)[1]


            temp += x

            answer = max(answer,len(temp))



        return answer
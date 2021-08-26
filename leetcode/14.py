class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=len)
        length = len(strs[0])
        answer = ""

        for i in range(length):
            flag = True
            temp = strs[0][i]
            for x in strs:
                flag = flag and x[i] == temp

            if flag:
                answer = answer + temp

            else:
                break

        return answer

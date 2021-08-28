class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        answer = ""
        while columnNumber:
            if columnNumber % 26:
                answer = chr(64+columnNumber % 26) + answer
                columnNumber = columnNumber - columnNumber % 26
            else:
                answer = "Z" + answer
                columnNumber = columnNumber - 26
            columnNumber = columnNumber // 26

        return answer

solution = Solution()
print(solution.convertToTitle(2147483647))

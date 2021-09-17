from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        answer = []

        for i in range(rowIndex+1):
            if i == 0:
                answer.append([1])
            else:
                temp = [1]
                for j in range(i-1):
                    temp.append(answer[i-1][j]+answer[i-1][j+1])
                answer.append(temp+[1])
                

        return answer[-1]
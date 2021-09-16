from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        answer = []

        for i in range(numRows):
            if i == 0:
                answer.append([1])
            else:
                temp = [1]
                for j in range(i-1):
                    temp.append(answer[i-1][j]+answer[i-1][j+1])
                answer.append(temp+[1])
                

        return answer

solution = Solution()
print(solution.generate(5))
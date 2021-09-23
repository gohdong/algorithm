from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        answer = 0

        for i,row in enumerate(board):
            if 'R' in row:
                temp = row.index('R')
                if temp > 0:
                    for j in range(temp-1,-1,-1):
                        if row[j] == 'B':
                            break
                        if row[j] == 'p':
                            answer +=1
                            break
                
                if temp <7:
                    for j in range(temp+1,8):
                        if row[j] == 'B':
                            break
                        if row[j] == 'p':
                            answer +=1
                            break

                if i > 0:
                    for j in range(i-1,-1,-1):
                        if board[j][temp] == 'B':
                            break
                        if board[j][temp] == 'p':
                            answer+=1
                            break
                
                if i < 7:
                    for j in range(i+1,8):
                        if board[j][temp] == 'B':
                            break
                        if board[j][temp] == 'p':
                            answer+=1
                            break
                
                break
            
        return answer


solution = Solution()
print(solution.numRookCaptures([[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]))
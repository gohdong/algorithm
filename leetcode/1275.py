from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        win =[
            {(0,0),(0,1),(0,2)},
            {(1,0),(1,1),(1,2)},
            {(2,0),(2,1),(2,2)},
            {(0,0),(1,0),(2,0)},
            {(0,1),(1,1),(2,1)},
            {(0,2),(1,2),(2,2)},
            {(0,0),(1,1),(2,2)},
            {(0,2),(1,1),(2,0)},
        ]
        if len(moves) < 5:
            return 'Pending'
        elif len(moves) in [5,7,9]:
            for w in win:
                if w.issubset({tuple(moves[a]) for a in range(0,len(moves),2)}):
                    return 'A'

            if len(moves) == 9:
                return 'Draw'

            return 'Pending'    
        else:
            for w in win:
                if w.issubset({tuple(moves[a]) for a in range(1,len(moves),2)}):
                    return 'B'

            return 'Pending'



solution = Solution()
print(solution.tictactoe([[0,0],[2,0],[1,1],[2,1],[2,2]]))
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        circle = [[i+1,0] for i in range(n)]
        answer = []
        for r in range(len(rounds)-1):
            temp = rounds[r]
            while temp != rounds[r+1]:
                circle[temp-1][1] +=1
                if temp == n:
                    temp = 1
                else:
                    temp += 1

            if r == len(rounds)-2:
                circle[temp-1][1]+=1
        circle.sort(key= lambda x : x[1],reverse=True)
        max_visited = circle[0][1]

        for a in circle :
            if a[1] == max_visited:
                answer.append(a[0])
            else:
                break
        return answer


solution = Solution()
print(solution.mostVisited(n = 4, rounds = [1,3,1,2]))
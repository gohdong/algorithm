from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        answer = [0 for _ in range(num_people)]
        temp = 0
        for c in range(candies):
            if temp + (c+1) < candies:
                answer[c%num_people] += (c+1)
                temp+=(c+1)
            else:
                answer[c%num_people] += candies-temp
                break

        return answer


solution = Solution()
print(solution.distributeCandies(candies = 7, num_people = 4))
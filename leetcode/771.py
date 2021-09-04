from typing import Counter, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        answer = 0
        s_counter = Counter(stones)

        for j in jewels:
            answer += s_counter[j]

        return answer

        
solution = Solution()
print(solution.problem())
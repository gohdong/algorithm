from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0
        min_price = prices[0]

        for p in prices:
            if p - min_price > answer:
                answer = p - min_price
            
            if p < min_price:
                min_price = p

        return answer 


solution = Solution()
print(solution.maxProfit([2,4,1]))
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        answer = 0
        for i,t in enumerate(timeSeries):
            if i+1 < len(timeSeries):
                if t+duration-1 < timeSeries[i+1]:
                    answer += duration
                else:
                    answer += (timeSeries[i+1] - timeSeries[i])
            else:
                answer += duration


        return answer


solution = Solution()
print(solution.findPoisonedDuration(timeSeries = [1,2,3,4,5], duration = 5))
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        answer = []
        for i in range(1,n+1):
            if i in target:
                answer.append("Push")
            else:
                answer += ["Push","Pop"]
            
            if i == target[-1]:
                break

        return answer

solution = Solution()
print(solution.buildArray(target = [1,3], n = 3))
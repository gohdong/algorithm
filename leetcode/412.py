from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []

        for i in range(1, n+1):
            temp = ""
            if i % 3 == 0:
                temp += "Fizz"
                if i % 5 == 0:
                    temp += "Buzz"    
            elif i % 5 == 0:
                temp += "Buzz"

            else:
                temp += str(i)

            answer.append(temp)
        return answer


solution = Solution()
print(solution.fizzBuzz(15))

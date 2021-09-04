from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        c_indexs = [i for i, x in enumerate(s) if x == c]
        answer = []
        pivot = 0

        for i, x in enumerate(s):
            if pivot < len(c_indexs)-1 and i > c_indexs[pivot]:
                pivot+=1

            if x == c:
                answer.append(0)
            else:
                if pivot == 0:
                    answer.append(abs(c_indexs[pivot]-i))

                else:
                    answer.append(
                        min(abs(i-c_indexs[pivot]), abs(i-c_indexs[pivot-1])))

        return answer


solution = Solution()
print(solution.shortestToChar(s="loveleetcode", c="e"))

from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from collections import deque
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        stu_queue = deque(students)
        sandwiches.reverse()
        change_count = 0
        while sandwiches:
            if change_count == len(stu_queue):
                break

            if stu_queue[0] == sandwiches[-1]:
                stu_queue.popleft()
                sandwiches.pop()
                change_count = 0

            else:
                stu_queue.append(stu_queue.popleft())
                change_count += 1



        return len(stu_queue)


solution = Solution()
print(solution.countStudents(students = [1,1,0,0], sandwiches = [0,1,0,1]))
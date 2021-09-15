from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        answer = []
        while head:
            if head.val not in answer:
                answer.append(head.val)
            head = head.next
        
        temp = None
        for v in answer[::-1]:
            if v == answer[-1]:
                temp = ListNode(val=v,next=None)
            else:
                temp = ListNode(val=v,next=temp)
        return temp


solution = Solution()
print(solution.problem())

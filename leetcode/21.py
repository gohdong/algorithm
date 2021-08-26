# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        n = []
        answer = None

        def recursion(l: ListNode):
            n.append(l.val)
            if l.next:
                recursion(l.next)
        if l1:
            recursion(l1)
        if l2:
            recursion(l2)
        n.sort(reverse=True)
        for i, x in enumerate(n):
            if i == 0:
                answer = ListNode(val=x, next=None)
            else:
                answer = ListNode(val=x, next=answer)

        return answer
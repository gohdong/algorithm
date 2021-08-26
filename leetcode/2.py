class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        answer = None
        def get_num(l3):
            temp = []
            while True:
                temp.append(l3.val)
                if not l3.next:
                    break
                l3 = l3.next
            return temp

        l1_nums = get_num(l1)
        l2_nums = get_num(l2)

        l1s = int(''.join(str(x) for x in l1_nums[::-1]))
        l2s = int(''.join(str(x) for x in l2_nums[::-1]))

        
        result = str(l1s+l2s)
        
        for x in result:
            if not answer:
                answer = ListNode(val=int(x),next=None)
            else:
                answer = ListNode(val=int(x),next=answer)
                
        return answer
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        answer = 0
        temp_stack = []
        for i, x in enumerate(s):
            if not temp_stack:
                temp_stack.append(x)
            elif x == temp_stack[0]:
                temp_stack.append(x)
            else:
                temp_stack.clear()
                temp_stack.append(x)

            length = len(temp_stack)
            stack_start = i- length+1
            stack_end = i 
            counter_string = str((int(temp_stack[0])+1 )%2)*length

            if stack_start - length >= 0 and s[stack_start-length:stack_start] == counter_string:
                # print(counter_string)
                answer += 1
            
            if stack_end + length < len(s) and stack_end+1<len(s) and s[stack_end+1:stack_end+length] == counter_string:
                # print(counter_string)
                answer +=1

            # if i - length +1:
            #     print(i - length +1)


            # if i - len(temp_stack) > 0 and i+1 < len(s) and (s[i-len(temp_stack):i+1] == "0"*len(temp_stack)+"1"*len(temp_stack) or s[i-len(temp_stack):i+1] == "1"*len(temp_stack)+"0"*len(temp_stack)):
            #     answer += 1
            # if i + len(temp_stack) + 1 < len(s) and i-len(temp_stack)+1 > 0 and (s[i-len(temp_stack)+1:i+len(temp_stack)+1] == "0"*len(temp_stack)+"1"*len(temp_stack) or s[i-len(temp_stack)+1:i+len(temp_stack)+1] == "1"*len(temp_stack)+"0"*len(temp_stack)):
            #     answer += 1

        return answer


solution = Solution()
print(solution.countBinarySubstrings("00110"))

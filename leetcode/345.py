from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseVowels(self, s: str) -> str:
        answer = s
        vowel = {
            'a': '-',
            'e': '-',
            'i': '-',
            'o': '-',
            'u': '-',
            'A': '-',
            'E': '-',
            'I': '-',
            'O': '-',
            'U': '-',
        }
        # 내 솔루션
        # temp = [x for x in s if x in vowel]

        # for i,x in enumerate(s):
        #     if x in vowel:
        #         answer = answer[:i]+temp.pop()+answer[i+1:]

        # return answer

        # 빠른 솔루션
        i = 0
        j = len(s)-1
        temp = list(s)
        while i < j:
            if temp[i] not in vowel:
                i += 1
            if temp[j] not in vowel:
                j -= 1

            if temp[i] in vowel and temp[j] in vowel:
                temp[i], temp[j] = temp[j], temp[i]
                i += 1
                j -= 1

        return ''.join(temp)


solution = Solution()
print(solution.reverseVowels(s="leetcode"))

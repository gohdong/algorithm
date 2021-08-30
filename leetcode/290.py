from typing import Counter, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        p_dict = {}
        words = s.split()
        if len(words) != len(pattern):
            return False

        for i,p in enumerate(pattern):
            if p not in p_dict and words[i] not in list(p_dict.values()):
                p_dict[p] = words[i]

            else:
                
                if p not in p_dict or p_dict[p] != words[i]:
                    return False

        return True
            




solution = Solution()
print(solution.wordPattern(pattern = "abbc", s = "dog dog dog dog"))
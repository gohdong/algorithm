from typing import Counter, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        answer = True
        counter_ransom = Counter(ransomNote)
        counter_magazine = Counter(magazine)

        for c in counter_ransom:
            if c not in counter_magazine:
                answer = False
                break
            
            if counter_magazine[c] < counter_ransom[c]:
                answer = False
                break

        return answer
        


solution = Solution()
print(solution.canConstruct(ransomNote = "aa", magazine = "aab"))
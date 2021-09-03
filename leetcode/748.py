from collections import defaultdict
from typing import Counter, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        words.sort(key=len)
        temp = defaultdict(int)
        i = 0
        flag = False

        for l in licensePlate:
            if l.isalpha():
                temp[l.lower()] +=1
        print(temp)
        while True:
            temp_word_counter = Counter(words[i])
            for t in temp:
                if t not in temp_word_counter or temp[t] > temp_word_counter[t]:
                    i+=1
                    break
                else:
                    if t == list(temp.keys())[-1]:
                        flag = True
                        break

            
            if flag:
                return words[i]


        # for word in words:



solution = Solution()
print(solution.shortestCompletingWord(licensePlate = "1s3 PSt", words = ["step","steps","stripe","stepple"]))
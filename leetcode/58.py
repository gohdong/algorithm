class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        return len(s.split(' ')[-1])
print(Solution.lengthOfLastWord('','   fly me   to   the moon  '))
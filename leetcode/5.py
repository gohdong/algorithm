class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindromes = []
        if (len(s) == 1 or s == s[::-1]):
            return s
        for x in range(0,len(s)):
            for y in range(x,len(s)):
                temp = s[x:y+1]
                if (temp == temp[::-1]):
                    palindromes.append(temp)
        
        return sorted(palindromes,key=len,reverse=True)[0]

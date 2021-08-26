class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        answer = 0
        length = len(s)

        for i, x in enumerate(s):
            if i + 1 < length and roman_dict[s[i]] < roman_dict[s[i + 1]]:
                answer -= roman_dict[x]
            else:
                answer += roman_dict[x]

        return answer
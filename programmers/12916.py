from collections import Counter


def solution(s):
    temp = Counter(s.lower())
    return temp['p'] == temp['y']


print(solution("pPoooyY"))
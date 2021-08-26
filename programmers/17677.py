from collections import defaultdict


def solution(str1, str2):
    answer = 0

    inter_count = 0
    comb_count = 0

    str1 = str1.lower()
    str2 = str2.lower()

    str1_dict = defaultdict(int)
    str2_dict = defaultdict(int)

    for s in range(len(str1) - 1):
        if str1[s:s + 2].isalpha():
            str1_dict[str1[s:s + 2]] += 1

    for s in range(len(str2) - 1):
        if str2[s:s + 2].isalpha():
            str2_dict[str2[s:s + 2]] += 1

    for s1 in str1_dict:
        if s1 in str2_dict:
            inter_count += min(str1_dict[s1], str2_dict[s1])

    for s1 in str1_dict:
        if s1 in str2_dict:
            comb_count += max(str1_dict[s1], str2_dict[s1])
        else:
            comb_count += str1_dict[s1]

    for s2 in str2_dict:
        if s2 not in str1_dict:
            comb_count += str2_dict[s2]

    if comb_count == 0:
        return 65536

    return int((inter_count / comb_count) * 65536)
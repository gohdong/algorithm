# 문자열 압축
# https://programmers.co.kr/learn/courses/30/lessons/60057

from collections import defaultdict


def solution(s):
    answer = [s]
    c_dict = defaultdict(list)
    cut = 1
    while cut <= len(s) // 2:
        for i in range(0, len(s), cut):
            c_dict[cut].append(s[i:i + cut])
        cut += 1

    for c in c_dict:
        for d in range(len(c_dict[c])):
            if d:
                if c_dict[c][d - 1] == c_dict[c][d]:
                    if d - 1 == 0 or type(c_dict[c][d - 2]) != int:
                        c_dict[c].insert(d - 1, 2)
                        c_dict[c].pop(d)
                    else:
                        c_dict[c][d-2] +=1
                        c_dict[c].insert(0, 0)
                        c_dict[c].pop(d)



    for c in c_dict:
        temp = ""
        for i in c_dict[c]:
            if i != 0:
                temp += str(i)
        answer.append(temp)
        
    answer.sort(key=len)

    return len(answer[0])
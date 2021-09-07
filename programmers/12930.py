def solution(s):
    answer = ''
    flag = True

    for x in s:
        if x == ' ':
            answer += ' '
            flag = True
        elif flag:
            answer += x.upper()
            flag = False
        else:
            answer += x.lower()
            flag = True

    return answer


print(solution())

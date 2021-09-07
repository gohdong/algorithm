def solution(s, n):
    answer = ''
    for x in s:
        if x.isalpha():
            if ord(x) >= 97:
                answer += chr(((ord(x)-97)+n) % 26 + 97)
            else:
                answer += chr(((ord(x)-65)+n) % 26 + 65)
        else:
            answer += x

    return answer


print(solution("b", 25))

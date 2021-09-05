def solution(n):
    return int(decimalto3(n)[::-1],3)

def decimalto3(a):
    temp = ''
    while a:
        temp = str(a%3)+temp
        a = a//3

    return temp


print(solution(125))
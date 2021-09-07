def solution(p):
    answer = ''

    def recursion(u,v):
        if not u:
            return ""

        temp = ""

        if is_valid(u):
            a,b = separator(v)
            temp += u
            temp += recursion(a,b)
        else:
            a,b = separator(v)
            temp += "("
            temp += recursion(a,b)
            temp += ")"
            temp += flip(u[1:-1])

        return temp

    u,v = separator(p)

    return recursion(u,v)

def separator(s):
    u = ''
    v = ''
    left = 0
    right = 0
    for i,x in enumerate(s):
        if x == "(":
            left += 1
        else:
            right += 1
        
        if left == right:
            u = s[:i+1]
            v = s[i+1:]
            break
        
    return u,v


def is_valid(s: str):
    left = 0

    for x in s:
        if x == "(":
            left += 1
        else:
            left -= 1

        if left < 0:
            return False

    return left == 0

def flip(s):
    answer = ""
    for x in s:
        if x == '(':
            answer += ')'
        else:
            answer += '('

    return answer



print(solution("((()(())()))"))


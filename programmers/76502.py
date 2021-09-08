def solution(s):
    answer = 0

    for _ in s:
        if is_valid(s):
            answer += 1        
        s = s[1:]+s[0]

    return answer


def is_valid(s: str):
    stack = []

    for x in s:
        if x == "[" or x == "{" or x == "(":
            stack.append(x)
            
        if not stack:
            return False
        if x == "]":
            if stack.pop() != "[":
                return False
        if x == "}":
            if stack.pop() != "{":
                return False
        if x == ")":
            if stack.pop() != "(":
                return False

    return len(stack) == 0


print(solution("[(])"))

def solution(s):
    stack = []

    for a in s:
        if stack and stack[-1] == a:
            stack.pop()
        else:
            stack.append(a)

    return 1 if not stack else 0
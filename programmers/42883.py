def solution(number, k):
    stack = []

    for n in number:
        if not stack:
            stack.append(n)
        else:
            while stack and k > 0 and stack[-1] < n:
                stack.pop()
                k -= 1
            stack.append(n)

    while k > 0:
        stack.remove(min(stack))
        k -= 1

    return ''.join(stack)
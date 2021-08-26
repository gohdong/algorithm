def solution(n, words):
    answer = []
    stack = []
    count = 0

    for w in words:

        if w in stack:
            break

        if stack and stack[-1][-1] != w[0]:
            break

        if w not in stack:
            stack.append(w)

        count += 1
    print(len(words))
    print(count)

    if count == len(words):
        return [0, 0]

    return [count % n + 1, count // n + 1]
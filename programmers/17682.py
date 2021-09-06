def solution(dartResult):
    stack = []
    for i, dart in enumerate(dartResult):
        if dart == 'S':
            if dartResult[i-2:i] == '10':
                stack.append(10)
            else:
                stack.append(int(dartResult[i-1]))
        elif dart == 'D':
            if dartResult[i-2:i] == '10':
                stack.append(10**2)
            else:
                stack.append(int(dartResult[i-1])**2)
        elif dart == 'T':
            if dartResult[i-2:i] == '10':
                stack.append(10**3)
            else:
                stack.append(int(dartResult[i-1])**3)

        elif dart == '*':
            stack[-1] = stack[-1] *2
            if len(stack) >=2:
                stack[-2] = stack[-2] * 2

        elif dart == '#':
            stack.append(stack.pop()*-1)

    return sum(stack)


print(solution("1S2D*3T"))
print(solution("1D2S#10S"))
print(solution("1D2S0T"))
print(solution("1S*2T*3S"))
print(solution("1D#2S*3S"))
print(solution("1T2D3D#"))
print(solution("1D2S3T*"))
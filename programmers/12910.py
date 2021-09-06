def solution(arr, divisor):
    answer = []
    for a in arr:
        if not a % divisor:
            answer.append(a)
    return sorted(answer) if answer else [-1]


print(solution([2, 36, 1, 3],1))
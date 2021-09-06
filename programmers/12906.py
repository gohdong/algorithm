def solution(arr):
    answer = []
    for a in arr:
        if not answer:
            answer.append(a)
        else:
            if answer[-1] != a:
                answer.append(a)
    return answer


print(solution([1,1,3,3,0,1,1]	))
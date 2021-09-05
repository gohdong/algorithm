def solution(numbers):
    answer = set()

    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i > j:
                answer.add(numbers[i]+numbers[j])

    return sorted(answer)


print(solution([2,1,3,4,1]))
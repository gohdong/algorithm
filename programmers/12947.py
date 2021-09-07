def solution(x):
    return x % sum(map(int,list(str(x)))) == 0


print(solution(10))
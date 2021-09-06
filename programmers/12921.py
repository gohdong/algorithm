def solution(n):
    answer = 0
    for i in range(n+1):
        if is_prime(i):
            answer+=1

    return answer

def is_prime(a: int):
    if a == 1 or a == 0:
        return False
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            return False

    return True

print(solution(10))